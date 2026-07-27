# AI detector

A generic, voice-neutral detection + edit-pass style. Load this when a
draft needs its AI-generated tells found and stripped out - regardless
of what positive voice the draft is supposed to end up in.

The name is "detector" because the primary job is spotting AI patterns
in prose. Fixes are provided for each pattern, so the same file also
works as an edit pass. Unlike a prose-voice style, this one produces no
new voice on its own. Pair it with whatever positive style is actually
in play (Coté, LinkedIn, Tyler Cowen questions, the user's own,
whatever).

## When to load

- The user asks to "detect AI", "strip AI", "de-AI this", "remove the
  AI tells", "make it not read like ChatGPT / Claude / an LLM".
- Any edit pass over text that was drafted, ghostwritten, or
  substantially rewritten by a model - especially if the model wasn't
  given a strong style anchor to begin with.
- As a companion pass at the end of any generation task. The positive
  style produces the draft; this style scans for AI fingerprints
  before handing back.

## Where the content came from

This file collects the anti-AI content that's scattered across the
shipped styles into one includable list. Nothing new is invented here.
Originals stay in place; this is the shared read.

- `styles/cote/general.md` (never-use word list) → §Vocabulary tells.
- `styles/cote/professional-voice.md` (never-use word list) →
  §Vocabulary tells.
- `styles/linkedin/no-linkedin-talk.md` (Mollick's short-mute list,
  self-important punchline closers) → §Sentence-pattern tells and
  §Closer tells.
- `references/no-signposting.md` → §Signposting.
- `references/ai-writing-tells.md` → the deeper, Wikipedia-derived
  catalog. Load that alongside this one when the piece is heavily
  AI-shaped and you want the full pattern list.

If any of the source files change, this file should be re-synced. The
list of overused words drifts as models drift.

## Vocabulary tells

Words to strike on sight in AI-drafted prose. Each one is almost
always replaceable with a simpler, more specific alternative - or
just deletable.

**Chronically overused across most models:**

- delve
- landscape (as metaphor)
- tapestry
- nuanced
- robust
- leverage (as verb)
- ecosystem (unless literally about ecology)
- navigate (as metaphor)
- "in today's rapidly evolving..."

**LinkedIn-adjacent AI vocabulary that also shows up outside
LinkedIn:**

- journey (except literal travel)
- passionate, thrilled, humbled, blessed
- game-changer, disruptor, thought leader
- synergy, circle back, deep dive (as noun)
- rockstar, ninja, guru (about people)
- value-add, learnings
- "in today's fast-paced world", "now more than ever"

**Fixes.** Cut or replace with a specific verb / noun. "Leverage the
framework" → "use the framework." "Delve into" → "look at", or just
start with the substance. "The vibrant landscape of Y" → name the
specific thing being described.

## Sentence-pattern tells

These are more diagnostic than any single word. A paragraph free of
banned words but built from these shapes is still AI-shaped.

### Mollick's short-mute list

Phrases that mark text as poorly-prompted AI:

- "doing the heavy lifting"
- "the real question is"
- "here's the thing nobody is talking about"
- "that's the real story"
- "what most people miss"
- "this is where it gets interesting"
- "it's not about X, it's about Y"

The last one is the most over-used AI sentence shape - see also the
"not X, but Y" negative-parallelism entry in
`references/ai-writing-tells.md`. Rewrite as a direct claim.

### Closer tells (self-important punchline closers)

Sentences at the end of a piece whose job is to elevate the story
being told - a vague-profound frame that says "and this one, right
here, is the one that matters" without saying what makes it matter.

- "It's the one worth telling."
- "That's the story worth telling."
- "It's the version that matters."
- "That's the moment worth remembering."
- "That's the part I keep coming back to."
- "That's the one that stayed with me."
- "It's the only [X] that matters."
- "That's the real lesson."
- "That's what I'll remember."

