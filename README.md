# Fun Title Generator Skill

`fun-title-generator` 是一个面向中文语境的 Codex/Cursor/OpenCode skill。
It is designed for Chinese-language contexts, especially Xiaohongshu, Bilibili, WeChat Moments, video covers, and other short-form Chinese social posts.

本项目用于生成 Remi 风格的中文幽默短标题。它关注的是具体日常场景中的动作、物体和心理张力，并通过“错位框架”将低风险小事改写成正式、冷静、荒谬但可理解的标题。

核心公式 / Core formula:

```text
真实小事 × 错位框架 × 严肃语气 × 精准表达 = 搞笑标题
```

## 适用范围 / Scope

适合：

- 小红书、B 站、朋友圈、视频封面等中文短标题。
- 吃喝、通勤、办公室、宿舍、宠物、游戏、二次元、轻微社死等低风险日常场景。
- 需要“冷静、精准、略荒谬”表达，而不是网络热词堆叠的标题。

不适合：

- 灾难、疾病、死亡、法律纠纷等严肃或高风险场景。
- 针对真实个人身份的羞辱、歧视或恶意攻击。
- 正式品牌 slogan、投资人材料、政府汇报等需要稳定可信语气的文本。

## 方法概述 / Method

这个 skill 不把幽默理解为“加热梗”或“加夸张词”。它的基本方法是：先提取场景中最小、最可视化的动作，再把这个动作放入一个不属于它但内部自洽的严肃系统。

示例：

```text
输入：视频会议以为关麦了，结果偷吃薯片被全公司听见
输出：我以为我 muted 了，但薯片没有
```

工作流程：

1. **提取具体动作 / Extract action**
   从输入中识别可视化动作、核心物体、场景关系和情绪压力。例如“偷吃薯片时没关麦”比“社死场景”更适合生成。

2. **建立错位框架 / Build mismatch**
   将日常动作映射到纪录片、情况通报、科研报告、技术分析、职场流程、空中管制、法律文书等严肃框架。

3. **生成候选 / Generate candidates**
   同时走两条路径：一条使用错位框架制造荒谬感，另一条使用精准观察命中日常共鸣。

4. **筛选与压缩 / Filter and compress**
   淘汰过泛、过长、解释笑点、只有夸张没有错位、或与场景映射关系不足的候选。

5. **规则校验 / Validate**
   使用内置 validator 检查标题长度、显性搞笑词、攻击性敏感词和 emoji 数量。

## 理论依据 / Research Basis

本 skill 的设计参考了幽默研究、认知语言学和语用学中的若干理论。为避免过度引用，下面每项只保留一条短原文摘录，并附中文译意和设计意图；完整论述见 `skills/fun-title-generator/references/theories.md`。

### 乖讹论 / Incongruity Theory

