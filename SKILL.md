---
name: create-ip-op-poster
description: Create or revise Chinese IP/OP招商海报 from a Brief and person, animal, case-screenshot, or Logo assets. Use for creator-matrix招商图、单人达人海报、人物素材确认、内容玩法方案、完整海报生成、严格保真合成或最终成图 QA. The default novice flow confirms people first, then lets one content-plan choice directly authorize a 16:9 whole-poster generation.
---

# Create IP OP Poster

Treat an OP as a commercial recruitment poster: the theme attracts attention, the play explains what creators will actually make, and people/cases make the proposal credible. Default to the two-confirmation novice flow in [novice-mode.md](references/novice-mode.md).

默认只有两个确认点。视觉导演是正式生图前的必经判断，按 [visual-director.md](references/visual-director.md) 实际查看参考原图并完成美观预检。

## Automatic opening and platform routing

When the Skill is first read and the user asks how to use it or starts without materials, automatically send the beginner opening from [novice-mode.md](references/novice-mode.md). Do not require the user to copy a long startup Prompt. If the user already supplied usable materials and requirements, acknowledge them and continue from the correct stage without repeating the full tutorial.

Detect the current platform internally. On Aime, read [aime-executor.md](references/platforms/aime-executor.md); on 豆包, read [doubao-executor.md](references/platforms/doubao-executor.md). Do not ask the user to select an adapter or explain platform files.

## Essential rules

1. `人物素材确认` always comes first. Do not propose the content plan or generate a formal poster until the user has approved the white person/animal preview.
2. Protect identity-critical details while preparing person material: faces, expressions, defining hair, animal faces, species, coat colors, markings, roster, and original inseparable groups. Never beautify, swap, cartoonize, duplicate, omit, or invent a subject.
3. Explain the material logic before requesting files: good portraits determine whether the poster's main visual is clear and convincing; creator cases reveal real scenes, relationships, narrative mechanisms, jokes, reversals, and account memory points, so the play does not become generic or detached from the creator.
4. Formal generation requires a concrete play. A slogan, category, or abstract style word alone is not enough. Each play needs explicit members, evidence, a scene or relationship, an action/conflict/interaction/reversal, a natural project or product entry, and one short poster line.
5. Use `16:9 横版` as the OP/招商 master. If a user casually asks for 3:4 or portrait without a stated channel requirement, treat it as a likely format conflict and keep the recommended plan at 16:9; only use portrait when the Brief or user explicitly identifies a portrait delivery channel or adaptation need. Never silently switch to portrait.
6. Before proposing the content plan, open 2—4 complementary original posters from [visual-case-library.md](references/visual-case-library.md): one for structure, one for density when needed, and one for mood. Learn abstract grammar only; never copy titles, copy, Logos, seals, exact composition, distinctive containers, or motifs.
7. Merge any user `视觉偏好` with the current Brief. Translate both into concrete color roles, materials, light, depth, atmosphere, and decoration boundaries; never replace the Brief with a generic industry formula.
8. Default to `generation_route = whole_poster`: one image-generation call directly produces the complete poster with theme, people, play, useful cases, fixed copy, and supplied commercial information. This route aims to keep people and cases recognizable but does not promise pixel-perfect fidelity.
9. Use `generation_route = strict_fidelity` only when the user explicitly requires a face, case screenshot, Logo, metric, or fixed Chinese copy to remain completely unchanged. Keep this routing decision in the background; do not ask a novice to choose a technical mode.
10. `默认完整海报一次生成`; `不得先生成空背景`，`不得生成排布稿`、空舞台、留洞底图、线框、SVG/HTML/Canvas/PPT 底图或程序化信息板。`默认只调用一次正式生图`; do not spend a second call without new user authorization.
11. For exact additions or replacements after production—Logo、中文、报价、权益、案例 or one isolated element—use a `局部图层修改`; `不得整图重绘` for an exact correction.
12. Inspect the actual final poster. Portrait output, missing concrete play, PPT-like information board, empty background, meaningless blank space, flat single plane, people/play disconnection, wrong face, missing or repeated subject, unreadable Chinese, severe case distortion, or an output the user cannot preview is a hard failure.

Read [material-integrity.md](references/material-integrity.md) before any image operation.

## State machine

Use exactly this order:

```text
intake
  -> person_material_pending
  -> content_plan_pending
  -> production
  -> qa
  -> complete

严格保真但平台能力不足 -> handoff
```

Read [workflow.md](references/workflow.md) at the start. Keep a resumable record with [handoff-template.md](references/handoff-template.md).

Before formal generation, compile the selected plan into one current `LockedPosterSpec`. Only the current locked version may enter the image model; exclude rejected directions, raw conversation history, platform-operation prose, and repeated instructions. After the user approves a finished poster, create `PosterVersionLock` and preserve that file. An exact local change must not overwrite or redraw the accepted whole poster.

## Confirmation 1: person material

