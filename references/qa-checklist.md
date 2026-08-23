# QA checklist and failure routing

## Contents

1. Evidence rule
2. Process checks
3. Content checks
4. Material checks
5. Visual checks and aesthetic hard failures
6. Cross-platform and handoff checks
7. Failure routing
8. Report format

## 1. Evidence rule

Use exactly:

- `PASS`: direct evidence proves the requirement.
- `FAIL`: direct evidence contradicts it.
- `NOT VERIFIABLE`: the artifact, resolution, source, or tool record cannot prove it.

`NOT VERIFIABLE` is unfinished. Never promote it to pass because the output looks plausible.

Inspect the final artifact at readable resolution and compare it with the source ledger, confirmed direction, confirmed cutouts, confirmed composition, and confirmed Prompt.

## 2. Process checks

- Gate 1 explicitly confirmed the direction/merge.
- Price/rights were asked as optional and were not invented.
- Gate 2 explicitly confirmed the source-versus-cutout review or produced a clearly labeled handoff.
- Gate 3 explicitly confirmed the creator composition mode, group mapping, size, overlap, and front/middle/back order; or produced a clearly labeled handoff.
- Gate 4 explicitly confirmed the complete Prompt.
- Upstream changes invalidated the correct downstream confirmations.
- A stage handoff receipt exists after every confirmed gate.

## 3. Content checks

- Theme and one-line expression match the confirmed direction.
- Project background is concise and contains no unsupported claims.
- The play is the main information body, not a generic slogan.
- Single-creator work explains what this creator does.
- Multi-creator work has evidence-based groups, exact members, and a distinct play per group.
- Creator images, IP theme, concise background, and refined play are all present.
- Case/data evidence appears only if supplied and space permits.
- Price, rights, dates, client names, metrics, and collaboration facts are supplied and confirmed.
- No unconfirmed cooperation mode, live-streaming claim, long category list, or platform feature was added.

## 4. Material checks

### Cutout confirmation

- Every required `Pxx` has a source-versus-cutout review page showing the original image and transparent cutout side by side.
- Every cutout was checked on both a checkerboard and a neutral solid background.
- Face, hairstyle, hair edge, clothing, hands, feet, animal fur, subject count, and original combination were compared with the source.
- Body regions missing in the source are labeled and were not generated or completed.
- No body part, animal, or identity-critical region was accidentally removed.
- No face or animal head changed; no hard cutout edge was accepted as pass.
- Gate 2 has an explicit `抠图通过` confirmation covering the accepted cutout set.

### Creator composition

- The confirmed mode is exactly one of: unified ensemble, grouped by play, independent cutouts, or hero plus supporting groups.
- The preview proves relative creator sizes, front/middle/back order, overlap, and face/animal-head safe zones.
- Every creator is mapped to the correct play, case, evidence, or scene.
- Every unique subject appears exactly once unless repetition was explicitly approved; there is no duplicate or omission.
- There is no hard rectangular source boundary, exposed source furniture/background edge, meaningless blank area, or person detached from the intended cluster.
- Gate 3 has an explicit `排布通过` confirmation covering the accepted preview and layer order.

### People and animals in the final artifact

- Unique creator/account count matches the ledger.
- Creator-presentation mode matches the confirmed layout: unified, grouped, independent, or hybrid.
- Every creator is visually mapped to the correct play/group; no forced all-person ensemble appears when grouped placement was confirmed.
- Visible person/animal count matches the chosen source combination.
- No duplicate, omission, stranger, split combination, or alternative miscount.
- Faces, hair, expressions, clothing, body, and poses match the source.
- Animal species, coat color, body, pose, and pairings match the source.
- Cutouts were made by masking/segmentation, not generative redraw.
- Proportions remain natural and no face/animal subject is covered.
- Public nicknames omit file-management suffixes unless explicitly approved.

### Case screenshots

- Every specified `Cxx` appears exactly in its mapped module.
- Complete screenshot bounds and meaningful content are visible.
- Text, titles, images, and data match the source.
- No crop, recolor, repair, rewrite, fabricated metric, or duplicate use.

### Logos

- Every specified `Lxx` appears once in its mapped position.
- All Logo elements, text, colors, and internal relationships match the source.
- Logo aspect ratio is preserved; visual-size normalization does not stretch it.

