# 傻瓜版完整海报默认流程 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 create-ip-op-poster 改成只需两次自然确认的新手流程：先确认人物素材，再确认包含具体玩法和视觉方向的方案并直接生成一张 16:9 完整招商海报。

**Architecture:** `SKILL.md` 只保留全局决策与路由，`workflow.md` 和 `novice-mode.md` 定义用户可见流程，创意、Prompt、素材保护与 QA 分别由对应 reference 负责。默认路线由生图模型一次完成整张海报；严格保真仅在用户明确要求时作为后台路线启用。源 Skill 是唯一真源，Plugin、本机安装版和发布压缩包均从它同步并做一致性验证。

**Tech Stack:** Markdown Skill instructions, YAML/JSON Plugin metadata, Python static contract tests, Git archive release packaging, Codex image-generation forward tests.

## Global Constraints

- 默认只有 `人物素材确认` 和 `内容方案＋生成授权` 两个确认点。
- 人物素材确认始终早于内容方向和正式海报生成。
- 正式生成前必须有具体玩法；只有口号、品类或抽象风格词时必须拦截。
- 用户未指定画幅时固定使用 16:9 横版。
- 正式生成前可问一句可跳过的颜色／气质偏好；已提供时不得重复询问。
- 视觉偏好必须和 Brief 主题共同转译成配色、材质、光影、氛围和装饰边界，并进入同一张方案卡。
- 默认只调用一次正式生图，直接生成包含人物、案例、主题、玩法和商务信息的完整海报；不得先生成空底图、排布稿或程序化信息板。
- 默认路线只承诺最大程度保持人物和案例，不承诺逐像素保真。
- 只有用户明确要求人脸、案例、Logo、数据或固定中文完全不变时，才自动进入严格保真路线。
- 精确添加或替换 Logo、中文、报价、权益、案例和单个元素时，只允许局部图层修改，不得整图重绘。
- 每次生成前实际打开 2—4 张互补视觉案例，分别学习结构、密度和气质，不照抄具体作品。
- 最终必须检查实际成图，并把竖版、无玩法、PPT 感、空背景、人物与玩法脱节、错脸、漏人、重复、乱码和不可交付视为硬失败。

---

### Task 1: 将新流程写成会失败的合同测试

**Files:**
- Modify: `tests/validate_skill.py`
- Modify: `tests/scenario-regression.md`

**Interfaces:**
- Consumes: 已批准的 `docs/superpowers/specs/2026-09-01-novice-whole-poster-default-design.md`。
- Produces: `check_workflow`、`check_production`、`check_visual`、`check_integrity`、`check_prompt`、`check_docs` 六组可执行合同，以及六个可前向验证的用户场景。

- [ ] **Step 1: 把状态机和确认词测试改为新合同**

  在 `check_workflow` 中要求以下状态块同时出现在 `SKILL.md` 与 `references/workflow.md`：

  ```python
  state_block = """intake
    -> person_material_pending
    -> content_plan_pending
    -> production
    -> qa
    -> complete"""
  ```

  要求活动包包含 `人物素材确认`、`内容方案＋生成授权`、`人物没问题`、`选 1 生成`、`视觉偏好`、`Brief`，并禁止活动文件出现旧的用户门槛 `direction_and_mode_pending`、`prompt_pending`、`选方向 1，用模式 B`、`确认生成`、`模式 A｜快速生图`、`模式 B｜保真合成`、`排布通过`。

- [ ] **Step 2: 增加默认整图与严格保真的生产测试**

  在 `check_production` 中要求：

  ```python
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
      require(active_corpus, needle, "production contract")
  ```

  同时保留“无生图能力只交付 Prompt／素材映射，不得生成 SVG、HTML、Canvas、PPT 或程序化信息板”的能力降级测试。

- [ ] **Step 3: 增加玩法、视觉偏好和实际成图 QA 测试**

  要求内容预检包含 `明确成员`、`账号/案例依据`、`具体场景或人物关系`、`动作、冲突、互动或反转`、`产品/项目自然进入方式` 和 `海报上的一句短文案`。要求视觉模块包含一句可跳过的视觉偏好问题、用户偏好与 Brief 的合并逻辑、2—4 张实际参考原图、结构／密度／气质三种参考角色，以及 `像 PPT`、`竖版`、`无意义空白`、`人物与玩法脱节` 等硬失败。

- [ ] **Step 4: 把场景回归改成六个新场景**

  `tests/scenario-regression.md` 必须包含：

  1. 七位游戏剧情达人＋浅蓝夏日偏好，默认 16:9 整图生成；
  2. 数码 Brief 在无具体玩法或 3:4 参数下被预检拦截；
  3. 成稿右上角新增两个原 Logo，仅目标区域变化；
  4. 明确要求人脸、案例和中文完全不变时自动进入严格保真；
  5. 无案例时继续但披露玩法贴合度有限；
  6. 无生图能力时只输出交接包。

