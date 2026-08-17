# Final poster Prompt template

## Contents

1. How to fill the template
2. Complete Prompt
3. Pre-confirmation check

## 1. How to fill the template

Use only confirmed facts and assets. Delete any section that does not apply; do not fill it with invented content. Replace angle-bracket labels with exact confirmed text. Preserve user-supplied fixed copy verbatim.

Use material IDs in the Prompt so another tool can map every protected asset without guessing.

## 2. Complete Prompt

```text
请制作一张 <画幅与尺寸> 的 <行业/IP 类型> 招商 OP 海报，呈现 <商业提案/平台征集/内部沟通等使用场景> 的专业质感。信息精简，视觉优先，中文清晰准确。

【任务边界】
这是一项分层排版与合成任务，不是对人物、动物、案例截图或 Logo 的重新创作。背景、装饰、容器和排版可以创作；P、C、L 编号素材必须作为独立受保护图层使用。

【项目背景】
<一到两句已确认的精炼背景，只写 Brief 或用户提供的事实>

【IP 主题】
项目主题：<已确认主题>
主题文案：<已确认的一句话表达>

【核心玩法】
<单人：账号识别资产 + 具体情境/角色/冲突/互动 + 产品或项目自然进入方式>
<多人：逐组写“组名｜成员｜一句玩法｜与其他组的差异”，不写冗长适配品类>

【版式与信息层级】
画布：<比例、像素、横/竖版、安全边距>
版式骨架：<已确认布局>
第一视觉：<人物/动物群像或单个达人，明确占比和位置>
第二层级：<IP 主题与主题文案>
第三层级：<精炼项目背景与玩法模块>
可选证据：<仅列实际提供的案例截图/数据；无则删除>
底部信息：<仅列用户确认需要呈现的合作信息；无则删除>
不要用密集小字填满空白；空间不足时先减少装饰和非必要证据。

【人物与动物素材映射】
<逐条写 P01 -> 公开昵称 -> 所属组/位置 -> z-order -> 大小关系>
使用已经确认的人物呈现方案：统一群像、按玩法分组、独立抠图或主视觉＋分组混合。按其图层映射合成，不得擅自改成全员群像或拆散已确认分组。人物/动物整体必须大于案例截图并成为视觉重点。允许前后错落和交叠，但不得遮挡任何脸部或动物主体。

绝对禁止改变任何人的脸、五官、发型、表情、服装、体型或姿势；绝对禁止改变动物的品种、毛色、体态、姿势或原始组合关系。不得生成陌生人物，不得漏人、重复人物、卡通化、美颜、补画或重绘。公开昵称不得包含文件管理后缀，除非用户明确说后缀属于昵称。

【案例截图映射】
<逐条写 C01 -> 对应玩法/模块 -> 位置 -> 显示比例；没有案例则删除整个章节>
每张截图完整保留为独立矩形图层，只可等比缩放和摆放。不得裁切、调色、重绘、修复、替换文字、改动数据或虚构播放量/点赞量/客户信息；任何标题和真实数据都必须保持原样可辨。

【Logo 映射】
<逐条写 L01 -> 位置/排列/相对大小；没有 Logo 则删除整个章节>
Logo 保留所有元素，只可去背景、等比缩放和排列。不得重绘、改字、漏元素或擅自改色。

【色调与视觉语言】
主题依据：<本次 Brief、行业、季节或节点证据>
主背景色：<颜色及作用>
标题/强调色：<颜色及作用>
正文色：<颜色及可读性>
辅助色：<颜色及使用上限>
视觉隐喻：<与玩法相关的场景/结构元素>
装饰：<允许的少量元素>
整体必须和谐且符合本次主题。不要因为过往示例而默认中秋、秋日、诗意、卷轴、圆月、印章或固定节日风格。

【固定文案】
<逐条原样写出必须出现的文案；没有则删除>

【报价与权益】
<只有用户明确要求呈现且已提供真实内容时，逐字写出；否则删除整个章节>

【参考使用边界】
参考案例只用于理解信息层级、人物与文字比例、模块组织和行业氛围。不得照抄任何参考图的标题、文案、版式、Logo、印章、装饰或独特视觉符号；本海报必须围绕当前 Brief 重新构思。

【输出与验收】
- 输出 <文件格式/分辨率/是否需要可编辑源文件>。
- 保持安全边距，文字不压脸，截图不裁切。
- 人物/动物数量与素材清单完全一致，无重复、无遗漏。
- 中文无乱码、错字或擅自改写。
- 不添加未提供的粉丝量、播放量、点赞量、客户名称、合作案例、价格或权益。
- 受保护素材必须作为原始图层合成；如果当前工具无法做到，请停止生成并输出图层执行说明，不要用近似重绘代替。

【负面要求】
不要改变脸和动物；不要端到端重画整张海报中的人物、截图或 Logo；不要密集小字；不要虚构事实；不要照抄参考；不要擅自添加直播、短直联动、品类列表或其他未确认的合作方式；不要用文件名后缀作为达人昵称。
```

## 3. Pre-confirmation check

Before showing the Prompt, verify:

- the theme and play match gate 1;
- the subject list and mapping match gate 2;
- every `P/C/L` ID exists in the ledger;
- no immutable text was paraphrased;
- no optional section was invented;
- palette rationale belongs to the current task;
- output limitations and protected-layer rules are explicit;
- the entire Prompt is shown, not a summary.

Then stop at gate 3.
