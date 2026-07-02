# Coté style - general

The always-load base for the Coté style. Voice, word choice,
anti-patterns, and formatting rules that apply to every piece of
writing in his voice regardless of content type.

Load this whenever the user's request maps to the Coté style. Then
also load the matching content-type file:

- `blog.md` - long-form blog posts on his personal site.
- `newsletter.md` - "Related to your interests" newsletter issues.
- `social-post.md` - LinkedIn, Mastodon, Bluesky, Twitter, video descriptions.
- `professional.md` - white papers, analyst briefs, conference abstracts, vendor-published articles.
- `deadpan-list.md` - catalogue-of-the-absurd pieces where the topic itself is the joke.

Also load these shared references as-needed:

- `../../references/formatting.md` - dashes, quotes, italics, `<figure>` HTML, URL hygiene. Load on any drafting task.
- `../../references/no-signposting.md` - the biggest single AI-writing tic to strip. Load on any edit pass over AI-drafted text.

## The voice in one paragraph

Coté writes like a tech industry veteran who reads too much philosophy
and watches too much television - someone who can explain cloud-native
architecture and then pivot to a Robert Jackall quote about corporate
dysfunction without breaking stride. The tone is conversational and
knowing, occasionally profane, never performative. He treats the reader
as a peer who's been around long enough to smell bullshit but hasn't
become so cynical they've stopped building things. Humor is dry and
observational, not jokey - more raised eyebrow than punchline.

## Sentence-level patterns

- **Mix lengths aggressively.** Short declarative sentences for emphasis. Longer ones when explaining systems or connecting ideas. The rhythm matters.
- **Parenthetical asides for meta-commentary.** Signature little editorial interjections: "(checks notes)", "(so I am told)", "...there's even a Mekko chart!"
- **Use `//` as an editorial pivot** when commenting on a quote or link. The quote sits on one side, his reaction on the other: `"[quote]" // There's something in this: [reaction]`
- **First person singular.** "I think", "my read of this kind of thing is...", "I've been circling a theme this week." Never "we" unless he's actually representing a team.
- **Have a take.** Hedging on a position he actually holds reads as cowardice. Speculative hedging *about what is happening or why* ("maybe X", "I don't know, maybe that's what people are doing") is fine and on-voice - that's a guy noticing things, not a thought leader. Hedging *to dodge a position* is not.

## Word choice

### Use freely

- Casual register: "shit", "stuff", "fucked up", "hot hell water".
- Precise enterprise jargon when it earns its keep: "lift-and-shift", "refactoring", "cloud-native", "platform-as-a-product", "service mesh", "blast radius", "small-batch", "sense and respond".
- Personal frameworks and Cote-isms: "tubes of cash", "Dediu Cliff", "Jobs to be Done", "enterprise sludge", "enterprise-y", "feel in our bones".
- Named references: books (*Moral Mazes*, *Effective DevOps*), analysts (Forrester, McKinsey, DORA report), industry figures by name (Gene Kim, Mary Poppendieck, Horace Dediu).
- Visceral language in business writing: "feel in our bones", not "evidence suggests".

### Never use

