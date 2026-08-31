# QA checklist and failure routing

## Contents

1. Evidence rule
2. Process and generation-provenance checks
3. Content checks
4. Person-material checks
5. Mode A checks
6. Mode B protected-layer checks
7. Visual checks and aesthetic hard failures
8. Cross-platform and handoff checks
9. Failure routing
10. Report format

## 1. Evidence rule

Use exactly:

- `PASS`: direct evidence proves the requirement.
- `FAIL`: direct evidence contradicts it.
- `NOT VERIFIABLE`: the artifact, resolution, source, hash, layer record, or tool record cannot prove it.

`NOT VERIFIABLE` is unfinished. Never promote it to pass because a manifest claims success or the output looks plausible.

Inspect the actual final artifact at target viewing size and at high resolution. Compare it with the source ledger, approved `PersonMaterialSet`, chosen direction and mode, complete confirmed Prompt, production receipt, and protected-source files where applicable.

## 2. Process and generation-provenance checks

- The person-material set has an explicit `人物素材通过` approval before direction and mode selection.
- The selected direction and generation mode are explicit; price or rights remain optional and were not invented.
- The user explicitly approved the complete final Prompt with `确认生成` or an equally explicit reply.
- The Prompt-confirmation round was text-only and did not consume a formal poster generation.
- Upstream changes invalidated the correct downstream work: person-source changes return to `person_material_pending`; theme/play/mode changes return to `direction_and_mode_pending`; fixed-copy/Logo/case mapping changes return to `prompt_pending`.
- Default behavior used one formal poster-generation call. `formal_generation_count > 1` has explicit user authorization or a recorded exceptional reason; a failure never silently triggered another generation.

For every production, record the selected mode, image-generation model/tool, output path and format, timestamps or equivalent ordering evidence, generation count, and QA artifact paths.

For Mode B, require this exact receipt:

```text
visual_base_path: <saved bitmap path>
visual_base_format: <PNG | WebP | JPEG>
image_generation_model_or_tool: <model/tool record>
visual_base_created_before_composite: <true | false | NOT VERIFIABLE>
protected_layer_ids: <P/C/L/T IDs actually overlaid>
formal_generation_count: <integer>
```

Check all of the following:

- `visual_base_path` resolves to an existing, decodable bitmap whose real file signature and format are PNG、WebP 或 JPEG.
- The first production action was the image-generation-model call that created the visual base.
- `visual_base_created_before_composite` is backed by direct ordering evidence; a prose assertion alone is `NOT VERIFIABLE`.
- The recorded model/tool is an image-generation capability, not a renderer, layout engine, or generic script.
- The base is an image-model output, not SVG, HTML, Canvas, PPT, Sharp drawing commands, fixed rectangles, a grid renderer, or any programmatic base merely exported with a bitmap extension.
- Protected compositing code ran only after the generated bitmap existed.

Any false or unverifiable provenance item keeps Mode B unfinished. A programmatic base is a hard `FAIL`; changing its extension does not cure the failure.

## 3. Content checks

- Theme and one-line expression match the confirmed direction.
- Project background is concise and contains no unsupported claims.
- The play is the main information body, not a generic slogan.
- Single-creator work explains the concrete creator action and content mechanism.
- Multi-creator work has evidence-based groups, exact members, and a distinct play per group.
- Creator image(s), IP theme, concise background, and refined play are all present.
- Case/data evidence appears only when supplied and legible.
- Price, rights, dates, client names, metrics, and collaboration facts are supplied and confirmed.
- No unconfirmed cooperation mode, live-streaming claim, long category list, platform feature, or fabricated result was added.

## 4. Person-material checks

### PersonMaterialSet outputs

- `review_white` is a 横版白底组合预览图 with every approved subject or inseparable source group exactly once.
- `master_transparent` is a 透明底人物总图 with the same arrangement and count as `review_white`.
- `subjects_transparent` contains one 独立透明抠图 per unique subject or inseparable source group, mapped to stable `Pxx` IDs.
- The ledger records public names, source filenames, variants, counts, limitations, and the exact approval message.
- White, neutral-solid, and checkerboard inspection covers face, hairstyle, hair edge, clothing, hands, feet, animal fur, recognizable markings, subject count, original combinations, and alpha edges.
- Body regions missing in the source are labeled and were not generated or completed.
- No body part or animal was accidentally removed; 人脸、动物头部 and every identity-critical region remain unchanged under the declared material mode.

