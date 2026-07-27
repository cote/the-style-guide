---
name: the-style-guide
description: A multi-style guide for writing and question-asking. Primarily for writing in the style of Michael Coté (likely the user of this skill), but designed to hold other styles too - other authors' prose voices, question-asking styles for interview prep (e.g. Tyler Cowen), or any repeatable "here's how to sound like X" bundle. Use when drafting, ghostwriting, or editing anything that should sound like a specific voice - blogs, newsletters, social media, video descriptions, conference abstracts, white papers, podcast show notes, talk titles, email replies - or when generating questions / interview outlines / prompts in someone's characteristic style.
compatibility: Requires bash.
metadata:
  author: cote
  version: "1.5"
---

# The Style Guide

A portable multi-style guide. Ships with the Coté prose style as the
default. Also holds question-generation styles (e.g. Tyler Cowen
interview questions) and can be extended with any other named style
without forking.

A "style" here is broader than just a prose voice. It's any repeatable
"do it in the style of X" bundle - author voices, interview-question
styles, review styles, negotiation styles. If it has recognizable
patterns you'd want to apply consistently, it can be a style.

## How style resolution works

**Only one style is loaded per task.** Do not preemptively read other
style files into context. Pick the style the user is asking for and
load only that one.

1. Read this file for the loading pattern.
2. Check for local customizations (see below). `SKILL.local.md` layers
   standing rules on top of every task, regardless of style.
3. Pick the style:
   - If the user's request names or clearly implies a style, load that
     one. Match by substring against filename stems and directory
     names under `styles/` and the local `styles/` dir
     (case-insensitive; treat hyphens, spaces, and underscores as
     equivalent, so "Tyler Cowen" matches `tyler-cowen-questions.md`).
     Local styles win on collision.
   - If the user does not name a style, default to Coté:
     `styles/cote/general.md`.
   - If the user names a style that doesn't exist, list what's
     available and ask - don't fall back to Coté silently.
4. Load only the picked style. If it's a multi-file style, load
   `general.md` plus the one content-type sibling that matches the
   task. Load pointed-at references only when the style calls for
   them or the specific task warrants it. Progressive disclosure at
   every step.

Do not load `styles/cote/*` when the user asked for Tyler Cowen. Do
not load `styles/tyler-cowen-questions.md` when the user asked for a
blog post. The point of the skill is to keep the context lean and
focused on the one style in play.

## Style file layouts

Two shapes, pick whichever fits:

### Single-file style: `styles/<name>.md`

For a compact style that doesn't split by content type. One file
covers everything. Example: `styles/tyler-cowen-questions.md` -
question-generation style, one file.

### Multi-file style: `styles/<name>/`

For a bigger style with meaningfully different content types. The
directory holds:

- **`general.md`** - always loaded when this style is picked. Voice /
  approach / word choice / anti-patterns / self-edit checklist.
- **Content-type siblings** - loaded on top of `general.md` when the
  task matches. A style names whatever content types make sense for
  it. In `styles/cote/` the siblings are `casual-voice.md`,
  `professional-voice.md`, `deadpan-list-essay.md`, and
  `social-media.md`. Another prose style might pick `blog.md`,
  `newsletter.md`, `keynote.md` instead.

Pick multi-file when the style really does behave differently by
content type. Pick single-file when it doesn't.

## Shipped styles

- **`styles/cote/`** - Michael Coté's prose voice across his registers. Default for prose writing / editing tasks when nothing else matches. Load `general.md` first, then the content-type sibling that matches the task.
- **`styles/tyler-cowen-questions.md`** - How to generate interview / conversation questions in the style of Tyler Cowen's *Conversations with Tyler* podcast. Load when the user asks for "Tyler Cowen style questions", interview prep in that style, or podcast question generation with wide-ranging / personal / unexpected angles.
- **`styles/ai-detector.md`** - A generic, voice-neutral detection + edit-pass style. Load when the user asks to "detect AI", "strip AI", "de-AI this", "make it not read like ChatGPT", or as a companion pass at the end of any generation task. Produces no voice on its own - pair with the actual positive style in play. Aggregates the anti-AI content that's scattered across the other shipped styles (never-use word lists, Mollick's short-mute list, self-important punchline closers, signposting frames, rationalist / LessWrong jargon) into one includable file. Cites the empirical evidence base (Kobak, Liang, Gray, Glynn, Cabanac) and the editorial essays (Gorrie, Vollmer, Hassid). Point at `references/ai-writing-tells.md` for the deeper Wikipedia-derived catalog. Pair with `scripts/cliche-check.py` for the automated scan.
- **`styles/linkedin/`** - LinkedIn-focused styles. Two peer files, load whichever the user asks for (this dir has no `general.md` - the two files are separate top-level styles that happen to share a subject):
  - **`no-linkedin-talk.md`** - A *negative* / edit-pass style. Load when the user asks to strip LinkedIn cliches from a draft ("don't sound like LinkedIn", "remove LinkedIn-talk", "de-LinkedIn this"). Produces no voice on its own - pair with the actual positive style in play. Catalogs the standard LinkedIn phrase set, the AI-prompted subset, structural tells (dramatic-opener + narrative + lesson + engagement closer), the extended banned lexicon (journey / thrilled / humbled / disruptor / etc.), broetry, the parable-to-lesson pivot, and gives before/after rewrites.
  - **`successful-posts.md`** - A positive / how-to style. Load when the user wants a LinkedIn post that will actually perform ("write me a LinkedIn post about X", "help me get engagement on this"). Grounded in Usera / Cox / Walker (2026) engagement research: the post-category hierarchy (Interpersonal + Observances win reactions/comments; Business + Observances win reposts; Expertise underperforms), the scarcity arbitrage, tagging mechanics, and per-post-type recipes (interpersonal / observance / business / personal / expertise). Deliberately ignores whether the post "sounds like LinkedIn" - pair with `no-linkedin-talk.md` if the user wants effective *and* not-embarrassing.

