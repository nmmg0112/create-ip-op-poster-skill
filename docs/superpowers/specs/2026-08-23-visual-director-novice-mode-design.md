# Visual Director and Novice Mode Design

Date: 2026-08-23  
Status: user-approved design, pending implementation plan  
Project: create-ip-op-poster

## 1. Objective

Improve the Skill in two ways:

1. produce more attractive, coherent, information-capable IP/OP posters by turning the authorized visual-case library into an operational visual-director system;
2. lower the usage threshold for people who are unfamiliar with Agent products, including ChatGPT-only users.

The change must preserve the existing source-integrity standard: people, animals, case screenshots, and Logos remain protected source layers. Better aesthetics must never be achieved by changing a face, animal identity, screenshot content, or Logo.

## 2. Evidence from the current library and workflow

The 26 current cases include substantially different structures: concept scenes, creator ensembles, play-owned modules, numbered journeys, dense matrices, and editorial collage. The common strengths are not a single color or fixed three-column layout. Strong cases generally:

- use one visual premise across background, title, containers, and decoration;
- make the title or creator group an intentional visual anchor;
- bind creators to the play, scene, evidence, or object they support;
- use whitespace for focus, separation, or reading pauses instead of leaving unexplained holes;
- create foreground, middle-ground, and background depth;
- carry high information density through numbering, alignment, color coding, and repeated modules rather than unreadably small type.

The current Skill documents many layout families, but runtime behavior can still fail because:

- creator cutouts or a unified collage may be produced before the layout relationship is sufficiently proven;
- reference retrieval records one-line principles but does not create a complete art-direction grammar;
- the final Prompt does not force a separate structural pass and surface-style pass;
- current QA is strong on material integrity but too light on visual focus, dead space, rhythm, and coherence;
- the interface exposes process language and makes inexperienced users infer what to answer next.

## 3. Scope and non-goals

### In scope

- a default novice-guided interaction;
- four mandatory user confirmation gates;
- a visual-director decision layer before final Prompt production;
- structured visual-case tags and complementary reference retrieval;
- dynamic creator presentation instead of forced all-person collage;
- structural and aesthetic preflight checks;
- cross-platform starter instructions and safe capability downgrade;
- scenario tests for single creator, creator matrix, minimal input, and ChatGPT-only use.

### Out of scope

- training a new image model;
- copying or extracting design elements from reference cases;
- turning the Skill into an industry-specific template generator;
- weakening material-integrity rules;
- guaranteeing source-preserved final production on a platform that cannot mask and composite protected layers.

## 4. Revised state machine

The current creator-presentation gate will split into cutout confirmation and composition confirmation:

    intake
      -> direction_pending
      -> cutout_pending
      -> composition_pending
      -> prompt_pending
      -> production
      -> qa
      -> complete

    Any protected-image stage -> handoff
    when the platform cannot preserve identity or source pixels

The four mandatory confirmations are:

1. direction confirmation;
2. cutout-material confirmation;
3. creator-composition confirmation;
4. complete final-Prompt confirmation.

Required user replies stay simple:

    选方向 1
    抠图通过
    排布通过
    确认生成

An equivalent explicit sentence is valid. A vague reaction, attachment, or partial correction is not confirmation.

## 5. Novice mode

Novice mode is the default. Expert users may ask for a compact response, but no mode may skip the four confirmations.

### 5.1 Intake

The opening instruction is:

> 请发送 Brief 和人物/动物原图。案例截图、Logo、固定文案、报价和合作权益都可以稍后补充，也可以不提供。

The Agent:

- accepts messy uploads and arbitrary filenames;
- builds the detailed material ledger internally;
- shows only a compact problem list when a duplicate, missing subject, ambiguous public name, or unreadable asset changes the result;
- does not require the user to learn IDs, layer terms, or Agent vocabulary;
- asks at most one decision-changing question per turn;
- continues with labeled assumptions when missing optional material does not block the stage.

### 5.2 Stage response

Every user-facing stage begins with:

    第 <n>/4 步｜<stage name>

It shows:

1. what the Agent understood;
2. the recommended option first;
3. only the information needed for the current decision;
4. a copyable one-line reply.

The internal ledger, capability report, reference-comparison record, and layer map remain available but are hidden by default unless they contain a problem or the user asks to see them.