### Review-versus-final boundary

- The white review proves material usability only; it was not treated as approved final layout.
- Mode B uses `master_transparent` or `subjects_transparent`, never the white review rectangle or a white-background extraction of it.
- Every final subject is mapped to the correct play, case, evidence, or scene; there is no 重复、遗漏、硬矩形边界、exposed furniture/background edge, meaningless hole, or detached sticker.
- A user-requested wireframe, if any, was optional and non-generative and did not become a production gate, visual base, or final poster.

## 5. Mode A checks

Mode A is evaluated as an end-to-end generated poster, not as protected-layer compositing:

- The Prompt and user-facing summary clearly disclosed that people, animals, screenshots, Logos, and Chinese copy may be redrawn.
- The final report makes no pixel-preservation, original-pixel, source-layer, or exact-Logo claim for any model-generated `P/C/L/T` item.
- Visible subject and creator roster matches the approved ledger; there is no obvious duplicate, omission, invented stranger, split original combination, or wrong variant.
- Theme, project context, play, first visual, commercial-poster readability, and aesthetics match the confirmed direction.
- Faces and animal heads receive an obvious-identity screen; distorted or substituted identities are `FAIL`, even though exact pixel equality is not expected.
- Screenshot, Logo, and Chinese-copy errors are reported honestly. If exactness is required, the result fails the requested requirement and must be rerouted to Mode B rather than mislabeled as preserved.

## 6. Mode B protected-layer checks

### Visual base and operation order

- The first production action called an image-generation model and produced a real PNG, WebP, or JPEG base.
- The bitmap is a complete artistic visual base: background scene, composition, material, lighting, foreground/middle/background, decoration language, and visual movement are all present.
- The base is not a wireframe, layout guide, avatar grid, equal-weight card board, PPT-like information board, or code-rendered composition.
- No SVG, HTML, Canvas, PPT, Sharp, fixed-rectangle, or grid-rendering step created or substituted for the base.
- After the base existed, deterministic operations were limited to masks, proportional placement, protected-layer compositing, non-destructive shadow connection, rasterized fixed copy, format conversion, export, and verification.

### People and animals

- Every required `Pxx` source layer appears once unless intentional repetition was explicitly approved.
- Each `Pxx` uses the approved transparent master or individual cutout, with natural proportions and safe faces/animal heads.
- Creator-to-play mapping and foreground/middle/background role match the final Prompt.
- No generative repair, face edit, pose change, clothing change, body completion, or whole-subject redraw was used during compositing.

### Case screenshots

- Every specified `Cxx` appears exactly in its mapped role.
- Complete screenshot bounds and meaningful content are visible.
- Text, titles, images, and data match the source.
- No crop, recolor, repair, rewrite, fabricated metric, or duplicate use occurred.

### Logos

- Every specified `Lxx` appears once in its mapped position.
- All Logo elements, text, colors, and internal relationships match the source.
- Logo aspect ratio is preserved; visual-size normalization does not stretch it.
- A supplied SVG Logo may remain a source layer, but no SVG is accepted as the poster base.

### Fixed copy and exact post-production changes

- Every `Txx` is reproduced exactly, readable at target size, and mapped to the specified role.
- A Logo/text/screenshot adjustment changes only its target layer and necessary edge pixels; direct before/after evidence confirms non-target regions remain unchanged.
- The whole finished image was not sent through a generative edit to make an exact Logo, text, screenshot, or protected-person correction.
- If non-target stability cannot be proven, record `NOT VERIFIABLE`, never `PASS`.

## 7. Visual checks

- The first visual focus (`第一视觉`) is explicit and matches the confirmed direction.
- Title, creator, play, and evidence use visibly different weights instead of equal-sized treatment.
- Palette, materials, containers, and decoration are justified by the current Brief, audience emotion, person/account evidence, brand rule, or content mechanism.
- Surface style is not a default seasonal, poetic, technology-blue, neon-interface, or prior-project carryover.
- Theme, key play, nicknames, and necessary evidence are readable at target viewing size.
- Every creator is visibly connected to the correct play through scene, gesture, proximity, overlap, eye line, container relationship, or another intentional device.
- White space is sufficient, and every major blank area has a focusing, separation, breathing, or eye-guidance purpose.
- Foreground, middle ground, and background are distinguishable; overlap creates depth without blocking faces or animal heads.
- Repeated peer elements have rhythm, while non-peer content is not forced into identical weight.
- Safe margins hold; text does not press against faces; screenshots are not clipped.
- Decorations support the visual premise and remain subordinate.
- No 参考案例 (reference case) has had its distinctive title, concrete composition, Logo, seal, or decorative system copied.