Drop additional `.md` files or subdirectories into the local `styles/`
dir (see below) to extend this.

## Shared references

Deep-dive docs that any style can point at. Not trigger-matched;
loaded when the picked style calls for them or the task warrants it.
These are style-agnostic - taste rules and edit-pass tools that apply
across authors, not tied to any one voice:

- `references/formatting.md` - dashes, quotes, italics, `<figure>` HTML, URL hygiene. Load on any drafting task.
- `references/no-signposting.md` - biggest AI-writing tic (framing sentences that announce what's coming instead of just saying it). Load on any edit over AI-drafted text.
- `references/ai-writing-tells.md` - broader catalog of AI-writing patterns and how to strip them, derived from the Wikipedia *Signs of AI writing* project page. Load alongside `no-signposting.md` on edit passes. Has a freshness rule - check the file's *Last fetched* date and prompt the user to refresh if it's 90+ days old.
- `references/dont-talk-like-an-ai.md` - the anti-AI rules packaged as a self-contained document meant to be pasted into someone else's system prompt, `CLAUDE.md`, or custom-instructions box. Load when the user asks for anti-AI rules they can take somewhere else ("give me something I can paste into ChatGPT", "write me a system prompt that stops this"), rather than asking for a draft to be edited. Covers ground the other files don't: the ban on one-sentence paragraphs and fragments-as-drama, sentence-length variation, and when a bulleted list is the wrong shape. For an actual edit pass over a draft, use `styles/ai-detector.md` instead.
- `references/dont-talk-like-an-ai-short.md` - the ~380-word version of the same, sized for a user-preferences box where it competes with everything else the user wants the model to know. Load when the user asks for a short version, or when the target is a preferences / personalization field rather than a full system prompt.

Style-specific deep dives (registers, per-content-type conventions,
per-style anti-patterns) live *inside* that style's dir, not here. See
`styles/cote/` for examples.

## Local customizations

Before doing the task, look for user customizations in this resolution
order:

1. `$THE_STYLE_GUIDE_CONFIG_DIR` (if set)
2. `$XDG_CONFIG_HOME/io.cote.ai.skill.the_style_guide/` (if `XDG_CONFIG_HOME` is set)
3. `~/.config/io.cote.ai.skill.the_style_guide/`

Inside whichever resolves first, treat these as load-bearing:

- **`SKILL.local.md`** - always loaded if present. Standing rules
  applied to every task (e.g. "I'm not Coté, I'm Pat - swap the
  first-person references but keep the voice", "always include a
  Mastodon variant alongside any LinkedIn draft", "when doing Tyler
  Cowen questions, always end with an overrated/underrated segment").
  Rules can supplement or override the shipped defaults - user wins on
  contradiction.
- **`styles/<name>.md`** or **`styles/<name>/`** - named styles. Same
  matching and layout rules as shipped styles. Drop one in for a
  voice, question style, or any other repeatable style bundle. Local
  wins on collision.
- **`references/<name>.md`** - static docs Claude should read as
  background (a personal style guide layered on top, a list of banned
  phrases specific to one employer, a vocabulary cheat sheet).

If the user names a style that doesn't exist under either the shipped
`styles/` or the local `styles/`, list what's available in both and
ask.

## XDG paths

| What | Location |
|------|----------|
| Config | `~/.config/io.cote.ai.skill.the_style_guide/` |
| Data | `~/.local/share/io.cote.ai.skill.the_style_guide/` |
| State | `~/.local/state/io.cote.ai.skill.the_style_guide/` |
| Cache | `~/.cache/io.cote.ai.skill.the_style_guide/` |

Config is load-bearing - see "Local customizations" above. Data,
state, and cache are reserved for future use (e.g. a per-user history
of phrases the model used and the user struck out, so the skill can
learn from edits).

## Writing new styles

A style file is a self-contained guide for a voice or approach.
Minimum shape:

1. One-paragraph "what this style is" description.
2. The core moves / patterns that make it recognizable.
3. Word choice or question shape - use freely / never use.
4. Structural defaults for whatever this style is used to produce.
5. Anti-patterns to strip on sight.
6. A short self-edit checklist.

Look at `styles/cote/general.md` for a prose style and
`styles/tyler-cowen-questions.md` for a question style as examples -
not rigid templates, just working references. Point at existing
`references/*.md` files where they apply, or ship your own alongside
the style.
