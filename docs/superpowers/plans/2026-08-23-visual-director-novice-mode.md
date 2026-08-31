# 视觉导演与新手模式实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**目标：** 将 create-ip-op-poster 升级为具有四个确认点、视觉导演机制、项目级完整 Prompt 和低门槛跨平台引导的通用 Skill。

**架构：** 保持 SKILL.md 为唯一权威入口，将新手交互、视觉导演、素材保护、Prompt 编译和 QA 拆到职责单一的参考文件。使用一个无第三方依赖的 Python 校验器检查状态机、关键规则、文件链接和跨平台入口，再用四类人工场景回归验证实际对话质量。

**技术栈：** Markdown、YAML、Python 3 标准库、Git、GitHub 文件／提交接口。

## 全局约束

- 四个确认点不可跳过：创意方向、抠图素材、人物排布、完整 Prompt。
- 默认新手模式；熟练用户只能减少解释，不能跳过确认。
- 人物和动物长相不得改变；案例截图和 Logo 始终严格保真。
- 视觉案例只学习抽象语法，不复制标题、文案、Logo、印章、专属容器、具体排布或标志性装饰。
- “秋日百味剧场”只作为 Prompt 完整度基准，不成为默认季节、风格或版式。
- 视觉母题、版式、密度和人物模式必须由当前 Brief 决定。
- 不具备保真抠图或图层合成能力的平台必须输出交接包，不得声称已经完成。
- 用户界面使用普通中文，每轮最多提出一个会改变结果的问题。

---

## 文件结构

### 新增文件

- `references/novice-mode.md`：新手默认交互、四步话术和信息隐藏规则。
- `references/visual-director.md`：六项视觉判断、六类版式家族、案例检索和美观预检。
- `examples/quick-start.md`：支持 Skill 的 Agent 平台快速启动。
- `examples/chatgpt-starter.md`：ChatGPT、豆包、Coze 等平台可复制启动语。
- `examples/successful-prompt-benchmark.md`：“秋日百味剧场”完整 Prompt 基准及可学／禁抄说明。
- `tests/validate_skill.py`：静态结构与关键规则校验器。
- `tests/scenario-regression.md`：四类场景和回归结果记录。

### 修改文件

- `SKILL.md`：四阶段确认、状态机、加载路由和回退规则。
- `references/workflow.md`：拆分抠图确认与人物排布确认。
- `references/direction-framework.md`：精简方向卡和视觉证明字段。
- `references/layout-grammar.md`：六类核心版式及其变体。
- `references/material-integrity.md`：原图／抠图对照页和排布确认标准。
- `references/visual-case-library.md`：26 张案例的结构化标签和互补检索。
- `references/prompt-template.md`：版式结构、艺术指导和受保护图层三层 Prompt。
- `references/qa-checklist.md`：审美硬性失败项和四确认检查。
- `references/platform-usage.md`：新手与平台能力降级规则。
- `references/handoff-template.md`：新状态和独立抠图／排布记录。
- `agents/openai.yaml`：低门槛默认启动语。
- `README.md`：中文四步快速使用、安装和平台说明。

---

### 任务 1：建立可重复运行的校验器

**文件：**

- 新建：`tests/validate_skill.py`

**接口：**

- 输入：`python3 tests/validate_skill.py <workflow|visual|integrity|prompt|docs|all> [skill-root]`
- 输出：成功时打印 `PASS <group>` 并返回 0；失败时逐条打印 `FAIL ...` 并返回 1。

- [ ] **步骤 1：写入校验器**

创建以下完整文件：

```python
from __future__ import annotations

import re
import sys
from pathlib import Path


GROUPS = ("workflow", "visual", "integrity", "prompt", "docs")
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


def check_workflow(root: Path) -> None:
    skill = read(root, "SKILL.md")
    workflow = read(root, "references/workflow.md")
    novice = read(root, "references/novice-mode.md")
    handoff = read(root, "references/handoff-template.md")
    interface = read(root, "agents/openai.yaml")

    for needle in (
        "direction_pending",
        "cutout_pending",
        "composition_pending",
        "prompt_pending",
        "## Gate 1:",
        "## Gate 2:",
        "## Gate 3:",
        "## Gate 4:",
    ):
        require(skill, needle, "SKILL.md")
    forbid(skill, "three mandatory confirmation gates", "SKILL.md")
    forbid(skill, "collage_pending", "SKILL.md")

    for needle in ("Cutout gate", "Composition gate", "Prompt gate", "第 <n>/4 步"):
        require(workflow + novice, needle, "workflow/novice")
    for reply in ("选方向 1", "抠图通过", "排布通过", "确认生成"):
        require(novice, reply, "novice-mode.md")
    require(handoff, "cutout_pending", "handoff-template.md")
    require(handoff, "composition_pending", "handoff-template.md")
    require(interface, "Brief", "agents/openai.yaml")
    require(interface, "人物", "agents/openai.yaml")


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


def check_integrity(root: Path) -> None:
    integrity = read(root, "references/material-integrity.md")
    workflow = read(root, "references/workflow.md")
    qa = read(root, "references/qa-checklist.md")

    for needle in (
        "原图与透明底抠图并排",
        "棋盘格",
        "误删身体",
        "抠图通过",
        "统一群像",
        "按玩法分组",
        "独立人物",
        "主视觉人物",
    ):
        require(integrity + workflow, needle, "integrity/workflow")
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

    for reply in ("选方向 1", "抠图通过", "排布通过", "确认生成"):
        require(quick + chatgpt + readme, reply, "quick start docs")
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
    "visual": check_visual,
    "integrity": check_integrity,
    "prompt": check_prompt,
    "docs": check_docs,
}


def main() -> int:
    group = sys.argv[1] if len(sys.argv) > 1 else "all"
    if group != "all" and group not in CHECKS:
        print("usage: validate_skill.py <workflow|visual|integrity|prompt|docs|all> [skill-root]")
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
```

