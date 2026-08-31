# 快速开始

适用于 Codex、Claude Code 等支持文件式 Skill 的 Agent。

## 1. 安装

Codex 用户直接发送：

```text
请使用 $skill-installer，从 https://github.com/nmmg0112/create-ip-op-poster-skill 安装根目录 Skill，并命名为 create-ip-op-poster。
```

其他 Agent 将完整 Skill 文件夹放入平台规定的 Skills 目录，并保留原有目录结构。

## 2. 先确认人物素材

上传人物／动物原图，然后发送：

```text
请使用 $create-ip-op-poster，先处理人物素材，不要直接做海报。
```

Agent 会展示横版白底组合预览，并保留透明底总图，以及每个人物／动物或不可拆原始组合的独立透明抠图。满意后回复：

```text
人物素材通过
```

## 3. 再选方向和模式

上传 Brief、案例截图、Logo 和建议。Agent 会给出 2—3 个方向并解释两种模式：

- 模式 A：整张快速生图，允许生成式重绘；
- 模式 B：先生图生成位图底图，再覆回保护素材。

直接回复：

```text
选方向 1，用模式 B
```

## 4. 确认 Prompt 后生成

Agent 会展示实际使用的完整文字 Prompt。确认无误后回复：

```text
确认生成
```

不会再生成独立排布稿。若平台没有生图能力，让它输出 Prompt／交接包，不要使用 SVG、HTML、PPT 或色块页面冒充最终海报。
