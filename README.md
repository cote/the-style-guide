# cote-style

A portable Claude skill that holds multiple named writing / style
guides in one place. Drop it into any AI session that needs to draft,
ghostwrite, or edit text in a specific voice (or generate questions in
a specific style, or strip a specific unwanted style) without
hand-coaching the model every time.

Named for Michael Coté because his prose style is the shipped default,
but the skill is designed to hold other styles too. Bring your own.

## What's in here

Shipped styles:

- **Coté** - his prose voice across content types (blog / newsletter /
  personal LinkedIn / podcast prose / white paper / analyst brief /
  conference abstract / deadpan-list catalogue-of-the-absurd). Default
  when no other style is named.
- **Tyler Cowen questions** - question-generation style for interview
  prep in the mode of *Conversations with Tyler*: cite everything, jump
  domains, ask about tacit knowledge, overrated/underrated segments,
  personal biographical detail.
- **LinkedIn** - two peer files:
  - *no-linkedin-talk* - a negative / edit-pass style. Load when
    you're stripping LinkedIn clichés from a draft. Doesn't produce a
    voice on its own.
  - *successful-posts* - a positive / how-to style grounded in
    engagement research. Load when you want a LinkedIn post that
    actually performs. Ignores taste; pair with no-linkedin-talk if
    you want both.

Shared references (style-agnostic, loaded as-needed):

- *formatting* - dashes (never em-), quotes (never smart), italics
  (`_underscore_`, never `*asterisk*`), never `**bold**` for
  emphasis, the `<figure>` HTML pattern for uploaded images, URL
  hygiene.
- *no-signposting* - the biggest AI-writing tic to strip on edit
  passes: "What's striking about X is...", "The thing that matters
  here is..." Worked before/after examples.
- *ai-writing-tells* - broader catalog derived from Wikipedia's
  *Signs of AI writing* project page. Has a 90-day freshness rule -
  if the file's *Last fetched* date is stale, prompt for a refresh.

## Layout

```
src/cote-style/
  SKILL.md                            # always-load: skill purpose, resolution order, XDG paths
  styles/
    cote/                             # multi-file style: general.md + register siblings
      general.md
      casual-voice.md
      professional-voice.md
      deadpan-list-essay.md
      social-media.md
    tyler-cowen-questions.md          # single-file style
    linkedin/                         # two peer styles that share a subject
      no-linkedin-talk.md
      successful-posts.md
  references/
    formatting.md
    no-signposting.md
    ai-writing-tells.md
```

## How to use it

Drop `src/cote-style/` into your Claude (or other AI) skills directory
as `cote-style/`. Then either:

- Reference it in a session: "use the cote-style skill for this draft."
- Or paste `SKILL.md` into the system prompt / context for one-off use.

Progressive disclosure: `SKILL.md` is always loaded. Individual style
files load only when the user's request matches (case-insensitive
substring match on filename stems, with hyphens / spaces / underscores
treated as equivalent). References load only when a style points at
them or the task warrants it. Only one style is loaded per task -
asking for Tyler Cowen questions does not drag the Coté files into
context.

If no style is named and the task is prose, the default is Coté. If a
named style doesn't exist, the skill lists what's available and asks
rather than silently falling back.

## Customizing without forking

Follows the XDG config convention. Drop your own files into
`~/.config/io.cote.ai.skill.cote_style/` (or set
`$COTE_STYLE_CONFIG_DIR` to point elsewhere) to layer on top of the
shipped defaults:

- `SKILL.local.md` - standing rules applied to every task. Useful if
  you're using this skill in your own voice adjacent to Coté's, or
  you want to disable rules that don't apply to you. Contradictions
  win for the user.
- `styles/<name>.md` or `styles/<name>/` - your own named styles.
  Same shapes as shipped. Local styles win on collision.
- `references/<name>.md` - static background docs.

See SKILL.md "Local customizations" for full resolution order.

## Adding new styles

Two shapes:

- **Single-file** (`styles/<name>.md`) - one file covers the whole
  style. Good for compact styles. See `tyler-cowen-questions.md` for
  an example.
- **Multi-file** (`styles/<name>/`) - `general.md` is the always-load
  base when the style is picked; content-type siblings
  (`blog.md`, `professional.md`, etc.) load on top when the task
  matches. See `styles/cote/` for an example.

A style file should cover: what the style is, sentence-level or
question-level patterns, word choice (use freely / never use),
structural defaults, anti-patterns, and a self-edit checklist.

## Content notes

- Examples in the Coté style files include casual profanity ("shit",
  "fucked up") because that's the voice being encoded.
- All third-party sources (Wikipedia's *Signs of AI writing*,
  Onwuka's LinkedIn clichés post, Mollick's LinkedIn mute-list post,
  Usera/Cox/Walker's SAGE Open paper) are cited with URL and
  retrieval date in the source notes at the bottom of each file
  that uses them.

## License

CC0 / public domain. See LICENSE. Copy, modify, redistribute. The
point is portability - if this is useful to anyone else trying to
encode a writing style for an AI to consume, help yourself.