## 5. Visual checks

- The first visual focus (`第一视觉`) is explicit and matches the confirmed direction.
- Title, creator, play module, and evidence use visibly different weights instead of equal-sized treatment.
- Palette is harmonious and justified by this theme, industry, season, or node.
- Surface style belongs to this brief and is not a default seasonal, poetic, technology-blue, neon-interface, or prior-project carryover.
- Creators are the first visual focus when required and are larger than case screenshots.
- Theme and content play are readable at target viewing size.
- Layout follows the confirmed region allocation and people-side placement.
- Treat wrong creator-side placement (for example, people on the left when the confirmed layout requires a right-side hero) as a hard layout failure.
- Group modules and creator attribution can be understood quickly; every creator is visibly connected to the correct play.
- White space is sufficient; every major blank area has a focusing, separation, breathing, or eye-guidance purpose; essential copy is not reduced to dense small text.
- No hard rectangular source boundary, exposed furniture edge, or detached creator weakens the composition.
- Foreground, middle ground, and background are distinguishable, and subject overlap creates depth without blocking faces or animal heads.
- Repeated peer modules have a stable rhythm; non-peer content is not forced into identical weight.
- Safe margins hold; text does not press against faces; screenshots are not clipped.
- Decorations support the confirmed visual premise and remain subordinate.
- No distinctive title, composition, Logo, seal, or decorative system was copied from a reference.

### Aesthetic hard failures

Any item below is a hard `FAIL`, even if all required text and assets are present:

- The first visual focus (`第一视觉`) cannot be identified.
- A large meaningless blank area (`无意义空白`) has no focusing, separation, breathing, or eye-guidance purpose.
- A creator is detached from the play they are meant to support (`人物与玩法脱节`).
- People or animals float like isolated stickers instead of participating in a scene, module, cluster, or deliberate editorial relationship.
- A title or decoration covers a face or animal head.
- The layout has no foreground, middle ground, and background relationship.
- Content that is not equivalent is incorrectly designed with identical visual weight.
- The visual style does not match the confirmed direction.
- The output silently reuses autumn, technology-blue, neon-interface, or another previous-project formula without support from the current brief.
- The output copies a reference case's (`参考案例`) distinctive title, container, Logo, seal, decoration, or concrete composition.
- A confirmed grouped or independent creator treatment is silently changed into an all-person ensemble.

Aesthetic repair never overrides material safety. Do not regenerate or repaint a person, animal, screenshot, or Logo to fix one of these failures.

## 6. Cross-platform and handoff checks

- The platform loaded the common `SKILL.md` and relevant references, not a divergent logic fork.
- The capability assessment records whether protected pixels can be preserved.
- When capability is insufficient, the output clearly says `handoff`, contains the layer map and Prompt, and does not claim a final preserved poster.
- A new agent can resume from the handoff without the user repeating confirmed choices.

## 7. Failure routing

| Failure | Return to |
|---|---|
| Wrong brief interpretation, theme, grouping, or play | `direction_pending` |
| Failed cutout, accidental body deletion, changed face/animal head, or bad mask | affected `Pxx` in `cutout_pending` |
| Wrong creator mode, grouping, relative size, overlap, layer order, detached subject, or meaningless hole with valid cutouts | `composition_pending` |
| Missing/wrong asset mapping, fixed copy, price/rights, palette instruction, or aesthetic constraint | `prompt_pending` |
| Wrong first visual, content hierarchy, visual premise, or density already present in the confirmed direction | `direction_pending` |
| Background/layout/decor/composite execution failure | `production` |
| Evidence too weak to verify protected pixels | `handoff` or a capable editing tool |

Do not repair a protected-source failure by regenerating the whole image.
Never repair a human face or animal head with generation. Return to the affected cutout or composition stage and rebuild from the protected source.

## 8. Report format

```markdown
## QA result

Overall: <PASS | FAIL | NOT VERIFIABLE>

| ID | Requirement | Result | Evidence | Return stage/action |
|---|---|---|---|---|
| QA-01 | <exact requirement> | <status> | <file/layer/visual comparison> | <action or none> |

Hard failures: <count and summary>
Unverifiable items: <count and required evidence>
Next action: <one concrete step>
```
