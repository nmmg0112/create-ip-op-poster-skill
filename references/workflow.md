# Person-first poster workflow

## Contents

1. Operating rule
2. Intake and person material
3. Direction and mode
4. Complete Prompt confirmation
5. Production and QA
6. Rollback
7. Stage response format
8. Handoff

## 1. Operating rule

Run the workflow as a state machine. Do useful work within the current stage, stop for the required user decision, and never turn a reaction, correction, or new attachment into permission to create the next artifact.

```text
intake
  -> person_material_pending
  -> direction_and_mode_pending
  -> prompt_pending
  -> production
  -> qa
  -> complete

Any unavailable required capability -> handoff
```

Person material comes first in both modes. A Brief, cases, Logos, fixed copy, price, or rights may arrive before or after person approval, but direction work cannot begin until person material is explicitly approved. There is no mandatory final-layout preview. If the user specifically asks for a wireframe, it may explain relationships non-generatively, but it is optional and never authorizes or blocks production.

Read [novice-mode.md](novice-mode.md) for the default user-facing presentation.

## 2. Intake and person material

Start with this low-barrier request:

> 请先发送人物／动物原图。我会先做好人物素材供你确认；Brief、案例截图、Logo 和固定文案可以现在一起发，也可以人物确认后再补。

### Build the source ledger

Assign stable IDs without renaming files:

- `B01...`: brief text, document, screenshot, or link summary.
- `P01...`: person/animal source images.
- `A01...`: account/homepage screenshots or account descriptions.
- `C01...`: case screenshots that may appear in the poster.
- `L01...`: Logos.
- `T01...`: fixed copy, brand rules, prohibitions, price, rights, or delivery requirements.

For every `Pxx`, record the exact source filename, public name, unique-subject count, original group relationship, type, variant relationship, visible quality limitation, and intended use. Treat a filename suffix as file-management metadata unless the user says it is public copy. Keep the ledger hidden unless a conflict, missing source, identity ambiguity, or capability limitation changes the result.

### Create `PersonMaterialSet`

`PersonMaterialSet` is the resumable unit passed into either production mode:

```text
review_white: horizontal white-background preview
master_transparent: same arrangement with alpha
subjects_transparent: one transparent layer per unique person/animal or inseparable original group
source_ledger: stable Pxx IDs, public names, counts, variants, and limitations
approval: exact user message or none
```

For multiple subjects, use this user-approved Prompt verbatim:

`把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 注意人物不能重复，且人物大小调整一致一些`

Mode A's later redraw permission applies only to final-poster generation. At this stage, both modes use the same identity-preserving material standard; do not change a face, animal head, roster, original group, or recognizable source detail while preparing `PersonMaterialSet`.

For one subject, create equivalent white-background and transparent outputs without inventing an ensemble. For inseparable original groups, keep the group as one transparent layer and record the limitation.

Create and retain all three artifacts:

1. `横版白底组合预览图` → `review_white`;
2. `透明底人物总图`, using the same arrangement → `master_transparent`;
3. `独立透明抠图`, one per unique person/animal or inseparable original group → `subjects_transparent`.

The review arrangement is only for material inspection; it does not determine final-poster grouping, position, scale, or layer order. Mode B must use the transparent master or individual transparent layers, never the white review rectangle.

### Run person-material QA

Before asking for approval, verify:

- every `Pxx` maps to the correct public name and original source;
- every unique person/animal appears exactly once unless reuse was explicitly requested;
- no new, missing, or duplicated subject exists;
- faces, defining hair, animal heads, markings, clothing, pose, and original group relationships remain recognizable;
- bodies are not accidentally deleted and hair/fur, hand/foot, clothing, and source edges are usable;
- white and transparent masters have the same subject arrangement;
- every individual transparent layer is present or its inseparable-group limitation is recorded.

Redo only affected material when possible. If a required capability cannot produce or verify these outputs, enter `handoff` with the ledger, exact Prompt, mask instructions, protected regions, limitations, and required target formats. Do not continue to direction selection.

End with:

> 请确认人物／动物长相、数量、原始组合、身体完整性和边缘。可直接回复：人物素材通过

Only the exact reply `人物素材通过` or an equally explicit approval advances to `direction_and_mode_pending`. Store the verbatim message in `approval`.

## 3. Direction and mode

Start only after `PersonMaterialSet.approval` is explicit. Parse the Brief and any supplied supporting material, preserving absent fields as absent and labeling assumptions. Ask at most one question per round when its answer would materially change the result.

Present 2–3 genuinely different directions, not title or palette variants. Put the recommendation first and explain it in one plain-language sentence. Each direction should cover theme, one-line expression, content play, creator-to-play logic, palette/visual language, and the broad generative composition idea. For one creator, connect a recognizable content asset to a concrete play. For multiple creators, group them by content/business logic and name every member.

Then show this compact mode card exactly:

