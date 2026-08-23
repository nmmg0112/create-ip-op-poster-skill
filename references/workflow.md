# Workflow and confirmation gates

## Contents

1. Operating rule
2. Intake
3. Direction gate
4. Cutout gate
5. Composition gate
6. Prompt gate
7. Production and QA
8. Rollback
9. Stage response format

## 1. Operating rule

Run the workflow as a state machine. Do useful work within the current stage, then stop at the next gate. Never turn a user's partial reaction into permission to generate the next artifact.

A vague reaction, change request, new attachment, or partial correction is not confirmation. The four protected decisions are:

1. What the IP idea and content play are.
2. Whether every source has been cut out correctly without identity or body loss.
3. How the confirmed cutouts are grouped, sized, overlapped, and layered.
4. What exact Prompt will be used for the final poster.

Read [novice-mode.md](novice-mode.md) for the default user-facing presentation. A skilled user may request a compact response, but all four decisions still require explicit confirmation.

## 2. Intake

Start with this low-barrier request:

> 请发送 Brief 和人物／动物原图。案例截图、Logo、固定文案、报价和合作权益都可以稍后补充，也可以不提供。

### Build a material ledger internally

Assign stable IDs without renaming source files:

- `B01`: brief text, document, screenshot, or link summary.
- `P01...`: person/animal source images.
- `A01...`: account/homepage screenshots or account descriptions.
- `C01...`: case screenshots that may appear in the poster.
- `L01...`: Logos.
- `T01...`: fixed copy, brand rules, prohibitions, price, rights, or delivery requirements.

For each file record source filename, subject/display name, subject count, type, variant/alternative relationship, visible quality limitations, and intended use. A filename suffix such as `-柒捌` or `-捌玖` is a file-management marker unless the user explicitly says it is part of the public nickname.

Keep this ledger hidden unless a conflict, missing source, identity ambiguity, or capability limitation changes the result.

### Parse an arbitrary brief

Extract only what is present:

- business context and user insight;
- IP/project theme, if fixed;
- eligible directions or scenes;
- creative request and allowed creator organization;
- submission requirement, cycle, deadline, and channel;
- required commercial information;
- other explicit constraints not covered above.

Keep absent fields empty. Preserve unfamiliar requirements under `other explicit constraints`; do not drop them because they do not match a template. Continue with labeled assumptions whenever safe, and ask at most one result-changing question per round.

## 3. Direction gate

Read `direction-framework.md`. Return 2–3 options that differ in strategy, not only title or palette. Put the recommended option first and explain the recommendation in one plain-language sentence.

End with the direct reply and the optional commercial-information question:

> 可直接回复：选方向 1
>
> 本次海报是否需要呈现报价或合作权益？不需要也可以。

The standard reply `选方向 1` is explicit confirmation. A custom reply is also valid when it identifies the chosen or merged content and clearly authorizes continuation. Do not accept `挺好`, `可以看看`, `再亮一点`, a new attachment, or a partial correction as a completed gate. Apply the feedback, re-show the affected option, and ask again.

## 4. Cutout gate

Read `material-integrity.md` before operating on images. This gate evaluates the cutout only; do not decide layout, grouping, overlap, or layer order yet.

Display a source-versus-cutout review page:

1. show each original source beside its transparent-background cutout;
2. label the stable `Pxx` ID and exact public name;
3. use a checkerboard or neutral solid background to expose edges;
4. show the full person/animal when the source permits;
5. mark uncertain hair, clothing, hand/foot, animal-fur, furniture, and source-edge regions;
6. check identity, subject count, original combination, and accidental body deletion.

If one source fails, redo only that source; keep the confirmed direction. End with:

> 请确认人物／动物长相、数量、原始组合、身体完整性和抠图边缘。可直接回复：抠图通过

Only explicit confirmation advances to `composition_pending`. If pixel-preserving cutout capability is unavailable, output the source ledger, exact mask instructions, protected regions, known limitations, and target format, then enter `handoff` without showing a generated approximation.

## 5. Composition gate

Use only cutouts confirmed at Gate 2. Read `layout-grammar.md` and choose the presentation mode from the confirmed content relationship:

- unified ensemble;
- grouped by play;
- independent cutouts;
- hero creator plus supporting groups.

Show a complete placement preview, or the smallest preview set that proves:

1. which play/group each person or animal supports;
2. relative subject sizes;
3. front/middle/back order and overlap;
4. clear faces and animal heads;
5. creator-to-play, case, or scene relationship;
6. no duplicate subject, hard rectangular source boundary, meaningless hole, or detached person.

End with:

> 请确认人物呈现方式、归属、大小、前后层级和交叠关系。可直接回复：排布通过

Only explicit confirmation advances to `prompt_pending`. If safe layer compositing is unavailable, output the presentation mode, group mapping, target canvas, layer-order sketch, size ratios, and non-negotiable protection rules, then enter `handoff`.

## 6. Prompt gate

Read `prompt-template.md`. Use only the confirmed direction, cutouts, composition, and immutable source text.

Before presenting the Prompt, check:

- every public nickname has a mapped source;
- every case screenshot has exactly one specified slot unless reuse was requested;
- fixed copy is verbatim;
- optional price/rights appear only when requested and supplied;
- palette logic is tied to this brief;
- protected person/animal layers match the confirmed composition;
- screenshot and Logo rules are explicit;
- negative constraints cover fabrication and reference copying.

Show a short production summary first, then the entire Prompt. The summary cannot replace the Prompt. End with:

> 以上是将实际用于生成／制作海报的完整 Prompt。可直接回复：确认生成

If the user edits any item, show the revised complete Prompt and wait for confirmation again.

## 7. Production and QA

Separate production into:

1. generated/editable background, decoration, containers, and typography plan;
2. protected person/animal layers exactly as confirmed;
3. protected case screenshot layers;
4. protected Logo layers;
5. final text layers.

Prefer an editable source file when supported. If a platform only produces a flattened image, first prove protected layers can be composited without regeneration; otherwise use the handoff path. Run `qa-checklist.md` against the final artifact, not the Prompt alone.

## 8. Rollback

- Theme, direction, or play changed: return to `direction_pending`; keep only valid source facts.
- Person/animal source added, removed, replaced, or changed: return to `cutout_pending`; invalidate composition and Prompt.
- Cutout or mask changed: return to `cutout_pending`; invalidate composition and Prompt.
- Grouping, size, overlap, or layer order changed: return to `composition_pending`; keep confirmed cutouts and invalidate Prompt.
- Screenshot, Logo, fixed copy, price, or rights changed: return to `prompt_pending` when direction, cutouts, and composition remain valid.
- Final background/decor feedback only: return to `production`, then rerun affected QA checks.
- Any face/source-pixel violation: discard the affected composite and return to the earliest responsible protected-image stage; never patch a face with generation.

Announce every invalidated confirmation explicitly.

## 9. Stage response format

Start every confirmation response with:

```markdown
第 <n>/4 步｜<步骤名称>
```

Show only the current understanding, recommended option, information needed for this decision, and one copyable reply. Keep ledgers, capability reports, case comparisons, and layer tables hidden unless a problem makes them necessary.

Use this compact internal/handoff footer when stage tracking must be visible:

```markdown
当前阶段：<stage>
已确认：<confirmed decisions or none>
本轮新增：<materials or decisions>
仍需确认：<the next gate>
下一步：<one concrete action after confirmation>
```