- [ ] **步骤 2：运行全量校验并确认旧版本失败**

运行：

```bash
python3 tests/validate_skill.py all
```

预期：返回 1；至少报告缺少 `references/novice-mode.md`、`references/visual-director.md` 和 `examples/successful-prompt-benchmark.md`。

- [ ] **步骤 3：提交校验器**

```bash
git add tests/validate_skill.py
git commit -m "test: add poster skill validation harness"
```

---

### 任务 2：实现四确认流程和新手模式

**文件：**

- 新建：`references/novice-mode.md`
- 修改：`SKILL.md`
- 修改：`references/workflow.md`
- 修改：`references/handoff-template.md`
- 修改：`agents/openai.yaml`

**接口：**

- 输入：任意 Brief、人物／动物原图和可选补充材料。
- 输出：固定四阶段用户界面；每阶段只要求一个明确回复。

- [ ] **步骤 1：运行流程校验并确认失败**

```bash
python3 tests/validate_skill.py workflow
```

预期：返回 1，首先报告缺少 `references/novice-mode.md`。

- [ ] **步骤 2：创建新手模式参考**

写入 `references/novice-mode.md`，内容必须包含：

```markdown
# 新手模式

新手模式默认开启。用户要求“精简模式”时可以减少解释，但四个确认点不能跳过。

## 启动语

请发送 Brief 和人物／动物原图。案例截图、Logo、固定文案、报价和合作权益都可以稍后补充，也可以不提供。

## 每一步的固定格式

第 <n>/4 步｜<步骤名称>

只展示：当前理解、推荐选项、当前决定所需信息、可直接复制的一句回复。
素材台账、能力报告、参考对比和图层表默认隐藏；出现冲突、缺失或能力限制时才展开。

## 四个标准回复

1. 选方向 1
2. 抠图通过
3. 排布通过
4. 确认生成

意思相同的明确表达可以接受。模糊评价、附件或局部修改不是确认。

## 提问规则

- 每轮最多询问一个会改变结果的问题。
- 可选材料缺失时继续推进，不反复追问。
- 报价和合作权益只在方向阶段询问一次；除非 Brief 强制要求，否则不阻塞。
- 推荐项始终放在第一位，并用一句普通中文说明理由。
```

- [ ] **步骤 3：改写 SKILL.md 的状态机和四个 Gate**

将状态机替换为：

```text
intake
  -> direction_pending
  -> cutout_pending
  -> composition_pending
  -> prompt_pending
  -> production
  -> qa
  -> complete

Any protected-image stage -> handoff when preservation is unavailable
```

将入口说明改为“四个强制确认点”，并设置四个独立标题：

```markdown
## Gate 1: confirm the IP direction
## Gate 2: confirm the cutout assets
## Gate 3: confirm the creator composition
## Gate 4: confirm the final generation Prompt
```

Gate 2 只处理原图、抠图和边缘确认；Gate 3 只处理人物模式、大小、分组、交叠和前后层级。加载路由增加 `novice-mode.md`。

- [ ] **步骤 4：同步 workflow.md**

将旧的 Creator-presentation gate 拆成：

```markdown
## 4. Cutout gate

展示原图与透明底抠图并排的确认页。用户回复“抠图通过”后才能排布。

## 5. Composition gate

从统一群像、按玩法分组、独立人物摆放、主视觉人物＋辅助分组中选择。用户回复“排布通过”后才能生成 Prompt。

## 6. Prompt gate

先展示制作摘要，再展示完整 Prompt。用户回复“确认生成”后才能成图。
```

更新阶段编号、回退规则和每轮 `第 <n>/4 步` 页脚。

- [ ] **步骤 5：更新 handoff 和默认启动语**

