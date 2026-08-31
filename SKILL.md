---
name: create-ip-op-poster
description: Create or revise Chinese IP/OP招商海报 from recruitment briefs and person, animal, case-screenshot, or Logo assets. Use for IP proposal posters, OP posters, creator-matrix招商图, 单人达人海报, 人物素材处理, poster directions, complete generation Prompts, protected-layer compositing, or final poster QA. The workflow confirms person material first, then routes to fast whole-poster generation or fidelity-preserving compositing.
---

# Create IP OP Poster

Treat an OP as a commercial communication poster, not a one-shot illustration. Both production modes begin by preparing and explicitly confirming person/animal material. Do not start creative-direction work or choose a production mode before that confirmation. Default to the low-barrier flow in [novice-mode.md](references/novice-mode.md).

## Non-negotiable rules

1. Lock identity-critical regions: every person's face, features, expression, hairline/core hairstyle, and every animal's face, species, coat color, and recognizable markings. Never beautify, swap, cartoonize, duplicate, omit, or invent a subject.
2. Preserve every case screenshot exactly in fidelity-sensitive work. Allow only proportional scaling and placement; never crop, recolor, rewrite, repaint, enhance, repair, fabricate data, or hide meaningful content.
3. Preserve every Logo completely in fidelity-sensitive work. Allow only background removal, proportional scaling, and arrangement.
4. The white person-material review image validates roster, identity, count, body completeness, and edges. It does not lock final-poster placement, grouping, scale, or layer order.
5. Match the palette and visual language to the current brief, industry, season, or marketing node. Do not inherit the style of a prior example by default.
6. Use reference posters to learn visual grammar only. Do not copy their title, copy, Logo, seal, decoration, exact composition, or distinctive motif.
7. Include at minimum: creator image(s), IP theme, a concise project background, and the refined content play. Add real cases or data only when supplied and useful.
8. Mode A may redraw people, screenshots, Logos, and Chinese copy. Disclose this before selection and never describe its result as pixel-preserved.
9. Mode B must generate a real bitmap visual base before any protected-layer compositing. A programmatic board, layout guide, or vector page cannot substitute for that base.
10. If a required image-generation or compositing capability is unavailable, return a complete Prompt/material handoff rather than fabricating a lower-fidelity poster.
11. Default to one formal poster-generation call. Do not spend a second call automatically after a failure.

Read [material-integrity.md](references/material-integrity.md) before any image operation.

## Run the state machine

Use exactly this order:

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

Read [workflow.md](references/workflow.md) at the start. Track the current stage in every response and keep a resumable record using [handoff-template.md](references/handoff-template.md).

## Prepare and confirm person material first

1. Ask first for the person/animal originals and build a source ledger with stable `Pxx` IDs, public names, counts, variants, and limitations. A Brief, cases, Logo, or fixed copy may arrive now or later, but do not enter direction work yet.
2. For multiple subjects, use this Prompt verbatim:

   `把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 注意人物不能重复，且人物大小调整一致一些`

3. Produce all three person-material artifacts: `横版白底组合预览图`, `透明底人物总图` with the same arrangement, and `独立透明抠图` for every unique person/animal or inseparable original group.
   Mode A's later redraw permission does not apply here: every `PersonMaterialSet` must preserve the supplied identities, roster, and usable source detail before either mode is chosen.
4. Record them as a `PersonMaterialSet`:

   ```text
   review_white: horizontal white-background preview
   master_transparent: same arrangement with alpha
   subjects_transparent: one transparent layer per unique person/animal or inseparable original group
   source_ledger: stable Pxx IDs, public names, counts, variants, and limitations
   approval: exact user message or none
   ```

5. Check every identity, unique-subject count, original combination, body completeness, hair/fur edge, hand/foot edge, accidental deletion, and duplicate. Resolve failures before asking for approval.
6. Stop with the copyable reply `人物素材通过`. Only that reply or an equally explicit approval advances to `direction_and_mode_pending`.

## Combine direction and production-mode selection

