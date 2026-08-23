# Material integrity rules

## Contents

1. Protected-source model
2. Material ledger
3. People and animals
4. Case screenshots
5. Logos
6. Creator composition confirmation
7. Capability decision
8. Preservation evidence
9. Cutout confirmation page

## 1. Protected-source model

Use one of two declared modes:

- `strict-preserve` (default): treat people, animals, screenshots, and Logos as immutable source pixels. The task is compositing, not re-illustration.
- `identity-locked-blend` (explicit opt-in): keep identity-critical regions immutable while allowing generative cleanup only outside them. Use this when the user accepts non-face reconstruction to achieve a unified group image.

Screenshots and Logos always stay in strict-preserve mode. Never silently switch modes.

## 2. Material ledger

Use one row per source file:

| ID | Source filename | Public name | Type | Subjects | Variant relation | Use status | Layer ID | Limitation |
|---|---|---|---|---:|---|---|---|---|

Rules:

- Count unique creator accounts/combinations and visible subjects separately.
- Mark alternate photos of the same creator as variants, not new creators.
- Preserve multi-person/pet combinations unless the user explicitly supplies separable sources and requests separation.
- Remove file-management suffixes from public names only after distinguishing them from the real nickname.
- Stop on an unresolved duplicate, omission, or name-to-source conflict.

## 3. People and animals

### Allowed

- remove only the background;
- refine the alpha mask without painting new identity pixels;
- proportionally scale;
- move;
- change front/back layer order;
- place a non-destructive shadow behind the protected cutout when it does not cover or recolor the subject.

### Conditionally allowed in `identity-locked-blend`

Only after explicit user authorization:

- delete or hide lower limbs, off-frame fragments, furniture, or source-background pieces that disrupt the composition;
- cover non-core body regions with another source layer;
- reconstruct small missing clothing/body-edge transitions outside locked identity masks;
- harmonize restrained light, color temperature, contact shadow, and edge treatment outside locked regions;
- use a user-approved reference for broad three-tier/stage composition grammar.

Keep human faces, facial features, expression, hairline/core hairstyle, and animal faces/recognizable coat markings locked. Preserve subject count and identity. Do not describe a blended result as pixel-preserved or original-pixel-only.

### Forbidden

- generative cutout recreation, face repair, face swap, beauty filter, skin smoothing, body completion, relighting that repaints the subject, clothing changes, pose changes, expression changes, hair changes, stylization, cartoonization;
- changing animal species, coat, body, pose, accessories, or original pairing;
- mirroring when it changes visible text, asymmetrical identity cues, or user intent;
- stretching, non-proportional resizing, face obstruction, duplicate use, hidden subject, invented stranger;
- presenting an approximation as `原脸保真`.

In authorized blend mode, face repair/swap, beauty edits, expression changes, new subjects, species/coat changes, and screenshot/Logo regeneration remain forbidden.

Prefer deterministic segmentation, path/mask extraction, or manual masking. If the only available action is an image-generation/edit prompt that can resynthesize the source, treat the capability as insufficient.

## 4. Case screenshots

Keep each `Cxx` as one complete rectangular layer.

Allowed:

- proportional scale;
- movement;
- a border, corner radius mask, or shadow outside the image when no content is cut off;
- placement inside a larger frame while the full screenshot remains visible.

Forbidden:

- crop, perspective warp, recolor, blur, content-aware fill, AI upscale that rewrites text, text replacement, data replacement, retouching, invented like/play/fan/customer numbers;
- hiding the screenshot's title or data beneath another layer;
- recreating a screenshot from its description.

If text is unreadable because the supplied file is too small, request a clearer original. Do not repair it with generation.

## 5. Logos

Keep all marks, symbols, taglines, borders, and internal spacing in the supplied Logo.

Allowed: background removal, proportional scale, movement, and left/right or top/bottom arrangement. When two Logos must be equal in visual size, normalize their bounding boxes without stretching either one.

Forbidden: redraw, omit an element, recolor without an explicit brand rule, rewrite text, fuse the Logos, or generate a new mark.

## 6. 人物排布确认 (Creator composition confirmation)

Choose one presentation mode before previewing:

