# Formatting rules

Apply to every register. These are mechanical - get them right or the
output looks wrong, no matter how good the voice is.

## Dashes

**Never use em dashes (`—`, U+2014).** Replace with a space-hyphen-space: ` - `.

Also avoid en dashes (`–`, U+2013) where a plain ASCII hyphen works.

Why: strongly-held personal preference; also typographic dashes render
as missing-glyph boxes in some fonts. If a sentence feels like it wants
an em dash, use ` - `, a colon, a comma, or two sentences.

If you're editing existing text and see em-dashes, normalize them.

## Quotes

**Straight / dumb quotes only**: `"` and `'`. Never smart / curly quotes
(`"` `"` `'` `'`).

When a quote begins mid-sentence in the source and starts with a
lowercase letter, capitalize it in square brackets: `"[T]his is an
example."`

When the outer quote is double and the quoted material itself contains
double quotes, convert the inner doubles to singles. Don't touch the
outer.

## Italics

**Use `_underscore_`, not `*single asterisk*`.**

Why: visual readability of the raw markdown, and underscores don't
interfere with `*` used for lists. Both render identically in CommonMark,
so it's purely a source-readability choice.

See "Titles: italic vs quoted" below for which titles get italics.

## Titles: italic vs quoted

Follow MLA. The heuristic: **italics for the big thing, quotes for the
small thing inside it.**

Italics - the standalone, self-contained work:

- Books: `_Moral Mazes_`
- Journals, magazines, newspapers: `_The Atlantic_`
- Films and TV series: `_Michael Clayton_`, `_Twin Peaks_`
- Albums: `_Zen Arcade_`
- Podcasts (the show): `_Software Defined Talk_`
- Plays, long poems, works of visual art, standalone reports and white
  papers: `_Software Factory 2.0_`

Quotes - the piece contained in something bigger:

- Articles and essays, including academic papers published in a journal
  or proceedings: `"No Silver Bullet"`
- Book chapters
- Blog posts
- Podcast episodes: `"Episode 512: the one about YAML"`
- Songs: `"Pink Turns to Blue"`
- TV episodes: `"The Suitcase"`
- Short stories and short poems

Two edge cases worth naming:

- **A paper gets quotes, not italics.** It's an article in a journal or
  proceedings, so it's the small thing. This is the rule people get
  wrong most often.
- **A white paper or standalone report gets italics** - it's published on
  its own, not inside a container. If it appeared as an article on a
  site, quote it instead.

When in doubt, ask whether the thing was published inside another thing.
If yes, quotes. If it stands alone, italics.

## Bold

**Don't use `**bold**` as in-paragraph emphasis or to highlight terms.**
Default for emphasis is no formatting at all - let the sentence carry it.

Bold *is* fine for actual semantic weight:

- An HTML form `<strong>` warning.
- A glossary's defined-term column header.
- The lead label of a deliberately structured bullet ("**Why:**" / "**How to apply:**" memo blocks).

But not as visual highlight inside running prose.

**Never wrap URLs in `**...**`.** Terminal and messaging-client
auto-linkers capture the surrounding asterisks as part of the URL, so
the "link" navigates to a URL with `**` in it and 404s. If you need
emphasis on a link, use a leading word ("Staging URL: ...") or a
separate line, not inline formatting around the URL itself.

## Lists

Use bullets when the content is genuinely list-shaped (criteria,
principles, components). Not as a way to break up dense paragraphs.

In casual register, inline numbered lists are fair game on social
posts: "(1) X. (2) Y. (3) Z."

## Headers

- Blog posts: `##` for top-level sections, `###` sparingly. Subheadings
  can be informal, sometimes playful.
- Newsletters: `##` only. No sub-headers.
- Short-form social: no headers at all.

## Links

- Inline links on a phrase, not citation sentences. Bad: "As DORA reports in their 2023 survey, X." Good: "[DORA's 2023 survey](url) shows X."
- Trust the reader. Don't add a sentence explaining why a link is relevant when the link's surrounding phrase already does that work.

## HTML inside markdown

CommonMark passes inline HTML through, so mix HTML into markdown as
needed - but sparingly. Use it only where markdown can't express the
structure.

Good uses:

- YouTube and other video embeds (`<iframe>`).
- The `<figure>` block for uploaded images, described below.
- Authorship spans and similar one-off structure.

Bad uses: anything markdown already has syntax for. Blockquotes are the
common mistake - use markdown's `>`, not a raw `<blockquote>`. Same for
headers, lists, links, emphasis, and code.

Never convert a whole post to HTML because a few parts of it use HTML.
That throws away markdown processing for no reason and makes the post
painful to edit later. Keep the body as markdown and drop in HTML blocks
where they're needed.

Inline HTML is not supported by every renderer. If you don't know what's
rendering the output, check before relying on it.

## The `<figure>` block (uploaded images)

For images embedded in blog posts, Coté uses a specific `<figure>`
shape:

```html
<figure>
    <img src="/path/to/image.jpg" width="600" alt="Descriptive alt text"/>
    <figcaption>Caption text here.</figcaption>
</figure>
```

Rules:

- **Always include `width="<px>"`** - lets the browser reserve space and matches the existing pattern.
- **Use a path-relative `src`** (`/wp-content/uploads/YYYY/MM/...` for WordPress, `/uploads/...` for other static sites) by default. Use an absolute `https://...` URL only when the figure will be embedded somewhere off the origin site (newsletter sent to subscribers, cross-posted to another platform).
- **No `class="..."`, no inline `style="..."`.** The site's CSS handles responsive sizing.
- **`alt` is required** and should describe the image substantively. For complex images (charts, infographics), spell out what the image shows, including readable text inside it.
- **Drop the `<figcaption>` line entirely** when the image has no caption. Don't emit an empty `<figcaption></figcaption>`.
- The 4-space indent inside `<figure>` is intentional - matches the existing pattern across his posts.

For a video embed, use a raw `<iframe>` block inside a markdown body:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="..." frameborder="0" allow="..." allowfullscreen></iframe>
```
