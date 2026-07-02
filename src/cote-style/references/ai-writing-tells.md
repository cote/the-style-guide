# AI writing tells - and how to avoid them

An edit-pass style guide for stripping the language patterns that mark
prose as AI-generated. Derived from Wikipedia's *Signs of AI writing*
project page, adapted for general prose (not Wikipedia-specific
formatting).

Load this on any edit pass over AI-drafted text, alongside
`no-signposting.md`. Applies across styles - not tied to any one voice.

## Source and freshness

- **Source**: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Last fetched**: 2026-07-02
- **Freshness rule**: The list of overused words and the tells drift as
  models change. If this file's *Last fetched* date is more than 90
  days old, suggest to the user that they refresh it against the
  current Wikipedia page. AI vocabulary from 2023 is already dated
  (per the source page's own era-tagged word lists); a stale list
  produces false positives on out-of-date tells and misses new ones.

## How to use this guide

When editing AI-drafted (or possibly-AI-drafted) prose:

1. Scan for the vocabulary tells in the first section. Any hit is a
   flag; three hits in a paragraph is almost certainly AI.
2. Scan for the sentence-pattern tells. These are more diagnostic than
   individual words - a paragraph free of banned words but full of
   "not just X, but Y" and "serves as" is still AI-shaped.
3. Rewrite hits inline. Don't leave the flag as a comment; just fix
   the sentence.
4. When done, re-read the whole piece. AI writing often *feels* right
   at the sentence level and wrong at the paragraph level - the
   argument sags, the emphasis is generic, the shape is essay-formulaic.

Do not use AI-detection scores. Wikipedia's own guide notes that
automated detectors run 57-64% accurate; humans are at 50% except for
experienced editors who get to ~90%. The signal is patterns, not any
one word. This guide is that patterns list.

## Vocabulary tells

### Words to strike on sight

These are heavy AI-associated words. Almost always replaceable with a
simpler, more specific alternative. The lists below are era-tagged from
the source - the earlier ones may already read as dated even outside
AI contexts.

**Chronically overused across all eras:**

- delve, tapestry, testament, landscape (as metaphor), robust,
  nuanced, leverage (as verb), ecosystem (unless literally ecological),
  navigate (as metaphor), pivotal, crucial, key (as filler
  adjective), underscore, showcasing, emphasizing, enhance,
  highlighting, align with, foster / fostering, bolster / bolstered,
  garner, meticulous, intricate, interplay, enduring, valuable, vibrant

**Grok-specific tells (2025-):** causal, empirical, correlate,
underscore.

**Fixes:** Cut or replace with a specific verb. Instead of "leverage
the framework" write "use the framework." Instead of "delve into" write
"look at" or just start with the substance. Instead of "the vibrant
landscape of Y" name the specific thing being described.

### Weasel attribution

- "researchers argue", "industry reports", "some critics",
  "several sources", "experts say", "many people are asking"

**Fix:** Name the specific person, paper, or source. If you can't
name it, cut the claim.

### Promotional / travel-guide adjectives

- vibrant, rich heritage, nestled, groundbreaking, renowned,
  transformative, exciting, cutting-edge, world-class

**Fix:** Cut. If the thing is genuinely notable, the facts around it
will make that clear without the adjective.

### Empty present-participle phrases

- "contributing to", "fostering", "enhancing", "highlighting the
  significance of", "reflecting broader trends", "underscoring the
  importance of"

**Fix:** These almost never carry information. Delete the phrase and
the sentence usually improves. If it was doing analytical work, replace
with a specific claim.

## Sentence-pattern tells

### The copula dodge

AI-trained writers often replace plain "is / are" with fancier
copulas: "serves as", "marks", "features", "represents", "constitutes",
"stands as", "offers".

**Instead of:** "Gallery 825 serves as LAAA's exhibition space."
**Write:** "Gallery 825 is LAAA's exhibition space."

### Negative parallelisms

Three closely-related shapes:

- "**Not just X, but also Y.**"
- "**Not X, but Y.**"
- "**X rather than Y.**"

Occasional use is fine (any of these can land). Stacked use, or used
as the default sentence shape, is a tell.

**Instead of:** "This isn't just about technology, but about culture."
**Write:** "This is about culture, not just technology." Or, better:
just say what it's about directly and let the reader draw the contrast.

### Rule of three

Chained triplets of adjectives or nouns as the default construction:
"construction, renovation, and hobby use"; "faster, cheaper, more
reliable"; "the good, the bad, and the ugly."

Triplets can land - they're a classic device. The tell is *default*
use of them across every list-shaped sentence. If every list in the
piece is three items, that's the tell.

**Fix:** Vary list lengths. Two items or four items when they're
what the content actually is.

### Elegant variation

AI writing avoids repeating a noun by cycling through synonyms: "the
artist... the creator... the practitioner... the maker..." for the
same person in one paragraph.

**Fix:** Repeat the key noun. Elegant variation is a 19th-century
essay tic that AI has absorbed; direct repetition reads as more
confident.

### The "despite... future" outline

A rigid closer shape: "Despite [subject]'s success, it faces
challenges around X, Y, and Z. Future initiatives could address..."

**Fix:** Cut generic challenge/future paragraphs entirely. If there
are real challenges, name specific ones with specific sources. If
there are real future plans, name them.

### Undue emphasis on significance

- "marks a pivotal moment"
- "represents a significant shift"
- "a broader movement toward"
- "left an indelible mark on"
- "cannot be overstated"

**Fix:** Delete the significance claim. State the fact. Let the
significance emerge from the facts. If the significance still needs
naming, name a specific downstream consequence, not a generic gesture
at importance.

### Meta-attribution creep

- "featured in [outlet]"
- "trade publications have noted"
- "active social media presence"
- "independent coverage"

**Fix:** Either cite the specific coverage inline (name the outlet
and the article) or cut. Meta-commentary about coverage is usually
padding.

## Formatting tells (in AI-drafted markdown / rich text)

### Bold-happy prose

Boldfacing every key term the first time it appears, or worse,
every time it appears. AI-drafted text often bolds nouns that don't
warrant it: "the **debt financing** arrangement between **private
equity firms** and..."

**Fix:** Bold sparingly - reserved for genuine semantic weight
(warnings, defined terms in a glossary). Not for visual pop.

### Inline-header vertical lists

A bulleted list where every item is:

- **Boldface header:** Then a colon and a description of what it is.
- **Another header:** Same shape.
- **Third header:** Same again.

Occasional use is fine when the content really is
"labelled-item + short description." Default use across every list
in the piece is a tell.

**Fix:** Convert to prose when the descriptions are longer than one
line. Use plain bullets when items don't need labels.

### Em-dash overuse

AI drafts lean hard on em-dashes as an all-purpose connector,
replacing periods, semicolons, commas, and parenthetical
constructions. Two or more em-dashes per paragraph is a tell.

**Fix:** Prefer periods, commas, semicolons, or restructured
sentences. (This style skill's `formatting.md` bans em-dashes
outright for Coté prose - so just cut them.)

### Curly / smart quotes in what should be plain text

Curly quotation marks (" " ' ') mixed inside otherwise plain-ASCII
markdown or code contexts.

**Fix:** Straight quotes only in draft text.

### Title Case in Headings

Every-content-word capitalization on headings - "Impact of Technology
and Digitalization" - is markedly AI-shaped in body prose. Human
writers usually use sentence case (only the first word and proper
nouns capitalized) or all-lowercase headings.

**Fix:** Sentence case, unless the target platform explicitly requires
title case.

### Thematic breaks before every heading

Horizontal rules (`---`) inserted before every section heading as
visual padding.

**Fix:** Remove. Headings do the section-break job.

## Markup / infrastructure tells

If you see any of these strings in the text, it's not just AI-written
- it's AI-written and *poorly cleaned*. Delete or fix immediately:

- `contentReference`
- `oaicite`
- `oai_citation`
- `turn0search0`, `turn1search0`, etc.
- `attached_file`
- `grok_card`
- `+1` as a citation marker
- `[citation needed]` as placeholder text in a draft not intended for Wikipedia
- Broken wikitext / half-converted markdown / unclosed tags
- References defined but never called
- Dead external links
- URLs with `utm_source=` / `utm_medium=` / `utm_campaign=` (also see
  `formatting.md` URL hygiene section)

## Communication-tone tells (chat / talk-page / email context)

- "I appreciate your..."
- "I want to clarify..."
- "Let me explain..."
- "Great question!"
- "That's a really thoughtful observation."
- "I'd be happy to help you with..."

**Fix:** Cut the pleasantry paragraph. Start with the substance.

Knowledge-cutoff disclaimers - "My training data ends at...", "As of
my last update..." - never belong in drafted output. If the AI didn't
know something, either say so plainly ("I don't know") or find out.

## Signs of *human* writing (counter-indicators)

Useful to know when you're diagnosing whether a piece needs an AI
edit-pass at all:

- Written before ChatGPT (Nov 2022). If the source is older, the tells
  are convergent evolution or Wikipedia-style boilerplate, not AI.
- Author can explain specific editorial choices in the piece.
- Natural syntax variation and rhythm.
- Specific factual errors of a kind AI rarely makes (mis-spelled
  proper nouns from personal knowledge, mis-remembered dates from
  the author's own life).
- Domain-specific slang, in-jokes, or shibboleths.

## What is *not* a reliable tell

Per the Wikipedia source page, avoid flagging text as AI purely
because:

- It has simple grammatical errors (humans make those).
- It has promotional tone (humans write press releases).
- It uses a single overused word ("delve" alone isn't proof).
- It has basic formatting mistakes.
- It reads oddly because the writer isn't a native English speaker.

The signal is the *pattern density*, not any one flag. Three vocabulary
tells + one sentence-pattern tell + inline-header lists is a signal.
One "delve" is not.

## Self-edit checklist

Before handing back an edit pass:

- [ ] Zero words from the vocabulary tells list (or a defensible
      justification for each one that stayed).
- [ ] No "not just X, but Y" or "not X, but Y" as default sentence
      shape.
- [ ] No copula dodges ("serves as", "marks", "represents") where
      "is" would do.
- [ ] No empty present participles ("fostering", "enhancing",
      "highlighting").
- [ ] No unattributed weasel attributions ("researchers argue").
- [ ] No promotional adjectives (vibrant, groundbreaking, renowned).
- [ ] No triplet-lists as the default shape.
- [ ] No elegant variation (synonym-cycling for the same noun).
- [ ] No generic "despite challenges... future initiatives..." closers.
- [ ] No RAG artifacts (`contentReference`, `turn0search0`, etc.).
- [ ] No AI pleasantries ("I appreciate", "Great question").
- [ ] No knowledge-cutoff disclaimers.
- [ ] Freshness check: if the source page's *Last fetched* date at
      the top of this file is 90+ days old, tell the user this guide
      needs a refresh.