- [ ] **Step 5: 运行测试并确认旧版失败**

  Run: `python3 tests/validate_skill.py`

  Expected: `FAIL`，失败项至少包含旧状态机或缺少 `content_plan_pending`，证明测试能捕获当前旧流程。

- [ ] **Step 6: 提交测试合同**

  ```bash
  git add tests/validate_skill.py tests/scenario-regression.md
  git commit -m "test: define novice whole-poster workflow"
  ```

### Task 2: 重写用户可见的两确认流程

**Files:**
- Modify: `SKILL.md`
- Modify: `references/workflow.md`
- Modify: `references/novice-mode.md`

**Interfaces:**
- Consumes: Task 1 的状态机和确认词合同。
- Produces: `PersonMaterialSet`、`ContentPlanCard`、后台 `generation_route` 和 `formal_generation_count`，供后续 Prompt、生产和 QA 使用。

- [ ] **Step 1: 精简 `SKILL.md` 为新的唯一流程入口**

  将状态机替换为：

  ```text
  intake
    -> person_material_pending
    -> content_plan_pending
    -> production
    -> qa
    -> complete

  严格保真但平台能力不足 -> handoff
  ```

  保留人物身份、案例真实性、Logo 和参考图借鉴边界；删除面向用户的模式 A/B 选择、独立 Prompt 确认和排布确认。入口明确：默认整图生成；明确要求素材完全不变时后台切换 `strict_fidelity`。

- [ ] **Step 2: 在 `workflow.md` 实现两个确认点**

  确认点一只展示横版白底人物组合预览并等待 `人物没问题` 或同等明确回复。确认点二先完成 Brief／案例分析；若用户尚未表达视觉偏好，只问：

  ```text
  这张海报你有没有偏好的颜色或感觉？比如清爽浅蓝、暖色活力、自然松弛。没有也可以，我会结合 Brief 推荐。
  ```

  随后展示推荐方案和一个真正不同的备选方案，结尾只要求 `选 1 生成`。这条回复同时完成方向选择、内容方案确认和正式生图授权。

- [ ] **Step 3: 在 `novice-mode.md` 移除技术选择**

  用户界面不得出现模式 A/B、蒙版、底图、图层、Prompt 长度或哈希。严格保真只在预期效果或能力边界需要解释时，用一句普通中文说明。每轮最多问一个真正改变结果的问题，报价／权益只问一次且默认不阻塞。

- [ ] **Step 4: 运行核心合同测试**

  Run: `python3 tests/validate_skill.py workflow`

  Expected: `PASS workflow`；其他尚未修改的组允许继续失败。

- [ ] **Step 5: 提交核心流程**

  ```bash
  git add SKILL.md references/workflow.md references/novice-mode.md
  git commit -m "feat: make whole-poster generation the novice default"
  ```

### Task 3: 重写内容方案、视觉导演、Prompt 和生产 QA

**Files:**
- Modify: `references/direction-framework.md`
- Modify: `references/visual-director.md`
- Modify: `references/layout-grammar.md`
- Modify: `references/prompt-template.md`
- Modify: `references/material-integrity.md`
- Modify: `references/platform-usage.md`
- Modify: `references/qa-checklist.md`
- Modify: `references/handoff-template.md`

**Interfaces:**
- Consumes: `PersonMaterialSet`、Brief、案例证据、可选视觉偏好和 `ContentPlanCard`。
- Produces: `execution_prompt`、`generation_route = whole_poster | strict_fidelity`、`PosterProductionReceipt` 和最终 QA 结论。

- [ ] **Step 1: 把内容玩法设为正式生图硬门槛**

  `direction-framework.md` 为每个玩法强制保存：玩法标题、成员、证据、具体场景／关系、动作／冲突／互动／反转、产品进入方式和海报短文案。只有口号、行业品类或“高级感／科技感”时必须回到 `content_plan_pending`。

- [ ] **Step 2: 把视觉偏好并入视觉导演判断**

  `visual-director.md` 和 `layout-grammar.md` 要求打开 2—4 张互补原图，分别承担结构、密度和气质参考；记录用户偏好和 Brief 依据如何共同决定配色、材质、光影、景深和装饰。当两者冲突时，方案卡必须用一句话说明调整，不得机械照搬或静默忽略。

- [ ] **Step 3: 把 Prompt 模板改成默认整图与后台严格保真两条路线**

  默认 `whole_poster` Prompt 按以下优先级编译且不向用户强制全文确认：

  ```text
  主题与内容玩法
  人物与案例的视觉角色
  完整艺术构图和信息层级
  固定文案与商务信息
  人物/案例尽量不改的要求
  少量关键禁令
  ```

  严格保真 `strict_fidelity` Prompt 先生成包含完整场景、玩法关系、材质、光影、前中后景和视觉动势的艺术底图，再覆回原素材。两条路线都禁止空背景、空舞台、留洞底图、程序化信息板和自动第二次正式生图。

