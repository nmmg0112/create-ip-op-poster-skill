# Generative-first IP/OP Poster Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the old four-gate, layout-preview workflow with a person-material-first, two-mode poster workflow in which Mode A generates one complete poster and Mode B first generates a real bitmap visual base before protected-layer compositing.

**Architecture:** The Skill repository remains the source of truth. Its state machine and references define shared behavior; the public Plugin mirrors those files except for four documented public-safe variants, and the installed local Skill is refreshed only after source and Plugin validation pass. Static contract tests prevent legacy composition gates and programmatic poster bases from returning; isolated forward tests check the actual conversation and image-production behavior.

**Tech Stack:** Markdown Skill package, Python 3 static validators, JSON Plugin manifest/parity contract, Codex image generation, deterministic raster layer compositing, Git, ZIP/SHA-256 release verification.

## Global Constraints

- Preserve the user's existing uncommitted edit in `docs/superpowers/specs/2026-08-23-ip-op-poster-plugin-design.md`; never stage, rewrite, stash, or commit it.
- The shared state order is exactly `intake -> person_material_pending -> direction_and_mode_pending -> prompt_pending -> production -> qa -> complete`.
- Both Mode A and Mode B must stop for `人物素材通过` before direction or mode selection.
- Multi-subject material processing uses the exact user-approved Prompt: `把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 注意人物不能重复，且人物大小调整一致一些`.
- Person-material output includes a white-background horizontal review image, a same-arrangement transparent master, and individual transparent cutouts.
- Delete the mandatory composition preview and every required `排布通过` gate. A user-requested wireframe is optional, non-generative, and never a production gate.
- Keep one final complete Prompt confirmation with reply `确认生成`; this confirmation is text-only and does not consume a poster generation.
- Mode A gives the image model the entire poster and discloses that people, screenshots, Logos, and Chinese copy may be redrawn.
- Mode B's first production action must create a PNG, WebP, or JPEG visual base with an image-generation model. SVG, HTML, Canvas, PPT, Sharp drawing commands, fixed rectangles, and grid renderers may not create or substitute for that base.
- Mode B code may run only after the generated bitmap exists, and only for masks, proportional placement, protected-layer compositing, rasterized fixed copy, format conversion, and verification.
- If no image-generation model is available, return a Prompt/handoff package and never fall back to a programmatic information board.
- Default to one formal poster-generation call. Do not automatically spend a second generation after a failure.
- Public Plugin files must retain their existing anonymization and copyright-safe substitutions.
- Source Skill, Plugin Skill, and installed local Skill must pass the same behavioral contract.

---

## File Responsibility Map

### Source Skill repository

- `SKILL.md`: concise state machine, mandatory person-material gate, A/B choice, final Prompt gate, production routing.
- `references/workflow.md`: detailed stage transitions, rollback, and exact confirmation language.
- `references/novice-mode.md`: low-friction user copy and minimal required replies.
- `references/material-integrity.md`: shared person-material outputs and mode-specific fidelity boundaries.
- `references/prompt-template.md`: Mode A complete-generation Prompt and Mode B bitmap-base Prompt plus composite manifest.
- `references/qa-checklist.md`: process, provenance, protected-layer, visual-quality, and duplicate-output checks.
- `references/platform-usage.md`: capability routing and safe handoff behavior.
- `references/handoff-template.md`: resumable state, generation mode, person assets, base-image provenance, and generation count.
- `references/direction-framework.md`, `references/visual-director.md`, `references/layout-grammar.md`: direction logic and generative composition grammar without a layout-confirmation artifact.
- `README.md`, `agents/openai.yaml`, `examples/*.md`: beginner-facing usage and current invocation text.
- `tests/validate_skill.py`: executable static contract.
- `tests/scenario-regression.md`: current behavioral scenarios.
- `tests/forward-test-results-2026-08-31.md`: new isolated evaluation evidence; historical `2026-08-23` results remain unchanged and clearly historical.

