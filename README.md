# The Style Guide

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
- *dont-talk-like-an-ai* and *dont-talk-like-an-ai-short* - the
  anti-AI rules packaged to work with no skill at all. See the next
  section.

## Two files you can use without the skill

`references/dont-talk-like-an-ai.md` and
`references/dont-talk-like-an-ai-short.md` are written to be lifted out
of this repo and used on their own. They're self-contained: no
cross-references to other files here, no skill-loading machinery, no
assumption that anything else got read first. Copy either one into a
chat session, a system prompt, a `CLAUDE.md`, a `.cursorrules`, or the
custom-instructions box of whatever assistant you use, and it works.

The long one runs about 200 lines and covers banned phrases grouped by
failure mode, banned words, nine banned sentence structures, paragraph
and document shape, punctuation, and a final-pass checklist. Use it
when you're setting up a drafting or editing context and have room for
it, or paste it into a single session when you want one piece cleaned
up.

The short one is about 380 words, sized for a user-preferences box
where you're competing with everything else you want the model to know
about you. It keeps the highest-frequency bans and the structural rules
that change how a reply reads, and drops the explanations. It opens
with a line scoping the rules to every reply rather than only to
documents you explicitly asked to have written, which is the difference
between a model that stops saying "load-bearing" in chat and one that
only stops when it thinks it's Writing.

Both are CC0 like the rest of the repo, so no attribution needed. If
you do want the full skill, these two files are also loaded as
references inside it, and `styles/ai-detector.md` plus
`scripts/cliche-check.py` give you the same material with the sources
and an automated scanner.

## Layout

```
src/the-style-guide/
  SKILL.md                            # always-load: skill purpose, resolution order, XDG paths
  styles/
    cote/                             # multi-file style: general.md + register siblings
      general.md
      casual-voice.md
      professional-voice.md
      deadpan-list-essay.md
      social-media.md
    tyler-cowen-questions.md          # single-file style
    ai-detector.md                    # single-file style, voice-neutral edit pass
    linkedin/                         # two peer styles that share a subject
      no-linkedin-talk.md
      successful-posts.md
  references/
    formatting.md
    no-signposting.md
    ai-writing-tells.md
    dont-talk-like-an-ai.md           # standalone, paste anywhere
    dont-talk-like-an-ai-short.md     # standalone, sized for a prefs box
  scripts/
    cliche-check.py                   # regex scanner for the phrase lists
```

## How to use it

Fastest path: clone the repo and run `./build.sh --install`. That
copies `src/the-style-guide/` into `~/.claude/skills/the-style-guide/`
so Claude Code picks it up. Set `SKILL_INSTALL_DIR` to install
somewhere else.

If you'd rather do it by hand, drop `src/the-style-guide/` into your
Claude (or other AI) skills directory as `the-style-guide/`. Then
either:

- Reference it in a session: "use the-style-guide skill for this draft."
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
`~/.config/io.cote.ai.skill.the_style_guide/` (or set
`$THE_STYLE_GUIDE_CONFIG_DIR` to point elsewhere) to layer on top of the
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