**Fix.** If the story is worth telling, telling it is the argument.
Don't also *tell the reader it's worth telling*. Cut the closer. If
something specific about why it stuck is load-bearing, say that
specific thing instead ("I've thought about the pause before she
answered maybe fifty times since"), not the meta-claim.

### Rationalist / LessWrong jargon

A distinct AI dialect that comes from the 2010s rationalist blogosphere
(LessWrong, Slate Star Codex, HN comment threads and their downstream).
Overrepresented in most model training corpora, so it comes out
whenever a model is asked to "think out loud." Compression that got
turned into vibes.

**Hard bans - swap for plain claims:**

- Structural / labor metaphors for importance: "load-bearing", "doing
  the work", "doing the heavy lifting", "carrying the argument",
  "carrying the sentence". Also "the smoking gun" when used the same
  way. All lazy synonyms for "important" that borrow gravitas from
  physical labor while staying vague about what the labor is.
  **Fix:** Say what the thing does and what breaks if it's wrong. "This
  assumption is doing a lot of work" → "If this assumption is wrong,
  the cost model is off by 10x."
- The "priors" family: "my priors", "my priors say", "updated my
  priors", "updating toward", "updating away from". Spec-sheet talk
  for the self. **Fix:** "assumptions", "expected", "changed my mind",
  "I was wrong about X".
- "Steelman" and "strawman" as verbs or nouns. Presents as intellectual
  charity; usually a puppet show. **Fix:** Describe the argument as
  strong or weak and engage with it directly. "Their strongest
  argument is X, and here's why it still fails."
- "Chesterton's fence" as a reference. **Fix:** Skip Chester. Go find
  out why the thing exists, then say whether it's still needed and why.

**Use sparingly - only when the technical meaning is genuinely
load-bearing (yes, the irony):**

- "orthogonal" (usually just means *unrelated*)
- "non-trivial" (usually just means *hard*)
- "in the limit" (usually means *if this went on forever, which
  nothing does*)
- "epistemic", "epistemic status"
- "object-level" / "meta-level"
- "motte-and-bailey"
- "galaxy-brained"
- "coordination problem"
- "Moloch"

**General rule.** When tempted by any of these, replace the phrase
with a concrete claim about what the thing does and what breaks if
it's wrong. The jargon survives because it lets a sentence *sound*
finished before it has actually said anything. Demand the concrete
claim and the tic has nowhere to hide.

### Signposting / meta-talk

The single biggest tell of AI-drafted text. Sentences whose job is to
announce what's coming instead of just saying it:

- "What's striking about X is..."
- "The thing that matters here is..."
- "is the most honest sentence in the literature."
- "It's worth noting that..."
- "One important thing to consider is..."

**Fix.** Strip the frame, let the sentence stand. Deep dive lives in
`references/no-signposting.md`.

## Automated scan

Most of the phrase lists in this file (plus Simon Willison's 12
regex patterns from
https://github.com/simonw/tools/blob/main/llm-cliche-highlighter.html)
are bundled into `scripts/cliche-check.py` at the skill root. Run it
on a draft before the human read-through - it won't catch everything
(taste and shape are still on you), but it catches every literal
phrase in the lists above.

    scripts/cliche-check.py draft.md
    cat draft.md | scripts/cliche-check.py
    scripts/cliche-check.py --category rationalist-hard draft.md
    scripts/cliche-check.py --list-categories

Exits 0 clean, 1 on hits. Output is grouped by category with a short
context window and line number per hit. When the source phrase lists
in this file or in the shipped styles change, update the script's
lists too - they're a mirror, not the source of truth.

## Sources beyond the shipped styles

Curated background reading and evidence base. The vocabulary and
patterns above draw on these; consult them directly when the built-in
lists feel incomplete or when a piece needs harder citations than
"Coté banned this."

The URLs below are the load-bearing links. The two sources that
change often are the **Kobak CSV**
(https://raw.githubusercontent.com/berenslab/llm-excess-vocab/main/results/excess_words.csv)
and the **AlpinDale YAMLs**
(https://raw.githubusercontent.com/AlpinDale/gptslop/main/gptslop.yaml
and .../claudeslop.yaml). Refresh those when the scanner's vocab
list feels stale; the arXiv papers won't change.

### Empirical corpus studies

- **Kobak, González-Márquez, Horváth & Lause (2025).** *Delving into
  LLM-assisted writing in biomedical publications through excess
  vocabulary.* Science Advances 11.
  https://doi.org/10.1126/sciadv.adt3813. Preprint arXiv:2406.07016.
  Public word CSV: https://github.com/berenslab/llm-excess-vocab.
  ~14M PubMed abstracts, 2010-2024. The citation floor for
  post-ChatGPT vocabulary shift. Top excess words: *delves,
  showcasing, underscores, pivotal, intricate, meticulously, realm,
  aligns, underpins, bolstering, garnered, burgeoning, commendable,
  compelling, adept, akin, amidst, notably, additionally, robust*.
- **Liang et al. (Zou lab, Stanford, 2024).** *Monitoring
  AI-Modified Content at Scale.* ICML 2024. arXiv:2403.07183. Plus
  *Mapping the Increasing Use of LLMs in Scientific Papers.*
  arXiv:2404.01268. Population-level MLE over ~49k peer reviews and
  ~950k papers. Highest-lift adjectives: *commendable* (~10x),
  *meticulous* (~35x), *intricate* (~11x). Canonical four-word
  fingerprint: *realm, intricate, showcasing, pivotal*.
- **Geng & Trotta (2024).** *Is ChatGPT Transforming Academics'
  Writing Style?* arXiv:2404.08627. Physics-side replication that
  confirms Kobak's list is not biomedicine-specific.
- **Gray (2024).** *ChatGPT "contamination": estimating the
  prevalence of LLMs in the scholarly literature.* arXiv:2403.16887
  (UCL Library Services). Origin of the "meticulously commendable"
  meme; ~60k 2023 papers estimated LLM-assisted.

### Curated leak-phrase and tortured-phrase catalogs

- **Glynn (2024) — Academ-AI.** *Documenting the undisclosed use of
  generative AI in academic publishing.* arXiv:2411.15218. Live
  tracker: https://academ-ai.info. Verbatim leak phrases to scan
  for: *"Certainly, here is/are…"*, *"As an AI language model, I…"*,
  *"As of my last knowledge update…"*, *"I don't have access to
  real-time…"*, *"I'm sorry, but I cannot…"*, *"Regenerate
  response."*
- **Cabanac, Labbé & Magazinov.** *Tortured phrases: A dubious
  writing style emerging in science.* arXiv:2107.06751 (2021),
  ongoing PubPeer + Nature News coverage 2023-2024. Powers the
  Problematic Paper Screener. Tortured examples: "counterfeit
  consciousness" (AI), "haze figuring" (cloud computing), "profound
  neural organization" (deep neural network).
- **AlpinDale — gptslop / claudeslop.**
  https://github.com/AlpinDale/gptslop. Community YAML dictionary
  separating GPT- vs Claude-family fingerprints; upstream to
  SLOP_Detector and antislop-sampler. Machine-readable, actively
  maintained.

### Editorial / linguistic essays

- **Colin Gorrie.** *Why ChatGPT writes like that.* Dead Language
  Society (Substack), 9 July 2025.
  https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai.
  Linguist rhetorical analysis. Structural tells: excessive
  em-dashes, compulsive parallelism, tricolon (rule of three),
  ascending tricolons ordered by syllable count, triple-adjective
  stacks ("efficient, reliable, and effective"), explicit "it's not
  X; it's Y" negation-contrasts.
- **Matthew Vollmer.** *A Field Guide to AI Tells.* Substack, April
  2026.
  https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself.
  Creative-writing professor synthesizing Kobak's data with editor
  practice. Names the prestige-metaphor cluster (*tapestry, realm,
  mosaic, ecosystem, symphony, labyrinth, beacon, cornerstone,
  bedrock, testament, kaleidoscope, odyssey*) and the inflated-verb
  cluster (*leverage, utilize, harness, streamline, facilitate,
  optimize, empower, navigate, illuminate, bolster, foster, elevate,
  unpack*).
- **Ruben Hassid.** *Ban.* How to AI (Substack), 9 November 2025.
  https://ruben.substack.com/p/delve. Marketing-copy audience;
  Mollick-adjacent ban list of 73 words plus syntactic patterns:
  *"In a world where…"*, *"Stop doing X. Start doing Y."*, *"It's
  never been easier/harder…"*, *"If you're not doing X, you're
  already behind."*

### Cross-source consensus (highest-signal words for a scanner)

Words appearing in three or more of the sources above:

> *delve/delves/delving, intricate, meticulous/meticulously,
> commendable, pivotal, realm, tapestry, landscape, showcasing,
> underscore, notable/notably, comprehensive, robust, seamless,
> testament, leverage, foster, elevate, harness*, plus the phrases
> *"it's important to note"*, *"in today's / ever-evolving
> landscape"*, *"not X, it's Y"*, and default tricolon lists.

The `scripts/cliche-check.py` vocabulary list is a subset of this
consensus. If you want more coverage, pull additional entries from
the Kobak CSV or the Vollmer prestige-metaphor and inflated-verb
clusters.

## Self-edit checklist

Before handing an edit back:

- [ ] Zero words from the vocabulary tells list (or a defensible
      justification for each one that stayed).
- [ ] No "not X, but Y" / "it's not about X, it's about Y" as sentence
      shape.
- [ ] No phrases from Mollick's short-mute list.
- [ ] No self-important punchline closer ("it's the one worth
      telling," "that's the version that matters," etc.).
- [ ] No signposting frames ("What's striking is...", "The thing that
      matters here...").
- [ ] No rationalist-jargon hard bans (load-bearing, my priors,
      steelman, Chesterton's fence, updating toward).
- [ ] No academ-ai-leak phrases ("Certainly, here is...", "As an AI
      language model...", "Regenerate response.", "I don't have
      access to real-time...").
- [ ] Ran `scripts/cliche-check.py` on the draft, dealt with each
      hit (rewrote, cut, or defensibly kept).
- [ ] If the piece is heavily AI-shaped, also run the broader
      `references/ai-writing-tells.md` checklist (copula dodge,
      empty present participles, elegant variation, promotional
      adjectives, RAG artifacts, AI pleasantries).
