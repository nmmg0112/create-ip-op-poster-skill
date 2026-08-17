# Workflow and confirmation gates

## Contents

1. Operating rule
2. Intake
3. Direction gate
4. Collage gate
5. Prompt gate
6. Production and QA
7. Rollback
8. Stage response format

## 1. Operating rule

Run the workflow as a state machine. Do useful work within the current stage, then stop at the next gate. Never turn a user's partial reaction into permission to generate the next artifact.

A vague reaction, change request, or added material is not confirmation.

The three protected decisions are:

1. What the IP idea and content play are.
2. Which exact people/animals appear, how they map to plays, and whether they are unified, grouped, independent, or hybrid.
3. What exact Prompt will be used for the final poster.

## 2. Intake

### Build a material ledger

Assign stable IDs without renaming the source files:

- `B01`: brief text, document, screenshot, or link summary.
- `P01...`: person/animal source images.
- `A01...`: account/homepage screenshots or account descriptions.
- `C01...`: case screenshots that may appear in the poster.
- `L01...`: Logos.
- `T01...`: fixed copy, brand rules, prohibitions, price, rights, or delivery requirements.

For each file record source filename, subject/display name, subject count, type, variant/alternative relationship, visible quality limitations, and intended use. A filename suffix such as `-柒捌` or `-捌玖` is a file-management marker unless the user explicitly says it is part of the public nickname.

### Parse an arbitrary brief

Extract only what is present:

- business context and user insight;
- IP/project theme, if fixed;
- eligible directions or scenes;
- creative request and allowed creator organization;
- submission requirement, cycle, deadline, and channel;
- required commercial information;
- other explicit constraints not covered above.

Keep absent fields empty. Preserve unfamiliar requirements under `other explicit constraints`; do not drop them because they do not match a template.

### Ask only decision-changing questions

Continue with labeled assumptions when possible. Ask before direction generation only when a missing answer would materially change the idea or make safe asset use impossible, such as an unreadable brief, no creator source image, contradictory subject names, or an unknown mandatory output ratio.

## 3. Direction gate

Read `direction-framework.md`. Return 2–3 options that differ in strategy, not only title or palette.

End with:

> 请选一个方向，或告诉我希望合并哪些部分。确认方向后，我才会处理人物/动物拼贴。另请顺便确认：本次海报是否需要呈现报价或合作权益？不需要也可以；需要但尚未提供时，我会等你补充，绝不自行估算。

Accept as explicit confirmation only when the reply identifies the choice or merged content and authorizes continuation, for example `选方向 2，确认继续` or `按 1 的主题加 3 的分组，确认做人物图`.

Do not accept `挺好`, `可以看看`, `再亮一点`, a new attachment, or a partial correction as a completed gate. Apply the feedback, re-show the affected option, and ask again.

## 4. Creator-presentation gate

Read `material-integrity.md` before operating on images.

Read `layout-grammar.md` and choose the presentation mode from the confirmed content relationship and layout. Deliver:

1. the preview set required by the mode: unified ensemble, one preview per play group, independent cutouts, or a full-board placement proof;
2. the unique-subject list and count;
3. every `play/group -> Pxx -> layer ID -> public display name` mapping;
4. alternative files that were not used;
5. any uncertain mask edge or source limitation;
6. confirmation question.

End with:

> 请确认人物呈现方式，以及每组人物/动物的长相、数量、归属、大小、前后层级和交叠关系。确认后我才会生成完整海报 Prompt；如需统一群像、按玩法分组、独立摆放、换图、增删人物或调整层级，请直接指出。

When pixel-preserving editing is unavailable, do not show a generated approximation. Output the ledger, presentation mode, group mapping, mask/cutout instructions, target canvas, layer-order sketch, size ratios, and non-negotiable rules, then label the state `handoff`.

## 5. Prompt gate

Read `prompt-template.md`. Use the confirmed direction, collage mapping, and immutable source text.

Before presenting the Prompt, check:

- every public nickname has a mapped source;
- every case screenshot has exactly one specified slot unless the user requests reuse;
- fixed copy is verbatim;
- optional price/rights appear only when the user asked and supplied them;
- palette logic is tied to this brief;
- people remain one or more protected layers matching the confirmed presentation mode;
- screenshot and Logo rules are explicit;
- the negative constraints cover fabrication and reference copying.

End with:

> 以上是将实际用于生成/制作海报的完整 Prompt。请确认或逐条修改；只有你明确确认后，我才会进入成图。

## 6. Production and QA

Separate production into:

1. generated/editable background, decoration, containers, and typography plan;
2. protected person/animal layer(s), unified or grouped exactly as confirmed;
3. protected case screenshot layers;
4. protected Logo layers;
5. final text layers.

Prefer an editable source file when the platform supports it. If it only produces a flattened image, first prove that protected layers can be composited without regeneration. Otherwise use the handoff path.

Run `qa-checklist.md` against the final artifact, not against the Prompt alone. A generated image is not evidence that the task succeeded.

## 7. Rollback

- Direction or grouping changed: return to `prompt_pending`; redo collage only if composition/subject membership changes.
- Subject source, group mapping, or presentation mode changed: return to `collage_pending`; invalidate Prompt.
- Screenshot, Logo, fixed copy, price, or rights changed: return to `prompt_pending`.
- Final background/decor feedback only: return to `production`, then rerun all affected QA checks.
- Any face/source-pixel violation: discard the affected composite and return to `collage_pending` or `production`; never patch the face with generation.

## 8. Stage response format

Use this compact footer at every stage:

```markdown
当前阶段：<stage>
已确认：<confirmed decisions or none>
本轮新增：<materials or decisions>
仍需确认：<the next gate>
下一步：<one concrete action after confirmation>
```
