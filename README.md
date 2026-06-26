# cote-style

A portable Claude skill that encodes the writing style of Michael Coté
(tech industry analyst, evangelist, writer). Drop it into any AI
session that needs to draft, ghostwrite, or edit text in his voice
without you having to hand-coach the model every time.

## What it covers

- The default conversational voice (blog posts, personal LinkedIn, podcast notes, newsletter prose).
- A more buttoned-up professional register (white papers, analyst briefs, conference abstracts).
- A deadpan list-essay mode for catalogue-of-the-absurd pieces.
- Per-platform social media voice (personal LinkedIn / Mastodon / Bluesky / Twitter), plus a separate company-page voice for posts that go out from an employer account.
- Anti-patterns Coté wants stripped on sight - especially AI-style signposting ("What's striking about X is...", "The thing that matters here is...").
- Formatting preferences: never em-dashes, straight quotes only, `_underscore_` italics (not `*single asterisk*`), no `**bold**` for in-paragraph emphasis, the specific `<figure>` HTML he uses for uploaded images, and newsletter section conventions.

## Layout

```
src/cote-style/
  SKILL.md            # always-load: voice summary, word lists, anti-patterns, self-edit checklist
  references/
    formatting.md         # markdown, HTML, quotes, dashes, figures, URL hygiene
    casual-voice.md       # default conversational register
    professional-voice.md # white papers, briefs, abstracts
    deadpan-list-essay.md # catalogue-of-the-absurd pieces
    social-media.md       # per-platform short-form; personal vs company-page
    no-signposting.md     # the biggest AI-writing tic to strip on edit
```

## How to use it

Drop `src/cote-style/` into your Claude (or other AI) skills directory
as `cote-style/`. Then either:

- Reference it in a session: "use the cote-style skill for this draft."
- Or paste the contents of `SKILL.md` into the system/context for one-off use.

The skill reads in two passes. `SKILL.md` is the always-load summary.
The `references/` directory has the deep dives - the skill loads the
one that matches the register you need.

## Customizing without forking

The skill follows the XDG config convention. Drop your own files into
`~/.config/io.cote.ai.skill.cote_style/` (or set `$COTE_STYLE_CONFIG_DIR`
to point somewhere else) to layer on top of the shipped defaults:

- `SKILL.local.md` - standing rules applied to every draft. Useful if
  you're using this skill to write in your own voice that's *adjacent*
  to Coté's, or if you want to disable rules that don't apply to you.
- `presets/<name>.md` - named scenarios loaded when the user's request
  matches the filename stem. Drop in `presets/keynote.md`,
  `presets/employer-x.md`, `presets/email-reply.md`, etc.
- `references/<name>.md` - static docs to load as background.

Local customizations take precedence over the shipped defaults. See
SKILL.md "Local customizations" for full resolution order.

## License

CC0 / public domain. Copy, modify, redistribute. The point is
portability - if this is useful to anyone else trying to write in this
voice (or train a model to), help yourself.
