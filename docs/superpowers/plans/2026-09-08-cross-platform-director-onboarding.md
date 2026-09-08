# Cross-Platform Poster Director and Onboarding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the poster Skill open with beginner guidance automatically and give Aime Image2 and Doubao Seedream 5.0 Pro the same locked visual-director execution contract used by Codex.

**Architecture:** Keep the two-confirmation workflow in the shared Skill core, then route platform-specific execution to two self-contained adapter files. Convert accepted user input into one `LockedPosterSpec`, compile only that current version into the image prompt, and protect accepted poster versions through `PosterVersionLock`. Package contest-required reproducible prompts and result evidence with the same source tree used by Codex, Aime, Doubao, the plugin mirror, and release ZIP.

**Tech Stack:** Markdown Skill instructions, YAML UI metadata, Python 3 static validation, Git, ZIP release tooling.

## Global Constraints

- Default user flow has exactly two confirmations: `人物没问题` and `选 1 生成`.
- The Skill itself emits the opening guidance; users never have to copy a long startup prompt.
- Aime formal image execution uses Image2.
- Doubao person preparation and formal image execution use Seedream 5.0 Pro.
- The default OP master is one complete `16:9 横版` poster.
- Do not restore layout-draft, full-Prompt, or technical-route confirmation gates.
- Formal generation consumes only the current `LockedPosterSpec`, not the raw conversation history.
- First accepted poster versions remain available; isolated text, Logo, price, right, or case changes do not trigger whole-poster redraw.
- The contest ZIP contains `SKILL.md`, `README.md`, `examples/prompt.txt`, and a result example.
- Preserve the unrelated working-tree modification in `docs/superpowers/specs/2026-08-23-ip-op-poster-plugin-design.md`.

---

### Task 1: Add failing validation for the new runtime contract

**Files:**
- Modify: `tests/validate_skill.py`
- Modify: `tests/scenario-regression.md`

**Interfaces:**
- Consumes: current Markdown package rooted at `DEFAULT_ROOT`.
- Produces: `check_onboarding`, `check_platforms`, and `check_contest` validation groups plus Aime/Doubao regression scenarios.

- [ ] **Step 1: Make package discovery recursive**

Replace top-level-only reference and example discovery with recursive Markdown/text discovery:

```python
def package_documents(root: Path) -> list[Path]:
    paths = [root / "SKILL.md", root / "README.md", root / "agents/openai.yaml"]
    for folder in (root / "references", root / "examples"):
        for suffix in ("*.md", "*.txt"):
            paths.extend(sorted(folder.rglob(suffix)))
    return paths
```

Use this helper in `active_package_files` and Markdown-link validation so the platform adapters and Golden Cases are part of the active corpus.

- [ ] **Step 2: Add focused checks**

Add checks equivalent to:

```python
def check_onboarding(root: Path) -> None:
    novice = read(root, "references/novice-mode.md")
    for needle in (
        "Skill 被读取后自动发送", "资料不全也没关系", "【主题／Brief】",
        "【喜欢的风格】", "【文字密度】", "【必须出现的文字】",
        "开场白只出现一次", "不要求用户复制",
    ):
        require(novice, needle, "automatic beginner onboarding")


def check_platforms(root: Path) -> None:
    aime = read(root, "references/platforms/aime-executor.md")
    doubao = read(root, "references/platforms/doubao-executor.md")
    shared = read(root, "references/platform-usage.md")
    for needle in ("Image2", "LockedPosterSpec", "当前锁定版本", "不得把整段聊天记录"):
        require(aime, needle, "Aime adapter")
    for needle in ("Seedream 5.0 Pro", "LockedPosterSpec", "稳定人物编号", "开场白"):
        require(doubao, needle, "Doubao adapter")
    for needle in ("PosterVersionLock", "上一版成功文件", "局部修改"):
        require(aime + doubao + shared, needle, "version protection")


def check_contest(root: Path) -> None:
    prompt = read(root, "examples/prompt.txt")
    result = read(root, "examples/result.md")
    for needle in ("人物没问题", "选 1 生成", "16:9 横版"):
        require(prompt, needle, "contest reproducible prompt")
    for needle in ("业务痛点", "关键链路", "真实案例", "可量化"):
        require(result, needle, "contest result evidence")
```

Register the three groups in `GROUPS`, `CHECKS`, and the CLI usage string.

- [ ] **Step 3: Add Aime and Doubao regression scenarios**

Append two scenarios to `tests/scenario-regression.md`:

- Aime evaluator uploads the package and says only “帮我安装并告诉我怎么使用”; expected automatic opening, Image2 route, locked current spec, and no copied long starter.
- Doubao user uploads the package and says only “用这个 Skill 帮我做海报”; expected automatic opening, Seedream 5.0 Pro route, stable subject IDs, and the same two confirmation points.

- [ ] **Step 4: Run the focused tests and verify failure**

Run:

```bash
python3 tests/validate_skill.py onboarding
python3 tests/validate_skill.py platforms
python3 tests/validate_skill.py contest
```

