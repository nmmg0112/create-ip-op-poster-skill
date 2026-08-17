# QA checklist and failure routing

## Contents

1. Evidence rule
2. Process checks
3. Content checks
4. Material checks
5. Visual checks
6. Cross-platform and handoff checks
7. Failure routing
8. Report format

## 1. Evidence rule

Use exactly:

- `PASS`: direct evidence proves the requirement.
- `FAIL`: direct evidence contradicts it.
- `NOT VERIFIABLE`: the artifact, resolution, source, or tool record cannot prove it.

`NOT VERIFIABLE` is unfinished. Never promote it to pass because the output looks plausible.

Inspect the final artifact at readable resolution and compare it with the source ledger, confirmed direction, confirmed collage, and confirmed Prompt.

## 2. Process checks

- Gate 1 explicitly confirmed the direction/merge.
- Price/rights were asked as optional and were not invented.
- Gate 2 explicitly confirmed the protected collage or produced a clearly labeled handoff.
- Gate 3 explicitly confirmed the complete Prompt.
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

### People and animals

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

- Palette is harmonious and justified by this theme, industry, season, or node.
- Surface style is not a default seasonal/poetic carryover.
- Creators are the first visual focus when required and are larger than case screenshots.
- Theme and content play are readable at target viewing size.
- Layout follows the confirmed region allocation and people-side placement.
- Treat wrong creator-side placement (for example, people on the left when the confirmed layout requires a right-side hero) as a hard layout failure.
- Group modules and creator attribution can be understood quickly.
- White space is sufficient; essential copy is not reduced to dense small text.
- Safe margins hold; text does not press against faces; screenshots are not clipped.
- Decorations support the idea and remain subordinate.
- No distinctive title, composition, Logo, seal, or decorative system was copied from a reference.

## 6. Cross-platform and handoff checks

- The platform loaded the common `SKILL.md` and relevant references, not a divergent logic fork.
- The capability assessment records whether protected pixels can be preserved.
- When capability is insufficient, the output clearly says `handoff`, contains the layer map and Prompt, and does not claim a final preserved poster.
- A new agent can resume from the handoff without the user repeating confirmed choices.

## 7. Failure routing

| Failure | Return to |
|---|---|
| Wrong brief interpretation, theme, grouping, or play | `direction_pending` |
| Duplicate/omitted/wrong person, changed face/animal, bad mask, wrong layer order | `collage_pending` |
| Missing/wrong mapping, fixed copy, price/rights, palette instruction | `prompt_pending` |
| Background/layout/decor/composite execution failure | `production` |
| Evidence too weak to verify protected pixels | `handoff` or a capable editing tool |

Do not repair a protected-source failure by regenerating the whole image.

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
