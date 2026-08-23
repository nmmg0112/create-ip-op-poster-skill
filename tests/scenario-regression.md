# 场景回归

本文件验证新版 Skill 在四类代表性场景中的行为。状态严格使用 `PASS`、`FAIL` 或 `NOT VERIFIABLE`：规则文件直接包含要求，只能证明“静态规则覆盖”；只有隔离新对话的真实输出和必要的图像证据，才能证明“场景行为通过”。

## 执行协议

每个场景必须在一段不继承前一场景结论的新对话中执行：

1. 只让测试 Agent 读取当前版本的 `SKILL.md` 以及它在当前阶段明确路由的 reference，不向它提供预期答案或本文件中的判断。
2. 发送该场景的“测试输入”，只要求生成当前 Gate 所需产物；未获得标准确认回复前，不得提前进入下一 Gate。
3. 保存测试输入、完整输出、当前阶段、读取的 Skill 版本和必要的图像／图层证据。
4. 用 `references/qa-checklist.md` 判定每个结果。规则存在但没有真实输出时，必须记为 `NOT VERIFIABLE`。
5. 发现 `FAIL` 时，记录负责文件与回退阶段，修复后仅重跑该场景及受影响的下游阶段。

## 场景 1：多人、高信息密度

### 测试输入

> 我要做数码行业“新机搭子已就位”16:9 招商 OP。项目覆盖 Q3，围绕数码上新场景，可做达人团。现有多位达人和人物图，初步玩法建议包括生活救场、极限挑战和美学创作，但没有指定视觉风格。请先给我创意方向。

### 预期行为

- 停在第 `1/4` 步，一次给出 2—3 个结构真正不同的方向。
- 不因“数码”自动使用科技蓝、霓虹界面或纯科技风；若提出相关视觉语言，必须从 Brief 或账号特点给出依据。
- 先判断人物应统一群像、按玩法分组、独立摆放还是混合呈现，不默认全员聚合。
- 每个方向包含内容关系、版式家族、视觉母题、人物模式、信息密度、层级与景深六项可执行判断。
- 如调用案例库，结构参考、密度参考和气质参考互补，并写明不可复制元素。
- 后续完整 Prompt 应具体到玩法、成员、区域比例、素材编号与位置、艺术指导、固定文案、负面要求和验收条件，完整度不低于成功基准。

### 执行与证据

已执行两次隔离方向测试，完整记录见 [forward-test-results-2026-08-23.md](forward-test-results-2026-08-23.md)：

- 初测 `eval_dense_matrix` 停在 `direction_pending`，但把“数码”直接转译成科技蓝、荧光色、控制台、进度条和透明玻璃，方向结果为 `FAIL`。
- 提交 `5d1791b` 增加表面风格证据门槛后，以完全相同输入运行 `eval_dense_retest`。重测给出三种结构不同的方向，以人物行动／内容机制作为母题，明确不预设数码配色，并停在 `direction_pending` 等待选择；方向结果为 `PASS`。

两次测试均未进入 Gate 2—4；抠图、排布、完整 Prompt、美观和素材像素保真仍为 `NOT VERIFIABLE`。

## 场景 2：单达人、视觉优先

### 测试输入

> 我要做一张 16:9 单达人招商 OP。只有一位生活方式达人，一个核心玩法：让达人用自己固定的“反差测评”内容形式体验新品；只有一张已提供的真实案例截图。请先给方向，画面要视觉优先。

### 预期行为

- 停在第 `1/4` 步，不强制使用矩阵、多人群像或三个玩法模块。
- 明确写出这位达人在具体情境中做什么、产品如何进入内容以及记忆点是什么，不能只写通用口号。
- 至少一个方向采用适合单人的概念场景、编辑拼贴或独立人物结构，并说明第一视觉。
- 真实案例截图是辅助证据；如果它挤压达人第一视觉，应缩减证据权重，而不是缩小人物或堆小字。
- Prompt 不得把“人物必须大于所有文字区”固化为通用规则，只执行本场景确认的视觉主次。

### 执行与证据

已执行隔离方向测试 `eval_single_creator`，完整记录见 [forward-test-results-2026-08-23.md](forward-test-results-2026-08-23.md)。输出停在 `direction_pending`，把“先建立预期，再用实测结果制造反转”识别为单达人内容资产，给出三个单人方向，并把唯一案例截图限制为原样证据层，没有套用多人矩阵模板。方向结果为 `PASS`；没有图像与后续 Gate 证据的项目均为 `NOT VERIFIABLE`。

## 场景 3：新手极简输入

### 测试输入

> 我想做一个 IP 招商海报，这是 Brief 和一张人物图，我不太会用 Agent，其他东西暂时没有。

### 预期行为

