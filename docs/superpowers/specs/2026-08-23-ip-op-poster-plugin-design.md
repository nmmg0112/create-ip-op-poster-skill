# IP/OP 海报 Plugin 打包设计

日期：2026-08-23

## 目标

把现有 `create-ip-op-poster` Skill 打包成可安装、可测试、可提交 OpenAI Plugin 目录的纯 Skill Plugin，同时保留现有 Skill 仓库和安装方式。

首版只解决一件事：让 ChatGPT 和 Codex 能稳定调用同一套 IP/OP 海报工作流。首版不接 MCP 服务，不登录第三方账号，不收集用户数据，也不执行外部写操作。

## 方案选择

采用独立 Plugin 仓库。新仓库暂定名为 `create-ip-op-poster-plugin`，现有 `create-ip-op-poster-skill` 仓库继续作为独立 Skill 使用，不改变目录结构。

未采用直接改造原仓库的方案，因为 Plugin 要把 Skill 放在 `skills/create-ip-op-poster/` 下，直接迁移会破坏现有用户的安装路径。未采用多 Plugin 市场仓库，因为当前只有一个 Plugin，额外目录和发布流程没有实际收益。

## Plugin 结构

```text
create-ip-op-poster-plugin/
├── .codex-plugin/plugin.json
├── skills/create-ip-op-poster/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   └── examples/
├── assets/
│   ├── icon.png
│   └── logo.png
├── README.md
├── SUPPORT.md
├── PRIVACY.md
└── TERMS.md
```

版本从 `0.1.0` 开始。Plugin 名称为 `create-ip-op-poster`，界面名称为“IP/OP 海报制作”。首版不声明 MCP、App 或 Hook。

## 内容与版权边界

Plugin 使用现有 Skill 的四次确认流程、素材保护规则、视觉导演规则、Prompt 模板、新手模式和验收标准。

公开包不带授权状态不明的行业海报原图、联系表或其他第三方案例图片。视觉案例库改成文字化设计语法，保留排版家族、信息密度、人物组织方式和适用条件。用户需要参考具体海报时，在当前任务中自行上传有权使用的参考图。

图标和 Logo 使用本项目自制的简洁 OP 标识，不使用品牌 Logo、达人肖像或第三方海报元素。

## 使用方式

安装后，ChatGPT 通过 `@create-ip-op-poster` 调用，Codex 通过 `$create-ip-op-poster` 调用。默认启动语要求从第 1/4 步开始，只给创意方向，不直接成图。

Plugin 继续执行四次确认：

1. 选择创意方向。
2. 确认人物或动物抠图。
3. 确认人物排布。
4. 确认完整成图 Prompt。

人物、动物、案例截图和 Logo 的保护规则不因打包方式改变。平台缺少保真抠图或分层能力时，Skill 必须停止并输出交接说明。

## 官方提交材料

公开提交包包括 Plugin 清单、完整 Skill、三条以内的启动 Prompt、自制图标、公开支持页、隐私政策、服务条款、发布说明，以及五个正向测试和三个负向测试。

提交前由用户确认公开发布身份。Manifest 暂以 GitHub 用户名作为开发者标识；如果 OpenAI Platform 的已验证身份不同，在提交前统一修改开发者名称、网站和政策页面署名。

## 测试与验收

先运行 Plugin 结构校验和 Skill 校验，再做本地安装测试。行为测试至少覆盖：单达人、多人矩阵、没有案例图的新手输入、平台缺少保真图像能力，以及截图或人物保护规则被要求跳过的负向场景。

完成标准：

- Plugin 清单通过官方结构校验。
- 内含 Skill 通过原有静态校验。
- Plugin 能在新任务中被识别并显式调用。
- 四次确认不被跳过。
- 公开包不包含授权状态不明的第三方海报图片。
- 官方提交所需的五个正向测试和三个负向测试齐全。

## 发布边界

本地打包、测试和 GitHub 发布可以由 Codex 完成。OpenAI Platform 的身份验证、政策声明、提交审核和最终点击发布，需要用户使用自己的账号确认。审核通过不会自动上架，用户仍需在提交后台执行发布。