### 5.3 Direction confirmation

Return 2–3 materially different directions. Each compact direction contains:

- theme and one-line expression;
- what the creator or creator groups actually do;
- layout family and creator-presentation mode in plain Chinese;
- visual atmosphere;
- one main risk.

Mark one option as recommended and explain the reason in one sentence. Ask the optional price/rights question at this stage. Missing price or rights never blocks progress unless the brief requires them.

### 5.4 Cutout confirmation

Show a contact sheet or equivalent preview containing:

- source image and transparent-background cutout side by side;
- stable subject number and public display name;
- full visible subject bounds where the source permits;
- a neutral checkerboard or solid review background;
- any uncertain hair, clothing, limb, pet-fur, furniture, or source-boundary edge.

The user confirms identity, subject count, original pairing, retained body areas, and mask quality before any final arrangement. A failed cutout returns only the affected subject to cutout work.

### 5.5 Composition confirmation

After cutouts pass, select one of:

- unified ensemble;
- grouped by play;
- independent protected cutouts;
- hero plus supporting groups.

Show the real cutouts in a full-board placement proof or the smallest preview set that proves:

- group membership;
- size relationships;
- overlap and z-order;
- face and animal-head safety;
- relation between creators and their plays;
- absence of duplicate subjects, hard source rectangles, unexplained holes, and isolated edge subjects.

The user confirms the arrangement before Prompt production.

### 5.6 Prompt confirmation

Show:

1. a short production summary;
2. the complete Prompt;
3. the exact reply “确认生成”.

The summary does not replace the complete Prompt. Any user edit produces a new full Prompt and requires confirmation again.

## 6. Visual director

The visual director runs before direction presentation and again before final Prompt presentation.

### 6.1 Six decisions

For every project, record:

1. content topology: parallel, sequence, hierarchy, scene, radial, evidence, matrix, or manifesto;
2. layout family: concept scene, ensemble hero, play-owned compartments, route/stages, matrix dossier, editorial collage, or a justified new family;
3. visual premise: one brief-specific world that unifies title, background, containers, texture, and decoration;
4. creator-presentation mode: unified, grouped, independent, or hybrid;
5. density band: low, medium, or high, with an explicit function for major whitespace;
6. hierarchy and depth: primary anchor, secondary play modules, tertiary evidence, plus foreground/middle/background treatment.

Surface style follows these structural decisions. Industry labels are constraints, not default styles. For example, digital work must not automatically become blue neon, interface panels, or generic futuristic decoration.

### 6.2 Reference retrieval

Retrieve 2–4 complementary cases, normally including:

- one structural reference;
- one density/information-capacity reference;
- one mood/surface-language reference.

The same case may satisfy two roles only when the comparison still contains a structurally different case.

For each selected case, record:

- retrieval role;
- layout family and reading path;
- creator-presentation mode;
- density mechanism;
- visual premise;
- headline behavior;
- depth method;
- reusable abstract grammar;
- intended differences for the current brief;
- forbidden copied elements.

Do not reuse a title, copy, Logo, seal, proprietary container, exact arrangement, signature decoration, or distinctive motif.

### 6.3 Direction proof

Each direction must specify:

- content topology;
- reading path;
- approximate region allocation;
- first visual anchor;
- creator-to-play mapping;
- screenshot/data location if supplied;
- density band;
- visual premise and palette roles;
- major whitespace purpose;
- main composition risk.

When layout is the unsettled variable, options must use genuinely different structures rather than recolors.

### 6.4 Prompt construction

The final Prompt is composed in three explicit layers:

1. **structure layer** — canvas, reading path, region allocation, hierarchy, density, creator mode, evidence locations, safe margins;
2. **art-direction layer** — visual premise, title behavior, palette roles, texture, depth, module rhythm, restrained decoration;
3. **protected-layer map** — every person, animal, screenshot, Logo, and immutable text item.

The merged Prompt must state that protected layers are composited, not redrawn.

## 7. Aesthetic preflight and QA

The Agent may not show the final Prompt until the preflight passes:

