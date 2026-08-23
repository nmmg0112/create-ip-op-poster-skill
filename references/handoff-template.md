# Confirmed-stage handoff template

Use this after every confirmed gate and whenever work moves to another window, agent, or image tool. Keep one current record; append user changes in chronological order.

```markdown
# IP OP poster handoff

## State
- Skill: create-ip-op-poster
- Current stage: <intake | direction_pending | cutout_pending | composition_pending | prompt_pending | production | qa | complete | handoff>
- Last explicit confirmation: <verbatim user confirmation>
- Confirmation time/context: <available timestamp or turn>
- Next mandatory gate: <gate or none>

## Brief facts
- Project/IP: <exact supplied text>
- Business background: <exact concise facts>
- Required direction/scene: <exact confirmed scope>
- Period/deadline/channel: <only if supplied>
- Other explicit constraints: <retain unfamiliar requirements>

## Confirmed creative direction
- Theme: <confirmed theme>
- One-line expression: <confirmed copy>
- Response logic: <brief need answered>
- Single-creator play or multi-creator grouping: <exact confirmed structure>
- Palette/visual language: <confirmed rationale>
- Layout skeleton: <confirmed layout>
- Price/rights on poster: <no | yes, supplied content | unanswered>

## Material ledger
| ID | Source filename | Public name | Type | Subjects | Variant relation | Use status | Layer ID | Limitation |
|---|---|---|---|---:|---|---|---|---|
| <ID> | <exact filename> | <display name> | <type> | <count> | <relation> | <status> | <layer> | <note> |

## Immutable items
- People/animals: <exact protected sources and combinations>
- Case screenshots: <IDs; no visual/text/data changes>
- Logos: <IDs; retain all elements>
- Fixed copy: <verbatim strings>
- Prohibited content: <task-specific bans>

## Cutout review
- Status: <not started | draft | explicitly confirmed | handoff required>
- Source/cutout comparison: <path or attachment reference>
- Rejected subjects: <IDs, reasons, and redo status>
- Subject count before/after: <counts>
- Known mask/source limitations: <facts>
- Explicit confirmation: <verbatim user confirmation or none>

## Creator composition
- Status: <not started | draft | explicitly confirmed | handoff required>
- Presentation mode: <unified ensemble | grouped by play | independent cutouts | hero plus supporting groups>
- Preview: <path or attachment reference>
- Canvas: <size/ratio/background>
- Layer order: <group, size, overlap, and front/middle/back mapping>
- Explicit confirmation: <verbatim user confirmation or none>

## Final Prompt
- Status: <not started | draft | explicitly confirmed>
- Full Prompt location/content: <path, attachment, or complete text>
- Asset mapping verified: <yes/no with gaps>

## User change log
| Order | User change | Affected stage | Invalidated confirmations | Applied result |
|---:|---|---|---|---|
| 1 | <change> | <stage> | <gates> | <result> |

## QA
- Overall: <not run | PASS | FAIL | NOT VERIFIABLE>
- Hard failures: <list>
- Unverifiable items: <list and missing evidence>

## Next action
<one action the receiving agent should take, including the next confirmation stop>
```

Do not replace source filenames with guessed public names. Do not omit limitations to make the transfer look complete.