### Public Plugin repository

- `skills/create-ip-op-poster/`: mirrored shared Skill plus four public-safe variants.
- `parity/capabilities.json`: exact-mirror list, public-override list, new capability markers, and forbidden legacy markers.
- `scripts/verify_parity.py`: byte equality for common files and marker checks for approved variants.
- `tests/test_plugin.py`: manifest, parity, and release-version checks.
- `.codex-plugin/plugin.json`, `README.md`, `CHANGELOG.md`, `tests/openai-submission.md`: version `0.2.0` listing and examples.
- `scripts/build_release.py`: reproducible Plugin/Skill ZIP generation and SHA-256 report.
- `tests/release-report.md`: generated release evidence for the current package.

---

### Task 1: Define the new source contract with failing tests

**Files:**
- Modify: `tests/validate_skill.py`
- Modify: `tests/scenario-regression.md`

**Interfaces:**
- Consumes: current Markdown package at the supplied Skill root.
- Produces: validator groups `workflow`, `production`, `visual`, `integrity`, `prompt`, and `docs`; exit code `0` only when the approved workflow is present and legacy gates are absent.

- [ ] **Step 1: Add order and production-contract helpers**

Replace the group tuple and add this helper beside `require`/`forbid`:

```python
GROUPS = ("workflow", "production", "visual", "integrity", "prompt", "docs")


def require_order(text: str, earlier: str, later: str, label: str) -> None:
    earlier_index = text.find(earlier)
    later_index = text.find(later)
    if earlier_index < 0 or later_index < 0 or earlier_index >= later_index:
        raise AssertionError(f"{label}: expected {earlier!r} before {later!r}")
```

- [ ] **Step 2: Replace the old four-gate workflow assertions**

Make `check_workflow` require the new states and replies, then reject legacy artifacts:

```python
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
```

- [ ] **Step 3: Add a Mode A/Mode B production check**

Add `check_production` and register it in `CHECKS`:

```python
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


CHECKS = {
    "workflow": check_workflow,
    "production": check_production,
    "visual": check_visual,
    "integrity": check_integrity,
    "prompt": check_prompt,
    "docs": check_docs,
}
```

- [ ] **Step 4: Update integrity and docs assertions**

Require the exact person-processing Prompt plus `横版白底组合预览图`, `透明底人物总图`, and `独立透明抠图`. Change the public reply checks to `人物素材通过` and `确认生成`, and forbid `排布通过` in active docs.

- [ ] **Step 5: Rewrite current scenario expectations**

In `tests/scenario-regression.md`, make person-only intake Scenario 1, Mode A Scenario 2, Mode B Scenario 3, and no-image-model handoff Scenario 4. Each scenario must state the exact stop stage and must not cite the 2026-08-23 direction-first runs as evidence for the new version.

- [ ] **Step 6: Run the test and verify that the old package fails**

Run:

```bash
python3 tests/validate_skill.py all
```

Expected: non-zero exit with failures mentioning `person_material_pending`, Mode A/Mode B, or forbidden `composition_pending`.

- [ ] **Step 7: Commit only the contract changes**

```bash
git add tests/validate_skill.py tests/scenario-regression.md
git commit -m "test: define generative-first poster contract"
```

---

### Task 2: Rewrite the state machine and beginner flow

**Files:**
- Modify: `SKILL.md`
- Modify: `references/workflow.md`
- Modify: `references/novice-mode.md`
- Modify: `references/handoff-template.md`

**Interfaces:**
- Consumes: source ledger and uploaded person/animal files.
- Produces: `PersonMaterialSet`, direction/mode decision, confirmed final Prompt, and resumable handoff state.

Define `PersonMaterialSet` in prose with these fields:

```text
review_white: horizontal white-background preview
master_transparent: same arrangement with alpha
subjects_transparent: one transparent layer per unique person/animal or inseparable original group
source_ledger: stable Pxx IDs, public names, counts, variants, and limitations
approval: exact user message or none
```

- [ ] **Step 1: Replace the SKILL state machine**

Use exactly:

```text
intake
  -> person_material_pending
  -> direction_and_mode_pending
  -> prompt_pending
  -> production
  -> qa
  -> complete

Any unavailable required capability -> handoff
```

- [ ] **Step 2: Make person material the first mandatory gate**

Place the exact user-approved collage Prompt in `SKILL.md` and `references/workflow.md`. Require the three `PersonMaterialSet` outputs, identity/count/edge QA, and the reply `人物素材通过`. Allow Brief and cases to arrive before or after this gate, but do not enter direction work until the gate passes.

- [ ] **Step 3: Combine creative direction and mode selection**

After person approval, give 2–3 genuinely different directions and show this compact mode card:

```text
模式 A｜快速生图：整张海报一次生成，通常更统一、更快；人物、截图、Logo 和中文可能被重绘。
模式 B｜保真合成：先生图生成完整艺术底图，再覆回确认过的人物、截图、Logo 和中文；更适合正式提报。
```

Accept replies such as `选方向 1，用模式 B`. If theme, play, and mode are already explicit, do not ask the user to choose them again.

- [ ] **Step 4: Keep one text-only final Prompt gate**

End with `确认生成`. State that this round shows text only and consumes no poster-generation call. Remove `玩法通过`, `视觉规格通过`, `抠图通过`, `排布通过`, and numbered four-step language from active workflow text.

- [ ] **Step 5: Update rollback and handoff state**

The handoff must include `generation_mode`, the three person-material outputs, `visual_base` path/format/model record, protected-layer manifest, `formal_generation_count`, and current QA. A person-source change returns to `person_material_pending`; a theme/play/mode change returns to `direction_and_mode_pending`; a fixed-copy/Logo/case mapping change returns to `prompt_pending`.

- [ ] **Step 6: Run the workflow group**

```bash
python3 tests/validate_skill.py workflow
```

Expected: `PASS workflow`.

- [ ] **Step 7: Commit the workflow**

```bash
git add SKILL.md references/workflow.md references/novice-mode.md references/handoff-template.md
git commit -m "feat: put person material before poster modes"
```

---

### Task 3: Implement the two production modes and visual QA contract

**Files:**
- Modify: `references/material-integrity.md`
- Modify: `references/prompt-template.md`
- Modify: `references/qa-checklist.md`
- Modify: `references/platform-usage.md`
- Modify: `references/direction-framework.md`
- Modify: `references/visual-director.md`
- Modify: `references/layout-grammar.md`

**Interfaces:**
- Consumes: confirmed `PersonMaterialSet`, Brief/cases/Logo/copy, chosen direction, chosen mode, confirmed final Prompt.
- Produces: Mode A flattened generated poster, or Mode B generated bitmap base plus protected-layer composite and provenance receipt.

- [ ] **Step 1: Merge cutout and composition review into person-material rules**

Keep identity-lock, screenshot, and Logo protections. Replace the old creator-composition confirmation section with rules that the white review image proves material usability but does not lock the final poster layout. Mode B must use the transparent master or individual cutouts, never the white review rectangle.

- [ ] **Step 2: Split the Prompt template by mode**

After the shared Brief, content, art-direction, asset map, fixed copy, references, and negative constraints, provide two exact production sections:

```text
【模式 A｜端到端整图生成】
将已确认人物素材作为主要人物参考，由生图模型一次完成整张海报。
明确列出允许发生生成式重绘的 P/C/L/T 项，并禁止声称像素保真。

【模式 B｜第一段：主视觉位图生成 Prompt】
直接生成一张完整的 PNG、WebP 或 JPEG 艺术底图。
底图必须包含背景场景、构图、材质、光影、前中后景、装饰语言和视觉动势。
为 P/C/L/T 保护图层留下自然位置，但不要生成或仿制其受保护内容。
不得输出 SVG、HTML、Canvas、PPT、线框稿、规则色块页或头像网格。

【模式 B｜第二段：保护图层合成说明】
在已落盘的位图底图上覆回透明人物总图或独立透明抠图、完整案例截图、原 Logo 和准确中文。
代码只负责蒙版、等比缩放、位置、层级、阴影衔接、文字栅格化、导出和验证。
```

- [ ] **Step 3: Harden Mode B provenance**

Require a receipt containing `visual_base_path`, `visual_base_format`, `image_generation_model_or_tool`, `visual_base_created_before_composite`, `protected_layer_ids`, and `formal_generation_count`. A user-supplied SVG Logo is allowed as a source layer; a generated SVG poster base is not.

- [ ] **Step 4: Add visual hard failures**

QA must fail a PPT-like information board, equal-weight card grid, missing foreground/middle/background, detached people/play, meaningless blank space, and any programmatic base. If the final file hash equals a complete-poster preview hash, fail it; do not compare against the white person-material review image.

- [ ] **Step 5: Add mode-specific material checks**

Mode A checks roster, theme, readability, aesthetics, and obvious identity failures but makes no pixel-preservation claim. Mode B checks every protected layer, confirms non-target regions remain unchanged after a Logo/text/screenshot adjustment, and refuses a whole-image generative edit for exact post-production changes.

- [ ] **Step 6: Update visual-director and layout language**

Keep the six layout families and content-topology reasoning, but describe them as generative composition grammar. Remove required preview confirmation. Explicitly state that grids, diagrams, and layout-guide SVGs may explain a relationship but may never become the Mode B base or final poster.

- [ ] **Step 7: Update platform routing**

Use this matrix:

```text
image generation + layered compositing -> Mode A or Mode B
image generation only -> Mode A; Mode B generates bitmap base then hands off protected compositing
no image generation -> Prompt/material map only; never SVG/HTML/PPT fallback
```

- [ ] **Step 8: Run focused and full validation**

```bash
python3 tests/validate_skill.py production
python3 tests/validate_skill.py integrity
python3 tests/validate_skill.py prompt
python3 tests/validate_skill.py visual
python3 tests/validate_skill.py all
git diff --check
```

Expected: every group prints `PASS`; `git diff --check` prints nothing.

- [ ] **Step 9: Commit production rules**

```bash
git add references/material-integrity.md references/prompt-template.md references/qa-checklist.md references/platform-usage.md references/direction-framework.md references/visual-director.md references/layout-grammar.md
git commit -m "feat: add generative and protected poster modes"
```

---

### Task 4: Refresh beginner docs, metadata, and source regression evidence

**Files:**
- Modify: `README.md`
- Modify: `agents/openai.yaml`
- Modify: `examples/quick-start.md`
- Modify: `examples/chatgpt-starter.md`
- Modify: `examples/successful-prompt-benchmark.md`
- Create: `tests/forward-test-results-2026-08-31.md`

**Interfaces:**
- Consumes: the new shared workflow.
- Produces: copyable novice instructions with no legacy gate and an evidence record that does not expose local paths or real client material.

- [ ] **Step 1: Rewrite the beginner entry point**

The first instruction must ask only for person/animal originals and may say the Brief/cases can arrive now or after person approval. The two required confirmation replies shown to beginners are `人物素材通过` and `确认生成`; direction/mode selection uses one natural reply such as `选方向 1，用模式 B`.

- [ ] **Step 2: Rewrite the ordinary-chat starter**

The copyable ChatGPT/豆包/Coze starter must include the exact person-processing Prompt, the three person-material outputs, both mode cards, no layout-preview gate, and Mode B bitmap-first production. It must tell a host without image generation to return a handoff instead of a generated SVG/page.