`handoff-template.md` 的状态列表加入 `cutout_pending` 和 `composition_pending`，并拆分：

```markdown
## Cutout review
- Status:
- Source/cutout comparison:
- Rejected subjects:
- Explicit confirmation:

## Creator composition
- Status:
- Presentation mode:
- Preview:
- Layer order:
- Explicit confirmation:
```

`agents/openai.yaml` 的默认提示改为：

```yaml
interface:
  display_name: "IP OP 海报共创"
  short_description: "从 Brief 和人物原图开始，四步完成保真 IP／OP 海报"
  default_prompt: "使用 $create-ip-op-poster。请先接收我的 Brief 和人物原图，从第 1/4 步创意方向开始，不要直接成图。"
```

- [ ] **步骤 6：运行流程校验**

```bash
python3 tests/validate_skill.py workflow
```

预期：打印 `PASS workflow`。

- [ ] **步骤 7：提交流程改造**

```bash
git add SKILL.md references/novice-mode.md references/workflow.md references/handoff-template.md agents/openai.yaml
git commit -m "feat: add four-gate novice poster workflow"
```

---

### 任务 3：实现视觉导演和结构化案例检索

**文件：**

- 新建：`references/visual-director.md`
- 修改：`references/direction-framework.md`
- 修改：`references/layout-grammar.md`
- 修改：`references/visual-case-library.md`

**接口：**

- 输入：Brief 事实、达人玩法关系、素材数量和可选案例。
- 输出：六项视觉导演判断、2—4 张互补参考和可执行的方向卡。

- [ ] **步骤 1：运行视觉校验并确认失败**

```bash
python3 tests/validate_skill.py visual
```

预期：返回 1，报告缺少 `references/visual-director.md`。

- [ ] **步骤 2：创建视觉导演参考**

`references/visual-director.md` 使用以下完整结构：

```markdown
# 视觉导演

## 六项必做判断

1. 内容关系：并列、顺序、主次、场景、中心发散、证据、矩阵或情绪宣言。
2. 版式家族：概念场景、群像主视觉、玩法分舱、路线阶段、矩阵档案、编辑拼贴，或有充分理由的新结构。
3. 视觉母题：用一个当前 Brief 专属的视觉世界统一标题、背景、容器、材质和装饰。
4. 人物模式：统一群像、按玩法分组、独立人物、主视觉人物＋辅助分组。
5. 信息密度：低、中或高；每一块主要留白都要写明用途。
6. 层级与景深：写明第一视觉、第二层玩法、第三层证据，以及前景、中景、背景。

## 互补参考

- 结构参考：学习阅读路径和区域关系。
- 密度参考：学习如何用编号、对齐、颜色编码和重复模块承载信息。
- 气质参考：学习色彩关系、材质、标题能量和画面情绪。

同一案例最多承担两个角色，并且必须再选一张结构不同的案例。

每张案例记录：参考角色、可借鉴抽象语法、本次差异、禁止复制元素。

## 六类版式

- 概念场景：一个行业或节点隐喻贯穿整页。
- 群像主视觉：标题与人物共同建立第一视觉。
- 玩法分舱：每个玩法拥有自己的人物、机制和证据。
- 路线阶段：只在内容确有先后关系时使用。
- 矩阵档案：用稳定网格、编号和颜色编码承载复杂映射。
- 编辑拼贴：用非对称尺度和材质变化建立节奏。

## 美观预检

- 第一视觉是否明确。
- 人物是否进入对应玩法。
- 主要留白是否都有用途。
- 标题、人物、模块是否有大小节奏。
- 是否形成前景、中景和背景。
- 装饰是否服务视觉母题。
- 高密度信息是否仍可快速扫描。
- 是否出现行业套路，例如“数码＝蓝色霓虹科技界面”。

任一项失败时，先修正方向或排布，不生成最终 Prompt。
```

- [ ] **步骤 3：把版式语法收束成六个核心家族**

在 `layout-grammar.md` 中保留现有 12 种结构的能力，但将它们映射到六个核心家族：

```markdown
| 核心家族 | 可用变体 |
|---|---|
| 概念场景 | 左右叙事、中心发散、情绪宣言 |
| 群像主视觉 | 舞台层级、主角＋辅助群像 |
| 玩法分舱 | 纵向栏目、分组岛、上下矩阵 |
| 路线阶段 | 时间线、接力、分镜 |
| 矩阵档案 | 横向信息带、证据墙、混合提案 |
| 编辑拼贴 | 杂志拼贴、纸张拼贴、场景切片 |
```

每个方向同时写明阅读顺序、第一视觉、区域分配、密度、人物模式、留白用途和构图风险。

- [ ] **步骤 4：更新方向卡**

`direction-framework.md` 的用户可见方向卡固定为：

