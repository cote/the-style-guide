# Changelog

## 1.5 - 2026-07-27

- New `references/dont-talk-like-an-ai.md`: a standalone, self-contained
  version of the anti-AI rules, written to be pasted straight into a
  system prompt, a CLAUDE.md, or a custom-instructions box by someone
  who isn't using this skill at all. Sections: banned phrases grouped by
  failure mode (importance-by-metaphor, fake-insight setups,
  signposting, punchline closers, significance inflation, rationalist
  tics, chat pleasantries, weasel attribution), banned words, nine
  banned sentence structures, paragraph and document shape, punctuation
  and formatting, positive rules, final-pass checklist. Adds material
  the shipped styles don't cover: the ban on one-sentence paragraphs
  and fragments-as-drama, sentence-length variation, and the rule
  against bulleting an argument.
- New `references/dont-talk-like-an-ai-short.md`: a ~380-word version
  of the same, sized for a user-preferences box (Claude.ai custom
  instructions, ChatGPT personalization, a short system prompt). Opens
  with a scope line stating the rules govern every reply rather than
  only pieces the user asked to have written, since models otherwise
  read prose-craft rules as document-only.
- New `styles/ai-detector.md`: generic voice-neutral detection +
  edit-pass style. Aggregates the anti-AI content that lives in
  `styles/cote/general.md`, `styles/cote/professional-voice.md`, and
  `styles/linkedin/no-linkedin-talk.md` into one includable file.
  Adds a rationalist / LessWrong jargon section (load-bearing, priors
  family, steelman, Chesterton's fence). Includes a §Sources block
  with URLs for the empirical evidence base (Kobak 2025 Science
  Advances, Liang 2024 ICML, Gray, Glynn, Geng & Trotta, Cabanac) and
  editorial essays (Gorrie, Vollmer, Hassid). Pair with any positive
  style; produces no voice on its own.
- New `scripts/cliche-check.py`: regex scanner over 167 patterns
  across 9 categories (vocabulary, mollick, punchline-closer,
  rationalist-hard, rationalist-sparingly, signposting,
  linkedin-opener, academ-ai-leaks, and Simon Willison's 12
  llm-cliche-highlighter regexes ported from JS). Reads stdin or a
  file arg; exits 0 clean, 1 on hits; `--category` filters,
  `--list-categories` inventories. Vocabulary list draws on the
  cross-source consensus in the Kobak / Liang / Gray / Vollmer word
  lists. Originals of the sources live outside the skill (Coté's
  iCloud archive); the skill ships URLs only.
- `SKILL.md`: added `styles/ai-detector.md` to the Shipped styles
  catalog, and both `dont-talk-like-an-ai` files to the Shared
  references catalog with load conditions that distinguish "give me
  rules to take elsewhere" from "edit this draft."
- `README.md`: new "Two files you can use without the skill" section,
  plus layout-tree entries for `styles/ai-detector.md`, `scripts/`,
  and the two new references.

## 1.4 - 2026-07-02

- `styles/linkedin/no-linkedin-talk.md`: added a "Self-important
  punchline closers" phrase list ("It's the one worth telling," "That's
  the version that matters," and variants) plus a matching self-edit
  checklist item. Catches the closer that elevates the writer's own
  story with a vague-profound frame instead of just letting the story
  do the work.

## 1.3 - 2026-07-02

- Renamed skill from `cote-style` to `the-style-guide`. Repo dir, inner
  skill dir, frontmatter `name:`, XDG namespace, and env var all updated
  to match. XDG namespace is now `io.cote.ai.skill.the_style_guide`;
  config override env var is now `$THE_STYLE_GUIDE_CONFIG_DIR`.
  Breaking: users with existing local overrides under
  `~/.config/io.cote.ai.skill.cote_style/` need to move them.
- Added `build.sh` (combined build / zip / install / package + SBOM),
  `CHANGELOG.md`, and expanded `.gitignore` per the-skill-builder
  policy.

## 1.2 and earlier

Pre-changelog. See git log for history: added `styles/linkedin/` peer
files, `styles/tyler-cowen-questions.md`, restructured `styles/cote/`
into `general.md` + register siblings, added
`references/ai-writing-tells.md` and `references/no-signposting.md`.