- [ ] **Step 3: Update UI metadata**

Set `agents/openai.yaml` to describe `人物素材先确认 + 两种成图模式`, and make its default prompt begin with person-material processing rather than `第 1/4 步` direction ideation.

- [ ] **Step 4: Keep the successful Prompt benchmark useful**

Retain the approved high-detail benchmark, then add a short mapping that shows how its content becomes either the Mode A complete-generation Prompt or the Mode B bitmap-base Prompt plus protected-layer manifest. Do not turn the seasonal example into a universal default.

- [ ] **Step 5: Add isolated forward-test result headings**

Create `tests/forward-test-results-2026-08-31.md` with four named scenarios: `person_first`, `mode_a_one_generation`, `mode_b_bitmap_then_layers`, and `no_imagegen_no_svg_fallback`. Initialize each as `NOT VERIFIABLE` until Task 6 runs it; do not rewrite the 2026-08-23 historical evidence.

- [ ] **Step 6: Validate docs and scan for legacy active copy**

```bash
python3 tests/validate_skill.py docs
python3 tests/validate_skill.py all
rg -n "composition_pending|排布通过|第 <n>/4 步|four mandatory confirmation gates|四个确认点不能跳过" SKILL.md README.md references agents examples
```

Expected: validator passes; `rg` returns no active-package matches.

- [ ] **Step 7: Commit source-facing docs**

```bash
git add README.md agents/openai.yaml examples/quick-start.md examples/chatgpt-starter.md examples/successful-prompt-benchmark.md tests/forward-test-results-2026-08-31.md
git commit -m "docs: simplify generative-first poster usage"
```

---

### Task 5: Mirror the public Plugin and strengthen parity

**Files:**
- Modify: `parity/capabilities.json`
- Modify: `scripts/verify_parity.py`
- Modify: `tests/test_plugin.py`
- Modify: `.codex-plugin/plugin.json`
- Modify: `skills/create-ip-op-poster/**`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `tests/openai-submission.md`

**Interfaces:**
- Consumes: validated source Skill and the existing four public-safe overrides.
- Produces: Plugin version `0.2.0` with exact shared behavior and copyright-safe public examples.

- [ ] **Step 1: Change the parity contract first**

Add `exact_mirror_files` for every byte-identical shared file and `public_overrides` for only:

```json
[
  "references/workflow.md",
  "references/platform-usage.md",
  "references/visual-case-library.md",
  "examples/successful-prompt-benchmark.md"
]
```

Replace old gate capabilities with `person_material_gate`, `direction_mode_choice`, `mode_a_fast_generation`, `mode_b_protected_composite`, `image_generated_bitmap_base`, `no_programmatic_fallback`, `single_formal_generation`, and `final_visual_qa`. Add forbidden legacy markers `composition_pending`, `排布通过`, `第 <n>/4 步`, and `four mandatory confirmation gates` to the active public package.

- [ ] **Step 2: Make common-file parity byte-exact**

Add this loop to `scripts/verify_parity.py` after the required-file check:

```python
for relative in contract["exact_mirror_files"]:
    source_path = source / relative
    plugin_path = skill / relative
    if not source_path.is_file() or not plugin_path.is_file():
        fail(f"exact mirror missing: {relative}", errors)
        continue
    if source_path.read_bytes() != plugin_path.read_bytes():
        fail(f"exact mirror differs: {relative}", errors)
```

For each forbidden marker, scan `SKILL.md`, `references/`, `examples/`, and `agents/openai.yaml`; fail with the relative path and marker.

- [ ] **Step 3: Run parity and confirm it fails before the mirror update**

```bash
POSTER_SKILL_SOURCE=/Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster python3 tests/test_plugin.py
```

Expected: non-zero exit naming legacy gate or exact-mirror differences.

- [ ] **Step 4: Mirror common files and manually adapt the four overrides**