```markdown
### 方向 <数字>｜<主题名>
- 一句话主题：
- 具体玩法：
- 人物怎么放：
- 视觉氛围：
- 主要风险：
- 推荐理由：
```

内部视觉记录增加：

```markdown
- 内容关系：
- 版式家族：
- 阅读顺序：
- 区域分配：
- 第一视觉：
- 信息密度：
- 视觉母题：
- 人物与玩法映射：
- 案例／数据位置：
- 留白用途：
- 构图风险：
```

- [ ] **步骤 5：给 26 张案例增加结构化标签**

在 `visual-case-library.md` 增加以下索引，保留现有逐图说明：

```markdown
| ID | 核心家族 | 内容关系 | 密度 | 人物模式 | 优先参考角色 |
|---|---|---|---|---|---|
| VC01 | 概念场景 | 场景 | 中 | 少人物／无群像 | 结构＋气质 |
| VC02 | 概念场景 | 情绪宣言 | 低 | 无群像 | 结构＋气质 |
| VC03 | 群像主视觉 | 矩阵＋证据 | 高 | 统一／分组 | 密度 |
| VC04 | 矩阵档案 | 矩阵 | 高 | 统一名单 | 密度 |
| VC05 | 玩法分舱 | 并列 | 高 | 按玩法分组 | 密度＋气质 |
| VC06 | 玩法分舱 | 并列 | 高 | 按玩法分组 | 结构＋气质 |
| VC07 | 路线阶段 | 顺序＋证据 | 高 | 独立人物 | 结构＋密度 |
| VC08 | 概念场景 | 矩阵＋证据 | 高 | 独立人物 | 气质 |
| VC09 | 矩阵档案 | 矩阵 | 高 | 按玩法分组 | 密度 |
| VC10 | 玩法分舱 | 并列 | 中 | 按玩法分组 | 结构＋气质 |
| VC11 | 群像主视觉 | 主次 | 高 | 统一主视觉 | 气质 |
| VC12 | 概念场景 | 情绪宣言 | 低 | 无群像 | 结构 |
| VC13 | 编辑拼贴 | 顺序 | 低 | 无群像 | 气质 |
| VC14 | 玩法分舱 | 并列 | 中 | 独立人物 | 结构 |
| VC15 | 群像主视觉 | 中心发散＋证据 | 高 | 统一群像 | 结构＋密度 |
| VC16 | 路线阶段 | 顺序 | 高 | 独立人物 | 结构＋密度 |
| VC17 | 群像主视觉 | 主次 | 中 | 统一群像 | 结构 |
| VC18 | 编辑拼贴 | 场景＋证据 | 高 | 统一群像 | 气质＋密度 |
| VC19 | 群像主视觉 | 主次 | 高 | 统一群像 | 气质 |
| VC20 | 路线阶段 | 顺序 | 高 | 独立人物 | 结构＋气质 |
| VC21 | 群像主视觉 | 主次 | 中 | 主视觉＋分组 | 气质 |
| VC22 | 概念场景 | 场景 | 中 | 独立人物 | 气质 |
| VC23 | 矩阵档案 | 并列＋证据 | 高 | 按玩法分组 | 密度 |
| VC24 | 编辑拼贴 | 矩阵＋宣言 | 高 | 独立人物 | 结构 |
| VC25 | 玩法分舱 | 并列 | 高 | 按玩法分组 | 结构＋气质 |
| VC26 | 矩阵档案 | 顺序＋矩阵 | 高 | 混合 | 结构＋密度 |
```

- [ ] **步骤 6：运行视觉校验**

```bash
python3 tests/validate_skill.py visual
```

预期：打印 `PASS visual`。

- [ ] **步骤 7：提交视觉导演**

```bash
git add references/visual-director.md references/direction-framework.md references/layout-grammar.md references/visual-case-library.md
git commit -m "feat: add visual director and case retrieval grammar"
```

---

### 任务 4：强化抠图确认、排布确认和素材保护

**文件：**

- 修改：`references/material-integrity.md`
- 修改：`references/workflow.md`
- 修改：`references/qa-checklist.md`

**接口：**

- 输入：原始人物／动物图片和已确认方向。
- 输出：原图／抠图对照页、通过的独立抠图、完整排布预览和素材保护证据。

- [ ] **步骤 1：运行素材校验并确认失败**

```bash
python3 tests/validate_skill.py integrity
```

预期：返回 1，报告缺少原图／抠图对照或独立排布检查文字。

- [ ] **步骤 2：加入抠图对照页规范**

在 `material-integrity.md` 增加：

```markdown
## 抠图确认页

- 原图与透明底抠图并排，使用相同编号和公开昵称。
- 抠图放在棋盘格和中性纯色背景上各检查一次。
- 检查脸、发型、头发边缘、衣服、手脚、宠物毛发和原始组合关系。
- 标注原图本身缺失的身体区域，不允许生成补全。
- 发现误删身体、误删宠物、脸部变化或边缘硬切时判定失败。
- 用户明确回复“抠图通过”后，才可以制作人物排布。
```

