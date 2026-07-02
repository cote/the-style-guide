# Changelog

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