Copy byte-identical files from the source repository. Reapply the public-safe filename example in `workflow.md`, keep Plugin installation guidance in `platform-usage.md`, keep the fully fictional successful Prompt benchmark, and keep anonymous layout-guide SVGs only as abstract reference diagrams. Add an explicit sentence that those SVG diagrams can never be used as a Mode B base or final poster.

- [ ] **Step 5: Update Plugin metadata to 0.2.0**

Change manifest and listing copy from “four steps” to “person material first + two generation modes”. Starter prompts must begin with the person-material gate. Add a `0.2.0 — 2026-08-31` changelog entry explaining bitmap-first Mode B, removal of layout confirmation, and one formal generation by default.

- [ ] **Step 6: Rewrite submission tests**

Update positive cases to cover person-only intake, Mode A, Mode B bitmap-first production, and post-production Logo overlay. Update the capability-limited negative case to require no SVG/HTML/PPT fallback.

- [ ] **Step 7: Run Plugin validation**

```bash
POSTER_SKILL_SOURCE=/Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster python3 tests/test_plugin.py
python3 scripts/verify_parity.py --source /Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster --plugin .
git diff --check
```

Expected: `PASS plugin`, `PASS parity`, and no diff-check output.

- [ ] **Step 8: Commit the Plugin update**

```bash
git add .codex-plugin/plugin.json CHANGELOG.md README.md parity/capabilities.json scripts/verify_parity.py tests/test_plugin.py tests/openai-submission.md skills/create-ip-op-poster
git commit -m "feat: release generative-first poster plugin"
```

---

### Task 6: Run independent forward tests and close evidence gaps

**Files:**
- Modify: `tests/forward-test-results-2026-08-31.md`
- Modify: `tests/scenario-regression.md`

**Interfaces:**
- Consumes: validated source Skill, private authorized test images outside the repository, and four fresh agent contexts.
- Produces: direct evidence for stage behavior, Mode A generation count, Mode B bitmap provenance, and no-fallback handling.

- [ ] **Step 1: Run `person_first` in a fresh agent context**

Give the agent only the current Skill and a set of authorized person/animal originals. Do not provide the expected answer. Verify it creates or specifies the white review image, transparent master, and independent cutouts; asks for `人物素材通过`; and does not ask for mode selection first.

- [ ] **Step 2: Run `mode_a_one_generation` in a second fresh context**

After an explicit person-material confirmation, provide a fictional Brief and choose Mode A. Verify the agent discloses redraw risk, shows the full Prompt, waits for `确认生成`, and makes exactly one formal poster-generation call. Do not approve an automatic retry.

- [ ] **Step 3: Run `mode_b_bitmap_then_layers` in a third fresh context**

After person-material approval, choose Mode B. Verify the first production artifact is a generated PNG/WebP/JPEG base with a recorded generation tool/model, then verify protected layers are composited afterward. Fail the scenario if any SVG/HTML/PPT/Canvas/Sharp artifact acts as the base.

- [ ] **Step 4: Run `no_imagegen_no_svg_fallback` in a fourth fresh context**

Tell the agent that no image-generation model is available. Verify it outputs the complete Prompt and handoff/material map and refuses to call an SVG/page renderer a final poster.

- [ ] **Step 5: Record only direct evidence**

For each scenario, use `PASS`, `FAIL`, or `NOT VERIFIABLE`; record the exact stop state, output artifact type, formal-generation count, and observed failure routing. Replace private filenames and absolute paths with stable fixture IDs before committing.

- [ ] **Step 6: Run the final source suite**

```bash
python3 tests/validate_skill.py all
git diff --check
git status --short
```

Expected: all groups pass; only the known unrelated spec edit and intended test-result changes are present.

- [ ] **Step 7: Commit the evidence**

```bash
git add tests/forward-test-results-2026-08-31.md tests/scenario-regression.md
git commit -m "test: verify generative-first poster behavior"
```