- [ ] **步骤 3：加入人物排布规范**

增加四种模式及统一验收：

```markdown
## 人物排布确认

- 统一群像：所有人物共同表达一个承诺。
- 按玩法分组：每组人物紧邻自己的玩法和证据。
- 独立人物：人物作为独立受保护图层进入不同位置。
- 主视觉人物＋辅助分组：一个主角或主群像负责第一视觉，其余人物保留在对应模块。

排布预览必须检查：人物大小、前后层级、真实交叠、人脸安全区、动物头部安全区、重复、遗漏、硬矩形边界、无意义空白和远离主体的人物。
```

- [ ] **步骤 4：同步回退和 QA**

在 `workflow.md` 中写明：

- 单个抠图失败只回到 `cutout_pending`；
- 人物分组、大小或层级变化回到 `composition_pending`；
- 人脸或动物头部变化属于硬失败，不能用生成式修脸。

在 `qa-checklist.md` 增加独立的 Cutout 和 Composition 检查表。

- [ ] **步骤 5：运行素材校验**

```bash
python3 tests/validate_skill.py integrity
```

预期：打印 `PASS integrity`。

- [ ] **步骤 6：提交素材确认机制**

```bash
git add references/material-integrity.md references/workflow.md references/qa-checklist.md
git commit -m "feat: split cutout and composition review"
```

---

### 任务 5：升级完整 Prompt 模板并加入成功基准

**文件：**

- 修改：`references/prompt-template.md`
- 新建：`examples/successful-prompt-benchmark.md`

**接口：**

- 输入：已确认方向、已确认抠图、已确认排布、素材台账和固定文案。
- 输出：项目级完整 Prompt；不保留未填写占位符。

- [ ] **步骤 1：运行 Prompt 校验并确认失败**

```bash
python3 tests/validate_skill.py prompt
```

预期：返回 1，报告缺少成功基准或三层 Prompt 标题。

- [ ] **步骤 2：将 Prompt 模板改为三层可执行结构**

`prompt-template.md` 的完整模板使用以下章节顺序：

```text
请设计一张 <已确认画幅、尺寸、行业和用途> 的招商 OP 海报。<已确认质量目标>。

【任务边界】
这是分层排版与合成任务。人物、动物、案例截图和 Logo 是受保护图层，不允许重新绘制。

【主题与背景】
项目主题：
主题文案：
精炼项目背景：

【视觉导演结论】
内容关系：
版式家族：
视觉母题：
人物模式：
信息密度：
第一视觉与前中后景：

【版式结构层】
画布与安全边距：
区域比例：
阅读顺序：
第一视觉：
主要留白用途：
底部区域：

【玩法内容】
1. <组名>
标题：
成员：
一句玩法：
案例截图：
与其他组的差异：

【人物与动物排布】
逐一写明编号、公开昵称、所属玩法、位置、相对大小、前后层级、交叠关系和脸部／动物头部安全区。

【案例截图】
逐一写明编号、所属玩法、排列方式、完整显示比例。不得裁切、改字、改数据、调色、重绘或虚构。

【Logo】
逐一写明编号、位置、相对大小。不得重绘、改字、漏元素或擅自改色。

【艺术指导层】
主背景色及作用：
标题与强调色：
正文色：
辅助色及使用上限：
标题形式：
材质与容器：
前景／中景／背景：
允许装饰及上限：

【受保护图层表】
P：人物／动物
C：案例截图
L：Logo
T：固定文案

【固定文案与底部信息】
逐字列出必须出现的文字；未确认的报价、权益或合作方式不得出现。

【参考边界】
只学习抽象信息层级和视觉语法，不复制参考案例的具体元素。

【美观预检】
第一视觉、人物与玩法、大小节奏、留白用途、前中后景、装饰相关性和信息可读性全部通过。

【输出与验收】
逐条列出尺寸、格式、人物数量、截图数量、中文准确性、素材保真和禁止虚构项。

【负面要求】
逐条列出当前项目禁止出现的视觉、业务和素材变化。
```

填充规则：

- 删除不适用章节，不写“无”。
- 完整 Prompt 展示给用户前，替换所有尖括号占位。
- “人物第一视觉”“人物大于文字”等要求只在已确认方向需要时写入。
- 每个抽象视觉词必须落到颜色、材质、布局、层级或装饰规则。

- [ ] **步骤 3：创建成功 Prompt 基准**

`examples/successful-prompt-benchmark.md` 包含以下说明和用户原始案例全文：

