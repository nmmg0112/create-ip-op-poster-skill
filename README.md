# create-ip-op-poster-skill

一份用于制作中文 IP / OP 招商海报的通用 Agent Skill。

它不把 OP 当成“一次生图”，而是将工作拆成创意方向、人物呈现、最终 Prompt 和成图 QA 四个部分，并通过三个强制确认节点降低返工与素材被 AI 改写的风险。

## 适用场景

- IP 征集海报
- OP 招商海报
- 达人矩阵方案图
- 单人达人提报图
- 人物/动物抠图与分组呈现
- 海报生成 Prompt
- 案例截图、Logo 和人物素材的保真合成

## 核心流程

1. 用户提供 Brief、达人素材、案例截图与具体建议。
2. Skill 提供 2–3 个真正不同的创意方向，等待用户确认。
3. 根据玩法关系选择人物呈现方式：统一群像、按玩法分组、独立摆放，或主视觉＋分组混合。
4. 人物/动物图完成后暂停，等待用户确认长相、数量、归属和层级。
5. 生成完整成图 Prompt，再次暂停并等待确认。
6. 人物、动物、案例截图和 Logo 作为受保护图层合成，最后逐项 QA。

## 不可违反的规则

- 不改变任何人的脸、五官、发型、表情和可识别特征。
- 不改变动物的脸、品种、毛色和原始组合关系。
- 案例截图只能等比缩放和摆放，不裁切、不改字、不改数据、不重绘。
- Logo 保留所有元素，只允许去背景、等比缩放和排列。
- 参考海报只用于学习信息层级与视觉语法，不照抄文案、Logo、版式或独特视觉符号。

## 目录结构

```text
create-ip-op-poster/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── direction-framework.md
│   ├── layout-grammar.md
│   ├── material-integrity.md
│   ├── prompt-template.md
│   ├── visual-case-library.md
│   ├── qa-checklist.md
│   ├── platform-usage.md
│   └── handoff-template.md
└── assets/
    └── visual-cases/
```

## 使用方式

### Codex / Claude Code 等支持文件式 Skill 的 Agent

1. 将整个目录复制到对应平台的 Skills 目录。
2. 确保 Agent 先读取 `SKILL.md`。
3. 使用时提供 Brief、人物/动物原图、案例截图和必须出现的文案。

示例启动语：

```text
请使用 create-ip-op-poster Skill。
以下是本次 IP 征集 Brief、达人素材和案例截图。
请先分析 Brief，给我 2–3 个创意方向，不要直接成图。
```

### Coze / 扣子 / WorkBuddy 等平台

将 `SKILL.md` 与任务所需的 `references/` 文件作为知识或工作流指令导入。若平台不支持受保护图层合成，Skill 会退化为执行规格和交付包，不应声称已完成原图保真成图。

## 视觉案例库说明

`assets/visual-cases/` 用于教 Agent 识别 IP / OP 海报的信息层级、版式结构、人物呈现方式和信息密度。

这些图片仅作为视觉研究参考，不代表获得原作品的改编、复制或商业使用授权。使用者必须自行判断并遵守素材的权利边界。

## 许可说明

当前仓库暂未添加开源许可证。请勿将仓库公开可访问等同于获得代码、文档或视觉案例的自由使用授权。
