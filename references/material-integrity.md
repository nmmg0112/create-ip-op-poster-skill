# Material integrity rules

## Contents

1. Protected-source model
2. Material ledger
3. PersonMaterialSet
4. People and animals
5. Case screenshots
6. Logos
7. Material review is not poster layout
8. Mode-specific fidelity boundaries
9. Capability decision
10. Preservation and production evidence

## 1. Protected-source model

Person-material preparation and Mode B use one of two declared source-processing modes:

- `strict-preserve` (default): treat people, animals, screenshots, and Logos as immutable source pixels. The task is masking and compositing, not re-illustration.
- `identity-locked-blend` (explicit opt-in): keep identity-critical regions immutable while allowing generative cleanup only outside them. Use this only when the user accepts non-face reconstruction to make an otherwise unusable person source compositable.

Screenshots and Logos always stay in `strict-preserve`. Never silently switch source-processing mode. Mode A is a separate end-to-end generation choice, not a pixel-preservation mode; its disclosure rules appear in section 8.

## 2. Material ledger

Use one row per source file:

| ID | Source filename | Public name | Type | Subjects | Variant relation | Use status | Layer ID | Limitation |
|---|---|---|---|---:|---|---|---|---|

Rules:

- Count unique creator accounts/combinations and visible subjects separately.
- Mark alternate photos of the same creator as variants, not new creators.
- Preserve inseparable multi-person, creator-and-pet, and multi-animal combinations as one source group.
- Remove file-management suffixes from public names only after distinguishing them from the real nickname.
- Stop on an unresolved duplicate, omission, source limitation, or name-to-source conflict.
- Assign stable `Pxx` IDs before producing review assets; later `Cxx`, `Lxx`, and `Txx` IDs must not reuse them.

## 3. PersonMaterialSet

Create and preserve one `PersonMaterialSet` before direction or mode work:

```text
review_white: 横版白底组合预览图 (horizontal white-background review image)
master_transparent: 透明底人物总图 (same arrangement with alpha)
subjects_transparent: 独立透明抠图 (one transparent layer per unique person/animal or inseparable original group)
source_ledger: stable Pxx IDs, public names, counts, variants, and limitations
approval: exact user message or none
```

For multiple subjects, use this exact user-approved processing Prompt without polishing it:

```text
把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 注意人物不能重复，且人物大小调整一致一些
```

The Prompt describes the review arrangement only. It does not authorize face redraw, subject invention, body completion, or a final poster composition. Produce all three visual outputs even when one person is supplied, so the approved material set remains usable in either production mode.

Before recording `approval`, verify:

- every unique subject or inseparable original group is present exactly once;
- the white review and transparent master have the same arrangement and subject count;
- every individual cutout maps to one stable `Pxx` ID;
- faces, animal heads, hair, coat markings, clothing, pose, and original combinations remain recognizable and unchanged under the declared source-processing mode;
- edges are usable on white, neutral solid, and checkerboard backgrounds;
- missing source body regions and uncertain edges are explicitly labeled, never invented.

Only the exact user reply `人物素材通过` or an equally explicit approval completes the set. If any source changes, rebuild the affected outputs and approval before direction or mode selection.

## 4. People and animals

### Allowed in `strict-preserve`

- remove only the background;
- refine the alpha mask without painting new identity pixels;
- proportionally scale and move;
- change front/back layer order;
- place a non-destructive shadow behind the protected cutout when it does not cover or recolor the subject.

### Conditionally allowed in `identity-locked-blend`

Only after explicit user authorization:

- delete or hide lower limbs, off-frame fragments, furniture, or source-background pieces that disrupt material usability;
- cover non-core body regions with another confirmed source layer;
- reconstruct small missing clothing/body-edge transitions outside locked identity masks;
- harmonize restrained light, color temperature, contact shadow, and edge treatment outside locked regions.

Keep human faces, facial features, expression, hairline/core hairstyle, and animal faces/recognizable coat markings locked. Preserve subject count and identity. Do not describe a blended result as pixel-preserved or original-pixel-only.

### Forbidden

- generative cutout recreation, face repair, face swap, beauty filters, skin smoothing, body completion, relighting that repaints the subject, clothing changes, pose changes, expression changes, hair changes, stylization, or cartoonization;
- changing animal species, coat, body, pose, accessories, or original pairing;
- mirroring when it changes visible text, asymmetrical identity cues, or user intent;
- stretching, non-proportional resizing, face obstruction, duplicate use, hidden subject, or an invented stranger;
- presenting an approximation as `原脸保真`.

In authorized blend mode, face repair/swap, beauty edits, expression changes, new subjects, species/coat changes, and screenshot/Logo regeneration remain forbidden.

Prefer deterministic segmentation, path/mask extraction, or manual masking. If the only available material-preparation action can resynthesize identity-critical source pixels without a reliable lock or restore path, treat the capability as insufficient and hand off.

## 5. Case screenshots

Keep each `Cxx` as one complete rectangular layer.

Allowed:

- proportional scale and movement;
- a border, corner-radius mask, or shadow outside the image when no content is cut off;
- placement inside a larger frame while the full screenshot remains visible.

Forbidden:

- crop, perspective warp, recolor, blur, content-aware fill, AI upscale that rewrites text, text replacement, data replacement, retouching, invented like/play/fan/customer numbers;
- hiding the screenshot title, source identity, or meaningful data beneath another layer;
- recreating a screenshot from its description.