```text
模式 A｜快速生图：整张海报一次生成，通常更统一、更快；人物、截图、Logo 和中文可能被重绘。
模式 B｜保真合成：先生图生成完整艺术底图，再覆回确认过的人物、截图、Logo 和中文；更适合正式提报。
```

Mode selection consequences:

- 模式 A：快速生图 gives the image model the entire poster. It is suitable when speed and visual unity matter more than pixel fidelity; disclose redraw risk before selection.
- 模式 B：保真合成 first generates a complete artistic bitmap base, then composites approved transparent people/animals, exact screenshots, original Logos, and accurate Chinese copy as protected layers.

End with one natural combined reply, for example:

> 可直接回复：选方向 1，用模式 B

Accept any reply that makes the chosen/merged direction and mode unambiguous. If the user has already made theme, play, and mode explicit, restate the understood decision and move to `prompt_pending` without asking for another choice. A vague aesthetic reaction or partial correction is feedback, not a completed decision.

## 4. Complete Prompt confirmation

Read [prompt-template.md](prompt-template.md). Build the final Prompt from the approved `PersonMaterialSet`, direction, play, and generation mode.

Before showing it, verify:

- every public nickname maps to a confirmed `Pxx` source;
- every case screenshot and Logo has one exact role unless reuse was requested;
- fixed copy is verbatim and optional price/rights appear only when supplied and requested;
- palette, scene, materials, light, depth, and visual movement follow this Brief;
- the selected mode's redraw or protection boundary is explicit;
- negative constraints prevent fabrication and copying reference art;
- Mode B specifies a generated PNG、WebP 或 JPEG base before protected-layer compositing.

Show a short production summary followed by the entire Prompt. This confirmation round contains text only and consumes no poster-generation call. End with:

> 以上是将实际用于生成／制作海报的完整 Prompt。本轮只展示文本，不会调用正式海报生成。可直接回复：确认生成

Only `确认生成` or an equally explicit approval advances to `production`. If the user edits any item, show the complete revised Prompt and wait again.

## 5. Production and QA

`默认只调用一次正式生图`; record it in `formal_generation_count` and do not automatically spend a second call after a failure.

### Mode A

Send the complete poster task and all allowed references to the image model in one formal call. Return the `完整海报预览` and disclose that people, screenshots, Logos, and Chinese copy may have been redrawn. Run roster, theme, readability, aesthetic, and obvious-identity checks; never claim pixel fidelity.

### Mode B

1. `生成主视觉位图底图`: `第一项生产动作必须调用生图模型` to create and save a complete PNG、WebP 或 JPEG artistic base. Record its path, format, and generation model/tool. `不得先运行 SVG、HTML、Canvas、PPT` or a drawing-command/fixed-grid renderer as the base.
2. `保护图层覆回`: only after that bitmap exists may code or graphics tools perform masks, proportional placement, protected-layer compositing, rasterized fixed copy, format conversion, and verification.

The generated base must be an artistic scene, not a programmatic information board.

Use the transparent master or individual transparent layers for people/animals. Composite exact case screenshots and Logos as independent protected layers. Run [qa-checklist.md](qa-checklist.md) on the final artifact itself.

If image generation is unavailable, return a handoff package containing the complete Prompt, person assets, material map, protected-layer manifest, limitations, and next action. Do not substitute a vector, page, presentation, drawing-command, or grid artifact for the poster base.

Use only `PASS`, `FAIL`, or `NOT VERIFIABLE`. Treat missing evidence as unfinished and return failures to the earliest responsible stage.

## 6. Rollback

- Person/animal source added, removed, replaced, or changed: return to `person_material_pending`; invalidate person approval and every downstream decision.
- A person mask, identity, count, edge, or original group changes: return the affected material to `person_material_pending`; keep only source facts and unaffected files.
- Theme, play, or generation mode changes: return to `direction_and_mode_pending`; keep the approved `PersonMaterialSet` when its sources are unchanged.
- Fixed copy, Logo, case mapping, price, or rights changes: return to `prompt_pending` when person material and direction/mode remain valid.
- Final background/decor feedback only: return to `production`, then rerun affected QA checks.
- Any changed human face or animal head is a hard failure. Discard the affected output and return to the earliest responsible person-material or production stage; do not hide it with a repair claim.

Announce every invalidated downstream decision explicitly.

## 7. Stage response format

Do not number the process. Show only the current decision, information needed for it, and one copyable reply. Keep ledgers, capability reports, and layer manifests hidden unless a problem makes them necessary.

Use this compact footer only when stage tracking helps:

```markdown
当前阶段：<stage>
已确认：<person material, direction/mode, or Prompt>
本轮新增：<materials or decisions>
仍需确认：<next user decision or none>
下一步：<one concrete action after confirmation>
```

## 8. Handoff

Write [handoff-template.md](handoff-template.md) after each explicit approval and whenever work moves to another window, agent, image model, or compositing tool. The record must include the three person-material outputs, `generation_mode`, final Prompt, `visual_base` provenance, protected-layer manifest, `formal_generation_count`, current QA, and one next action.
