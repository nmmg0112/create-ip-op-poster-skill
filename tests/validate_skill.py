from __future__ import annotations

import re
import sys
from pathlib import Path


GROUPS = (
    "workflow",
    "production",
    "visual",
    "integrity",
    "prompt",
    "onboarding",
    "platforms",
    "contest",
    "docs",
)
DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def package_documents(root: Path) -> list[Path]:
    """Instruction and example files that ship in the active package."""
    paths = [root / "SKILL.md", root / "README.md", root / "agents/openai.yaml"]
    for folder in (root / "references", root / "examples"):
        for suffix in ("*.md", "*.txt"):
            paths.extend(sorted(folder.rglob(suffix)))
    return paths


def active_package_files(root: Path) -> list[Path]:
    """Files that define current user-visible or runtime behavior."""
    return package_documents(root)


def active_corpus(root: Path) -> str:
    return "\n".join(
        path.read_text(encoding="utf-8") for path in active_package_files(root)
    )


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise AssertionError(f"missing file: {relative}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def require_any(text: str, needles: tuple[str, ...], label: str) -> None:
    if not any(needle in text for needle in needles):
        raise AssertionError(f"{label}: missing any of {needles!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"{label}: forbidden legacy text {needle!r}")


def require_order(text: str, earlier: str, later: str, label: str) -> None:
    earlier_index = text.find(earlier)
    later_index = text.find(later)
    if earlier_index < 0 or later_index < 0 or earlier_index >= later_index:
        raise AssertionError(f"{label}: expected {earlier!r} before {later!r}")


def check_workflow(root: Path) -> None:
    skill = read(root, "SKILL.md")
    workflow = read(root, "references/workflow.md")
    novice = read(root, "references/novice-mode.md")
    workflow_corpus = "\n".join((skill, workflow, novice))

    state_block = """intake
  -> person_material_pending
  -> content_plan_pending
  -> production
  -> qa
  -> complete"""
    for text, label in ((skill, "SKILL.md"), (workflow, "references/workflow.md")):
        require(text, state_block, label)

    for needle in (
        "人物素材确认",
        "内容方案＋生成授权",
        "人物没问题",
        "选 1 生成",
        "默认只有两个确认点",
        "视觉偏好",
        "Brief",
    ):
        require(workflow_corpus, needle, "two-confirmation workflow")

    for legacy in (
        "direction_and_mode_pending",
        "prompt_pending",
        "选方向 1，用模式 B",
        "确认生成",
        "模式 A｜快速生图",
        "模式 B｜保真合成",
        "排布通过",
        "生成确认卡",
    ):
        forbid(workflow_corpus, legacy, "two-confirmation workflow")

    require_order(
        workflow,
        "person_material_pending",
        "content_plan_pending",
        "references/workflow.md state order",
    )
    require_order(
        workflow,
        "人物没问题",
        "选 1 生成",
        "references/workflow.md confirmation order",
    )
    for needle in (
        "人物肖像素材好，整张海报的呈现才会好",
        "案例图不是装饰",
        "贴合度有限",
    ):
        require(workflow_corpus, needle, "material explanation")

    visual_question = (
        "这张海报你有没有偏好的颜色或感觉？比如清爽浅蓝、"
        "暖色活力、自然松弛。没有也可以，我会结合 Brief 推荐。"
    )
    require(workflow_corpus, visual_question, "optional visual-preference question")
    for needle in (
        "视觉偏好不是独立确认点",
        "已提供时不重复询问",
        "并入人物预览",
        "不得形成第三个等待点",
        "用户偏好",
        "配色",
        "材质",
        "光影",
        "氛围",
        "装饰边界",
        "同时完成方向选择、方案确认和正式生图授权",
        "报价",
        "权益",
        "不阻塞",
    ):
        require(workflow_corpus, needle, "optional visual preference and authorization")


def check_production(root: Path) -> None:
    skill = read(root, "SKILL.md")
    workflow = read(root, "references/workflow.md")
    prompt = read(root, "references/prompt-template.md")
    platform = read(root, "references/platform-usage.md")
    qa = read(root, "references/qa-checklist.md")
    handoff = read(root, "references/handoff-template.md")
    integrity = read(root, "references/material-integrity.md")
    corpus = active_corpus(root)

    for needle in (
        "默认完整海报一次生成",
        "16:9 横版",
        "不得先生成空背景",
        "默认只调用一次正式生图",
        "严格保真",
        "用户明确要求",
        "局部图层修改",
        "不得整图重绘",
    ):
        require(corpus, needle, "production contract")

    for text, label in (
        (skill, "SKILL.md default production route"),
        (workflow, "workflow.md default production route"),
        (prompt, "prompt-template.md default production route"),
    ):
        require(text, "默认完整海报一次生成", label)
        require(text, "16:9 横版", label)
        require(text, "不得先生成空背景", label)
        require(text, "不得生成排布稿", label)
        require(text, "默认只调用一次正式生图", label)
        require(text, "空舞台", label)
        require(text, "留洞底图", label)

    for needle in (
        "whole_poster",
        "strict_fidelity",
        "generation_route",
        "formal_generation_count",
    ):
        require(prompt + platform + qa + handoff, needle, "production receipt and routing")

    for needle in (
        "content_plan_pending",
        "visual_preference",
        "brief_basis",
        "play_preflight",
        "generation_route",
        "formal_generation_count",
        "final_image_path",
        "Current QA",
    ):
        require(handoff, needle, "handoff-template.md")

    for needle in (
        "strict_fidelity",
        "只有用户明确要求",
        "后台路由",
        "艺术底图",
        "原素材覆回",
        "底图不能只是空背景",
    ):
        require(skill + workflow + prompt + integrity, needle, "strict-fidelity route")
    require_order(prompt, "艺术底图", "原素材覆回", "strict-fidelity production order")
    for needle in ("完整场景", "前中后景", "视觉动势"):
        require(prompt + platform + qa, needle, "strict-fidelity visual base")
    for needle in ("锁定画布", "蒙版", "围绕真实素材", "覆回校验"):
        require(prompt + platform + integrity + qa, needle, "strict-fidelity integration")
    for needle in ("900—1600", "最多约 2200", "不把模板字段逐项机械展开"):
        require(prompt, needle, "execution prompt information budget")
    for needle in ("竖版渠道", "3:4"):
        require(skill + workflow + prompt + qa, needle, "landscape master contract")

    for needle in (
        "人物",
        "案例",
        "Brief",
        "主题",
        "玩法",
        "商务信息",
        "formal_generation_count: 1",
        "最大程度保持",
        "不承诺逐像素保真",
    ):
        require(prompt, needle, "whole-poster execution prompt")

    for needle in ("没有生图", "Prompt", "素材映射", "SVG", "HTML", "Canvas", "PPT", "程序化信息板"):
        require(platform, needle, "platform capability downgrade")
    require(platform, "handoff", "platform capability downgrade")
    require(platform, "formal_generation_count: 0", "platform capability downgrade")
    forbid(platform, "确认生成", "platform capability downgrade")

    for needle in (
        "局部图层修改",
        "不得整图重绘",
        "非目标区域",
    ):
        require(skill + workflow + qa, needle, "exact post-production edits")


def check_visual(root: Path) -> None:
    skill = read(root, "SKILL.md")
    director = read(root, "references/visual-director.md")
    layout = read(root, "references/layout-grammar.md")
    direction = read(root, "references/direction-framework.md")
    qa = read(root, "references/qa-checklist.md")

    require(skill, "visual-director.md", "SKILL.md visual-director routing")
    require(skill, "视觉导演", "SKILL.md mandatory visual direction")

    for needle in (
        "内容关系",
        "版式家族",
        "视觉母题",
        "人物模式",
        "信息密度",
        "层级与景深",
        "第一视觉",
        "阅读路径",
        "主要留白",
    ):
        require(director + direction, needle, "visual-direction preflight")

    for family in ("概念场景", "群像主视觉", "玩法分舱", "路线阶段", "矩阵档案", "编辑拼贴"):
        require(layout, family, "layout-grammar.md")

    for needle in (
        "实际打开",
        "2—4",
        "参考原图",
        "原图路径",
        "只写 `opened: yes` 不算证据",
        "结构参考",
        "密度参考",
        "气质参考",
    ):
        require(director, needle, "visual reference use")

    for text, label in (
        (director, "visual-director.md"),
        (direction, "direction-framework.md"),
    ):
        for needle in ("用户偏好", "Brief", "配色", "材质", "光影", "氛围", "装饰边界"):
            require(text, needle, label)
        require(text, "冲突", label)
        require(text, "说明", label)
        require(text, "数码＝科技蓝", label)

    for needle in (
        "实际查看最终图片",
        "实际成图",
        "16:9 横版",
        "竖版",
        "无玩法",
        "像 PPT",
        "空背景",
        "同一平面",
        "无意义空白",
        "人物与玩法脱节",
        "第一视觉",
        "前景",
        "中景",
        "背景",
        "无法直接预览或下载",
    ):
        require(qa, needle, "actual-final visual QA")


def check_integrity(root: Path) -> None:
    skill = read(root, "SKILL.md")
    integrity = read(root, "references/material-integrity.md")
    workflow = read(root, "references/workflow.md")
    qa = read(root, "references/qa-checklist.md")
    person_prompt = (
        "把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，"
        "横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 "
        "注意人物不能重复，且人物大小调整一致一些"
    )

    for text, label in ((skill, "SKILL.md"), (workflow, "references/workflow.md")):
        require(text, person_prompt, label)

    require_any(
        skill + workflow + integrity,
        ("横版白底人物组合预览", "横版白底组合预览图"),
        "person-material preview",
    )
    for needle in (
        "只展示一张",
        "人物没问题",
        "身份",
        "数量",
        "重复",
        "遗漏",
        "身体完整",
        "交叠",
        "遮脸",
        "残边",
    ):
        require(skill + workflow + integrity, needle, "person-material review")

    for needle in ("最大程度保持", "不承诺逐像素保真"):
        require(skill + integrity, needle, "whole-poster fidelity disclosure")

    for needle in (
        "用户明确要求",
        "完全不变",
        "严格保真",
        "完整案例",
        "原 Logo",
        "准确中文",
    ):
        require(skill + integrity, needle, "strict-fidelity activation and protection")

    for needle in (
        "只能用于 `unified-ensemble`",
        "`grouped-by-play`",
        "`independent-cutouts`",
        "`hybrid-hero-groups`",
    ):
        require(integrity + workflow + qa, needle, "person-layout routing")
    require(integrity, "不得仅凭“正式提报”自行推断", "explicit strict-fidelity trigger")

    for needle in (
        "局部图层修改",
        "不得整图重绘",
        "前后图像差异",
        "非目标区域",
    ):
        require(integrity + qa, needle, "exact post-edit integrity")

    for needle in (
        "edit_target_region",
        "pre_edit_image",
        "post_edit_image",
        "non_target_diff_pixel_count",
        "formal_generation_count",
    ):
        require(integrity + qa, needle, "exact post-edit receipt")

    for needle in ("人脸", "动物头部", "陌生人", "错脸", "漏人", "重复", "乱码", "虚构数据"):
        require(qa + integrity, needle, "final material QA")


def check_prompt(root: Path) -> None:
    prompt = read(root, "references/prompt-template.md")
    direction = read(root, "references/direction-framework.md")
    benchmark = read(root, "examples/successful-prompt-benchmark.md")
    qa = read(root, "references/qa-checklist.md")

    content_fields = (
        "玩法标题",
        "明确成员",
        "账号/案例依据",
        "具体场景或人物关系",
        "动作、冲突、互动或反转",
        "产品/项目自然进入方式",
        "海报上的一句短文案",
    )
    for needle in content_fields:
        require(direction + prompt, needle, "content-play preflight")

    for needle in (
        "只有口号",
        "抽象风格",
        "达人没有玩法归属",
        "没有场景、动作或产品进入方式",
        "未解决",
        "16:9",
        "视觉偏好",
        "禁止",
        "正式生图",
    ):
        require(direction + prompt, needle, "content-play generation block")

    priority = (
        "主题与内容玩法",
        "人物与案例的视觉角色",
        "完整艺术构图和信息层级",
        "固定文案与商务信息",
        "人物/案例尽量不改的要求",
        "少量关键禁令",
    )
    for needle in priority:
        require(prompt, needle, "prompt priority")
    for earlier, later in zip(priority, priority[1:]):
        require_order(prompt, earlier, later, "prompt priority")

    for needle in (
        "whole_poster",
        "strict_fidelity",
        "默认完整海报一次生成",
        "不得先生成空背景",
        "16:9 横版",
        "视觉偏好",
        "Brief",
    ):
        require(prompt, needle, "prompt routes and visual evidence")
    for needle in ("批准画幅", "竖版渠道／适配", "未批准例外"):
        require(prompt + qa, needle, "approved aspect-ratio handling")

    for needle in ("成功基准", "不得固化", "16:9", "玩法", "第一视觉"):
        require(benchmark, needle, "successful-prompt-benchmark.md")
    for needle in ("第一视觉", "人物与玩法", "参考案例", "实际成图"):
        require(qa, needle, "qa-checklist.md")


def check_onboarding(root: Path) -> None:
    skill = read(root, "SKILL.md")
    novice = read(root, "references/novice-mode.md")
    readme = read(root, "README.md")
    corpus = "\n".join((skill, novice, readme))

    for needle in (
        "Skill 被读取后自动发送",
        "资料不全也没关系",
        "【主题／Brief】",
        "【喜欢的风格】",
        "【文字密度】",
        "【必须出现的文字】",
        "开场白只出现一次",
        "不要求用户复制",
        "4 位达人",
        "运动赛事主题",
    ):
        require(corpus, needle, "automatic beginner onboarding")

    for needle in (
        "人物肖像质量",
        "案例截图",
        "内容玩法",
        "人物没问题",
        "选 1 生成",
    ):
        require(corpus, needle, "beginner material and reply guidance")


def check_platforms(root: Path) -> None:
    aime = read(root, "references/platforms/aime-executor.md")
    doubao = read(root, "references/platforms/doubao-executor.md")
    shared = read(root, "references/platform-usage.md")
    skill = read(root, "SKILL.md")

    for needle in (
        "Image2",
        "LockedPosterSpec",
        "当前锁定版本",
        "不得把整段聊天记录",
        "正式生图一次",
    ):
        require(aime, needle, "Aime adapter")
    for needle in (
        "Seedream 5.0 Pro",
        "LockedPosterSpec",
        "稳定人物编号",
        "开场白",
        "正式生图一次",
    ):
        require(doubao, needle, "Doubao adapter")
    for needle in (
        "PosterVersionLock",
        "上一版成功文件",
        "局部修改",
        "当前平台",
    ):
        require(aime + doubao + shared + skill, needle, "platform version protection")


def check_contest(root: Path) -> None:
    prompt = read(root, "examples/prompt.txt")
    result = read(root, "examples/result.md")
    multi = read(root, "examples/golden-case-multi-person.md")
    single = read(root, "examples/golden-case-single-person.md")

    for needle in (
        "人物没问题",
        "选 1 生成",
        "16:9 横版",
        "告诉我怎么使用",
    ):
        require(prompt, needle, "contest reproducible prompt")
    for needle in (
        "业务痛点",
        "关键链路",
        "真实案例",
        "可量化",
        "NOT VERIFIABLE",
    ):
        require(result, needle, "contest result evidence")
    for text, label in (
        (multi, "multi-person Golden Case"),
        (single, "single-person Golden Case"),
    ):
        for needle in (
            "用户输入",
            "导演判断",
            "LockedPosterSpec",
            "执行 Prompt",
            "成功标准",
            "不得固化",
        ):
            require(text, needle, label)


def check_docs(root: Path) -> None:
    platform = read(root, "references/platform-usage.md")
    quick = read(root, "examples/quick-start.md")
    chatgpt = read(root, "examples/chatgpt-starter.md")
    readme = read(root, "README.md")
    scenarios = read(root, "tests/scenario-regression.md")
    docs_corpus = "\n".join((quick, chatgpt, readme))

    for text, label in (
        (quick, "examples/quick-start.md"),
        (chatgpt, "examples/chatgpt-starter.md"),
        (readme, "README.md"),
    ):
        for reply in ("人物没问题", "选 1 生成"):
            require(text, reply, label)
        for needle in (
            "视觉偏好（可选）",
            "16:9 横版",
            "默认整图生成",
            "严格保真",
            "不得整图重绘",
        ):
            require(text, needle, label)

    require(readme, "不会再单独等待", "README.md optional style flow")
    require(quick, "不再单独追问", "examples/quick-start.md optional style flow")
    for needle in ("同一条人物预览消息", "不要再停下来追问"):
        require(chatgpt, needle, "examples/chatgpt-starter.md optional style flow")

    for legacy in (
        "人物素材通过",
        "确认生成",
        "模式 A｜快速生图",
        "模式 B｜保真合成",
        "模式 A：快速生图",
        "模式 B：保真合成",
        "选方向 1，用模式 B",
        "生成确认卡",
        "排布通过",
    ):
        forbid(active_corpus(root), legacy, "active package docs and runtime")

    for needle in (
        "两个确认",
        "完整海报",
        "整图",
        "严格保真",
        "完全不变",
        "不承诺逐像素",
    ):
        require(docs_corpus, needle, "low-barrier docs")
    if "查看完整 Prompt" in docs_corpus:
        require(docs_corpus, "不新增确认门槛", "optional full Prompt")

    for needle in ("ChatGPT", "豆包", "Coze", "交接包"):
        require(platform + chatgpt + readme, needle, "cross-platform docs")

    for needle in (
        "场景 1：七位游戏剧情达人",
        "浅蓝夏日",
        "场景 2：数码 Brief",
        "3:4",
        "预检拦截",
        "场景 3：精确 Logo 修改",
        "新增两个原 Logo",
        "仅目标区域变化",
        "场景 4：严格保真",
        "人脸、案例和中文完全不变",
        "场景 5：无案例",
        "贴合度有限",
        "场景 6：无生图能力",
        "交接包",
        "不能只靠关键词",
        "实际成图",
        "图像差异",
    ):
        require(scenarios, needle, "scenario-regression.md")

    markdown_files = [path for path in package_documents(root) if path.suffix == ".md"]
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = (source.parent / raw_target).resolve()
            if not target.is_file():
                raise AssertionError(
                    f"{source.relative_to(root)}: broken Markdown link {raw_target}"
                )


CHECKS = {
    "workflow": check_workflow,
    "production": check_production,
    "visual": check_visual,
    "integrity": check_integrity,
    "prompt": check_prompt,
    "onboarding": check_onboarding,
    "platforms": check_platforms,
    "contest": check_contest,
    "docs": check_docs,
}


def main() -> int:
    group = sys.argv[1] if len(sys.argv) > 1 else "all"
    if group != "all" and group not in CHECKS:
        print(
            "usage: validate_skill.py "
            "<workflow|production|visual|integrity|prompt|onboarding|"
            "platforms|contest|docs|all> [skill-root]"
        )
        return 2
    root = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else DEFAULT_ROOT
    selected = GROUPS if group == "all" else (group,)
    failures: list[str] = []
    for name in selected:
        try:
            CHECKS[name](root)
            print(f"PASS {name}")
        except AssertionError as exc:
            failures.append(f"FAIL {name}: {exc}")
    if failures:
        print("\n".join(failures))
        return 1
    if group == "all":
        print("PASS all")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