Expected: each group fails because the new files and required contract text do not exist yet.

- [ ] **Step 5: Commit the failing contract tests**

```bash
git add tests/validate_skill.py tests/scenario-regression.md
git commit -m "test: define Aime Doubao poster runtime contract"
```

### Task 2: Implement automatic onboarding and locked-spec behavior

**Files:**
- Modify: `SKILL.md`
- Modify: `references/novice-mode.md`
- Modify: `references/workflow.md`
- Modify: `references/prompt-template.md`
- Modify: `references/handoff-template.md`
- Modify: `references/qa-checklist.md`

**Interfaces:**
- Consumes: user materials, the approved person preview, and selected `ContentPlanCard`.
- Produces: one current `LockedPosterSpec`, one compiled execution Prompt, and one `PosterVersionLock` record.

- [ ] **Step 1: Add the automatic opening contract**

In `novice-mode.md`, state that the Skill emits the approved opening automatically after it is read, only once, and skips repeated teaching when the user already supplied materials. Include the exact short template fields and multiplayer example from the design specification.

- [ ] **Step 2: Route the entrypoint to onboarding and platform adapters**

In `SKILL.md`, add:

```text
When the user asks how to use the uploaded Skill or starts without materials, emit the automatic beginner opening from novice-mode.md. Do not ask the user to copy a long startup Prompt. Detect the current host and read only its adapter under references/platforms/ when one exists.
```

Keep the existing two-confirmation state machine unchanged.

- [ ] **Step 3: Define `LockedPosterSpec` compilation**

Add the exact fields from the approved design to `workflow.md`, `prompt-template.md`, and `handoff-template.md`. Require `spec_version`, current sources, aspect ratio, plays, first visual, person mode, density, color/material/light/depth/motion, reading path, required/forbidden copy, reference grammar, and `formal_generation_count`.

State that `选 1 生成` locks the current spec and that rejected earlier directions, platform instructions, and explanatory chat are excluded from the image prompt.

- [ ] **Step 4: Define `PosterVersionLock`**

Add fields for accepted output path, accepted hash when available, approval wording, allowed local-edit target, successor version, and previous-version preservation. Make whole-style changes return to `content_plan_pending`; isolated exact changes remain in `production` and preserve the accepted file.

- [ ] **Step 5: Update QA**

Require checks that the prompt was compiled from one current spec, stale directions are absent, the expected platform model was used, the accepted version is preserved, and a local edit did not mutate non-target regions.

- [ ] **Step 6: Run core validation**

```bash
python3 tests/validate_skill.py workflow
python3 tests/validate_skill.py production
python3 tests/validate_skill.py prompt
python3 tests/validate_skill.py onboarding
```

Expected: all four groups print `PASS`.

- [ ] **Step 7: Commit the shared behavior**

```bash
git add SKILL.md references/novice-mode.md references/workflow.md references/prompt-template.md references/handoff-template.md references/qa-checklist.md
git commit -m "feat: add automatic onboarding and locked poster specs"
```

### Task 3: Add self-contained Aime and Doubao adapters

**Files:**
- Create: `references/platforms/aime-executor.md`
- Create: `references/platforms/doubao-executor.md`
- Modify: `references/platform-usage.md`
- Modify: `agents/openai.yaml`

**Interfaces:**
- Consumes: approved `PersonMaterialSet` and current `LockedPosterSpec`.
- Produces: a platform-specific image call, production receipt, and version-lock outcome.

- [ ] **Step 1: Write the Aime adapter**

Make the file self-contained and require this order:

```text
read package -> automatic opening -> person preview -> 人物没问题
-> two ContentPlanCards -> 选 1 生成 -> lock current spec
-> compile minimal prompt -> call Image2 once -> inspect output -> lock accepted version
```

Include Aime-specific failures: failing to call Image2, forwarding the raw conversation, carrying rejected requirements, generating portrait, and redrawing the full image for a label change.

- [ ] **Step 2: Write the Doubao adapter**

Use the same order, but require Seedream 5.0 Pro for both person preparation and formal generation. Require stable `Pxx` names for multi-image input and stop with a capability explanation if the current conversation cannot use Seedream 5.0 Pro or multi-image reference.

- [ ] **Step 3: Add shared adapter routing**

In `platform-usage.md`, state that platform detection is internal and users never choose an adapter. Link both adapter files and preserve the existing safe downgrade contract.

- [ ] **Step 4: Simplify the UI default prompt**

Change `agents/openai.yaml` so `default_prompt` asks the Skill to introduce itself and start the automatic flow, rather than teaching the entire workflow to the user.

- [ ] **Step 5: Run platform validation**

```bash
python3 tests/validate_skill.py platforms
python3 tests/validate_skill.py docs
```

Expected: both groups print `PASS`.

- [ ] **Step 6: Commit the adapters**

```bash
git add references/platforms references/platform-usage.md agents/openai.yaml
git commit -m "feat: add self-contained Aime and Doubao executors"
```

