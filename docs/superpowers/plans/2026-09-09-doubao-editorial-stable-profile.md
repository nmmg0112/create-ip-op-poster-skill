# Doubao Editorial Stable Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Doubao-only Seedream 5.0 Pro editorial poster profile that preserves the proven large-title, approved-person hero, case-collage composition while keeping Aime and generic-agent behavior unchanged.

**Architecture:** Keep the existing shared two-confirmation director core. Route Doubao to a focused executor that explicitly invokes `skill://seedream-50?type=2&id=360075272194`, binds an `ApprovedPersonAssetSet`, compiles an editorial whole-poster prompt, and allows a lower model only after an informed user opt-in. Mirror the tested source Skill into the public Plugin and rebuild versioned archives.

**Tech Stack:** Markdown Skill instructions, Python 3 standard-library validation, Git, ZIP release scripts.

## Global Constraints

- Aime continues to use the current Image2 dynamic visual-director path.
- Generic agents retain the current adaptive layout path.
- Doubao defaults to [`Seedream 5.0 Pro`](skill://seedream-50?type=2&id=360075272194) and must invoke the Skill URI instead of merely naming the model.
- The Doubao default composition is editorial: large title, approved person hero or ensemble, real case collage, and concrete play copy.
- Each play may use one to three lines; it is not limited to one sentence.
- Doubao must not silently fall back. A lower model is allowed only after the user explicitly replies `继续用当前模型` following a quality warning.
- The normal flow still has only `人物没问题` and `选 1 生成` as confirmation points.
- One explicit generation authorization permits one formal whole-poster generation.
- Code may make an exact local correction to an accepted image; it may not design the background, layout, card wall, or complete poster.
- Aime and generic behavior tests must continue to pass.

---

### Task 1: Define failing Doubao behavior tests

**Files:**
- Modify: `tests/validate_skill.py`
- Modify: `tests/scenario-regression.md`

**Interfaces:**
- Consumes: current `check_platforms`, `check_prompt`, `check_integrity`, and scenario protocol.
- Produces: a new `doubao_editorial` validation group and observable regression scenarios for the implementation tasks.

- [ ] **Step 1: Add the new validation group and checks**

Add `doubao_editorial` to `GROUPS` and implement `check_doubao_editorial(root)` with direct assertions for:

```python
def check_doubao_editorial(root: Path) -> None:
    skill = read(root, "SKILL.md")
    doubao = read(root, "references/platforms/doubao-executor.md")
    prompt = read(root, "references/prompt-template.md")
    qa = read(root, "references/qa-checklist.md")
    corpus = "\n".join((skill, doubao, prompt, qa))

    for needle in (
        "skill://seedream-50?type=2&id=360075272194",
        "不得只在 Prompt 中写模型名称",
        "本次生图模型：Seedream 5.0 Pro",
        "继续用当前模型",
        "不得静默降级",
        "actual_model",
        "ApprovedPersonAssetSet",
        "大标题＋人物主视觉＋案例拼贴＋玩法说明",
        "一至三行",
        "杂志编辑式",
        "creative-design",
    ):
        require(corpus, needle, "Doubao editorial stable profile")

    for forbidden_default in (
        "默认三等分玻璃舱",
        "默认霓虹控制台",
        "先生成无字空底图",
    ):
        forbid(corpus, forbidden_default, "Doubao visual fallback")
```

Register the function in `CHECKS` as `"doubao_editorial": check_doubao_editorial`.

- [ ] **Step 2: Add four observable scenario regressions**

Append scenarios covering:

```text
场景 9：豆包默认模型为 4.5
Expected: invoke the exact Seedream URI first; if unavailable, explain the actual reason and wait; do not call 4.5 automatically.

场景 10：用户明确接受降级
Expected: only after “继续用当前模型”, record actual_model, permit one formal generation, and retain all QA thresholds.

场景 11：豆包多人＋六张案例＋中等文字密度
Expected: first formal poster contains large title, approved ensemble, case collage, and one-to-three-line copy per play; no glass compartments or PPT card wall.

场景 12：Aime control
Expected: Image2 adaptive composition remains unchanged and does not inherit the Doubao editorial default.
```

- [ ] **Step 3: Run the new test and verify failure**

Run:

```bash
python3 tests/validate_skill.py doubao_editorial
```

Expected: `FAIL doubao_editorial` because the current Skill lacks the exact URI, asset set, editorial profile, and informed fallback fields.

- [ ] **Step 4: Commit the failing tests**

```bash
git add tests/validate_skill.py tests/scenario-regression.md
git commit -m "test: define Doubao editorial stable profile"
```

### Task 2: Add top-level model routing and approved-person binding

**Files:**
- Modify: `SKILL.md`
- Modify: `references/workflow.md`
- Modify: `references/handoff-template.md`
- Modify: `references/material-integrity.md`

**Interfaces:**
- Consumes: `LockedPosterSpec`, stable `Pxx` identifiers, the two-confirmation state machine.
- Produces: `ApprovedPersonAssetSet` and model receipt fields used by the Doubao executor and QA.

- [ ] **Step 1: Add the Doubao model invocation hard gate to `SKILL.md`**

Immediately below platform routing, state:

```markdown
On 豆包, before any generative image operation, explicitly invoke [Seedream 5.0 Pro](skill://seedream-50?type=2&id=360075272194). Naming the model in prose is not an invocation. If the Skill cannot be verified, explain the actual platform reason and do not silently use a default model. A lower model is allowed only after the user explicitly replies `继续用当前模型` to the disclosed quality warning.
```

Keep the Aime routing paragraph unchanged.

- [ ] **Step 2: Define `ApprovedPersonAssetSet`**

Add this shared record to `workflow.md`, `handoff-template.md`, and `material-integrity.md`:

```yaml
approved_person_asset_set:
  version: person-v1
  assets:
    - id: P01
      public_name: example-name
      approved_source: /absolute/or-platform/asset-reference.png
      original_group: single
  approved_preview: /absolute/or-platform/approved-preview.png
  presentation_mode: unified-ensemble | grouped-by-play | hybrid-hero-groups | single-hero
  user_approved: true
```

Require every formal call to attach the approved preview for `unified-ensemble`, approved independent assets for `grouped-by-play`, or both for `hybrid-hero-groups`. Names alone never satisfy the binding.

- [ ] **Step 3: Add model receipt fields to the handoff**

Add:

```yaml
requested_model: Seedream 5.0 Pro
model_skill_uri: skill://seedream-50?type=2&id=360075272194
model_skill_loaded: true | false | NOT_VERIFIABLE
actual_model: Seedream 5.0 Pro | platform-reported-model | NOT_VERIFIABLE
downgrade_approved: true | false
```

- [ ] **Step 4: Run shared regression groups**

Run:

```bash
python3 tests/validate_skill.py workflow
python3 tests/validate_skill.py integrity
python3 tests/validate_skill.py platforms
```

Expected: all three commands print `PASS`.

- [ ] **Step 5: Commit the shared contract**

```bash
git add SKILL.md references/workflow.md references/handoff-template.md references/material-integrity.md
git commit -m "feat: bind approved people and Doubao model receipts"
```

### Task 3: Rewrite the Doubao executor around the proven editorial path

**Files:**
- Modify: `references/platforms/doubao-executor.md`
- Modify: `references/prompt-template.md`
- Modify: `references/platform-usage.md`
- Modify: `references/qa-checklist.md`

**Interfaces:**
- Consumes: `ApprovedPersonAssetSet`, `LockedPosterSpec`, exact Seedream Skill URI, optional platform-native `creative-design` capability.
- Produces: one Doubao editorial whole-poster call and a truthful model/QA receipt.

- [ ] **Step 1: Replace the Doubao model opening with an explicit invocation sequence**

Use this exact order:

```text
detect Doubao
  -> invoke skill://seedream-50?type=2&id=360075272194
  -> verify model_skill_loaded
  -> show “本次生图模型：Seedream 5.0 Pro” without waiting
  -> use creative-design when actually available
  -> continue person or formal generation
```

If verification fails, show the design-spec warning and wait for either `切换／开通后继续` or `继续用当前模型`. Do not infer that billing is the cause without platform evidence.

- [ ] **Step 2: Add the editorial visual profile**

Write the default visual grammar as:

```markdown
豆包默认使用“大标题＋人物主视觉＋案例拼贴＋玩法说明”的杂志编辑式构图。标题、人物与案例可跨区、交叠和穿插；多人默认使用批准群像，单人改为单一明星／达人主视觉。配色、标题字体、材质、光线和拼贴语言随 Brief 变化，因此这不是固定坐标模板。
```

Explicitly reject default glass compartments, holographic UI, neon control rooms, equal card walls, tiny people, and code-built visual design. Translate “科技炫酷” into real industry scenery, restrained cool colors, metal, exhibition lighting, speed, crop, and depth.

- [ ] **Step 3: Add first-pass content density**

Require the first formal poster to include theme, concise background, approved people, four-to-six provided case screenshots, and for each play:

```text
玩法标题
对应成员
1—3 行说明：场景／关系，动作／挑战／互动，产品进入；有空间时补案例依据、合作价值或内容结果
```

Do not invent cases when none were provided. Do not limit play copy to one sentence.

- [ ] **Step 4: Add one-call revision control and QA**

Forbid the observed chain `新版 -> 无字底图 -> 代码叠字版 -> 聚合底图 -> 精装修版`. One explicit revision request creates one new locked spec and one formal generation. Add hard QA failures for wrong model receipt, missing attached approved assets, people reduced to card illustrations, no case/play linkage, and PPT-style layout.

- [ ] **Step 5: Run focused and full source tests**

Run:

```bash
python3 tests/validate_skill.py doubao_editorial
python3 tests/validate_skill.py prompt
python3 tests/validate_skill.py production
python3 tests/validate_skill.py visual
python3 tests/validate_skill.py all
```

Expected: every command prints `PASS`; `all` ends with `PASS all`.

- [ ] **Step 6: Commit the Doubao executor**

```bash
git add references/platforms/doubao-executor.md references/prompt-template.md references/platform-usage.md references/qa-checklist.md
git commit -m "feat: add Doubao editorial Seedream profile"
```

### Task 4: Update beginner and contest-facing documentation

**Files:**
- Modify: `README.md`
- Modify: `examples/quick-start.md`
- Modify: `examples/prompt.txt`
- Modify: `examples/result.md`
- Create: `examples/golden-case-doubao-editorial.md`

**Interfaces:**
- Consumes: the finalized Doubao runtime contract.
- Produces: a reproducible judge/user example without requiring a long startup prompt.

- [ ] **Step 1: Add a concise Doubao note to user docs**

State that Doubao attempts to invoke the exact Seedream Skill automatically, shows the actual model before generation, warns before any downgrade, and defaults to the proven editorial composition. Do not make the user paste the Skill URI or a long startup prompt.

- [ ] **Step 2: Add the sanitized good-case example**

Create `examples/golden-case-doubao-editorial.md` with a fictional creator matrix and this result structure:

```text
16:9 landscape
large expressive theme title
approved 11-person ensemble as the right/center hero
two evidence-backed plays with members and 1–3 lines each
six real supplied case screenshots in editorial collage
restrained cream/orange magazine palette
no card wall, no glass compartments, no invented metrics
```

Include user input, director judgment, `ApprovedPersonAssetSet`, `LockedPosterSpec`, condensed execution prompt, actual model receipt schema, and success criteria. Clearly state that it teaches visual grammar rather than a fixed theme.

- [ ] **Step 3: Extend contest evidence without inventing live results**

In `examples/result.md`, record the two observed Doubao failure categories and the extracted good-case mechanism. Mark the new 0.4.x Doubao forward result `NOT VERIFIABLE` until the user completes a live test.

- [ ] **Step 4: Run documentation tests**

Run:

```bash
python3 tests/validate_skill.py onboarding
python3 tests/validate_skill.py contest
python3 tests/validate_skill.py docs
```

Expected: all three commands print `PASS`.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md examples/quick-start.md examples/prompt.txt examples/result.md examples/golden-case-doubao-editorial.md
git commit -m "docs: add reproducible Doubao editorial workflow"
```

### Task 5: Validate and synchronize the installed Skill

**Files:**
- Modify: `/Users/bytedance/.codex/skills/create-ip-op-poster/**` by deterministic synchronization after source validation.
- Create: `tests/forward-test-results-2026-09-09-doubao-editorial.md`

**Interfaces:**
- Consumes: validated source package.
- Produces: locally installed parity and a forward-test receipt distinguishing static validation from live Doubao output.

- [ ] **Step 1: Run official source validation**

Run:

```bash
PYTHONPATH=/private/tmp/create-ip-op-poster-validator-deps \
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12 \
/Users/bytedance/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Expected: `Skill is valid!`.

- [ ] **Step 2: Record source-level results truthfully**

Create a receipt with `PASS` for static contract validation, `PASS` for source package structure, and `NOT VERIFIABLE` for live Seedream image quality until the user returns a new Doubao conversation link and image.

- [ ] **Step 3: Synchronize the validated package**

Copy only active package files—`SKILL.md`, `README.md`, `agents`, `assets`, `examples`, `references`—into `/Users/bytedance/.codex/skills/create-ip-op-poster`, preserving any unrelated workspace files. Re-run:

```bash
for group in workflow production visual integrity prompt onboarding platforms contest doubao_editorial; do
  python3 /Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster/tests/validate_skill.py \
    "$group" /Users/bytedance/.codex/skills/create-ip-op-poster
done
```

Expected: every listed active-package group prints `PASS`. Do not run the `docs` group against the installed copy because `tests/scenario-regression.md` is intentionally not shipped. Then run official `quick_validate.py` on the installed directory.

- [ ] **Step 4: Commit the source test receipt**

```bash
git add tests/forward-test-results-2026-09-09-doubao-editorial.md
git commit -m "test: record Doubao editorial profile validation"
```

### Task 6: Mirror, release, and publish version 0.4.1

**Files:**
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/skills/create-ip-op-poster/**`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/.codex-plugin/plugin.json`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/parity/capabilities.json`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/tests/test_plugin.py`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/CHANGELOG.md`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/README.md`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/openai-submission.md`
- Generated: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/dist/create-ip-op-poster-skill-0.4.1.zip`
- Generated: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/dist/create-ip-op-poster-plugin-0.4.1.zip`

**Interfaces:**
- Consumes: the validated source Skill and existing parity/build scripts.
- Produces: public 0.4.1 source and Plugin repositories plus testable archives.

- [ ] **Step 1: Mirror active source files and extend parity**

Synchronize the active package into `skills/create-ip-op-poster`. Add capability markers for the exact Seedream URI, informed downgrade, `ApprovedPersonAssetSet`, editorial profile, one-to-three-line play copy, and Aime isolation to `parity/capabilities.json` and `tests/test_plugin.py`.

- [ ] **Step 2: Bump public release metadata**

Change manifest and release documentation from `0.4.0` to `0.4.1`. Describe the release as a Doubao-specific stability patch; do not claim live image-quality validation before the user's test.

- [ ] **Step 3: Run Plugin validation and parity**

Run:

```bash
python3 tests/test_plugin.py
python3 scripts/verify_parity.py \
  --source /Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster \
  --plugin /Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster
PYTHONPATH=/private/tmp/create-ip-op-poster-validator-deps \
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12 \
/Users/bytedance/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: `PASS plugin`, `PASS parity`, and `Plugin validation passed`.

- [ ] **Step 4: Commit and build clean archives**

```bash
git add .codex-plugin/plugin.json skills parity tests CHANGELOG.md README.md openai-submission.md
git commit -m "feat: release Doubao editorial profile 0.4.1"
python3 scripts/build_release.py
unzip -t dist/create-ip-op-poster-skill-0.4.1.zip
unzip -t dist/create-ip-op-poster-plugin-0.4.1.zip
```

Expected: both archives pass integrity checks and the release report lists their SHA-256 hashes.

- [ ] **Step 5: Copy user-facing archives and push both repositories**

Copy the new ZIPs to:

```text
/Users/bytedance/Documents/work/deliverables/create-ip-op-poster-skill-0.4.1.zip
/Users/bytedance/Documents/work/deliverables/create-ip-op-poster-plugin-0.4.1.zip
/Users/bytedance/Documents/work/create-ip-op-poster-skill.zip
```

Push source and Plugin `main`, then verify both remote heads with `git ls-remote`. Preserve the unrelated modified file `docs/superpowers/specs/2026-08-23-ip-op-poster-plugin-design.md` and do not include it in any commit.

- [ ] **Step 6: Hand off live Doubao testing**

Give the user the 0.4.1 Skill ZIP and the one-line starter:

```text
我已经上传了 create-ip-op-poster Skill。请读取它，告诉我怎么使用，并带我开始制作一张海报。
```

Ask for the resulting share link or images. Keep live model selection, person fidelity, visual quality, and content density as `NOT VERIFIABLE` until that evidence returns.
