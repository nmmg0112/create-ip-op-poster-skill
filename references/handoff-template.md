# Resumable poster handoff template

Use this after each explicit approval and whenever work moves to another window, agent, image model, or compositing tool. Keep one current record and append user changes in chronological order.

```markdown
# IP OP poster handoff

## State
- Skill: create-ip-op-poster
- Current stage: <intake | person_material_pending | direction_and_mode_pending | prompt_pending | production | qa | complete | handoff>
- generation_mode: <A | B | undecided>
- Last explicit confirmation: <verbatim user message or none>
- Confirmation time/context: <available timestamp or turn>
- Next required decision: <person material | direction and mode | final Prompt | none>

## Brief facts
- Project/IP: <exact supplied text>
- Business background: <exact concise facts>
- Required direction/scene: <exact supplied or confirmed scope>
- Period/deadline/channel: <only if supplied>
- Other explicit constraints: <retain unfamiliar requirements>

## PersonMaterialSet
- review_white: <path or attachment for horizontal white-background preview>
- master_transparent: <path or attachment for the same arrangement with alpha>
- subjects_transparent: <optional; none by default, or only paths for subjects needing independent control>
- source_ledger: <stable Pxx IDs, public names, counts, variants, and limitations>
- approval: <exact user message or none>
- Identity/count/edge QA: <PASS | FAIL | NOT VERIFIABLE, with affected Pxx IDs>

## Source ledger
| ID | Source filename | Public name | Type | Unique subjects | Variant relation | Use status | Limitation |
|---|---|---|---|---:|---|---|---|
| <ID> | <exact filename> | <display name> | <type> | <count> | <relation> | <status> | <note> |

## Confirmed direction and mode
- Theme: <confirmed theme>
- One-line expression: <confirmed copy>
- Content play: <confirmed play>
- Creator/group mapping: <single-creator logic or exact multi-creator groups>
- Palette/visual language: <confirmed rationale>
- Broad generative composition: <scene, depth, movement, and hierarchy>
- Direction/mode decision: <verbatim user reply or none>
- Price/rights on poster: <no | yes with supplied content | unanswered>

## Immutable items and protected-layer manifest
| Layer ID | Source ID | Type | Exact content/path | Allowed operations | Planned role | Limitation |
|---|---|---|---|---|---|---|
| <layer> | <P/C/L/T ID> | <person, animal, screenshot, Logo, fixed copy> | <source> | <operations> | <role> | <note> |

## Final Prompt
- Status: <not started | draft | explicitly confirmed>
- Full Prompt location/content: <path, attachment, or complete text>
- User-facing generation card: <one-screen confirmation summary shown to the user>
- Full Prompt display status: <hidden by default | shown on explicit request>
- Asset mapping verified: <yes/no with gaps>
- Explicit confirmation: <verbatim user message or none>
- Confirmation was text-only: <yes/no>

## Production provenance
- formal_generation_count: <0 or positive integer>
- visual_base.path: <path or none>
- visual_base.format: <PNG | WebP | JPEG | none>
- visual_base.image_generation_model_or_tool: <exact record or none>
- visual_base.created_before_composite: <yes | no | not applicable>
- Composite/output path and format: <path and format or none>
- Protected layer IDs actually composited: <IDs or none>
- Known production limitations: <facts>

## User change log
| Order | User change | Return stage | Invalidated downstream decisions | Applied result |
|---:|---|---|---|---|
| 1 | <change> | <stage> | <decisions> | <result> |

## Current QA
- Overall: <not run | PASS | FAIL | NOT VERIFIABLE>
- Person roster/identity: <status and evidence>
- Protected-layer integrity: <status and evidence or not applicable>
- Visual quality/readability: <status and evidence>
- Hard failures: <list>
- Unverifiable items: <list and missing evidence>

## Next action
<one action the receiving agent should take, including the next required user decision>
```

Do not replace source filenames with guessed public names, omit limitations, claim pixel fidelity for Mode A, or mark missing evidence as passed.