- [ ] **Step 4: 更新素材保护和精确后期规则**

  `material-integrity.md` 明确：默认整图只做“尽量保持”声明；严格保真才做原人物、完整截图、原 Logo 和准确中文保护。成图后的 Logo、中文、报价、权益、案例和单个元素修改必须是局部图层操作，并通过前后图像差异证明非目标区域未变化。

- [ ] **Step 5: 更新平台路由、交接记录和最终 QA**

  `platform-usage.md` 按真实能力路由默认整图或严格保真；无生图时只交付方案、Prompt 和素材映射。`handoff-template.md` 保存人物确认、视觉偏好、Brief 依据、玩法闭环、generation route、执行 Prompt、正式生图次数、成图文件和 QA。`qa-checklist.md` 必须检查实际成图，并将竖版、无玩法、PPT 感、空背景、同平面、人物与玩法脱节、身份错误、案例严重变形和不可预览设为硬失败。

- [ ] **Step 6: 运行所有源 Skill 测试**

  Run: `python3 tests/validate_skill.py`

  Expected: 六组全部 `PASS`，结尾为 `PASS all`。

- [ ] **Step 7: 提交生产与 QA 合同**

  ```bash
  git add references/direction-framework.md references/visual-director.md references/layout-grammar.md references/prompt-template.md references/material-integrity.md references/platform-usage.md references/qa-checklist.md references/handoff-template.md
  git commit -m "feat: enforce content-led whole-poster production"
  ```

### Task 4: 更新新手文案、安装说明和公开示例

**Files:**
- Modify: `agents/openai.yaml`
- Modify: `README.md`
- Modify: `examples/quick-start.md`
- Modify: `examples/chatgpt-starter.md`
- Modify: `examples/successful-prompt-benchmark.md`

**Interfaces:**
- Consumes: Task 2 与 Task 3 的最终用户流程。
- Produces: Codex 自动入口、普通 ChatGPT／豆包／Coze 可复制启动语和与实际行为一致的公开教程。

- [ ] **Step 1: 更新 Skill UI 入口**

  `agents/openai.yaml` 的描述和默认提示只说明“先确认人物，再根据 Brief 和视觉偏好确认玩法方案并生成 16:9 完整海报”，不得要求用户选择模式或再次确认 Prompt。

- [ ] **Step 2: 更新 README 与快速开始**

  用四段普通中文说明：上传人物；回复 `人物没问题`；补 Brief／案例并回答可选风格问题；回复 `选 1 生成`。同时说明默认整图可能产生细节变化，只有明确要求完全不变时才启用严格保真。

- [ ] **Step 3: 重写普通 AI 会话启动语**

  `chatgpt-starter.md` 必须完整携带两确认流程、具体玩法硬门槛、16:9 默认值、可选视觉偏好、默认整图生成、严格保真后台路由、一次正式生图和精确修改不得整图重绘规则，且不要求用户理解技术术语。

- [ ] **Step 4: 更新成功 Prompt 示例**

  保留完全虚构素材，展示一份“最少充分但执行信息完整”的 16:9 招商海报 Prompt，包含主题、背景、玩法、人物／案例角色、完整艺术构图、配色依据、商务信息和少量关键禁令。

- [ ] **Step 5: 运行源 Skill 测试并提交**

  Run: `python3 tests/validate_skill.py`

  Expected: `PASS all`。

  ```bash
  git add agents/openai.yaml README.md examples/quick-start.md examples/chatgpt-starter.md examples/successful-prompt-benchmark.md
  git commit -m "docs: simplify poster skill for first-time users"
  ```

### Task 5: 同步 Plugin、更新版本并构建发布包