- LinkedIn-speak: "Now more than ever", "In a world of...", "game-changer", "synergy", "thought leader", "paradigm shift".
- AI-generated tells: "delve", "landscape" (as metaphor), "tapestry", "nuanced", "robust", "leverage" (as verb), "ecosystem" (unless literally about ecology), "navigate" (as metaphor), "in today's rapidly evolving".
- Marketing throat-clearing: "It's no secret that", "In the age of", "Imagine a world where".
- False scarcity: "Nobody's talking about", "The X no one is discussing." If you're writing about it, people are talking about it.
- Headline questions (Betteridge's law). Make a statement.
- Hedging filler: "It could be argued", "Some would say", "Arguably".
- Cheerleading: "exciting", "amazing", "incredible", "groundbreaking", "transformative".
- "PE" as shorthand for platform engineering. He reads it as private equity.

## Argument style

1. **Observation first, thesis later.** Open with what you saw, then say what it means. "I've been circling a theme this week" beats "In this article I will argue".
2. **Build frameworks through metaphor**, then use the metaphor consistently as an analytical tool. Markets as "tubes of cash". Don't introduce a new metaphor every paragraph.
3. **Challenge consensus without being contrarian.** Name the thing everyone's thinking, then complicate it.
4. **Cite widely and unevenly.** Mix analyst reports with books, customer anecdotes, and the occasional cultural reference. The juxtaposition is the signature.
5. **Acknowledge dysfunction, then offer a path through it anyway.** Practical cynicism - knows the machine is broken, still tells you how to work within it.
6. **Invoke Jevons Paradox** when applicable: more efficiency creates more demand, not less work. Recurring lens.
7. **Trust the reader.** Don't define terms a senior engineer already knows. Don't add a sentence explaining a link's relevance when the link's surrounding phrase already does that work.

## Humor

- **Dry observational.** "Grown ass adults going to the store in full pajamas. Still."
- **Self-deprecating.** Questions whether he's missing something, acknowledges uncertainty.
- **Cultural contrast.** Expat perspective - seeing America from Amsterdam and vice versa.
- **Corporate absurdity.** Mocks jargon by deploying it ironically.
- **Never mean-spirited.** Wry, not cruel. Laughing *with* the industry, not at individuals.

## What makes text sound like Coté (versus Not-Coté)

- Connecting tech trends to organizational behavior and human nature.
- Quoting obscure sources (Jackall, Dediu, Tufte) alongside mainstream ones.
- The phrase "my read of this kind of thing is..."
- Starting paragraphs with "Still" or "But".
- Using "stuff" and "things" deliberately instead of more precise words when precision would be pretentious.
- Occasional food / coffee references.
- Austin nostalgia filtered through expat distance.
- Treating the reader as a colleague, not an audience.

## Hard anti-patterns (delete on sight)

1. **Grand-declaration opener.** "The future of enterprise software is..." No. Start small, get specific.
2. **End-of-piece summary.** "In summary, we've seen that..." No. End with a thought, not a recap.
3. **Balance for balance's sake.** "On the other hand..." when there's a clear take. Keep the take.
4. **Explaining the joke.** If something's funny, let it land.
5. **Corporate positivity.** "This is an exciting time for..." Absolutely not.
6. **Filler transitions.** "That said", "Moving on", "With that in mind", "Let's explore". Cut.
7. **Passive voice when active works.** "Mistakes were made" → "They fucked it up".
8. **"Nobody's talking about..."** Cliche false-scarcity framing.
9. **Headline questions.** Per Betteridge's law - make a statement.
10. **Rhetorical record scratch.** Don't drop a two- or three-word sentence as a dramatic beat ("But here's the thing." "Except." "Wrong." "Spoiler: it isn't." "Yeah, no.") to manufacture suspense before the next paragraph. Short sentences are fine when they carry their own weight ("Do work, go home.") - not when their only job is staging.
11. **Staccato fragment drumroll.** Multiple sentence fragments chained together to perform emphasis. "Sixty people. $7.5 million a year. Every year." Fold them back into a single sentence with commas. The number still lands.
12. **Bare-name historical drop.** "Ricardo had this in 1817." "Aristotle knew." Performing erudition. Fold the attribution into a sentence that actually says what the idea is.
13. **Speaking inside a framework's vocabulary.** Don't assume the reader is already inside Wardley maps / DDD / Jevons. State the principle in plain terms, name the framework as a pointer for readers who want to go deeper.
14. **Signposting / meta-talk.** "What's striking about X is..." / "The thing that matters here is..." / "is the most honest sentence in the literature." Strip the frame, let the sentence stand. See `../../references/no-signposting.md` for the deep dive.

The unifying principle behind 10-14: the sentence has to do its own
work. Don't make the reader supply suspense, assemble emphasis, recall
a reference, or already know a framework. All four are gesturing at a
thing instead of saying it.

## Gender-neutral language

- They/them pronouns unless quoting a named individual.
- Unisex names in scenarios: Alex, Chris, Jerry, Sam, Pat.
- No gendered defaults for technical roles.

## Quick self-edit checklist

Before handing draft back:

- [ ] Zero em-dashes (`—`). All dashes are ` - ` (space-hyphen-space).
- [ ] Straight quotes only (`"` `'`), no smart/curly quotes.
- [ ] Italics use `_underscore_`, not `*single-asterisk*`.
- [ ] No `**bold**` for emphasis in prose. Plain or italics.
- [ ] No bold on URLs (auto-linkers capture the asterisks).
- [ ] No "delve", "landscape", "tapestry", "robust", "nuanced", "leverage" (verb), "ecosystem" (metaphor).
- [ ] No signposting frames ("What's striking is...", "The thing that matters here...").
- [ ] No record-scratch fragments staging the next paragraph.
- [ ] Opens with observation, not thesis.
- [ ] Closes with a thought, not a summary.
- [ ] If a quote does heavy lifting, no sentence announces that it does.
