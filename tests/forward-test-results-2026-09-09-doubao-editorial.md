# 豆包杂志编辑式稳定模式验证记录

## 验证范围

本轮验证对象为源 Skill 中新增的豆包专属执行合同、模型门禁、批准人物资产绑定、杂志编辑式构图、玩法密度和一次生成控制。静态规则和包结构可以在本地验证；真实 Seedream 5.0 Pro 调用与最终图片质量必须在豆包新会话中验证。

## 静态结果

| 项目 | 结果 | 直接证据 |
|---|---|---|
| 官方 Skill 包结构 | PASS | `quick_validate.py` 返回 `Skill is valid!` |
| 完整回归 | PASS | `tests/validate_skill.py all` 返回 `PASS all` |
| Seedream 5.0 Pro 精确 Skill URI | PASS | `SKILL.md` 与豆包执行合同包含 `skill://seedream-50?type=2&id=360075272194` |
| 不静默降级与知情选择 | PASS | 豆包执行合同包含平台原因、质量影响和 `继续用当前模型` 门禁 |
| 批准人物素材实际绑定 | PASS | `ApprovedPersonAssetSet` 进入工作流、Prompt、交接和 QA |
| 豆包杂志编辑式稳定模式 | PASS | 大标题、人物主视觉、案例拼贴、玩法说明和禁用模板均进入执行合同与 Golden Case |
| Aime／通用流程隔离 | PASS | Aime 仍使用 Image2 动态视觉导演；完整回归通过 |

## 真实平台结果

| 项目 | 结果 | 缺少证据 |
|---|---|---|
| 豆包是否实际加载 Seedream 5.0 Pro | NOT VERIFIABLE | 新会话的模型调用回执 |
| 批准人物图是否实际进入正式调用 | NOT VERIFIABLE | 新会话的附件／调用记录 |
| 人脸和人物数量 | NOT VERIFIABLE | 批准人物图与最终海报对照 |
| 案例截图和中文准确度 | NOT VERIFIABLE | 原截图与最终海报对照 |
| 杂志编辑式视觉质量 | NOT VERIFIABLE | 新版完整 16:9 成图 |
| 一次正式生图 | NOT VERIFIABLE | 完整新会话调用记录 |

## 下一步

在豆包上传更新后的完整 Skill 压缩包，只发送：

> 我已经上传了 create-ip-op-poster Skill。请读取它，告诉我怎么使用，并带我开始制作一张海报。

完成后返回分享链接或人物预览、模型提示和最终海报。只有直接查看这些证据后，才更新真实平台结果。
