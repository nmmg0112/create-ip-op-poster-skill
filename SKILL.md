---
name: create-ip-op-poster
description: Create or revise Chinese IP/OP招商海报 from an arbitrary recruitment brief and creator, person, animal, case-screenshot, or Logo assets. Use when a user wants an IP proposal poster, OP poster, creator-matrix招商图, 单人达人海报, 达人抠图拼贴, 海报创意方向, 海报生成 Prompt, or final poster QA. This Skill guides brief analysis, 2–3 direction choices, single-creator play or multi-creator grouping, theme-matched color/layout, identity-preserving cutout collage, a user-confirmed final generation Prompt, pixel-preserved case/Logo placement, cross-platform handoff, and strict acceptance checking.
---

# Create IP OP Poster

Treat an OP as a commercial communication poster, not a one-shot illustration. Co-create it through three mandatory confirmation gates and preserve supplied people, animals, screenshots, and Logos as source layers.

## Non-negotiable rules

1. Always lock identity-critical regions: every person's face, features, expression, hairline/core hairstyle, and every animal's face, species, coat color, and recognizable markings. Never beautify, swap, cartoonize, duplicate, omit, or invent a subject.
2. Default to `strict-preserve` mode: allow only background removal, proportional scaling, movement, layer ordering, and non-destructive shadow. Preserve clothing, body, pose, and source pixels.
3. Enter `identity-locked-blend` mode only after the user explicitly authorizes relaxing non-face restrictions. In this mode, allow deletion/occlusion of non-core body areas, removal of source backgrounds/furniture, reconstruction of small clothing or body-edge gaps, and restrained light/color unification. Never edit a locked identity region, change a recognizable pose, or add a new subject. Label the result as generatively blended, not pixel-preserved.
4. Preserve every case screenshot exactly. Allow only proportional scaling and placement. Never crop, recolor, rewrite, repaint, enhance, repair, fabricate data, or hide meaningful content.
5. Preserve every Logo completely. Allow only background removal, proportional scaling, and arrangement.
6. Generate background, typography, and decoration separately from protected screenshots and Logos. Keep identity masks available when blending people or animals.
7. Match the palette and visual language to the current brief, industry, season, or marketing node. Do not default to autumn, poetry, or any prior example.
8. Include at minimum: creator image(s), IP theme, a concise project background, and the refined content play. Add real cases or data only when the user supplied them and space permits.
9. Use reference posters to learn visual grammar only. Do not copy their title, copy, Logo, seal, decoration, or distinctive motif. A user-approved reference may guide broad group-layout grammar such as a three-tier stage composition.
10. Never claim pixel preservation after generative blending. Report the active mode, run identity QA, and return to Gate 2 on any face, hair, animal-head, count, or identity failure.

Read [material-integrity.md](references/material-integrity.md) before any image operation.

## Run the state machine

Use these stages and do not skip ahead:

```text
intake
  -> direction_pending
  -> collage_pending
  -> prompt_pending
  -> production
  -> qa
  -> complete

Any image stage -> handoff when identity or source-pixel preservation is unavailable
```

Read [workflow.md](references/workflow.md) at the start. Track the current stage in every response and write a handoff receipt after each confirmed gate using [handoff-template.md](references/handoff-template.md).

## Gate 1: confirm the IP direction

1. Inventory the brief and files before ideating.
2. Separate `user/brief facts`, `evidence-based interpretation`, and `open questions`.
3. Produce 2–3 materially different directions using [direction-framework.md](references/direction-framework.md).
4. For one creator, define that creator's recognizable content asset and a concrete play.
5. For multiple creators, group them by content/business logic, name every member, and give every group a distinct play that supports the common theme.
6. Present the options and stop.
7. Ask alongside the choice: `本次海报是否需要呈现报价或合作权益？不需要也可以。` Do not make this a required input.

Advance only after the user explicitly selects/merges a direction and confirms continuation. A vague reaction, change request, or added material is not confirmation.

## Gate 2: confirm the protected creator presentation

