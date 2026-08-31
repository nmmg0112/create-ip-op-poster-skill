from __future__ import annotations

import re
import sys
from pathlib import Path


GROUPS = ("workflow", "production", "visual", "integrity", "prompt", "docs")
DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise AssertionError(f"missing file: {relative}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


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
    handoff = read(root, "references/handoff-template.md")
    interface = read(root, "agents/openai.yaml")

    for needle in (
        "person_material_pending",
        "direction_and_mode_pending",
        "prompt_pending",
        "人物素材通过",
        "确认生成",
    ):
        require(skill + workflow + novice, needle, "workflow")

    require_order(skill, "person_material_pending", "direction_and_mode_pending", "SKILL.md")

    for legacy in (
        "composition_pending",
        "排布通过",
        "four mandatory confirmation gates",
        "四个确认点不能跳过",
        "第 <n>/4 步",
    ):
        forbid(skill + workflow + novice, legacy, "workflow")

    for needle in (
        "person_material_pending",
        "direction_and_mode_pending",
        "generation_mode",
        "formal_generation_count",
    ):
        require(handoff, needle, "handoff-template.md")
    require(interface, "Brief", "agents/openai.yaml")
    require(interface, "人物", "agents/openai.yaml")


def check_production(root: Path) -> None:
    skill = read(root, "SKILL.md")
    workflow = read(root, "references/workflow.md")
    prompt = read(root, "references/prompt-template.md")
    platform = read(root, "references/platform-usage.md")
    qa = read(root, "references/qa-checklist.md")
    corpus = "\n".join((skill, workflow, prompt, platform, qa))

    for needle in (
        "模式 A：快速生图",
        "模式 B：保真合成",
        "PNG、WebP 或 JPEG",
        "第一项生产动作必须调用生图模型",
        "不得先运行 SVG、HTML、Canvas、PPT",
        "默认只调用一次正式生图",
        "完整海报预览",
    ):
        require(corpus, needle, "generative production contract")

    require_order(
        workflow,
        "生成主视觉位图底图",
        "保护图层覆回",
        "references/workflow.md",
    )


def check_visual(root: Path) -> None:
    director = read(root, "references/visual-director.md")
    layout = read(root, "references/layout-grammar.md")
    cases = read(root, "references/visual-case-library.md")
    direction = read(root, "references/direction-framework.md")

    for needle in (
        "内容关系",
        "版式家族",
        "视觉母题",
        "人物模式",
        "信息密度",
        "层级与景深",
        "结构参考",
        "密度参考",
        "气质参考",
        "美观预检",
    ):
        require(director, needle, "visual-director.md")
    for family in ("概念场景", "群像主视觉", "玩法分舱", "路线阶段", "矩阵档案", "编辑拼贴"):
        require(layout, family, "layout-grammar.md")
    for case_id in (f"VC{i:02d}" for i in range(1, 27)):
        require(cases, case_id, "visual-case-library.md")
    for field in ("阅读顺序", "区域分配", "第一视觉", "留白用途", "构图风险"):
        require(direction, field, "direction-framework.md")

    # An industry category may guide retrieval, but it must never become the
    # evidence for a palette, material, container, or motif. Keep this policy in
    # both the visual-director preflight and the direction-generation rules.
    for text, label in (
        (director, "visual-director.md"),
        (direction, "direction-framework.md"),
    ):
        require(text, "行业标签本身不是表面风格证据", label)
        require(text, "数码＝科技蓝／霓虹／玻璃／UI／控制台", label)
        require(text, "推荐方向必须以 Brief 专属的人物行动或内容机制作为视觉母题", label)
        for evidence in ("Brief 原文", "受众情绪", "人物／账号证据", "品牌规则", "内容机制"):
            require(text, evidence, label)


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

    for needle in (
        "横版白底组合预览图",
        "透明底人物总图",
        "独立透明抠图",
        "人物素材通过",
    ):
        require(skill + integrity + workflow, needle, "integrity/workflow")
    for needle in ("人脸", "动物头部", "重复", "遗漏", "硬矩形边界", "无意义空白"):
        require(qa + integrity, needle, "qa/integrity")


def check_prompt(root: Path) -> None:
    prompt = read(root, "references/prompt-template.md")
    benchmark = read(root, "examples/successful-prompt-benchmark.md")
    qa = read(root, "references/qa-checklist.md")

    for needle in (
        "【版式结构层】",
        "【艺术指导层】",
        "【受保护图层表】",
        "【玩法内容】",
        "【美观预检】",
        "区域比例",
        "前景",
        "中景",
        "背景",
    ):
        require(prompt, needle, "prompt-template.md")
    for needle in ("秋日百味剧场", "每一种秋味，都有自己的出场方式", "成功基准", "不得固化"):
        require(benchmark, needle, "successful-prompt-benchmark.md")
    for needle in ("第一视觉", "无意义空白", "人物与玩法", "参考案例"):
        require(qa, needle, "qa-checklist.md")
    forbid(prompt, "人物/动物整体必须大于案例截图并成为视觉重点", "prompt-template.md")


def check_docs(root: Path) -> None:
    platform = read(root, "references/platform-usage.md")
    quick = read(root, "examples/quick-start.md")
    chatgpt = read(root, "examples/chatgpt-starter.md")
    readme = read(root, "README.md")

    active_docs = "\n".join((quick, chatgpt, readme))
    for reply in ("人物素材通过", "确认生成"):
        require(active_docs, reply, "quick start docs")
    forbid(active_docs, "排布通过", "quick start docs")
    for needle in ("ChatGPT", "豆包", "Coze", "交接包"):
        require(platform + chatgpt + readme, needle, "cross-platform docs")

    markdown_files = [
        root / "SKILL.md",
        root / "README.md",
        *sorted((root / "references").glob("*.md")),
        *sorted((root / "examples").glob("*.md")),
    ]
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
    "docs": check_docs,
}


def main() -> int:
    group = sys.argv[1] if len(sys.argv) > 1 else "all"
    if group != "all" and group not in CHECKS:
        print(
            "usage: validate_skill.py "
            "<workflow|production|visual|integrity|prompt|docs|all> [skill-root]"
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