```markdown
# 成功 Prompt 基准：秋日百味剧场

## 用途

本案例用于检查 Prompt 的完整度、映射准确性和可执行性。成功基准包括：明确比例、逐组玩法、人物顺序、六张案例截图的严格映射、具体视觉语言、底部固定信息和完整负面要求。

## 不得固化

不得把中秋、秋日、左文右人、奶油米色、圆月、桂花、胶片或“人物第一视觉”变成其他项目的默认规则。

## 原始成功案例
```

随后复制本计划“附录 A：成功 Prompt 原文”的完整文本，逐字放入 `examples/successful-prompt-benchmark.md`。保持标题、达人名称、六张截图映射、固定文案和禁止项原样，不做精简或改写。

- [ ] **步骤 4：运行 Prompt 校验**

```bash
python3 tests/validate_skill.py prompt
```

预期：打印 `PASS prompt`。

- [ ] **步骤 5：提交 Prompt 升级**

```bash
git add references/prompt-template.md examples/successful-prompt-benchmark.md
git commit -m "feat: add project-level poster prompt compiler"
```

---

### 任务 6：完成审美 QA 和四类场景回归

**文件：**

- 修改：`references/qa-checklist.md`
- 新建：`tests/scenario-regression.md`

**接口：**

- 输入：四个模拟项目及对应阶段输出。
- 输出：每个场景的 PASS／FAIL／NOT VERIFIABLE 结果和回退阶段。

- [ ] **步骤 1：补充审美硬性失败项**

在 `qa-checklist.md` 增加：

```markdown
### Aesthetic hard failures

- 看不出第一视觉。
- 出现大块无意义空白。
- 人物与玩法脱节。
- 人物像孤立贴纸一样悬在版面上。
- 标题或装饰覆盖人脸或动物头部。
- 没有形成前景、中景和背景。
- 非并列内容被错误设计成完全相同的权重。
- 视觉风格与确认方向不一致。
- 擅自沿用秋日、科技蓝、霓虹界面或其他旧项目套路。
- 复制参考案例的独特标题、容器、Logo、印章、装饰或具体排布。
```

同时将流程检查由三个 Gate 改为四个 Gate。

- [ ] **步骤 2：创建场景回归文件**

`tests/scenario-regression.md` 使用以下测试表：

```markdown
# 场景回归

## 场景 1：多人、高信息密度

输入：数码“新机搭子已就位”Brief，多位达人，有玩法建议，无固定视觉风格。
检查：不能自动使用科技蓝；先判断分组／独立／混合；方向卡包含六项视觉判断；Prompt 达到成功基准的具体程度。

## 场景 2：单达人、视觉优先

输入：单个达人、一个核心玩法、少量证据。
检查：不能强制矩阵；必须说明达人具体做什么；可选证据不挤压第一视觉。

## 场景 3：新手极简输入

输入：只有 Brief 和人物图。
检查：只问一个决定；显示第 1/4 步；报价、案例和 Logo 不成为必填。

## 场景 4：平台能力不足

输入：完整 Brief 和素材，但平台只能生成图片，不能保真抠图或分层合成。
检查：在 cutout_pending 停止；输出交接包；不生成近似人物。

## 回归结果

| 场景 | 方向 | 抠图 | 排布 | Prompt | 美观 | 素材安全 | 结果 |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |
```

- [ ] **步骤 3：逐场景执行干跑**

每个场景使用一段新的对话上下文读取更新后的 SKILL.md，只生成当前 Gate 所需产物。按 `qa-checklist.md` 记录 PASS、FAIL 或 NOT VERIFIABLE。任何失败都先修复负责文件，再重跑该场景。

预期：

- 场景 1 能产生非科技套路的 2—3 个方向；
- 场景 2 能产生单人专属玩法和非矩阵版式；
- 场景 3 只显示当前决定和标准回复；
- 场景 4 明确交接，不声称成图完成。

- [ ] **步骤 4：填写回归结果**

将四行结果全部填写为 `PASS`，并在表后写明每个场景使用的方向、参考案例角色和已验证限制。若存在 NOT VERIFIABLE，保留该状态并列出缺少的验证能力，不能改写成 PASS。

- [ ] **步骤 5：提交 QA 和回归记录**

```bash
git add references/qa-checklist.md tests/scenario-regression.md
git commit -m "test: add aesthetic and scenario regression checks"
```

---

### 任务 7：完成跨平台新手文档

**文件：**

- 新建：`examples/quick-start.md`
- 新建：`examples/chatgpt-starter.md`
- 修改：`references/platform-usage.md`
- 修改：`README.md`

**接口：**

- 输入：用户所在平台和可用图片能力。
- 输出：一段可复制启动语、四步回复和能力不足时的交接说明。

- [ ] **步骤 1：运行文档校验并确认失败**

```bash
python3 tests/validate_skill.py docs
```

预期：返回 1，报告缺少 quick-start 或 chatgpt-starter。

- [ ] **步骤 2：创建支持 Skill 平台的快速启动**

`examples/quick-start.md` 写入：