---

### Task 7: Package, install, and publish without losing user work

**Files:**
- Create: `scripts/build_release.py` in the Plugin repository
- Modify: `tests/release-report.md` in the Plugin repository
- Update: `/Users/bytedance/.codex/skills/create-ip-op-poster/` after validation
- Produce: `dist/create-ip-op-poster-plugin-0.2.0.zip`
- Produce: `dist/create-ip-op-poster-skill-0.2.0.zip`

**Interfaces:**
- Consumes: committed source and Plugin repositories.
- Produces: reproducible archives, local installation, GitHub updates, and an updated Feishu distribution attachment.

- [ ] **Step 1: Add a reproducible release builder**

The script must read version `0.2.0` from `.codex-plugin/plugin.json`, call `git archive` for the full Plugin and `HEAD:skills/create-ip-op-poster` for the Skill archive, compute SHA-256 and byte size for both, inspect archive members against forbidden patterns, and write the exact results to `tests/release-report.md`. It must fail if the Plugin worktree is dirty or the version is not `0.2.0`.

- [ ] **Step 2: Commit the builder before packaging**

```bash
git add scripts/build_release.py tests/release-report.md
git commit -m "build: add reproducible poster plugin release"
```

- [ ] **Step 3: Build and smoke-test clean archives**

```bash
python3 scripts/build_release.py
POSTER_SKILL_SOURCE=/Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster python3 tests/test_plugin.py
shasum -a 256 dist/create-ip-op-poster-plugin-0.2.0.zip dist/create-ip-op-poster-skill-0.2.0.zip
```

Extract both archives into separate `mktemp -d` directories and run the source validator and Plugin test against the extracted roots. Expected: all validation passes and hashes match `tests/release-report.md`.

- [ ] **Step 4: Commit the generated release evidence**

```bash
git add tests/release-report.md
git commit -m "test: record poster plugin 0.2.0 release"
```

- [ ] **Step 5: Run official structural validation in an isolated dependency directory**

Use the bundled Python at `/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. If PyYAML is still absent, install only `PyYAML` into a fresh `/private/tmp` target and set `PYTHONPATH` for the validator; do not modify the bundled runtime. Run Skill Creator quick validation for source, installed copy, and Plugin Skill, plus Plugin Creator validation for the Plugin root.

- [ ] **Step 6: Refresh the installed local Skill non-destructively**

Copy the validated source files into `/Users/bytedance/.codex/skills/create-ip-op-poster/` without deleting unknown files, then run:

```bash
python3 tests/validate_skill.py all /Users/bytedance/.codex/skills/create-ip-op-poster
```

Expected: every group passes.

- [ ] **Step 7: Reconcile and publish the source repository safely**

Fetch `origin` and inspect `main...origin/main`. Because the source checkout contains a user-owned dirty file, never rebase or merge in that checkout. If local and remote diverge, create a clean temporary worktree from `origin/main`, merge local `main` there without force, resolve only project-owned conflicts, rerun validation, and push the clean integration result. Never use `--force` or `--force-with-lease`.

- [ ] **Step 8: Publish the clean Plugin repository**

Fetch, verify no unexpected divergence, push `main`, then read back `.codex-plugin/plugin.json` and confirm version `0.2.0` from the public repository.

- [ ] **Step 9: Update the existing Feishu tutorial distribution**

Upload `create-ip-op-poster-plugin-0.2.0.zip` to the existing tutorial document, change its visible version/capability description, and keep the previous attachment recoverable unless the user separately requests deletion. Verify the final document contains the current GitHub installation command and the Mode A/Mode B explanation.

- [ ] **Step 10: Final audit**

Report source commit, Plugin commit, archive filenames/sizes/SHA-256, local-install validation, public read-back, Feishu attachment, and any `NOT VERIFIABLE` image behavior. Do not claim full parity if any required forward test or public smoke check remains unresolved.
