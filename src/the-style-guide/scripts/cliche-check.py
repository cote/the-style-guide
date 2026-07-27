#!/usr/bin/env python3
"""cliche-check - scan text for AI / LinkedIn / rationalist cliches.

Reads text from stdin (or a file path arg) and prints matches grouped
by category with a short context window per hit. Exit 0 when clean,
1 when hits found.

Patterns come from:

- The literal phrase lists in styles/ai-detector.md (vocabulary tells,
  Mollick's short-mute list, self-important punchline closers,
  rationalist / LessWrong jargon).
- Simon Willison's llm-cliche-highlighter regexes:
  https://github.com/simonw/tools/blob/main/llm-cliche-highlighter.html
  (adapted from JS to Python).

See styles/ai-detector.md §Sources for the empirical evidence base
(Kobak et al. 2025, Liang et al. 2024, Gray 2024, Glynn 2024,
Cabanac et al.) and editorial essays (Gorrie, Vollmer, Hassid) that
back the vocabulary list.

Usage:

    cat draft.md | scripts/cliche-check.py
    scripts/cliche-check.py draft.md
    scripts/cliche-check.py --category rationalist draft.md
    scripts/cliche-check.py --list-categories
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass


@dataclass
class Pattern:
    category: str
    label: str
    regex: re.Pattern


def _phrase_re(phrase: str) -> re.Pattern:
    """Compile a literal phrase as a case-insensitive, word-boundary regex.

    Straight and curly apostrophes are treated as equivalent so a phrase
    like "it's" matches text with either quote style.
    """
    escaped = re.escape(phrase).replace(r"\'", r"['’]")
    return re.compile(rf"\b{escaped}\b", re.IGNORECASE)


VOCAB_TELLS = [
    "delve", "tapestry", "nuanced", "robust", "leverage", "ecosystem",
    "in today's rapidly evolving", "in today's fast-paced world",
    "now more than ever", "journey", "passionate", "thrilled",
    "humbled", "blessed", "game-changer", "disruptor", "thought leader",
    "synergy", "circle back", "deep dive", "rockstar", "ninja", "guru",
    "value-add", "learnings",
    "vibrant", "groundbreaking", "renowned", "transformative",
    "cutting-edge", "world-class", "meticulous", "meticulously",
    "intricate", "intricacies", "interplay", "enduring", "pivotal",
    "crucial", "commendable", "realm", "seamless", "seamlessly",
    "testament", "elevate", "elevates", "harness", "harnesses",
    "notable", "notably", "comprehensive",
    "underscore", "underscores", "underpins", "showcasing", "emphasizing",
    "enhance", "highlighting", "align with", "aligns", "foster",
    "fostering", "bolster", "bolstered", "bolstering", "garner",
    "garnered", "adept", "akin", "amidst", "burgeoning", "compelling",
    "additionally",
]

MOLLICK_SHORT_MUTE = [
    "doing the heavy lifting",
    "the real question is",
    "here's the thing nobody is talking about",
    "that's the real story",
    "what most people miss",
    "this is where it gets interesting",
    "it's not about",
    "it is not about",
]

PUNCHLINE_CLOSERS = [
    "it's the one worth telling",
    "that's the story worth telling",
    "it's the version that matters",
    "that's the moment worth remembering",
    "that's the part i keep coming back to",
    "that's the one that stayed with me",
    "that's the real lesson",
    "that's what i'll remember",
]

RATIONALIST_HARD = [
    "load-bearing", "doing the work", "doing a lot of work",
    "doing the heavy lifting", "carrying the argument",
    "carrying the sentence", "the smoking gun",
    "my priors", "my priors say", "updated my priors",
    "updating my priors", "updating toward", "updating away from",
    "steelman", "steelmanning", "strawman",
    "chesterton's fence",
]

RATIONALIST_SPARINGLY = [
    "orthogonal", "non-trivial", "in the limit", "epistemic status",
    "object-level", "meta-level", "motte-and-bailey", "galaxy-brained",
    "coordination problem", "moloch",
]

SIGNPOSTING = [
    "what's striking about",
    "the thing that matters here is",
    "it's worth noting that",
    "one important thing to consider",
    "let me be very clear",
]

ACADEM_AI_LEAKS = [
    "certainly, here is",
    "certainly, here are",
    "as an ai language model",
    "as an ai, i",
    "as of my last knowledge update",
    "as of our knowledge cutoff",
    "as of my last update",
    "new developments may have occurred since my last update",
    "i don't have access to real-time",
    "i'm sorry, but i cannot",
    "however, it is important to note",
    "however, it's important to note",
    "regenerate response",
    "as a large language model",
    "as an ai assistant",
    "i'm an ai",
    "i am an ai",
    "my training data",
]

LINKEDIN_OPENERS = [
    "here's the truth", "let that sink in", "let's unpack this",
    "here's the thing", "if you know, you know",
    "buckle up", "here's the harsh reality",
    "unpopular opinion", "not sure who needs to hear this",
    "this changed everything for me", "i wish someone told me this earlier",
    "soft skills are the new hard skills", "this is your sign",
    "i'm humbled and excited", "thrilled to announce",
    "humbled and honored",
]

# Simon Willison llm-cliche-highlighter regexes, JS -> Python.
SIMONW_REGEXES = [
    ("simonw:whole",
     "\"That's the whole ...\"",
     r"\b(?:that|this)(?:['’]s|\s+(?:is|was))\s+the\s+whole\b(?:\s+\w+)?"),
    ("simonw:sit-with",
     "\"Sit with that\" / \"sit with the discomfort\"",
     r"\bsit(?:s|ting)?\s+with\s+(?:that|this|it|(?:the|your)\s+(?:discomfort|feelings?|tension|weight|uncertainty|ambiguity|grief|silence|unease))\b(?:\s+for\s+a\s+\w+)?"),
    ("simonw:already-know",
     "\"You already know\"",
     r"\byou\s+already\s+knows?\s+(?:the\s+answer|what|how|why|this|that|it|who|where)\b|\byou\s+already\s+knows?\b(?![ \t]+\w)"),
    ("simonw:is-the-entire",
     "\"is the entire ...\"",
     r"(?:\b(?:is|was|are|were)|['’]s)\s+the\s+entire\b(?:\s+\w+)?"),
    ("simonw:the-entire-is",
     "\"the entire ... is\"",
     r"\bthe\s+entire\s+[\w'’-]+(?:\s+[\w'’-]+){0,4}?\s+(?:is|was|are|were)\b"),
    ("simonw:is-real",
     "\"is real ... and / not\"",
     r"\bis\s+(?:(?:the|a)\s+real\b(?![\s-]+(?:estate|time|life|world|quick)\b)[^.!?\n]*?\b(?:and|not)\s+it\b|real\b(?![\s-]+(?:estate|time|life|world|quick)\b)[^.!?\n]*?\b(?:and|not)\b)"),
    ("simonw:punchline",
     "\"The punchline is\"",
     r"\bthe\s+punchline(?:\s+(?:is|was|being)\b|\s*[:?])"),
    ("simonw:worth-naming",
     "\"Worth naming\"",
     r"(?:\b(?:is|are|was|were|feels?|felt|seems?|seemed)|['’]s)\s+(?:\w+\s+){0,2}?worth\s+naming\b(?!\s+names\b)|\bworth\s+naming\s*:"),
    ("simonw:not-nothing",
     "\"That's not nothing\"",
     r"\b(?:that|this|it|which)(?:['’]s|\s+(?:is|was))\s+not\s+nothing\b"),
    ("simonw:no-chain",
     "\"No X, no Y\" chain",
     r"\bno[-\s]\w[\w-]*(?:[\s,;:.!?–—]+no[-\s]\w[\w-]*){1,}"),
    ("simonw:did-not-chain",
     "\"Did not X, did not Y\" chain",
     r"\b(?:did\s+not|didn['’]t)\s\w[\w-]*(?:[\s,;:.!?–—]+(?:did\s+not|didn['’]t)\s\w[\w-]*){1,}"),
    ("simonw:dont-verb-it",
     "\"Don't VERB it ... VERB it\"",
     r"\b(?:do\s+not|don['’]t)\s+(?:just\s+|simply\s+|merely\s+)?(\w+)(?:\s+(?:of|about|at|on|for|with|to))?\s+it\b[^.!?\n]*?[.!?;,:–—]['\"”’]*\s*(?:just\s+|simply\s+|merely\s+)?\1(?:\s+(?:of|about|at|on|for|with|to))?\s+it\b"),
]


def build_patterns() -> list[Pattern]:
    patterns: list[Pattern] = []
    groups = {
        "vocabulary": VOCAB_TELLS,
        "mollick": MOLLICK_SHORT_MUTE,
        "punchline-closer": PUNCHLINE_CLOSERS,
        "rationalist-hard": RATIONALIST_HARD,
        "rationalist-sparingly": RATIONALIST_SPARINGLY,
        "signposting": SIGNPOSTING,
        "linkedin-opener": LINKEDIN_OPENERS,
        "academ-ai-leaks": ACADEM_AI_LEAKS,
    }
    for cat, phrases in groups.items():
        for p in phrases:
            patterns.append(Pattern(cat, p, _phrase_re(p)))
    for pid, label, src in SIMONW_REGEXES:
        cat = pid.split(":", 1)[0]
        patterns.append(Pattern(cat, label, re.compile(src, re.IGNORECASE)))
    return patterns


def scan(text: str, patterns: list[Pattern], only: set[str] | None) -> list[tuple[Pattern, re.Match]]:
    hits: list[tuple[Pattern, re.Match]] = []
    for pat in patterns:
        if only and pat.category not in only:
            continue
        for m in pat.regex.finditer(text):
            hits.append((pat, m))
    hits.sort(key=lambda h: h[1].start())
    return hits


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def context(text: str, m: re.Match, radius: int = 40) -> str:
    start = max(0, m.start() - radius)
    end = min(len(text), m.end() + radius)
    snippet = text[start:end].replace("\n", " ")
    hit = m.group(0)
    return snippet.replace(hit, f"[{hit}]", 1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?", help="path to text file; stdin if omitted")
    ap.add_argument("--category", action="append", default=[],
                    help="only check this category (repeatable). See --list-categories.")
    ap.add_argument("--list-categories", action="store_true")
    args = ap.parse_args()

    patterns = build_patterns()
    categories = sorted({p.category for p in patterns})

    if args.list_categories:
        for c in categories:
            n = sum(1 for p in patterns if p.category == c)
            print(f"{c:24s} {n} patterns")
        return 0

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    only = set(args.category) if args.category else None
    if only:
        unknown = only - set(categories)
        if unknown:
            print(f"unknown categories: {', '.join(sorted(unknown))}", file=sys.stderr)
            print(f"available: {', '.join(categories)}", file=sys.stderr)
            return 2

    hits = scan(text, patterns, only)
    if not hits:
        print("clean", file=sys.stderr)
        return 0

    by_cat: dict[str, list[tuple[Pattern, re.Match]]] = {}
    for pat, m in hits:
        by_cat.setdefault(pat.category, []).append((pat, m))

    for cat in sorted(by_cat):
        print(f"## {cat} ({len(by_cat[cat])})")
        for pat, m in by_cat[cat]:
            ln = line_of(text, m.start())
            print(f"  L{ln:>4}  {pat.label!r} -> {context(text, m)}")
        print()

    print(f"{len(hits)} hit(s) across {len(by_cat)} categor(y|ies)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
