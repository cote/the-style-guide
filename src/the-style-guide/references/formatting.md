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

For book titles, paper titles, podcast names: italics. (`_Moral Mazes_`,
`_Software Factory 2.0_`.)

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

CommonMark passes inline HTML through. For blog and micro.blog posts,
keep the body as markdown and drop HTML blocks only where you need
specific structure: figures, iframes, authorship spans, etc. Don't
convert the whole post to HTML - that throws away markdown processing
for no reason and makes the post painful to edit later.

## The `<figure>` block (uploaded images)

For images embedded in blog posts, Coté uses a specific `<figure>`
shape:

```html
<figure>
    <img decoding="async" src="/path/to/image.jpg" width="600" alt="Descriptive alt text"/>
    <figcaption>Caption text here.</figcaption>
</figure>
```

Rules:

- **Always include `decoding="async"`** on the `<img>`.
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

## Markdown over HTML, except where HTML is required

Default: write markdown. Drop HTML blocks (figures, iframes, authorship
spans) where the structure needs them. Don't convert the whole post to
HTML just because some parts of it use HTML.

For platforms that take markdown (micro.blog, most blog engines, most
newsletter tools), pass markdown directly - inline HTML passes through
fine via CommonMark.
