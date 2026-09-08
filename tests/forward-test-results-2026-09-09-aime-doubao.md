# Aime／豆包跨平台前向测试记录

日期：2026-09-09  
Skill：create-ip-op-poster

## 测试范围

本轮先验证参赛包内可静态复现的行为合同。Aime Image2 和豆包 Seedream 5.0 Pro 的真实图片生成必须在对应平台独立会话中执行；未产生实际对话和图片证据前保持 `NOT VERIFIABLE`。

## 静态验证

| 项目 | 结果 | 证据 |
|---|---|---|
| 自动新手开场白 | PASS | `references/novice-mode.md`，用户不复制长启动 Prompt |
| Aime 平台执行合同 | PASS | `references/platforms/aime-executor.md` |
| 豆包平台执行合同 | PASS | `references/platforms/doubao-executor.md` |
| 两次确认 | PASS | `人物没问题`、`选 1 生成` |
| 当前锁定规格 | PASS | `LockedPosterSpec` 已进入工作流、Prompt 和交接记录 |
| 第一版保护 | PASS | `PosterVersionLock` 与局部修改分流已进入工作流和 QA |
| 比赛可复现 Prompt | PASS | `examples/prompt.txt` |
| 结果示例与量化字段 | PASS | `examples/result.md` |
| 多人／单人 Golden Case | PASS | 两份公开虚构案例，不包含真实肖像 |
| 全部自定义验证组 | PASS | `python3 tests/validate_skill.py all` |
| 官方 Skill 结构校验 | PASS | `quick_validate.py` 输出 `Skill is valid!` |

## Aime Image2 实测

| 项目 | 当前结果 | 需要的直接证据 |
|---|---|---|
| 上传包后一句话自动开始 | NOT VERIFIABLE | Aime 完整对话截图或分享链接 |
| 人物素材先确认 | NOT VERIFIABLE | 白底人物预览及“人物没问题” |
| 两个内容／视觉方案 | NOT VERIFIABLE | 方案卡和具体玩法 |
| 只调用一次正式生图 | NOT VERIFIABLE | Aime 工具调用或完整对话记录 |
| Image2 输出 16:9 完整海报 | NOT VERIFIABLE | 原尺寸成图 |
| 画面不竖版、不像 PPT、有第一视觉和前中后景 | NOT VERIFIABLE | 实际成图视觉 QA |
| 第一版通过后局部修改不整图重画 | NOT VERIFIABLE | 修改前后图和非目标区域对比 |

## 豆包 Seedream 5.0 Pro 实测

| 项目 | 当前结果 | 需要的直接证据 |
|---|---|---|
| 上传包后一句话自动开始 | NOT VERIFIABLE | 豆包完整对话截图或分享链接 |
| 人物素材阶段使用 Seedream 5.0 Pro | NOT VERIFIABLE | 模型选择和人物预览 |
| 正式海报使用 Seedream 5.0 Pro | NOT VERIFIABLE | 模型选择和成图记录 |
| 稳定人物编号、无漏人重复串脸 | NOT VERIFIABLE | 原素材映射和最终图 |
| 只调用一次正式生图并输出 16:9 | NOT VERIFIABLE | 完整对话和原尺寸成图 |

## Aime 评委最短测试输入

```text
我已经上传了 create-ip-op-poster Skill。请读取它，告诉我怎么使用，并带我开始制作一张海报。
```

完成 Aime 实测后，必须用真实证据更新本文件，不能把模型可用性或静态规则写成成图 `PASS`。
