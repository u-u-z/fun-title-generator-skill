# Fun Title Generator Skill

`fun-title-generator` is a Codex/Cursor skill for generating Remi-style funny short titles for concrete everyday scenes. It is tuned for Xiaohongshu, Bilibili, Moments, video covers, and other lightweight social posts where the title should feel precise, deadpan, and a little absurd.

The skill's core formula:

```text
真实小事 × 错位框架 × 严肃语气 × 精准表达 = 搞笑标题
```

## Installation

### Codex

If your Codex installation includes the built-in `skill-installer` skill, install directly from this GitHub repository:

```sh
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo u-u-z/fun-title-generator-skill \
  --path skills/fun-title-generator
```

Restart Codex after installation so the new skill is loaded.

If you do not have the installer script, install it manually:

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p ~/.codex/skills
cp -R fun-title-generator-skill/skills/fun-title-generator ~/.codex/skills/
```

Then restart Codex.

### Cursor

For a project-local Cursor skill, copy the skill folder into your project's `.cursor/skills` directory:

```sh
git clone https://github.com/u-u-z/fun-title-generator-skill.git
mkdir -p .cursor/skills
cp -R fun-title-generator-skill/skills/fun-title-generator .cursor/skills/
```

Your project should then contain:

```text
.cursor/skills/fun-title-generator/SKILL.md
```

Restart Cursor or reload the window if the skill does not appear immediately.

### Update

To update a manual installation, pull the latest repository version and copy the skill folder again:

```sh
cd fun-title-generator-skill
git pull
cp -R skills/fun-title-generator ~/.codex/skills/
```

For Cursor, replace `~/.codex/skills/` with your project's `.cursor/skills/` directory.

## Use

Invoke it explicitly:

```text
Use $fun-title-generator to generate titles for: 视频会议以为关麦了，结果偷吃薯片被全公司听见
```

The skill works best when the input includes a small, visible action. If the scene is too abstract, it will ask for the most concrete action before generating titles.

## Examples

### Video meeting snack accident

Input:

```text
视频会议以为关麦了，结果偷吃薯片被全公司听见
```

Output:

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

### Delivery tracking

Input:

```text
外卖快到了，我一直盯着地图上骑手的小蓝点靠近
```

Output:

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

### Phone drop reflex

Input:

```text
手机掉地上时，我第一反应用脚去垫，结果踢得更远
```

Output:

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

## Repository Layout

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

## Validate Titles

The bundled validator checks hard title rules such as visible length, obvious joke words, sensitive words, and emoji count:

```bash
python3 skills/fun-title-generator/scripts/validate_titles.py \
  "睡眠计划宣布无条件投降" \
  "沙发塔台正在管制外卖蓝点"
```

## License

MIT