- one deliberate first visual is identifiable;
- title, creators, modules, and proof have clear scale contrast;
- creators visually belong to the relevant play;
- all large whitespace has a stated function;
- no unrelated decorative system fills space;
- the layout has an intentional foreground, middle ground, and background;
- parallel items repeat a stable rhythm;
- non-parallel items do not receive falsely equal weight;
- high density remains scannable without shrinking essential text into unreadability;
- the surface style belongs to the current brief and does not inherit a previous seasonal or technology cliché.

Production QA adds hard failures for:

- no identifiable focal point;
- a large unexplained dead zone;
- creator/play disconnection;
- isolated creator cutouts that look pasted on;
- title or decoration covering a face or animal head;
- visual style contradicting the confirmed direction;
- copied distinctive reference elements;
- a full-person collage replacing confirmed grouped or independent placement.

Visual QA remains subordinate to source integrity. Never repair an aesthetic problem by regenerating a protected person, animal, screenshot, or Logo.

## 8. Cross-platform behavior

### Skill-aware Agent platforms

Install the full folder and invoke “$create-ip-op-poster”. The interface default prompt should ask only for Brief and creator sources.

### ChatGPT, Doubao, Coze, and knowledge-instruction platforms

Provide one copyable starter:

    请按 create-ip-op-poster 的四步流程协助我：
    1. 先给创意方向；
    2. 抠图后必须让我确认；
    3. 排布后必须让我确认；
    4. 完整海报 Prompt 必须让我确认。
    不许改变人物或动物长相，不许改案例截图和 Logo。
    我现在会上传 Brief 和人物原图。

If the platform cannot load the whole Skill, import SKILL.md, the stage reference, and the selected visual-case metadata. If it cannot perform pixel-preserving masks or layered composition, it must stop at the relevant gate and output an execution handoff rather than generate an approximate person or altered screenshot.

## 9. Planned file changes

### Add

- references/visual-director.md
- references/novice-mode.md
- examples/quick-start.md
- examples/chatgpt-starter.md

### Update

- SKILL.md: revised state machine, four gates, novice default, visual-director stage;
- references/workflow.md: cutout and composition gates split;
- references/direction-framework.md: compact direction cards and visual proof requirements;
- references/layout-grammar.md: six operational families and whitespace/depth checks;
- references/material-integrity.md: side-by-side cutout review format;
- references/visual-case-library.md: structured retrieval roles and case tags;
- references/prompt-template.md: structure, art direction, and protected-layer sections;
- references/qa-checklist.md: aesthetic hard failures;
- references/platform-usage.md: novice and ChatGPT-only starter path;
- references/handoff-template.md: new cutout/composition states;
- agents/openai.yaml: lower-friction default prompt;
- README.md: four-step quick start and cross-platform instructions.

## 10. Validation plan

Run at least four scripted or manual scenario tests:

1. **Multi-creator, high-density OP**  
   Verify grouped/independent placement is considered before ensemble; reference retrieval uses complementary cases; no technology-style default appears without brief evidence.

2. **Single-creator, visual-first OP**  
   Verify the creator mechanism is specific, the layout is not forced into a matrix, and optional evidence does not crowd the page.

3. **Novice with only Brief and creator sources**  
   Verify the Agent proceeds without jargon, asks one decision at a time, exposes four confirmations, and never requires price/case/Logo input.

4. **ChatGPT-only or incapable image platform**  
   Verify the starter works, the workflow remains intact, and protected-image limitations trigger a labeled handoff rather than false completion.

Regression checks:

- the supplied digital “新机搭子已就位” example;
- a creator-and-pet account;
- duplicate/alternative creator photos;
- a cutout failure that must not invalidate the confirmed direction;
- a composition change that invalidates the final Prompt;
- a screenshot or Logo change that does not force re-cutout.

## 11. Acceptance criteria

The implementation is complete when:

- all four gates appear in the authoritative workflow and rollback rules;
- a user can start with only Brief and creator images;
- cutout assets are explicitly reviewed before composition;
- creator composition is selected from four modes and explicitly reviewed;
- every direction records the six visual-director decisions;
- reference retrieval separates structure, density, and mood roles;
- final Prompt generation is blocked by the aesthetic preflight;
- QA includes aesthetic hard failures without weakening protected-source checks;
- cross-platform instructions include a ChatGPT-only starter and safe handoff;
- all four scenarios and regressions pass;
- installed local copy and public GitHub source match the verified project version.