After person material is approved, use the available Brief and supporting material to present 2–3 genuinely different directions. Put the recommended direction first and explain it in one plain-language sentence. For one creator, connect a recognizable content asset to a concrete play. For multiple creators, group them by content/business logic and give each group a distinct play.

Show this compact mode card exactly:

```text
模式 A｜快速生图：整张海报一次生成，通常更统一、更快；人物、截图、Logo 和中文可能被重绘。
模式 B｜保真合成：先生图生成完整艺术底图，再覆回确认过的人物、截图、Logo 和中文；更适合正式提报。
```

Accept a natural combined decision such as `选方向 1，用模式 B`. If the theme, play, and mode are already explicit, acknowledge them and continue without asking the user to choose them again. A wireframe may be supplied only when the user requests one; it is non-generative, optional, and never a production stop.

## Confirm one complete final Prompt

1. Use the confirmed `PersonMaterialSet`, direction, play, and generation mode.
2. Map every person/animal, case screenshot, Logo, and fixed-copy item to its exact role. Preserve supplied names and immutable copy verbatim.
3. Build the full mode-specific Prompt with [prompt-template.md](references/prompt-template.md).
4. Show a short production summary followed by the entire Prompt. This round is text-only and consumes no poster-generation call.
5. End with the copyable reply `确认生成`. If the user edits anything, show the revised complete Prompt and wait again.

## Produce and verify

- 模式 A：快速生图. Give the image model the complete poster task and return the generated `完整海报预览`. Apply roster, theme, readability, and obvious-identity QA without making a pixel-preservation claim.
- 模式 B：保真合成. `第一项生产动作必须调用生图模型` to create a PNG、WebP 或 JPEG visual base. Only after that bitmap exists may tools apply masks, proportional placement, protected-layer compositing, rasterized fixed copy, format conversion, and verification. `不得先运行 SVG、HTML、Canvas、PPT` or any fixed-grid renderer as the base.
- When image generation is unavailable, enter `handoff` with the complete Prompt, person assets, mappings, limitations, and next action. Do not fall back to a programmatic information board.
- `默认只调用一次正式生图`; do not spend a second generation automatically after a failure.
- Run every applicable check in [qa-checklist.md](references/qa-checklist.md). Use only `PASS`, `FAIL`, or `NOT VERIFIABLE`; unfinished evidence is never a pass.
- Mark `complete` only after all hard checks pass and the user receives the verified output or a clearly labeled handoff package.

## Invalidate downstream work

| User change | Return to | Keep |
|---|---|---|
| Add, remove, replace, or change a person/animal source or material mask | `person_material_pending` | valid Brief facts and unaffected source files |
| Change theme, play, or generation mode | `direction_and_mode_pending` | approved `PersonMaterialSet` when its sources are unchanged |
| Change fixed copy, Logo, case mapping, price, or rights | `prompt_pending` | approved person material and direction/mode when still valid |
| Change only final background or decoration after production | `production` | confirmed Prompt structure and unaffected protected layers |

Announce every invalidated downstream decision explicitly and rerun the affected QA checks.

## Load only the needed reference

- Stages, confirmation language, and rollback: [workflow.md](references/workflow.md)
- Low-barrier presentation and copyable replies: [novice-mode.md](references/novice-mode.md)
- Brief analysis, single/matrix strategy, color, and direction comparison: [direction-framework.md](references/direction-framework.md)
- Generative composition grammar: [layout-grammar.md](references/layout-grammar.md)
- Person-material and protected-layer boundaries: [material-integrity.md](references/material-integrity.md)
- Complete mode-specific final Prompt: [prompt-template.md](references/prompt-template.md)
- Visual examples and non-copying retrieval: [visual-case-library.md](references/visual-case-library.md)
- Final acceptance and failure routing: [qa-checklist.md](references/qa-checklist.md)
- Capability routing and safe downgrade: [platform-usage.md](references/platform-usage.md)
- Cross-window state record: [handoff-template.md](references/handoff-template.md)