### Aesthetic hard failures

Any item below is a hard `FAIL`, even if all required text and assets are present:

- The output resembles a PPT-like information board (`像 PPT／画板`) rather than a legible commercial-recruitment poster.
- An equal-weight card grid, avatar matrix, or fixed-rectangle renderer flattens all content into the same visual weight.
- The first visual focus cannot be identified.
- Foreground, middle ground, or background is missing, or all elements sit on one flat plane.
- A large meaningless blank area (`无意义空白`) has no focusing, separation, breathing, or eye-guidance purpose.
- A creator is detached from the play they support (`人物与玩法脱节`) or floats as an isolated sticker.
- A title, decoration, or foreground object covers a face or animal head.
- Essential theme, play, nickname, or evidence is unreadable at target size.
- The style contradicts the confirmed direction or silently reuses an unsupported historical formula.
- The output copies a reference's distinctive composition or branded elements.
- Any programmatic base is used for Mode B, even if its pixels or extension look like a normal bitmap.

### Duplicate-output and preview checks

- Hash the final artifact and any complete-poster preview or Mode B visual-base preview.
- If the final file hash equals a complete-poster preview hash, return `FAIL`: the confirmed production did not create or apply a distinct final composite.
- Do **not** compare the final hash against the white person-material `review_white` image; that image is a roster/edge review, not a complete-poster preview.
- A different hash alone is not a visual pass. Inspect the final pixels for the artistic base, protected overlays, hierarchy, depth, readability, and people/play connection.

Aesthetic repair never overrides material safety. Do not regenerate or repaint a protected person, animal, screenshot, Logo, or fixed copy to fix a visual failure.

## 8. Cross-platform and handoff checks

- The platform loaded the common `SKILL.md` and relevant references, not a divergent logic fork.
- Capability assessment distinguishes image generation from viewing images, programmatic drawing, and protected-layer compositing.
- With image generation plus layered compositing, Mode A or Mode B may complete.
- With image generation only, Mode A may complete; Mode B may generate the bitmap base and then must hand off protected compositing.
- With no image generation, the output is a Prompt/material map only and never an SVG/HTML/Canvas/PPT/programmatic fallback.
- A handoff includes the mode, approved person-material files, source ledger, complete Prompt, visual-base provenance if created, protected-layer map, formal generation count, current QA, and one next action.
- A new agent can resume without the user repeating confirmed choices.

## 9. Failure routing

| Failure | Return to |
|---|---|
| Changed, missing, duplicate, or newly supplied person/animal source; failed mask or identity review | affected `Pxx` in `person_material_pending` |
| Wrong brief interpretation, theme, grouping, play, visual premise, density, or selected mode | `direction_and_mode_pending` |
| Missing/wrong asset mapping, fixed copy, price/rights, mode disclosure, palette instruction, or production constraint | `prompt_pending` |
| No image-generation capability | `handoff` with Prompt/material map; do not produce a programmatic poster |
| Mode B has an invalid/unverifiable bitmap source or code ran first | `production` for a real generated bitmap, or `handoff` if unavailable |
| Mode B protected layer changed, disappeared, or cannot be verified | rebuild the affected deterministic composite from source |
| PPT-like board, weak hierarchy, missing depth, unreadable copy, detached person/play, or meaningless blank space | `production` if execution drifted; `direction_and_mode_pending` if the confirmed direction itself caused it |
| Evidence too weak to verify protected pixels or operation order | `handoff` or a capable editing/verifying tool |

Never repair a protected-source failure by regenerating the whole image. Never repair a human face or animal head with generation. For an exact Logo, fixed-copy, or screenshot correction, replace only the affected independent layer and verify non-target regions.

## 10. Report format

```markdown
## QA result

Overall: <PASS | FAIL | NOT VERIFIABLE>
Mode: <A | B>
Formal generation count: <integer>

| ID | Requirement | Result | Evidence | Return stage/action |
|---|---|---|---|---|
| QA-01 | <exact requirement> | <status> | <file/layer/hash/visual comparison> | <action or none> |

Visual-base provenance: <Mode B receipt or not applicable>
Hard failures: <count and summary>
Unverifiable items: <count and required evidence>
Next action: <one concrete step>
```