1. Build a source ledger and resolve duplicates, alternatives, missing subjects, and filename suffixes.
2. Read [layout-grammar.md](references/layout-grammar.md). Select the creator-presentation mode from the confirmed content relationship and layout: `unified-ensemble`, `grouped-by-play`, `independent-cutouts`, or `hybrid-hero-groups`. Never force all creators into one ensemble.
3. Start in `strict-preserve` mode with pixel-preserving background removal or masking.
4. Produce the smallest useful preview set: one unified preview, one preview per play group, individual cutout previews, or a full-board placement proof. For grouped work, keep every creator beside the play and evidence they support.
5. Use coordinated sizes and real front/middle/back overlap inside each intended cluster. Do not line subjects up, leave hard source boundaries, create unexplained holes, or repeat a creator in multiple groups unless explicitly requested.
6. If strict compositing stays visibly fragmented, explain why and ask whether to enter `identity-locked-blend` mode. Do not infer permission from aesthetic feedback alone.
7. In authorized blend mode, create locked face/animal-head masks before any generative edit. Allow only the non-identity operations listed above, then restore locked regions when possible and inspect every identity at high resolution.
8. Show the chosen presentation mode, preview(s), active preservation mode, unique-subject count, group-to-layer mapping, and all known limitations.
9. Stop and ask for explicit creator-presentation confirmation.

If no suitable editing capability exists, output the creator-presentation execution specification and enter `handoff` rather than `prompt_pending`.

## Gate 3: confirm the final generation Prompt

1. Use only the confirmed direction and creator presentation.
2. Map every creator, case screenshot, Logo, and fixed copy to an exact placement or role.
3. Build the complete Prompt using [prompt-template.md](references/prompt-template.md).
4. Reproduce supplied names, copy, and screenshot content exactly; do not polish immutable text.
5. Show the entire Prompt and stop.

Advance only after the user explicitly confirms the complete Prompt. If the user edits it, show the revised complete Prompt and wait again.

## Produce and verify

1. Generate only the editable/background components the current tool can safely generate.
2. Composite people, animals, screenshots, and Logos as independent protected layers.
3. Run every applicable item in [qa-checklist.md](references/qa-checklist.md).
4. Use only `PASS`, `FAIL`, or `NOT VERIFIABLE`. Treat `NOT VERIFIABLE` as unfinished, never as pass.
5. Return any failure to its responsible stage and redo only the affected downstream work.
6. Mark `complete` only after all hard checks pass and the user receives the verified output or a clearly labeled handoff package.

## Invalidate downstream confirmations

| User change | Keep | Invalidate |
|---|---|---|
| Theme, direction, grouping, or play | valid source ledger | final Prompt |
| Add, remove, replace, change, regroup, or change the presentation mode of a person/animal source | chosen direction unless meaning changes | creator presentation and final Prompt |
| Case screenshot, Logo, fixed copy, price, or rights change | chosen direction and confirmed collage | final Prompt |
| Cosmetic background/decor adjustment after production | direction, collage, Prompt structure | affected production and QA items |

Announce invalidation explicitly and return to the earliest affected gate.

## Load only the needed reference

- Intake, stages, confirmation language, and rollback: [workflow.md](references/workflow.md)
- Brief analysis, single/matrix strategy, color, layout, and direction comparison: [direction-framework.md](references/direction-framework.md)
- Content topology, layout families, density, and creator-presentation modes: [layout-grammar.md](references/layout-grammar.md)
- Pixel and identity protection for people, animals, screenshots, and Logos: [material-integrity.md](references/material-integrity.md)
- Complete final generation Prompt: [prompt-template.md](references/prompt-template.md)
- Visual examples and non-copying retrieval: [visual-case-library.md](references/visual-case-library.md)
- Final acceptance and failure routing: [qa-checklist.md](references/qa-checklist.md)
- Cross-platform loading and capability downgrade: [platform-usage.md](references/platform-usage.md)
- Confirmed-stage transfer record: [handoff-template.md](references/handoff-template.md)
