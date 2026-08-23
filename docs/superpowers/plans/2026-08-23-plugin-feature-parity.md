# IP/OP Poster Plugin Feature-Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, package, and publish a skills-only OpenAI Plugin whose poster workflow is functionally equivalent to the current `create-ip-op-poster` Skill.

**Architecture:** The existing Skill remains the source of truth. A separate Plugin repository contains the official manifest and a public-distribution copy of that Skill under `skills/create-ip-op-poster/`. A parity checker compares required files, workflow markers, confirmation gates, fallback behavior, and starter prompts; third-party visual examples are replaced by structured visual grammar plus anonymous layout diagrams without removing the retrieval workflow.

**Tech Stack:** OpenAI Plugin manifest, Markdown Skill resources, SVG layout diagrams, Python 3 standard-library validation, Git, GitHub CLI.

## Global Constraints

- The existing web-uploaded Skill is the only functional baseline.
- Preserve Brief analysis, solo/multi-creator classification, visual retrieval, visual direction, layouts, density decisions, four confirmation gates, protected-material handling, novice mode, handoff behavior, Prompt compilation, and final QA.
- Do not distribute third-party poster originals or creator likenesses whose public-license status is unclear.
- Do not claim pixel-identical generative output across models or surfaces.
- Do not add an MCP server, external login, user-data collection, or external write action in version `0.1.0`.
- Publish the Plugin in a separate repository named `create-ip-op-poster-plugin` without changing the current Skill installation path.

---

### Task 1: Scaffold the standalone Plugin and parity contract

**Files:**
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/.codex-plugin/plugin.json`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/parity/capabilities.json`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/scripts/verify_parity.py`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/tests/test_plugin.py`

**Interfaces:**
- Consumes: source Skill at `/Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster`.
- Produces: `verify_parity.py --source <path> --plugin <path>` returning exit code `0` only when every required capability is present.

- [ ] **Step 1: Write the failing Plugin structure and parity tests**

The tests must require the manifest, `skills/create-ip-op-poster/SKILL.md`, all referenced Markdown files, four independent Gate markers, protected-layer language, novice mode, visual direction, Prompt confirmation, and handoff behavior. They must also reject `.DS_Store`, source tests, internal design documents, and third-party visual-case raster files.

- [ ] **Step 2: Run the tests before scaffolding**

Run: `python3 tests/test_plugin.py`

Expected: non-zero exit with missing manifest and missing bundled Skill errors.

- [ ] **Step 3: Create the official Plugin manifest and capability contract**

Use the `plugin-creator` Skill to create a skills-only manifest with name `create-ip-op-poster`, display name `IP/OP 海报制作`, version `0.1.0`, and the bundled Skill path `skills/create-ip-op-poster`.

The capability contract must enumerate these stable IDs: `brief_analysis`, `solo_multi_strategy`, `visual_case_retrieval`, `visual_direction`, `layout_selection`, `density_control`, `direction_gate`, `cutout_gate`, `composition_gate`, `prompt_gate`, `protected_layers`, `novice_mode`, `cross_platform_handoff`, `prompt_compiler`, and `final_qa`.

- [ ] **Step 4: Implement the parity checker**

Use Python standard-library modules only. The checker must load `capabilities.json`, verify declared files and marker strings, verify every local relative Markdown link resolves, compare the bundled Skill name and description with the source, and print one `PASS <capability-id>` line per capability followed by `PASS parity`.

- [ ] **Step 5: Commit the scaffold**

Run: `git add .codex-plugin parity scripts tests && git commit -m "feat: scaffold feature-parity poster plugin"`

Expected: one commit containing only the manifest, contract, validator, and tests.

### Task 2: Bundle the full public Skill without workflow loss

**Files:**
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/skills/create-ip-op-poster/SKILL.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/skills/create-ip-op-poster/agents/openai.yaml`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/skills/create-ip-op-poster/references/*.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/skills/create-ip-op-poster/examples/*.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/skills/create-ip-op-poster/assets/layout-guides/*.svg`

**Interfaces:**
- Consumes: source Skill instructions, references, examples, and source visual-case index.
- Produces: a self-contained installable Skill with all functional references resolving inside the Plugin.

- [ ] **Step 1: Copy the complete functional core**

Mechanically copy `SKILL.md`, `agents/`, `references/`, and `examples/`. Do not copy `.git`, `tests`, `docs`, `.DS_Store`, contact sheets, or third-party poster raster images.

- [ ] **Step 2: Add anonymous visual equivalents**

Create original SVG diagrams for six layout families: left-copy/right-creator, three-column gameplay, dense information matrix, single-creator hero, central creator with satellite cards, and grouped creator clusters. Use only neutral rectangles, circles, lines, and generic labels; include no brands, faces, copied slogans, or case-specific symbols.