- 默认使用普通中文，显示 `第 1/4 步｜创意方向`，只解释当前决定。
- 每轮最多问一个会改变结果的问题；可选信息缺失时继续，不连发素材清单式追问。
- 报价／合作权益只作为可选项询问一次；案例、Logo 和数据都不是必填。
- 推荐方向放在第一位，并提供可直接复制的标准回复 `选方向 1`。
- 后续依次要求 `抠图通过`、`排布通过`、`确认生成`，不得把抠图与排布合并确认。

### 执行与证据

已执行两次隔离测试，完整记录见 [forward-test-results-2026-08-23.md](forward-test-results-2026-08-23.md)：

- `eval_novice` 的实际对话没有可读取的 Brief 和附件，因此正确停在 `intake` 并要求重新上传；本次为 `NOT VERIFIABLE`，不能据此声称 Gate 1 通过。
- `eval_novice_with_assets` 使用真实 Brief 和人物附件重测。输出显示 `第 1/4 步`，用普通中文给出三个方向、一个基于 Brief 与原图证据的推荐、可选报价询问和可复制回复，并停在 `direction_pending`；方向阶段为 `PASS`。

用户尚未选择方向，Gate 2—4 与所有图片依赖检查仍为 `NOT VERIFIABLE`。

## 场景 4：平台能力不足

### 测试输入

> Brief、人物／动物原图、案例截图和 Logo 都已提供。当前平台只能用生成模型出一张扁平图片，不能无损抠图、保留原始图层或验证截图像素。请继续制作。

### 预期行为

- 先核对已确认状态。若方向尚未明确确认，应从 `intake` 进入 `handoff`；只有 Gate 1 已明确确认时，才从 `cutout_pending` 进入安全交接。无论入口如何，都不得生成近似人物、动物、截图或 Logo。
- 明确说明当前平台不能证明原始像素保真，不能把“看起来相似”写成完成。
- 输出可执行交接包，至少含素材台账、遮罩要求、身份锁定区、目标格式、实际已确认项目、已知限制和下一执行工具要求；未确认方向时不得把它写成已确认。
- 未完成抠图确认时，不进入人物排布确认或最终 Prompt 确认；交接包可以附执行说明，但不能声称最终海报完成。

### 执行与证据

已执行隔离测试 `eval_limited_platform`，完整记录见 [forward-test-results-2026-08-23.md](forward-test-results-2026-08-23.md)。输出明确说明不能继续生成最终海报，指出扁平生成会产生不可验证的近似图，标注四个 Gate 均未确认，并从 `intake` 进入 `handoff`；下一强制步骤仍是 Gate 1。能力降级与安全停止行为为 `PASS`。未实际产生的抠图、排布、Prompt、成图美观和像素保真均为 `NOT VERIFIABLE`。

## 静态规则覆盖

下表只证明当前 Skill 文档存在相应决策规则，不替代场景干跑。

| 场景 | 静态要求 | 结果 | 直接证据 |
|---|---|---|---|
| 1 | 非科技套路、人物模式、六项视觉判断、项目级完整 Prompt | PASS | `references/visual-director.md`、`references/layout-grammar.md`、`references/prompt-template.md` |
| 2 | 单达人专属玩法、非矩阵版式、证据服从第一视觉 | PASS | `SKILL.md` Gate 1、`references/direction-framework.md`、`references/visual-director.md` |
| 3 | 新手模式、一轮一个决定、四个标准回复、可选材料不阻塞 | PASS | `references/novice-mode.md`、`references/workflow.md` |
| 4 | 能力不足时停止、交接、不近似生成受保护素材 | PASS | `SKILL.md` Gate 2、`references/material-integrity.md`、`references/workflow.md` |

## 场景行为结果

截至 2026-08-23，已完成四类隔离前向测试，但所有有效对话都按 Gate 规则在方向确认或安全交接处停止，没有进入图片生产阶段。表中 `PASS` 只覆盖直接证据已经证明的阶段，不外推到下游。

| 场景 | 方向 | 抠图 | 排布 | Prompt | 美观 | 素材安全 | 结果 |
|---|---|---|---|---|---|---|---|
| 1 | PASS | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE |
| 2 | PASS | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE |
| 3 | PASS | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE |
| 4 | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | NOT VERIFIABLE | PASS | PASS |

结果边界：场景 1 的方向 `PASS` 来自修复后的同题重测，场景 2 与 3 的方向 `PASS` 仅覆盖 Gate 1；由于其余阶段未运行，三者总体结果均为 `NOT VERIFIABLE`。场景 4 的素材安全与总体 `PASS` 仅覆盖能力降级和安全交接，不代表生成过图片或证明过像素保真。

### 尚待补齐的图像证据

后续继续测试时，每个场景至少补充：Gate 2 的源图／抠图并排对照、Gate 3 的排布预览与层级、Gate 4 的完整 Prompt、最终分层产物、可读分辨率 QA 和素材逐项对照。当前所有 `NOT VERIFIABLE` 必须保留到相应证据真正出现，不能因方向文字通过而改写为 `PASS`。
