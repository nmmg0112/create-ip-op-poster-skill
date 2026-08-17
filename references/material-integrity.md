# Material integrity rules

## Contents

1. Protected-source model
2. Material ledger
3. People and animals
4. Case screenshots
5. Logos
6. Collage specification
7. Capability decision
8. Preservation evidence

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

## 6. Creator-presentation specification

Choose one presentation mode before previewing:

- one unified ensemble;
- one protected cluster per play group;
- independent protected cutouts;
- a hybrid hero plus supporting groups.

Do not require a unified ensemble when creators support different plays. For any preview:

- 16:9 horizontal white canvas;
- all unique subjects included once;
- creator sizes visually coordinated while proportions remain natural;
- composition uses front/back overlap rather than an even lineup inside each intended cluster;
- no face or animal subject covered;
- exact source appearance retained;
- front/back order chosen by the confirmed idea unless the user fixes it.

For `grouped-by-play`, return one preview per group or a full-board proof and map every creator to exactly one play unless the user explicitly approves repetition. Return both visual preview(s) and a layer map. A preview alone cannot prove no duplicate or omission.

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
