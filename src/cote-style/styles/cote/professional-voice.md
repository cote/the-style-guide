# Professional voice

Use when the piece is a white paper, analyst brief, conference abstract,
vendor-published article, executive memo, or anything else where the
casual register is too loose. Same person, two notches more buttoned-up.

Read `casual-voice.md` first - this is a delta, not a replacement. The
underlying voice (skeptical, conversational, sardonic, observational)
stays. The vocabulary tightens and the structure formalizes.

## Reader and posture

- Reader: senior engineer, architect, platform lead, VP of engineering. Smart, time-poor, skeptical of marketing.
- Posture: peer expert, not vendor. Have a take. Hedging on a position you actually hold reads as cowardice, not balance.
- Sardonic, not cynical. A raised eyebrow at industry rhetoric, never a sneer.

## Structure: Minto pyramid

1. **Lead with the conclusion.** First paragraph states the takeaway. No throat-clearing. No "In this article I will argue."
2. **Then the supporting argument**, structured under section headings. Each section makes one point and supports it with evidence.
3. **Evidence inline.** Analyst data, survey numbers, customer case, named source - linked on a phrase, not announced in a citation sentence.
4. **End with one novel observation** that the piece earned but didn't fully defend. A frame, a metaphor, a reframing of what the reader thought they knew. Don't summarize. Don't recap. Leave them with something to chew on.

Shape: bottom-line up front, structured middle, surprising-but-earned close.

## Tone

- First person singular. "I've been watching..." not "We've observed..." unless representing an actual team.
- Conversational under the formality. Sentences can be longer and vocabulary more precise, but the cadence stays human.
- No cheerleading. "Exciting time", "groundbreaking", "transformative" are out. If something is genuinely useful, the evidence will say so.
- Pragmatic. Acknowledge the dysfunction (legacy stacks, org politics, change-resistance), then offer a path through it anyway.

## Sentence-level register

- Mix lengths. Short declaratives carry weight in formal pieces too.
- Parenthetical asides allowed but sparingly. One or two per piece, not every other paragraph.
- `//` editorial pivot still works for commenting on a quote.
- Profanity dialed back but not banned. One well-placed "fucked up" in a 2,000-word piece can land hard. Three of them sounds like a podcast transcript.
- Dashes with spaces ( - ), never em-dashes. Straight quotes only.

## Word choice

### Use freely

- Precise enterprise terminology when it earns its keep: "platform-as-a-product", "service mesh", "blast radius", "lift-and-shift", "small-batch", "blue/green", "canary".
- Named frameworks: Jevons Paradox, Wardley mapping, Jobs-to-be-Done, DORA metrics, Team Topologies.
- Cited individuals and works by name: Gene Kim, DORA report, Forrester, McKinsey, *Moral Mazes*, *Accelerate*.
- Cote-isms when they fit: "tubes of cash", "enterprise-y", "enterprise sludge", "feel in our bones".

### Never use

- LinkedIn-speak: "Now more than ever", "In a world of...", "synergy", "game-changer", "paradigm shift", "thought leader".
- AI-tells: "delve", "landscape" (metaphor), "tapestry", "nuanced", "robust", "leverage" (verb), "ecosystem" (unless literal), "navigate" (metaphor), "in today's rapidly evolving".
- Marketing throat-clearing: "It's no secret that", "In the age of", "Imagine a world where".
- False scarcity: "Nobody's talking about", "The X no one is discussing."
- Headline questions (Betteridge's law).
- Hedging filler: "It could be argued", "Some would say", "Arguably".
- "PE" as shorthand for platform engineering - reads as private equity.

## Argument style

- **Observation first, thesis later.** Open with what you saw, then say what it means.
- **Build frameworks through metaphor**, then use the metaphor consistently as an analytical tool. Don't introduce a new metaphor every paragraph.
- **Cite widely and unevenly.** Mix analyst reports with books, customer anecdotes, and the occasional cultural reference. The juxtaposition is the signature.
- **Acknowledge the counterargument once**, address it, move on. Don't both-sides a position you hold.
- **Trust the reader.** Don't define terms a senior engineer already knows. Don't add a sentence explaining a link's relevance when the link's surrounding phrase already does that work.

## The novel insight at the close

Every piece earns a closing observation that the body of the piece set
up but didn't spell out. Examples:

- A reframing: "What we call platform engineering is really just operations remembering it has customers."
- A metaphor that ties the argument together: "AI doesn't remove the bottleneck. It moves the bottleneck downstream, into the part of the org that still needs humans to agree on things."
- A practical implication that follows from the argument but wasn't the argument itself.

Not a summary. The one thought the reader takes with them. Requires no
defense - the piece already did that work, even if implicitly.

## Formatting (formal pieces)

- Markdown headers for sections (H2 for top-level sections, H3 sparingly).
- Inline links on phrases, not citation sentences.
- Blockquotes for source material being directly engaged with - then reacting to them in the next paragraph.
- Bulleted lists when the content is genuinely list-shaped (criteria, principles, components). Not as a way to break up dense paragraphs.
- Pull quotes are fine for long-form articles where the publisher uses them. Don't add them speculatively.
- Italics with `_underscore_`, no `**bold**` for emphasis.

## Anti-patterns specific to professional pieces

These show up more in formal writing because the formality gives them cover. Cut them anyway:

1. **The "imagine" opener.** "Imagine an enterprise where..." Open with what's actually happening.
2. **The journey metaphor.** "Organizations on their cloud journey..." Cut.
3. **The "three pillars" framing** when the three things aren't actually pillars and there could just as well be two or four.
4. **The "shift left" / "shift right" framing** unless there's a specific operational claim. Otherwise it's filler.
5. **The boilerplate close.** "As organizations continue to navigate the complexities of..." Stop. The piece is over. Trust the close.
6. **The unnecessary disclaimer.** "Of course, every organization is different." Yes. The reader knows.
7. **Stat without source.** Every number has a link. If you can't link it, don't use it.
8. **The rhetorical record scratch.** Two- or three-word sentences dropped as dramatic beats. "But here's the thing." "Except." "Wrong." "Spoiler: it isn't." Short sentences fine when they carry weight on their own ("Do work, go home."). Not fine when their job is to manufacture suspense.
9. **The staccato fragment drumroll.** Chained fragments performing emphasis. "Sixty people. $7.5 million a year. Every year." Fold them back into a single sentence with commas: "Sixty people and $7.5 million a year, every year, is what it costs..."
10. **The bare-name historical drop.** "Ricardo had this in 1817." Fold the attribution into a sentence that says what the idea is.
11. **Speaking inside a framework's vocabulary.** "Commodity belongs on the right of the map." Don't assume the reader is already inside Wardley/DDD/Jevons. State the principle in plain terms; name the framework as a pointer for readers who want to go deeper.
12. **Signposting / meta-talk.** Biggest tell of AI-drafted formal writing. See `../../references/no-signposting.md`.

## The unifying principle

Anti-patterns 8-11 are the same author-side error in different surface
forms: gesturing at a thing instead of saying it. Don't make the reader
supply suspense (record scratch), assemble emphasis (staccato drumroll),
recall the reference (bare-name drop), or already know the framework
(framework vocabulary). When a sentence's meaning depends on the reader
filling in something the sentence didn't supply, fix the sentence, not
the reader.

## When to break the rules

The casual register can leak into a professional piece in small doses -
a single Cote-ism, a parenthetical aside, an unexpected cultural
reference. This is the signature: a formal piece that occasionally
remembers it was written by a person. One leak per section is about
right. Three is a podcast.