### Task 4: Add contest-ready reproducible examples and user documentation

**Files:**
- Create: `examples/prompt.txt`
- Create: `examples/result.md`
- Create: `examples/golden-case-multi-person.md`
- Create: `examples/golden-case-single-person.md`
- Modify: `README.md`
- Modify: `examples/quick-start.md`
- Replace: `examples/chatgpt-starter.md`

**Interfaces:**
- Consumes: the automatic opening, current two-confirmation workflow, and approved good-case reasoning.
- Produces: contest-required reproducible input, result evidence format, and platform-readable Golden Cases.

- [ ] **Step 1: Add the reproducible evaluator Prompt**

`examples/prompt.txt` must start with one natural sentence:

```text
我已经上传了 create-ip-op-poster Skill。请读取它，告诉我怎么使用，并带我开始制作一张海报。
```

Then provide a complete fictional four-person test payload and the two replies `人物没问题` and `选 1 生成`, so evaluators can replay the whole chain without using private source material.

- [ ] **Step 2: Add the result evidence file**

`examples/result.md` must explain the business pain, key chain, one multi-person and one single-person real test, result location or attachment slot, model/tool used, observable pass/fail items, time/call-count baseline, and measurement fields. Do not invent usage counts or time savings; label unmeasured metrics as awaiting Aime test evidence.

- [ ] **Step 3: Add two Golden Cases**

Each Golden Case must contain user input, director decisions, `LockedPosterSpec`, compact execution Prompt, visible success criteria, and anti-copy guidance. Use the sports ensemble and single-person beauty patterns, but do not include private source images or copyrighted source portraits in the public package.

- [ ] **Step 4: Replace the long copied starter**

Rewrite `chatgpt-starter.md` as an upload-and-one-sentence guide. Keep platform-specific model guidance and state that the Skill itself emits the detailed opening.

- [ ] **Step 5: Update README and quick start**

Lead with the minimal evaluator/user path, list Aime first because it is the contest environment, then Doubao, Codex, and ChatGPT. Explain that the ZIP must be uploaded and that the user does not copy a long startup Prompt.

- [ ] **Step 6: Run documentation and contest validation**

```bash
python3 tests/validate_skill.py contest
python3 tests/validate_skill.py docs
python3 tests/validate_skill.py visual
```

Expected: all three groups print `PASS`.

- [ ] **Step 7: Commit the examples and docs**

```bash
git add README.md examples
git commit -m "docs: add contest-ready poster skill examples"
```

### Task 5: Validate, mirror, package, and publish

**Files:**
- Create: `tests/forward-test-results-2026-09-08-aime-doubao.md`
- Modify: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster/skills/create-ip-op-poster/`
- Modify: `/Users/bytedance/.codex/skills/create-ip-op-poster/`
- Create: `/Users/bytedance/Documents/work/deliverables/create-ip-op-poster-skill-2026-09-08.zip`

**Interfaces:**
- Consumes: validated source Skill repository.
- Produces: identical installed Skill, plugin mirror, contest ZIP, GitHub commit, and Aime test handoff.

- [ ] **Step 1: Run complete local validation**

```bash
python3 tests/validate_skill.py all
python3 /Users/bytedance/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
git diff --check
```

Expected: `PASS all`, `Skill is valid!`, and no whitespace errors.

- [ ] **Step 2: Record behavior-forward results**

Create `tests/forward-test-results-2026-09-08-aime-doubao.md` with separate Aime and Doubao rows. Static package checks may be `PASS`; live Aime and Doubao image results remain `NOT VERIFIABLE` until the user runs them. Do not convert unavailable live evidence into `PASS`.

- [ ] **Step 3: Synchronize the plugin mirror and local installation**

Copy the active Skill files while excluding `.git`, `docs/superpowers`, and transient outputs. Verify file-list and SHA-256 parity for `SKILL.md`, `README.md`, `agents`, `references`, `examples`, and `assets` across source, plugin mirror, and installed Skill.

- [ ] **Step 4: Build the contest ZIP**

Create a package whose top directory is `create-ip-op-poster/` and verify:

```text
create-ip-op-poster/SKILL.md
create-ip-op-poster/README.md
create-ip-op-poster/examples/prompt.txt
create-ip-op-poster/examples/result.md
```

Run `unzip -t` and reject macOS metadata or missing required files.

- [ ] **Step 5: Commit test evidence**

```bash
git add tests/forward-test-results-2026-09-08-aime-doubao.md
git commit -m "test: record cross-platform poster skill validation"
```

- [ ] **Step 6: Push the public Skill repository**

```bash
git push origin main
```

Expected: the remote `main` contains the local HEAD.

- [ ] **Step 7: Hand off the Aime test**

Give the user the ZIP path and this one-sentence evaluator input:

```text
我已经上传了 create-ip-op-poster Skill。请读取它，告诉我怎么使用，并带我开始制作一张海报。
```

Ask the user to return the Aime share link or screenshots so live image quality, task completion, and measurable time/call savings can replace the `NOT VERIFIABLE` entries.
