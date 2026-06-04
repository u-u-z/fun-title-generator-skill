# Fun Title Generator Skill

`fun-title-generator` 是一个面向中文语境的 Codex/Cursor skill。  
It is designed for Chinese-language contexts: 小红书、B 站、朋友圈、视频封面，以及其他需要中文短标题的轻量社交内容。

它专门生成一种 Remi 风格的有趣短标题：观察具体，语气一本正经，笑点来自“把小事放进不属于它的严肃系统里”。不是营销号热梗，也不是段子手喊麦，而是轻巧、冷静、精准、有一点荒谬。

核心公式 / Core formula:

```text
真实小事 × 错位框架 × 严肃语气 × 精准表达 = 搞笑标题
```

## 工作原理 / How It Works

这个 skill 不是给场景硬加网络热词，而是把一个小而具体的动作，写成另一个严肃系统里的事件。

比如“视频会议以为关麦了，结果偷吃薯片被全公司听见”，会被改写成一个一本正经的设备失控事件：

```text
我以为我 muted 了，但薯片没有
```

基本流程：

1. **提取具体动作 / Extract the concrete action**  
   优先找画面里真正发生的动作、物体、场景和压力点。它更喜欢“偷吃薯片时没关麦”，而不是“一个社死场景”。

2. **选择错位框架 / Choose a mismatched frame**  
   把日常小事放进纪录片、情况通报、科研报告、职场流程、空中管制、法律文书、考古发现、技术分析等严肃框架里。

3. **生成并筛选 / Generate and filter candidates**  
   同时走两条路：一种靠错位框架制造荒谬感，一种靠精准观察命中日常共鸣。太泛、太解释、太长、只是在夸张的候选会被淘汰。

4. **校验最终标题 / Validate the final title**  
   内置 validator 会检查硬规则：标题长度、显性搞笑词（如 `哈哈哈`、`笑死`）、攻击性敏感词、emoji 数量等。

好的输出应该是：表面冷静，底下荒谬。标题不解释为什么好笑，而是让读者在一秒内自己发现错位。

## 安装 / Installation

### Codex

如果你的 Codex 里有内置的 `skill-installer` skill，可以直接从这个 GitHub repo 安装：

```sh
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo u-u-z/fun-title-generator-skill \
  --path skills/fun-title-generator
```

安装后重启 Codex，让新 skill 被加载。

如果你没有这个 installer script，也可以手动安装：

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p ~/.codex/skills
cp -R fun-title-generator-skill/skills/fun-title-generator ~/.codex/skills/
```

然后重启 Codex。

### Cursor

如果你想作为项目内的 Cursor skill 使用，把 skill 文件夹复制到项目的 `.cursor/skills` 目录：

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p .cursor/skills
cp -R fun-title-generator-skill/skills/fun-title-generator .cursor/skills/
```

复制后项目里应该有：

```text
.cursor/skills/fun-title-generator/SKILL.md
```

如果没有立刻出现，重启 Cursor 或 reload window。

### OpenCode / opencode

OpenCode 支持从项目目录或全局配置目录发现 `SKILL.md`。这个 skill 可以直接安装到 OpenCode 的 native skills path。

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

安装后路径应该类似：

```text
~/.config/opencode/skills/fun-title-generator/SKILL.md
```

或：

```text
.opencode/skills/fun-title-generator/SKILL.md
```

OpenCode 也兼容 `.agents/skills/<name>/SKILL.md` 这样的 agent-compatible 路径；如果你希望同一份 skill 同时给多个 agent 工具读取，也可以放到 `.agents/skills/fun-title-generator/`。

### 更新 / Update

手动安装后，如果要更新：

```sh
cd fun-title-generator-skill
git pull
cp -R skills/fun-title-generator ~/.codex/skills/
```

如果是 Cursor，把 `~/.codex/skills/` 换成你项目里的 `.cursor/skills/`。

## 使用 / Use

显式调用：

```text
Use $fun-title-generator to generate titles for: 视频会议以为关麦了，结果偷吃薯片被全公司听见
```

这个 skill 最适合有具体画面的输入。如果你只说“帮我想一个社死标题”，它可能会先追问：这个场景里最具体的动作是什么？

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

## 标题校验 / Validate Titles

内置 validator 用来检查标题硬规则：可见字符长度、显性搞笑词、敏感词、emoji 数量等。

```bash
python3 skills/fun-title-generator/scripts/validate_titles.py \
  "睡眠计划宣布无条件投降" \
  "沙发塔台正在管制外卖蓝点"
```

## 许可证 / License

MIT
