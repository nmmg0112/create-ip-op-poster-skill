# create-ip-op-poster-skill

一份制作中文 IP／OP 招商海报的通用 Agent Skill：从 Brief 和人物原图开始，经过四次确认，完成创意方向、保真抠图、人物排布、完整成图 Prompt 和最终 QA。

## 四步使用

第一次只需上传 Brief 和人物／动物原图。Agent 每完成一步都会暂停，你依次回复：

1. 选择创意方向：`选方向 1`
2. 检查原图与抠图对照：`抠图通过`
3. 检查人物大小、遮挡和前后层级：`排布通过`
4. 检查完整海报 Prompt：`确认生成`

案例截图、Logo、固定文案、参考图、报价和合作权益都可以后补，也可以不提供。

## 在 Codex 安装

在 Codex 中发送：

```text
请使用 $skill-installer，从 https://github.com/nmmg0112/create-ip-op-poster-skill 安装根目录 Skill，并命名为 create-ip-op-poster。
```

安装后发送：

```text
请使用 $create-ip-op-poster，从第 1/4 步开始。先接收我的 Brief 和人物原图，不要直接成图。
```

如果安装后没有出现，重新启动 Codex。Codex 也支持把完整文件夹放入用户或项目的 Skills 目录；具体规则见 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

更短的操作说明见[快速开始](examples/quick-start.md)。

## 只会用 ChatGPT、豆包或 Coze

不需要安装。打开 [ChatGPT／豆包／Coze 启动语](examples/chatgpt-starter.md)，复制整段文字，再上传 Brief 和人物原图即可。

若平台不能保真人物抠图或分层合成，它应停止并输出交接包，而不是重新生成一张“长得相似”的人物图。详细适配方式见[跨平台使用](references/platform-usage.md)。

## Skill 会做什么

- 根据 Brief、账号特征和素材关系给出真正不同的创意方向；
- 选择概念场景、群像主视觉、玩法分舱、路线阶段、矩阵档案或编辑拼贴等合适版式；
- 按季节、行业和节点确定和谐色彩，不把某个成功案例固化成默认风格；
- 对人物／动物逐一抠图，并展示原图与透明底抠图对照；
- 先确认人物排布，再编写项目级完整 Prompt；
- 用视觉案例学习结构、信息密度和气质，但不照抄；
- 对第一视觉、留白、层级、可读性和素材完整性做最终 QA。

## 不可违反的规则

- 不改变人物的脸、五官、发型、表情和可识别特征。
- 不改变动物的脸、品种、毛色和原始组合关系。
- 案例截图不裁切、不改字、不改数据、不重绘，只能等比缩放和摆放。
- Logo 保留所有元素，只允许去背景、等比缩放和排列。
- 参考海报只学习抽象的视觉语法，不复制文案、Logo、独特版式或标志性元素。
- 不能保真处理受保护素材时，交付执行说明和图层表，不谎称已经完成成图。

## 适用场景

- IP 征集海报、OP 招商海报
- 达人矩阵方案图、单人达人提报图
- 人物／动物抠图与分组呈现
- 海报生成 Prompt
- 案例截图、Logo 和人物素材的保真合成

## 目录

```text
create-ip-op-poster/
├── SKILL.md
├── agents/
├── references/
├── examples/
└── assets/visual-cases/
```

`assets/visual-cases/` 仅供研究 IP／OP 海报的信息层级、版式结构、人物呈现和信息密度，不代表已获得原作品的复制、改编或商业使用授权。

## 许可说明

当前仓库暂未添加开源许可证。公开可访问不等于获得代码、文档或视觉案例的自由使用授权。