```markdown
# 快速开始

1. 安装完整 create-ip-op-poster 文件夹。
2. 上传 Brief 和人物／动物原图。
3. 发送：

请使用 $create-ip-op-poster，从第 1/4 步开始。先给我 2—3 个创意方向，不要直接成图。

后续只需依次回复：

- 选方向 1
- 抠图通过
- 排布通过
- 确认生成

案例截图、Logo、固定文案、报价和合作权益都可以不提供。
```

- [ ] **步骤 3：创建 ChatGPT 等平台启动语**

`examples/chatgpt-starter.md` 写入：

```markdown
# ChatGPT／豆包／Coze 启动语

复制以下内容后，再上传 Brief 和人物原图：

请按 create-ip-op-poster 的四步流程协助我：
1. 先给 2—3 个创意方向，让我回复数字选择；
2. 抠图完成后必须展示原图与抠图对照，让我确认；
3. 人物排布完成后必须让我确认大小、遮挡和前后层级；
4. 完整成图 Prompt 必须让我确认。

不许改变人物或动物长相，不许改案例截图和 Logo。每次只问我一个问题；没有案例、Logo 或报价也可以继续。

如果你不能保真人物抠图或分层合成，请停止在对应步骤，输出交接包，不要重新生成人物。
```

- [ ] **步骤 4：更新平台说明和 README**

`platform-usage.md` 增加：

- 新手默认只上传 Brief 和人物图；
- 支持 Skill、知识库平台、ChatGPT 普通会话三条路径；
- 四个标准回复；
- 平台能力不足时交接包必须包含方向、素材台账、已确认抠图或抠图说明、排布图层表、完整 Prompt 和 QA 限制。

`README.md` 首页先显示“四步使用”，再显示安装方式和完整规则。删除“三个强制确认节点”的旧描述。

- [ ] **步骤 5：运行文档和全量校验**

```bash
python3 tests/validate_skill.py docs
python3 tests/validate_skill.py all
```

预期：依次打印 `PASS docs`，随后五个分组全部 PASS。

- [ ] **步骤 6：提交跨平台文档**

```bash
git add README.md references/platform-usage.md examples/quick-start.md examples/chatgpt-starter.md
git commit -m "docs: add low-friction cross-platform poster guide"
```

---

### 任务 8：集成验证、本地安装和公开仓库同步

**文件：**

- 验证：全部项目文件
- 更新安装目录：`/Users/bytedance/.codex/skills/create-ip-op-poster`
- 发布仓库：`nmmg0112/create-ip-op-poster-skill`

**接口：**

- 输入：已通过全部校验和场景回归的项目目录。
- 输出：本地安装版本与 GitHub main 内容一致。

- [ ] **步骤 1：执行最终静态检查**

```bash
python3 tests/validate_skill.py all
git diff --check
git status --short
```

预期：五个分组全部 PASS；无空白错误；只显示已知计划文件或工作区干净。

- [ ] **步骤 2：检查旧规则残留**

```bash
rg -n "three mandatory|三个强制|collage_pending|Gate 3: confirm the final" SKILL.md README.md references agents examples
```

预期：没有旧“三确认”或 `collage_pending`；最终 Prompt 标题应为 Gate 4。

- [ ] **步骤 3：提交最终整合修正**

如果最终检查产生修正：

```bash
git add SKILL.md README.md agents references examples tests
git commit -m "fix: align poster skill workflow and validation"
```

如果没有修正，不创建空提交。

- [ ] **步骤 4：安装到本地 Skill 目录**

先确认目标：

```bash
test -d /Users/bytedance/.codex/skills/create-ip-op-poster
```

然后同步操作文件，不删除目标中的未知文件：

```bash
rsync -a SKILL.md /Users/bytedance/.codex/skills/create-ip-op-poster/
rsync -a agents references assets examples /Users/bytedance/.codex/skills/create-ip-op-poster/
```

运行安装副本校验：

```bash
python3 tests/validate_skill.py all /Users/bytedance/.codex/skills/create-ip-op-poster
```

预期：五个分组全部 PASS。

- [ ] **步骤 5：比较公开仓库**

```bash
git fetch origin
git diff --name-status origin/main -- SKILL.md README.md agents references examples tests docs
```

预期：只列出本次计划涉及的文本文件。assets 中已有 26 张案例，不重新上传未变化的二进制文件。

- [ ] **步骤 6：发布到 GitHub main**

由于本地仓库和公开仓库历史不共祖，不执行强推。以 `origin/main` 的最新提交为父提交，通过已授权的 GitHub 文件／提交接口：

1. 为新增和修改的文本文件创建 blob；
2. 以远端 main 的 tree 为 base tree 创建新 tree；
3. 创建提交，信息为 `feat: add visual director and novice poster workflow`；
4. 将 `refs/heads/main` 更新到新提交；
5. 不修改未变化的视觉案例文件。