1. Ask first for person/animal originals. Cases are strongly recommended but optional; a homepage screenshot, representative-work link, or account description can substitute. Brief、Logo and fixed copy may arrive now or later.
2. Build a source ledger with stable `Pxx/Cxx/Lxx/Txx` IDs, public names, subject counts, original group relationships, variants, limitations, and intended use.
3. For multiple subjects, use this material-preparation Prompt:

   `把以上人物/动物 拼贴成组合形式，有交叠感，不要并列罗列出来，我要做海报用，横版，其他顺序不重要，横版白底，不要改变任何一个人的长相，抠人物图即可 注意人物不能重复，且人物大小调整一致一些`

4. Show only one `横版白底组合预览图`. Retain the same arrangement as one `透明底人物总图` internally only for a final unified ensemble; grouped-by-play, independent, and hybrid compositions must use originals or separate transparent subjects. The preview validates identity, roster, body completeness, and edges; it does not determine final-poster grouping, scale, or placement.
5. Verify every identity, unique-subject count, original combination, body completeness, hair/fur edge, hand/foot edge, accidental deletion, and duplicate before asking.
6. If no visual preference is known, include the skippable color/feeling question in the same preview message. End with the copyable reply `人物没问题`; if the user gives no style answer, derive it from the Brief instead of waiting again. That reply or an equally explicit approval advances to `content_plan_pending`.

## Confirmation 2: content plan and generation authorization

After person approval:

1. Analyze the Brief and available cases. If no creator-content evidence exists, continue but label creator-fit confidence as limited.
2. If the user has not stated a visual preference, use the answer collected with person approval; when they skipped it, recommend from the Brief without another waiting turn.
3. Read [direction-framework.md](references/direction-framework.md), [visual-director.md](references/visual-director.md), [layout-grammar.md](references/layout-grammar.md), and the selected original reference posters before drafting options.
4. Present one recommended `ContentPlanCard` and one genuinely different alternative. Each must include the theme, concise background, evidence-based creator play, exact members, poster short line, first visual and broad composition, merged Brief/preference visual language, case/Logo/business use, and the 16:9 output.
5. End with `选 1 生成`. This single reply selects the plan, approves its content, and authorizes the one formal generation call. Do not add a separate full-Prompt approval, placement-preview approval, or technical route choice.

## Production and QA

- Compile the execution Prompt internally with [prompt-template.md](references/prompt-template.md); show it only when the user asks to inspect it.
- For the default route, the first formal production artifact is the complete 16:9 poster itself. Do not generate a separate empty base or layout artifact first.
- If exact preservation was explicitly requested, follow the background `strict_fidelity` rules in [material-integrity.md](references/material-integrity.md) and [platform-usage.md](references/platform-usage.md) without adding another user choice.
- If the required image-generation capability is unavailable, return the approved plan, complete Prompt, and material mapping as a handoff. Never substitute SVG、HTML、Canvas、PPT or a programmatic board.
- Run [qa-checklist.md](references/qa-checklist.md) on the actual final artifact. Use only `PASS`, `FAIL`, or `NOT VERIFIABLE`; missing evidence is unfinished.
- Mark `complete` only after all hard checks pass and the user receives a viewable final poster or a clearly labeled handoff package.

## Rollback

| User change | Return to | Keep |
|---|---|---|
| Add, remove, replace, or change a person/animal source | `person_material_pending` | valid Brief facts and unaffected source files |
| Change theme, grouping, concrete play, visual preference, or overall composition | `content_plan_pending` | approved person material when its sources are unchanged |
| Change only one exact Logo, fixed-copy, price, right, case, or isolated final element | `production` for local replacement | approved plan and all unaffected pixels/layers |
| Request a new overall style or background after production | `content_plan_pending` | approved person material and unchanged Brief facts |

Announce invalidated downstream work and rerun affected QA checks.

## Reference routing

- User-visible stages, confirmations, rollback, and handoff timing: [workflow.md](references/workflow.md)
- Beginner-facing copy and the two low-barrier replies: [novice-mode.md](references/novice-mode.md)
- Brief analysis and concrete single/matrix plays: [direction-framework.md](references/direction-framework.md)
- Mandatory visual judgment before the plan and execution Prompt: [visual-director.md](references/visual-director.md)
- Generative composition and density: [layout-grammar.md](references/layout-grammar.md)
- Person and protected-material boundaries: [material-integrity.md](references/material-integrity.md)
- Internal whole-poster or strict-fidelity execution Prompt: [prompt-template.md](references/prompt-template.md)
- Original visual references and non-copying retrieval: [visual-case-library.md](references/visual-case-library.md)
- Actual-final acceptance and failure routing: [qa-checklist.md](references/qa-checklist.md)
- Capability routing and safe downgrade: [platform-usage.md](references/platform-usage.md)
- Cross-window state record: [handoff-template.md](references/handoff-template.md)
- Aime Image2 execution: [aime-executor.md](references/platforms/aime-executor.md)
- 豆包 Seedream 5.0 Pro execution: [doubao-executor.md](references/platforms/doubao-executor.md)