Source: [Stanford Encyclopedia of Philosophy, "Philosophy of Humor"](https://plato.stanford.edu/entries/humor/#IncThe)

- 原文短摘 / Source excerpt: “violates our standard mental patterns and normal expectations”
- 中文译意：幽默往往来自某个事件违反了读者已有的认知模式和预期。
- 设计意图：标题需要制造“正常生活框架”和“错误严肃框架”之间的可感知冲突。例如，偷吃薯片本是小动作，但被写成设备失控或声音事故后，读者会在两个框架之间完成快速切换。

### 语义脚本理论 / Semantic Script Theory of Humor

Source: [Victor Raskin, *Semantic Mechanisms of Humor*, 1985](https://doi.org/10.1007/978-94-009-6472-3)

- 原文短摘 / Source excerpt: “compatible, fully or in part, with two different scripts”
- 中文译意：一个幽默文本通常可以同时被两个不同脚本解释。
- 设计意图：标题生成时不只寻找一个好听表达，而是要求同一句标题同时容纳两个脚本。例如“正常开会”和“薯片暴露现场”必须都能解释“我以为我 muted 了，但薯片没有”。

### 框架转换 / Frame-Shifting

Source: [Seana Coulson, *Semantic Leaps*, 2001](https://www.cambridge.org/core/books/semantic-leaps/frameshifting/49BD69ED5074D33574C2B6B27ADD582C)

- 原文短摘 / Source excerpt: “meaning emerges from the integration of linguistic and nonlinguistic knowledge”
- 中文译意：意义不是只由字面语言给出，也来自语言和背景知识的整合。
- 设计意图：标题必须调动读者对场景的背景知识。比如“muted”不仅是一个按钮状态，还隐含了线上会议、社死风险、声音泄露和自我误判。

### 概念整合 / Conceptual Blending

Source: [Fauconnier & Turner, "Conceptual Integration Networks", 1998](https://doi.org/10.1207/s15516709cog2202_1)

- 原文短摘 / Source excerpt: “structure from input mental spaces is projected”
- 中文译意：不同心理空间中的结构可以被投射并整合到新的意义空间。
- 设计意图：标题生成会把真实场景和错位框架合成为一个临时世界。例如“外卖地图小蓝点”与“塔台管制”整合后，才会出现“沙发塔台正在管制外卖蓝点”。

### 良性违背 / Benign Violation Theory

Source: [McGraw & Warren, "Benign Violations", 2010](https://doi.org/10.1177/0956797610376073)

- 原文短摘 / Source excerpt: “violations that are simultaneously seen as benign”
- 中文译意：幽默需要某种违背，但这种违背同时应被感知为安全、可接受或低风险。
- 设计意图：本 skill 只适合处理轻量日常场景。它可以把偷吃薯片写成“事故”，但不应把真实灾难、疾病或伤害事件包装成笑点。

### 关联理论 / Relevance Theory

Source: [Wilson & Sperber, "Relevance Theory", 2004](https://www.dan.sperber.fr/?p=93)

- 原文短摘 / Source excerpt: “Human cognition tends to be geared to the maximisation of relevance”
- 中文译意：人类理解语言时倾向于寻找最大相关性，以较低处理成本获得足够认知效果。
- 设计意图：标题不能把笑点解释完，而应提供足够线索，让读者自行完成重构。好的标题通常需要一秒内可理解，但读者会在理解瞬间意识到框架错位。

## 安装 / Installation

### Codex

如果你的 Codex 环境包含内置 `skill-installer` skill，可以直接安装：

```sh
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo u-u-z/fun-title-generator-skill \
  --path skills/fun-title-generator
```

安装后重启 Codex。

手动安装：

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p ~/.codex/skills
cp -R fun-title-generator-skill/skills/fun-title-generator ~/.codex/skills/
```

### Cursor

项目内安装：

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p .cursor/skills
cp -R fun-title-generator-skill/skills/fun-title-generator .cursor/skills/
```

安装后应存在：

```text
.cursor/skills/fun-title-generator/SKILL.md
```

如果没有立即生效，请重启 Cursor 或 reload window。

### OpenCode / opencode

OpenCode 支持从项目目录或全局配置目录发现 `SKILL.md`。

全局安装 / Global install:

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p ~/.config/opencode/skills
cp -R fun-title-generator-skill/skills/fun-title-generator ~/.config/opencode/skills/
```

项目内安装 / Project-local install:

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p .opencode/skills
cp -R fun-title-generator-skill/skills/fun-title-generator .opencode/skills/
```

安装后路径应为：

```text
~/.config/opencode/skills/fun-title-generator/SKILL.md
```

或：

```text
.opencode/skills/fun-title-generator/SKILL.md
```

OpenCode 也兼容 `.agents/skills/<name>/SKILL.md`。如果希望同一份 skill 被多个 agent 工具读取，可以放入 `.agents/skills/fun-title-generator/`。

### 更新 / Update

手动安装后，可以通过重新复制 skill 目录更新：

```sh
cd fun-title-generator-skill
git pull
cp -R skills/fun-title-generator ~/.codex/skills/
```

Cursor 用户将目标目录替换为项目内 `.cursor/skills/`；OpenCode 用户替换为 `~/.config/opencode/skills/` 或 `.opencode/skills/`。

## 使用 / Usage

显式调用：

```text
Use $fun-title-generator to generate titles for: 视频会议以为关麦了，结果偷吃薯片被全公司听见
```

推荐输入应包含一个具体、可视化动作。如果输入过于抽象，例如“帮我想一个社死标题”，skill 会优先追问具体画面。

## 案例 / Examples

### 视频会议偷吃薯片 / Video meeting snack accident

输入 / Input:

```text
视频会议以为关麦了，结果偷吃薯片被全公司听见
```

输出 / Output:

```text
Top titles:
1. 我以为我 muted 了，但薯片没有
2. 薯片在静音状态下仍被声呐捕获
3. 关于线上会议擅自咀嚼的调查报告
4. 静音键按下后出现进食冲动
5. 每声咔嚓都在证明麦没关

Recommended:
我以为我 muted 了，但薯片没有
```

### 盯外卖小蓝点 / Delivery tracking

输入 / Input:

```text
外卖快到了，我一直盯着地图上骑手的小蓝点靠近
```

输出 / Output:

```text
Top titles:
1. 沙发塔台正在管制外卖蓝点
2. 人类与地图蓝点建立单方面连接
3. 骑手离你两百米筷子已就位
4. 外卖蓝点进入家庭空管区
5. 本次外卖追踪行动全程受控

Recommended:
沙发塔台正在管制外卖蓝点
```

### 手机掉落脚部救援失败 / Phone drop reflex

输入 / Input:

```text
手机掉地上时，我第一反应用脚去垫，结果踢得更远
```

输出 / Output:

```text
Top titles:
1. 关于手机被脚二次击飞的技术分析
2. 脚垫那下是在给落地加弧线
3. 人类触发无意义脚部拦截反射
4. 手机坠落中脚部完成救援到助攻
5. 脚以为在救它，其实在加速

Recommended:
关于手机被脚二次击飞的技术分析
```

## 项目结构 / Repository Layout

```text
skills/fun-title-generator/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── examples.md
│   ├── theories.md
│   └── toolbox.md
└── scripts/
    └── validate_titles.py
```

## 标题校验 / Validation

内置 validator 用于检查硬规则：可见字符长度、显性搞笑词、敏感词、emoji 数量等。

```bash
python3 skills/fun-title-generator/scripts/validate_titles.py \
  "睡眠计划宣布无条件投降" \
  "沙发塔台正在管制外卖蓝点"
```

## 许可证 / License

MIT
