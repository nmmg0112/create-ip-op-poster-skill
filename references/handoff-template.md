# 可恢复海报交接记录

每次人物素材获得明确批准、方案被选择，或工作跨窗口／平台／生图模型／合成工具时更新同一份记录。只保留一个当前版本，并按时间追加用户修改。

```markdown
# IP OP poster handoff

## State
- Skill: create-ip-op-poster
- Current stage: <intake | person_material_pending | content_plan_pending | production | qa | complete | handoff>
- generation_route: <whole_poster | strict_fidelity | undecided>
- Last explicit confirmation: <用户原话或 none>
- Next required decision: <person material | content plan and generation | none>

## Brief facts
- Project/IP: <用户原文>
- Concise background: <一到两句事实>
- Required scene/direction: <用户明确要求或 none>
- Period/deadline/channel: <仅在提供时记录>
- Other fixed requirements: <准确保留>

## PersonMaterialSet
- review_white: <横版白底预览附件/路径>
- master_transparent: <同排布透明底总图附件/路径>
- subjects_transparent: <按需独立透明图；默认 none>
- source_ledger: <Pxx、公开昵称、数量、变体、原始组合、限制>
- approval: <用户批准原话或 none>
- identity/count/edge QA: <PASS | FAIL | NOT VERIFIABLE，含 Pxx>

## Source ledger
| ID | Source filename | Public name | Type | Unique subjects | Variant relation | Use | Limitation |
|---|---|---|---|---:|---|---|---|
| <ID> | <原文件名> | <公开名> | <type> | <count> | <relation> | <status> | <note> |

## Visual preference
- visual_preference: <用户原话 | 你来定 | not asked>
- User words: <用户原话 | 你来定 | not asked>
- brief_basis: <主题、场景、人物行动、受众情绪、品牌规则>
- Brief/theme evidence: <场景、人物行动、受众情绪、品牌规则>
- Combined visual direction: <配色、材质、光影、景深、标题能量、装饰边界>
- Conflict adjustment: <一句说明或 none>

## ContentPlanCard
- play_preflight: <PASS | FAIL，说明每组是否具备成员、证据、场景、机制、产品进入和短文案>
- Selected option: <方案编号/名称或 none>
- Theme: <主题>
- Theme copy: <一句文案>
- Brief background: <精炼背景>
- Plays:
  - <标题> | <明确成员> | <A/C 证据> | <具体场景/关系> | <动作/冲突/互动/反转> | <产品进入> | <海报短文案>
- First visual: <对象、尺度、位置、视觉动作>
- Layout family/reading path: <结构与顺序>
- Foreground/middle/background: <三层关系>
- Case/Logo/price use: <真实映射；未提供不写>
- Fidelity boundary: <尽量保持 | 严格保真>
- Selection and generation authorization: <用户“选 1 生成”等原话或 none>

## Visual references
| Case | Role | Borrowed grammar | Intentional difference | Forbidden copy elements | Original opened |
|---|---|---|---|---|---|
| <case path/ID> | <结构/密度/气质> | <从原图实际看到的一项具体特征> | <本次变化> | <禁止元素> | <yes + 原图路径/ID / no> |

## Execution Prompt
- Status: <not started | compiled | executed>
- Full Prompt: <路径、附件或完整文本>
- User display: <hidden by default | shown on request>
- Asset mapping verified: <yes/no 与缺口>
- Contains no extra confirmation gate: <yes/no>

## LockedPosterSpec
- spec_version: <integer or timestamp>
- source: <selected ContentPlanCard and approval wording>
- approved_person_material: <PersonMaterialSet reference>
- aspect_ratio_and_use: <default 16:9 OP or approved exception>
- theme_and_background: <current approved facts>
- plays_and_member_mapping: <current approved plays only>
- first_visual/person_mode/information_density: <current values>
- color_material_light_depth_motion: <current visual director result>
- reading_path: <current order>
- case_logo_fixed_copy_business_use: <current source mapping>
- required_and_forbidden_content: <current requirements only>
- visual_reference_grammar: <borrowed abstraction and forbidden copy elements>
- rejected_or_stale_directions_excluded: <yes/no>

## Protected manifest (strict_fidelity only)
| Layer ID | Source ID | Type | Exact source/content | Allowed operations | Planned role | Limitation |
|---|---|---|---|---|---|---|
| <layer> | <P/C/L/T> | <type> | <source> | <operations> | <role> | <note> |

## Production receipt
- generation_route: <whole_poster | strict_fidelity>
- formal_generation_count: <integer>
- image_generation_model_or_tool: <记录或 none>
- visual_base_path: <strict_fidelity 位图或 not applicable>
- visual_base_format: <PNG | WebP | JPEG | not applicable>
- visual_base_created_before_composite: <true | false | NOT VERIFIABLE | not applicable>
- protected_layer_ids: <IDs 或 not applicable>
- final_output_path: <路径或 none>
- final_image_path: <可直接预览的最终图片路径或 none>
- final_format/dimensions: <格式与像素>
- directly previewed: <yes/no>

## Exact post-edit receipt
- Requested target: <Logo/text/price/case/element or none>
- Whole-poster generation called again: <must be no for an exact edit>
- Before/after files: <paths>
- Allowed difference mask: <path/description>
- Non-target region unchanged: <PASS | FAIL | NOT VERIFIABLE>

## PosterVersionLock
- accepted_output_path: <path or none>
- accepted_output_hash_if_available: <hash or not available>
- approval_wording: <user wording or none>
- allowed_local_edit_target: <target or none>
- successor_version: <new path/version or none>
- previous_version_preserved: <yes/no/not applicable>

## User change log
| Order | User change | Return stage | Invalidated work | Applied result |
|---:|---|---|---|---|
| 1 | <change> | <stage> | <items> | <result> |

## Current QA
- Overall: <not run | PASS | FAIL | NOT VERIFIABLE>
- Person roster/identity: <status and evidence>
- Content play closure: <status and evidence>
- 16:9/default ratio: <status and dimensions>
- Visual quality/readability: <status and direct image evidence>
- Protected-source integrity: <status or not applicable>
- Hard failures: <list>
- Unverifiable items: <list and missing evidence>

## Next action
<唯一下一步；不要让用户重复已经完成的确认>
```

不要猜公开昵称、遗漏限制、把默认整图说成像素保真、把程序图说成艺术底图，或把缺少证据的 QA 写成通过。
