# jianzhen-photo-caption — Jane Zhen-style Photo Captions

Generate **captions in the literary style of Jane Zhen (简媜, Taiwanese essayist)** for your photos. One run produces two parts:

1. **25 most relevant excerpts from Jane Zhen's works** — each with 《book》(essay) source attribution and a one-line reason connecting it to the photo (supports multi-sentence fragments and mood-matched passages)
2. **15 original captions**: 5 prose pieces, 5 modern poems, 5 short lines — written in Jane Zhen's sentence rhythm, image logic, and diction, but fully original (no verbatim reuse of her sentences)

Great for photography social media, Xiaohongshu / Moments posts, video cover captions, and aesthetic image copy.

## Features

- **1,521 curated excerpts**: built-in public quote / famous-line corpus from Jane Zhen, grouped across 90 books and essays — including *女儿红 (The Pink Bride)*, *水问 (Asking the Water)*, *红婴仔 (The Red Infant)*, *我为你洒下月光 (I Shed Moonlight for You)*, *梦游书 (The Sleepwalking Book)*, *空灵 (The Ethereal)*, and more
- **Zero third-party dependencies**: the search script uses only Python's standard library, runs fully offline, sends no data anywhere
- **Progressive disclosure**: the corpus is searched on demand rather than loaded wholesale into context, so it works in any AI environment
- **Regenerable**: after each delivery it asks whether you'd like another completely different round of options

## Installation

Put the whole `jianzhen-photo-caption` folder into your AI's **skills directory** (location varies by product):

- **Claude Desktop / Claude Code**: `~/.claude/skills/`
- **Doubao / other clients**: look for "Skills / 技能库" in Settings and point it at this folder
- **Cursor etc.**: place it in the project or global skills directory

Restart / refresh your AI afterward so it picks up the new skill.

## Usage

Just talk to the AI naturally — it auto-triggers. For example:

> "Write a caption in the style of Jane Zhen for this photo."

Or name the skill explicitly:

> "Use the jianzhen-photo-caption skill to caption this photo."

The AI will: parse the photo's imagery → search the corpus → pick 25 excerpts (with sources + reasons) → generate 15 original captions in Jane Zhen's style → ask if you'd like another round.

## Sample Output

> Scene: an empty plaza, a large tree ringed by a flower bed, red rubber pavement, a few wooden benches, afternoon slanting light.

Excerpts:
> 「门墙边，老树浓荫，曳着天风；草色釉青，三三两两的粉蝶梭游。」——《女儿红》（四月裂帛）
> 「枯坐半日，心思缥缈，如浮云、流光无法拘捕入罐。」——《女儿红·序》

Original poem excerpt:
> 老树把一年又一年的叶子，交给风，交给雨，交给秋天，交得那么大方，仿佛它从不心疼。可它偷偷把年轮，一圈一圈，藏进身体里。——（现代诗·《老树的话》）

## Directory Layout

```
jianzhen-photo-caption/
├── SKILL.md                    # Skill spec + 5-step workflow (what the AI triggers on and follows)
├── references/
│   ├── corpus/                 # 1,521 Jane Zhen excerpts (85 md files + book index)
│   ├── style_guide.md          # Style knowledge: diction / sentence rhythm / imagery / tone + taboos
│   ├── delivery-format.md      # Output spec + QA checklist
│   └── topic-index.md          # Theme → mood index
└── scripts/
    └── search_corpus.py        # Corpus search script (pure Python stdlib)
```

## Safety

- The search script uses only the Python standard library: no network calls, no file writes — safe to install
- As a general rule, read through any third-party skill's `SKILL.md` and scripts before installing

## Copyright

All corpus entries come from **publicly available book excerpts, famous quotes, and single-essay selections** of Jane Zhen, each retaining its 《book》(essay) source attribution. No full works are transcribed; all captions are original writing. Contact the repository maintainer if any copyright concern arises.

## License

MIT
