# OP generative layout grammar

This reference turns content topology into composition language for an image-generation model. It does not define a mandatory placement-preview artifact. The approved white person-material review establishes roster and source usability only; its arrangement never locks the final poster.

## Contents

1. Decide from content topology
2. Layout families
3. Creator-presentation modes
4. Density planning
5. Direction requirements
6. Production-mode translation
7. Failure patterns

## 1. Decide from content topology

Do not begin from `left text/right people`, `three columns`, or another favorite template. First classify the relationship among theme, plays, creators, cases, and data:

- `parallel`: several plays have equal weight;
- `sequence`: phases, route, relay, before/during/after, or funnel;
- `hierarchy`: one hero or mechanic leads supporting modules;
- `scene`: plays belong to distinct life spaces or occasions;
- `radial`: one shared IP idea has several expressions;
- `evidence`: cases, screenshots, or data prove the main proposal;
- `matrix`: creators, roles, plays, and evidence cross-map;
- `manifesto`: one emotional or conceptual premise dominates.

Select a layout family that expresses the real relationship. Do not imply sequence when the plays are parallel or equality when one creator is clearly primary.

## 2. Six core layout families

Retain the capabilities of the 12 structures below, but retrieve them through six core families. The core family describes the content logic; the variant describes the concrete composition.

| 核心家族 | 可用变体 |
|---|---|
| 概念场景 | 左右叙事、中心发散、情绪宣言 |
| 群像主视觉 | 舞台层级、主角＋辅助群像 |
| 玩法分舱 | 纵向栏目、分组岛、上下矩阵 |
| 路线阶段 | 时间线、接力、分镜 |
| 矩阵档案 | 横向信息带、证据墙、混合提案 |
| 编辑拼贴 | 杂志拼贴、纸张拼贴、场景切片 |

The 12 retained structures map to those families as follows:

| Retained structure | Core family | Best for | Reading path | Main risk |
|---|---|---|---|---|
| Left/right split | 概念场景 | one strong creator cluster plus rationale | title -> play -> people | repetitive and empty with many parallel plays |
| Top theme/bottom matrix | 玩法分舱 | several equal groups | title -> row/column groups -> footer | can become a rigid template |
| Horizontal content bands | 矩阵档案 | dense parallel groups | top to bottom | long rows and small evidence |
| Vertical pillars | 玩法分舱 | 2–4 parallel plays | left to right | falsely equal modules; easy to copy references |
| Group islands | 玩法分舱 | distinct scenes or creator families | visual cluster to cluster | weak reading order without anchors |
| Central hero/radial | 概念场景 | one common IP with several expressions | center -> surrounding scenes | crowding around the hero |
| Route/timeline/relay | 路线阶段 | real sequence or journey | start -> steps -> close | misleading when plays are not sequential |
| Stage/tiers | 群像主视觉 | roster, hierarchy, or reveal | front hero -> back support | people can overpower the play |
| Split-screen/storyboard | 路线阶段 | contrasts, episodes, or scene cuts | frame sequence | screenshots can become too small |
| Evidence wall/contact sheet | 矩阵档案 | case-heavy proof | claim -> evidence clusters | dense but strategically weak |
| Editorial collage | 编辑拼贴 | emotion-led or culture-led idea | title -> visual anchors -> modules | decorative emptiness or unclear mapping |
| Hybrid dossier | 矩阵档案 | strategy, people, cases, and data all matter | summary -> modules -> proof | needs strict density and alignment control |

Do not treat this table as a closed template library or a set of code-renderable grids. A new layout is valid when its reading path, scene logic, content mapping, depth, and visual movement are explicit.

## 3. Creator-presentation modes

Choose after the layout family, not before it:

- `unified-ensemble`: all creators jointly express one promise; use one protected group cluster.
- `grouped-by-play`: each play owns its creator cluster and case evidence; no all-person collage is required.
- `independent-cutouts`: creators appear as separate protected layers where the layout needs flexible placement.
- `hybrid-hero-groups`: one hero or ensemble anchors the poster while supporting creators remain inside their play modules.

Rules:

- Let the play relationship decide the mode.
- Preserve every creator once unless repetition has a declared communication purpose and user approval.
- Keep creator-to-play attribution visually immediate.
- For grouped-by-play, name every member and give each group a scene role, depth, scale relationship, and visual connection to its play in the complete Prompt.
- Do not create a unified ensemble merely because multiple source images exist.
- Do not reuse the white-background review as a final creator cluster. Mode B uses its transparent same-arrangement master or individual transparent cutouts.
- Protect every face and animal head while allowing intentional non-identity overlap and foreground/middle/background depth.

## 4. Density planning

Choose a density band before styling:

- `low`: concept/manifesto-led; one play, minimal proof.
- `medium`: 2–3 plays with concise rationale and selected proof.
- `high`: several groups, role mapping, execution detail, cases, or data.

High density does not mean small text everywhere. Reserve visual capacity for:

1. theme and one-line premise;
2. concise project context;
3. play title and mechanism;
4. creator attribution;
5. supplied evidence;
6. optional supplied commercial information.

Use grouping, numbering, color coding, scale contrast, and repeated alignment to make density scannable. Remove decorative emptiness and repeated summaries before shrinking essential copy.

## 5. Direction requirements

Every proposed direction must state:

- content topology;
- core layout family, concrete variant, and 阅读顺序;
- 第一视觉 and 区域分配;
- density band and approximate occupied-area target;
- creator-presentation mode;
- generative scene role and approximate spatial relationship of each play, creator group, screenshot, data block, and footer;
- foreground, middle ground, background, light direction, contact surfaces, and visual movement;
- 留白用途;
- what reference grammar is borrowed and what is deliberately different;
- 构图风险.

When layout is the unsettled decision, present 2–3 genuinely different layout structures for the same creative direction. Do not disguise recolors as layout options.

Translate the chosen structure directly into the complete text Prompt. Do not require a separate creator-layout preview or a layout-confirmation reply. If the user specifically asks to see a wireframe, relationship diagram, grid guide, or layout-guide SVG, it is optional, non-generative, consumes no formal poster-generation call, and never becomes a gate.

## 6. Production-mode translation

### 模式 A：快速生图

Describe the whole composition as one coherent generated poster: complete scene, people as references, title energy, play relationships, evidence roles, materials, lighting, foreground/middle/background, decoration language, and visual movement. Disclose that `P/C/L/T` reference content may be redrawn. Do not make pixel-preservation claims.

### 模式 B：保真合成

Split execution, not visual thinking:

1. The image-generation model first creates a complete PNG、WebP 或 JPEG artistic base with the entire scene, composition, material, lighting, depth, decoration language, and movement.
2. The base reserves natural roles, contact points, light direction, and safe zones for protected `P/C/L/T` layers without generating or imitating them.
3. Only after the bitmap exists may deterministic tools place the approved transparent person master or individual cutouts, complete screenshots, original Logos, and rasterized fixed copy.

The first production action must never be a grid renderer, fixed rectangles, or SVG/HTML/Canvas/PPT/Sharp drawing. Grids, diagrams, and layout-guide SVGs can explain a relationship, but they may never become the Mode B base, complete-poster preview, or final poster. Rasterizing a programmatic guide into PNG does not make it an image-generated base.

For matrix and compartment families, create hierarchy through scene, scale, depth, material, overlap, and directional flow. Stable alignment can support scanning, but an equal-weight card board is not an acceptable artistic base.

## 7. Failure patterns

- defaulting every poster to left text/right people;
- defaulting every matrix to three equal columns;
- forcing all creators into one collage before choosing the layout;
- isolating the creator ensemble from the plays it is meant to support;
- filling a large region with repeated summary text instead of new information;
- choosing a style reference by color while ignoring its information architecture;
- treating high density as permission for unreadable type;
- adding route, screen, interface, or stage metaphors that the content does not justify.
- copying the white person-material arrangement into the final composition without reconsidering creator-to-play roles;
- using an optional wireframe, grid, diagram, SVG, HTML, Canvas, PPT, Sharp render, or programmatic information board as the Mode B base;
- producing a PPT-like equal-weight card wall without foreground, middle ground, background, or visual movement;
- leaving people detached from the play, scene, evidence, or visual action they are meant to support.
