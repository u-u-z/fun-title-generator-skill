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