**Files:**
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/skills/create-ip-op-poster/**`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/parity/capabilities.json`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/.codex-plugin/plugin.json`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/scripts/build_release.py`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/tests/test_plugin.py`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/README.md`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/CHANGELOG.md`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/tests/openai-submission.md`

**Interfaces:**
- Consumes: 已通过测试的源 Skill 运行文件。
- Produces: Plugin `0.3.0`、Skill `0.3.0` 压缩包和源／Plugin 一致性报告。

- [ ] **Step 1: 同步 Skill 运行文件到 Plugin 镜像**

  将 `SKILL.md`、`README.md`、`agents/openai.yaml`、`references/*.md` 和 `examples/*.md` 从源 Skill 机械同步到 `skills/create-ip-op-poster/`。保留 Plugin 公开版 `visual-case-library.md` 和其他明确 public override 的匿名化边界，但其流程合同必须同步。

- [ ] **Step 2: 更新 parity 合同**

  删除 `direction_mode_choice`、`mode_a_fast_generation`、`mode_b_protected_composite` 等旧能力标记，新增 `two_confirmation_flow`、`optional_visual_preference`、`content_play_preflight`、`whole_poster_default`、`strict_fidelity_auto_route`、`exact_post_edit`、`landscape_default` 和 `actual_final_qa`。Plugin 活动文件中禁止旧状态、旧确认词和用户模式卡。

- [ ] **Step 3: 将 Plugin 版本更新为 0.3.0**

  同步更新 manifest、构建脚本、测试、README、CHANGELOG 和提交审核说明。Plugin UI 只描述两确认流程与 16:9 完整海报默认行为。

- [ ] **Step 4: 运行 Plugin 和 parity 测试**

  Run: `POSTER_SKILL_SOURCE=/Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster python3 tests/test_plugin.py`

  Expected: 所有能力标记和镜像校验通过，结尾为 `PASS plugin`。

- [ ] **Step 5: 提交 Plugin 并构建可复现压缩包**

  ```bash
  git add .codex-plugin/plugin.json skills/create-ip-op-poster parity/capabilities.json scripts/build_release.py tests/test_plugin.py README.md CHANGELOG.md tests/openai-submission.md
  git commit -m "feat: release novice whole-poster workflow"
  python3 scripts/build_release.py
  ```

  Expected: 生成 `dist/create-ip-op-poster-plugin-0.3.0.zip` 与 `dist/create-ip-op-poster-skill-0.3.0.zip`，压缩包检查均为 `PASS`。

### Task 6: 同步本机版、前向测试并发布 GitHub

**Files:**
- Replace runtime files under: `/Users/bytedance/.codex/skills/create-ip-op-poster/`
- Create: `tests/forward-test-results-2026-09-01-novice-whole-poster.md`
- Update external L1 tutorial and its attached Skill archive when the existing document can be resolved safely.

**Interfaces:**
- Consumes: 通过静态测试的源 Skill、Plugin 0.3.0 和两个发布压缩包。
- Produces: 本机可调用的新 Skill、真实 badcase 回归证据、公开 GitHub 更新和外部教程一致性。

- [ ] **Step 1: 同步并验证本机安装版**

  将源 Skill 的活动运行文件同步到 `/Users/bytedance/.codex/skills/create-ip-op-poster/`，然后逐文件比较 `SKILL.md`、`agents/openai.yaml`、`references/*.md` 和 `examples/*.md`。任何差异都必须在前向测试前修复。

- [ ] **Step 2: 独立运行三个前向场景**

  使用隔离临时目录和独立 Agent：

  - 场景 A：七位剧情达人，用户偏好“蓝色清爽、不要太科技”；期望人物确认后形成三组具体玩法，第二张方案卡体现偏好与 Brief 的结合，并直接授权一次 16:9 完整海报生成。
  - 场景 B：数码 Brief 只有口号，执行参数被错误写成 3:4；期望生图前拦截并补齐具体玩法与 16:9 参数。
  - 场景 C：成稿后增加两个原 Logo；期望只做局部覆回，非目标区域像素不变，不发生第二次整图生图。

  每个结果记录实际对话、工具调用次数、输出文件、图片尺寸、直接预览、视觉检查和失败路由；不能只用字符串匹配声称通过。

- [ ] **Step 3: 检查实际成图质量**

  打开最终图片，确认第一视觉、玩法可读性、人物与玩法关系、前中后景、结构／密度／气质参考边界和商务海报感。出现竖版、PPT 感、空背景、无玩法、错脸、漏人、重复、案例严重乱码或无法预览时记录 `FAIL`，不得自动消耗第二次正式生图。

- [ ] **Step 4: 更新外部教程**

  将 L1 教程中的旧模式选择、`确认生成` 和排布确认删除，改成“人物没问题”与“选 1 生成”两次回复；加入可选视觉偏好问题、16:9 默认值、整图生成保真边界、严格保真自动路由和精确修改不得整图重绘。用新 `create-ip-op-poster-skill-0.3.0.zip` 替换或新增附件。

- [ ] **Step 5: 推送两个公开仓库**

  Run in source repo: `git push origin main`

  Run in Plugin repo: `git push origin main`

  Expected: 两个远端 main 分支分别包含本轮提交；release 包、源文件、本机安装版和教程描述使用同一流程合同。

- [ ] **Step 6: 最终交付检查**

  报告源 Skill commit、Plugin commit、压缩包路径与 SHA-256、静态测试结果、三项前向测试结果、教程链接或无法安全定位时的明确缺口。不得把未执行的测试或未更新的外部文档写成已完成。