预期：main 前进一个提交，历史保留。

- [ ] **步骤 7：发布后验证**

重新读取 GitHub 上的以下文件并与本地比较：

- `SKILL.md`
- `references/novice-mode.md`
- `references/visual-director.md`
- `references/prompt-template.md`
- `examples/successful-prompt-benchmark.md`
- `README.md`

确认远端存在四个 Gate、成功 Prompt 基准和 ChatGPT 启动语。最后记录远端提交 SHA 和仓库链接。

- [ ] **步骤 8：交付**

向用户提供：

- 更新完成的一句话结论；
- 四个确认点；
- 本地 Skill 路径；
- GitHub 链接和提交；
- 四类测试结果；
- 一句最简启动语。

---

## 附录 A：成功 Prompt 原文

以下文本必须逐字写入 `examples/successful-prompt-benchmark.md` 的“原始成功案例”章节：

```text
请设计一张 16:9 横版中秋食饮类达人矩阵招商海报，高清商业提案质感，信息精简、视觉优先。
不许改变原图人脸，案例截图上的文字，
【主题】
项目主题：秋日百味剧场
主题文案：每一种秋味，都有自己的出场方式

【版式】
采用左文右人的横版结构：
- 左侧约 60%：主题信息 + 三个子主题玩法，每个子主题固定放 2 张真实案例截图。
- 右侧约 40%：放大展示全部达人和萌宠的抠图群像，人物是第一视觉重点，尺寸明显大于案例截图。
- 底部仅保留简短合作信息，不放冗长品类说明。

整体留白充足，不要堆文字。每个子主题只保留“标题 + 一句玩法 + 两张截图”，不写细分适配品类，不写长段解释。

【左侧三个子主题】

1. 秋日家庭团圆
标题：回家这一口，才叫入秋
达人：沸羊羊（回家版）、包子好
玩法短句：用返乡、家宴与代际互动，把秋日新品自然写进团圆轻喜剧。
案例截图：放置家庭团圆案例截图 1、2，两张并排。

2. 秋日聚会出游
标题：人一到齐，秋天就开席
达人：五百次快递、丰丰丰丰、于鱼丘比特
玩法短句：用好友局、情侣互动与出游反转，让新品成为聚会和野餐的气氛担当。
案例截图：放置聚会出游案例截图 1、2，两张并排。

3. 萌宠秋日上新
标题：秋天第一口，萌宠先来围观
达人：憨憨猪大虫、猪大肠&方一蛋、屋内有饿犬
玩法短句：突出猫咪“方师傅”精准接水的账号记忆点，结合新品开箱与萌宠反应制造轻松剧情。
案例截图：放置萌宠上新案例截图 1、2，两张并排，其中一张优先展示“方师傅精准接水”。

【右侧达人群像】
使用提供的真实人物和动物素材进行抠图拼贴，人物与萌宠整体占据右侧主要区域，画面大、清晰、有层次，允许轻微前后错落，但不能遮挡脸部和动物主体。

按以下顺序组织：
- 家庭团圆：沸羊羊（回家版）、包子好
- 聚会出游：五百次快递、丰丰丰丰、于鱼丘比特
- 萌宠上新：憨憨猪大虫、猪大肠&方一蛋、屋内有饿犬

达人昵称只写上述名称，禁止出现“-柒捌”“-捌玖”“2-捌玖”等文件名后缀。保留原脸、发型、服装、表情、姿势、宠物品种、毛色和原始组合关系；不要新增陌生人物，不要漏人，不要重复人物，不要把真人卡通化。

【案例截图要求】
图1是人物图，图2-7是案例截图，图8是参考图，不许照抄图8
全海报共 6 张真实案例截图，每个子主题严格对应 2 张。截图使用统一比例、圆角和细边框，尺寸足够清晰；保留原始画面、人物、标题和真实数据，不重绘、不篡改、不虚构点赞量或播放量。

【视觉风格】
参考前两张海报的信息层级和秋日氛围，但不要照抄版式、标题、卷轴、logo、印章或文案。采用年轻化“秋日开席 × 剧情片场”风格，主色为奶油米色、桂花金、柿子橙和深墨绿，少量朱红点题；可加入圆月、桂花、秋叶、野餐布和胶片分镜元素，但装饰必须克制。

【底部合作信息】
仅保留：短视频植入｜达人矩阵共创｜节点主题专场
收束文案：让产品进入剧情，让秋味留在记忆里。
不要出现“短直联动”、直播承接或其他短直玩法。

【输出要求】
中文清晰准确、无乱码。人物图大于文字区和案例截图，右侧群像需要成为视觉焦点。不要密集小字，不写细分适配品类，不添加虚构粉丝量、播放量、点赞量、客户名称或合作案例。保持安全边距，文字不压脸，截图不裁切。
```