If text is unreadable because the supplied file is too small, request a clearer original. Do not repair it with generation.

## 6. Logos

Keep all marks, symbols, taglines, borders, and internal spacing in the supplied Logo.

Allowed: background removal, proportional scale, movement, and left/right or top/bottom arrangement. When two Logos must be equal in visual size, normalize their bounding boxes without stretching either one.

Forbidden: redraw, omit an element, recolor without an explicit brand rule, rewrite text, fuse the Logos, or generate a new mark.

A user-supplied SVG Logo is allowed as a protected source layer. An SVG generated or drawn as the Mode B poster base is not allowed.

## 7. Material review is not poster layout

The `review_white` image proves roster completeness, identity, edge quality, size coordination, overlap usability, and absence of duplicates. It does **not** lock creator-to-play mapping, final position, scale, overlap, z-order, crop relationship, foreground/middle/background role, or any other poster composition decision.

The review image therefore has no separate composition-confirmation gate. After `人物素材通过`, direction work describes the final relationship through generative composition grammar, and the complete Prompt maps every subject to a role. If a user asks for a wireframe or placement explanation, it is optional, non-generative, and never a production gate.

Mode B must composite from `master_transparent` or `subjects_transparent`. Never place the white `review_white` rectangle into a poster, mask white away from it, or treat it as a finished creator cluster. Choose the transparent master when its approved overlap works for the final direction; choose individual cutouts when creator-to-play roles require different positions or depths.

Every final composition must still:

- include each approved subject exactly once unless intentional repetition was explicitly approved;
- keep every creator connected to the correct play, case, evidence, or scene;
- protect faces and animal heads from text, decoration, and foreground occlusion;
- avoid exposed source furniture/background edges, meaningless holes, hard white rectangles, or detached sticker-like subjects;
- create an intentional hierarchy and foreground/middle/background relationship rather than an even lineup or equal-weight avatar grid.

## 8. Mode-specific fidelity boundaries

### 模式 A：快速生图

The image model receives the confirmed person material as reference and generates the entire poster in one end-to-end pass. Before production, disclose that people, animals, screenshots, Logos, and Chinese copy may be redrawn, distorted, omitted, or misspelled. The final report may assess roster, theme, readability, aesthetics, and obvious identity failures, but it must not claim pixel preservation for any model-generated `P/C/L/T` item.

If exact faces, screenshots, Logos, or Chinese wording are required, recommend Mode B. Choosing Mode A after disclosure does not relax the requirement to report obvious identity, roster, or content failures.

### 模式 B：保真合成

The first production artifact must be a real PNG、WebP 或 JPEG visual base created by an image-generation model. It must establish the artistic scene, composition, materials, lighting, depth, decoration language, and visual movement while reserving natural roles for protected layers. It may not be an SVG/HTML/Canvas/PPT/Sharp layout, wireframe, fixed-rectangle information board, or grid renderer.

Only after that generated bitmap exists on disk may code or deterministic editing run. It may then perform masks, proportional placement, protected-layer compositing, non-destructive shadow connection, rasterized fixed copy, format conversion, export, and verification. It may not draw, repair, or substitute the artistic base.

Use the original `Cxx`, `Lxx`, and exact `Txx` content, plus `master_transparent` or `subjects_transparent`. For an exact post-production Logo, text, or screenshot change, edit only the targeted independent layer; never send the whole finished poster through a generative edit.

## 9. Capability decision

Before production, answer:

1. Can the platform call an image-generation model and save its output as PNG, WebP, or JPEG?
2. Can person material be inspected at useful resolution?
3. For Mode B, can the platform preserve and composite original `P/C/L/T` layers after the bitmap base exists?
4. For Mode B, can it prove the base was created before code or deterministic compositing ran?
5. For any authorized identity-locked blend, can identity regions be locked/restored and inspected independently?

If image generation is unavailable, return a Prompt/material-map handoff and never substitute SVG, HTML, Canvas, PPT, Sharp drawing commands, a rule-based grid, or a programmatic information board. If image generation exists but protected compositing does not, Mode A may complete; Mode B may generate its bitmap base and then hand off the protected-layer composite.

## 10. Preservation and production evidence

For the `PersonMaterialSet`, record:

- source and output dimensions;
- unique-subject and inseparable-group counts before/after;
- source-to-`Pxx` map;
- whether each cutout used segmentation/mask or generative editing;
- visible edge limitations and reviewer result;
- the exact approval message.

For protected screenshots and Logos, record source checksums when files are available and confirm the original file is embedded as the layer. For a person mask, compare retained foreground pixels against the source and inspect every face/animal head at high resolution.

Mode B additionally requires this provenance receipt:

```text
visual_base_path: <saved bitmap path>
visual_base_format: <PNG | WebP | JPEG>
image_generation_model_or_tool: <model/tool record>
visual_base_created_before_composite: <true only with direct evidence>
protected_layer_ids: <P/C/L/T IDs actually overlaid>
formal_generation_count: <integer>
```

Record base dimensions and hash, composite/final dimensions and hash, operation timestamps or equivalent ordering evidence, the deterministic operations performed after base creation, and the final layer map. `visual_base_created_before_composite` is `NOT VERIFIABLE` unless the record proves the order; a programmatic file renamed `.png` is not evidence of image-model provenance.

For `identity-locked-blend`, also record user authorization, edited-region description, locked-region list, face/animal-head comparison sheet, and any region that could not be verified.