- [ ] **Step 3: Make visual retrieval self-contained**

Update the bundled `visual-case-library.md` so every retrieval family points to a local anonymous diagram and retains the source Skill's evidence fields: industry/occasion, density, creator organization, information hierarchy, and suitable/unsuitable conditions. Keep the rule that user-uploaded references are visual grammar, not copy targets.

- [ ] **Step 4: Run parity and original Skill validation**

Run: `python3 scripts/verify_parity.py --source /Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster --plugin .`

Expected: fifteen capability PASS lines and `PASS parity`.

Run the official Skill validator against `skills/create-ip-op-poster`.

Expected: `Skill is valid!` or the current validator's equivalent success result.

- [ ] **Step 5: Commit the bundled Skill**

Run: `git add skills && git commit -m "feat: bundle complete public poster skill"`

Expected: one commit containing the complete public Skill and anonymous layout assets.

### Task 3: Add public metadata, support pages, and starter prompts

**Files:**
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/README.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/SUPPORT.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/PRIVACY.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/TERMS.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/CHANGELOG.md`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/assets/icon.svg`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/assets/logo.svg`

**Interfaces:**
- Consumes: Plugin identity and complete Skill behavior.
- Produces: public-facing installation, usage, privacy, support, and release information required for GitHub and Plugin submission.

- [ ] **Step 1: Write concise installation and usage guidance**

Document the ChatGPT invocation `@create-ip-op-poster`, Codex invocation `$create-ip-op-poster`, required uploads, four confirmation replies, and the difference between an installed Plugin and a temporarily uploaded zip file.

- [ ] **Step 2: Write privacy, terms, and support documents**

State that version `0.1.0` is skills-only, has no MCP server, performs no independent data collection, and processes files only through the host product's capabilities and policies. State that users must have rights to uploaded people, screenshots, Logos, and references.

- [ ] **Step 3: Add original identity assets**

Create minimal original SVG icon and logo assets using the letters `OP` and neutral geometric framing only.

- [ ] **Step 4: Add release notes**

Record version `0.1.0` as the feature-parity public preview with the four Gate workflow, protected layers, novice mode, visual direction, Prompt compiler, QA, and capability fallback.

- [ ] **Step 5: Commit public metadata**

Run: `git add README.md SUPPORT.md PRIVACY.md TERMS.md CHANGELOG.md assets && git commit -m "docs: add public plugin metadata"`

Expected: one documentation and identity-asset commit.

### Task 4: Validate, install-test, package, and publish

**Files:**
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/dist/create-ip-op-poster-plugin-0.1.0.zip`
- Create: `/Users/bytedance/Documents/work/evaluation/plugin-build/create-ip-op-poster-plugin/tests/release-report.md`

**Interfaces:**
- Consumes: complete Plugin repository.
- Produces: a verified GitHub repository, downloadable release archive, checksum, and evidence-based release report.

- [ ] **Step 1: Run all static tests**

Run: `python3 tests/test_plugin.py`

Expected: `PASS plugin`.

Run: `python3 scripts/verify_parity.py --source /Users/bytedance/Documents/work/evaluation/skill-build/create-ip-op-poster --plugin .`

Expected: fifteen capability PASS lines and `PASS parity`.

- [ ] **Step 2: Perform a clean-install inspection**

Extract the release candidate into a new temporary directory, verify the manifest and all bundled references resolve there, then rerun `tests/test_plugin.py` against that extracted copy. Record the result in `tests/release-report.md`.

- [ ] **Step 3: Package the public archive**

Create `dist/create-ip-op-poster-plugin-0.1.0.zip` from tracked public files only. Exclude `.git`, local caches, test fixtures containing user materials, and the `dist` directory itself. Generate and record a SHA-256 checksum.

- [ ] **Step 4: Publish to GitHub**

Create or update the public repository `nmmg0112/create-ip-op-poster-plugin`, push the validated `main` branch, create tag `v0.1.0`, and attach the release archive. Do not rewrite unrelated repository history.

- [ ] **Step 5: Verify the remote release**

Read back the remote default branch, tag, manifest, bundled `SKILL.md`, and release asset. Compare the remote commit to the local `HEAD` and record the URLs and commit SHA in `tests/release-report.md`.

- [ ] **Step 6: Update the institution tutorial attachment**

Add the Plugin repository link and attach the validated Plugin archive to the existing Feishu tutorial without removing the standalone Skill archive. Read back the edited section and both attachments.

- [ ] **Step 7: Commit release evidence**

Run: `git add tests/release-report.md && git commit -m "test: record plugin release verification"`

Expected: the final local commit contains only release evidence; publish that commit and confirm the remote branch matches it.