- **统一群像 (unified ensemble):** all people and animals jointly express one shared promise;
- **按玩法分组 (grouped by play):** each compact protected group stays next to its own play, case evidence, or scene;
- **独立人物 (independent cutouts):** protected cutouts occupy separate positions when the layout does not require a combined ensemble;
- **主视觉人物＋辅助分组 (hero plus supporting groups):** one creator or compact hero group carries the first visual focus, while every other creator remains attached to the correct supporting module.

Do not require a unified ensemble when creators support different plays. For any preview:

- 16:9 horizontal white canvas;
- all unique subjects included once;
- creator sizes visually coordinated while proportions remain natural;
- composition uses front/back overlap rather than an even lineup inside each intended cluster;
- intentional front/middle/back order and real overlap;
- **人脸和动物头部安全区：** no identity-critical region is covered;
- exact source appearance retained;
- front/back order chosen by the confirmed idea unless the user fixes it;
- **重复检查：** every unique subject is used exactly once unless repetition was explicitly approved;
- **遗漏、硬矩形边界和无意义空白检查：** no omitted subject, exposed furniture/background edge, meaningless hole, or person detached from the intended cluster;
- compact spacing: when authorized, an adjacent confirmed person/animal layer may cover a removable non-core source edge, but never a face, animal head, or required body cue;
- each creator visibly connected to the confirmed play, case, evidence, or scene.

For `grouped-by-play`, return one preview per group or a full-board proof and map every creator to exactly one play unless the user explicitly approves repetition. For every mode, show a full-board preview or the smallest preview set that proves the relationships, plus a layer map. A preview alone cannot prove no duplicate or omission. Do not generate the final Prompt until the user explicitly replies `排布通过` or gives an equally explicit confirmation.

For a handoff-only creator-presentation specification, include mode, group mapping, canvas size, each layer ID, approximate `x/y/width` as percentages of the canvas, z-order, mask notes, overlap notes, and face-safe zones.

## 7. Capability decision

Before editing, answer:

1. Can the tool remove the background without resynthesizing the subject?
2. Can it keep screenshots and Logos byte/pixel preserved as independent layers?
3. Can the result be inspected at sufficient resolution?

In `strict-preserve`, if any answer is `no` or `unknown`, do not promise final preservation. Produce the confirmed creative plan plus execution handoff.

In `identity-locked-blend`, also answer:

4. Can identity-critical regions be locked or restored independently?
5. Can every face/animal head be inspected at useful resolution after blending?
6. Can the output be clearly labeled as blended rather than pixel-preserved?

If any blend-mode answer is `no` or `unknown`, stay in strict-preserve or hand off.

## 8. Preservation evidence

Record:

- source and output dimensions;
- unique-subject counts before/after;
- layer map;
- source checksum for each screenshot and Logo when files are available;
- whether people/animals were processed by segmentation/mask or generative editing;
- visible edge limitations;
- reviewer result.

For `identity-locked-blend`, additionally record the user authorization, edited-region description, locked-region list, face/animal-head comparison sheet, and any region that could not be verified.

For screenshots and Logos, a checksum of the source file plus confirmation that the original file is embedded as the layer is stronger evidence than visual similarity. For a person mask, compare the retained foreground against the source and inspect faces at high resolution.

## 9. 抠图确认页 (Cutout confirmation page)

Gate 2 reviews each cutout by itself. Do not combine this review with creator grouping or poster composition.

- **原图与透明底抠图并排：** show both with the same stable `Pxx` ID and exact public nickname.
- **棋盘格检查：** inspect the cutout once on a checkerboard background and once on a neutral solid background. A white-only preview is insufficient evidence for pale clothing, hair, or animal fur.
- Compare the face, facial features, expression, hairstyle, hair edges, clothing, hands, feet, animal fur, recognizable markings, subject count, and original person/animal combination.
- Mark body regions already missing or outside the frame in the original image. Do not generate, paint, or infer missing body parts.
- **误删身体属于失败：** treat an accidentally removed body part or animal, any face or animal-head change, a changed original combination, or a hard cutout edge as `FAIL`.
- Record uncertain hair, clothing, hand/foot, animal-fur, furniture, and source-edge regions beside the affected `Pxx` item.

If one cutout fails, redo only that cutout and show its comparison again. Do not begin creator composition until every required cutout passes and the user explicitly replies `抠图通过` or gives an equally explicit confirmation.
