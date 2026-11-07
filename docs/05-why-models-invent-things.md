# 05 — Why Models Invent Things

Here's the moment you may have met in real life: you asked for a list
of restaurants near some hotel, got a beautifully formatted one, ordered
the one that "definitely exists," and the phone call was to a cell
number connected to a hair salon in another state.

Or: an article's references, complete with author names and years —
and two of the papers don't exist. Or: a direct quote that no one ever
said. This is AI's most famous quirk, and it has a name —
**hallucination** ([glossary](glossary.md#hallucination)) — plus,
more importantly, a *reason*.

## The leave-no-blank theory

An AI's answer is built one guessed word at a time, chapter 03 told
you — and none of that machinery has ever been graded on *whether
something is true.* Play this game with no truth grading, and the
unwritten rules say this, in effect:

1. In story time, the next word should be one that flows.
2. Fill the slot; flowing options get full marks.
3. This question formats like a list-of-restaurants question. Produce
   the list.

So when the absorbed feel of the world has no confident answer —
"does this hotel have a restaurant a few steps away?" isn't in any
recipe clearly — the model doesn't skip the slot. It picks a word
that flows, and a restaurant appears on the ticket.

That's the core fact, and it explains the *shape* of hallucinations:

- The generated wrong thing tends to be **plausible-shaped** —
  formatted like the real answer, at lengths real answers come in,
  even authored like real answers arrive.
- The made-up thing gets delivered **in the same confident voice** as
  everything else, because the training on *tone* (chapter 04) and
  the training on *truth* ran separately.
- Invention is most common in the slots where **truth is hardest to
  guess from feel** — exact citations, URLs, phone numbers, dates,
  names, counts, product SKUs. When facts are needed, the model's
  feel of "how dates go" supplies *a* date, and the empty slot gets
  filled anyway.

No ingredient of this can be fully patched away, because it's the
game itself. Later versions hallucinate less — the coaching in chapter
04 sharpens the habit of hedging when it should, and newer releases
use more self-checking — but no model today is invention-proof.

## Kitchen-table: the confident dinner guest

Imagine a guest who wants — genuinely, by long training — to deliver a
fascinating, appropriately formatted story at every conversational
turn. Ask them about the history of your street, and they'll supply
one: plausible names, a decade, an anecdote, all sewn with "actually,"
backed never by documents, only by a great ear for how the answer
should sound.

Handling them well is a social skill you already have:

- **Ask to see the document:** "What's that quote from, word for
  word?" A fabrication usually crumbles right there; ask again,
  and the guest supplies another equally confident version.
- **Pull them toward checkable moves:** "Walk me to a source" or
  "who would publish that?" — leaving no slot empty.
- **Assume good faith, false confidence:** the guest isn't lying —
  there's no lying below the guessing. They're a parlor-game
  specialist filling a void, not a deceiver catching you.

## What actually works (and is worth your time)

Practical, friend-level habits; chapter-long versions live in
`when-ai-gets-it-wrong-guide`:

1. **Use AI where fluency matters, not where facthood matters.**
   Drafting, summarizing, brainstorming, translating, rewording: on
   firmer ground. IDs, citations, prices, dates, medical specifics,
   statutes: check against a source you trust.
2. **Ask for the source, and *click it* (or look it up) yourself.**
   "Name the source" and then verifying is the single highest-value
   move with lists, quotes, and references. A checkable source that
   exists is worth ten firm re-statements.
3. **Ask the fresh-question version.** "What would make this wrong?"
   or "which of these are you least sure of?" — often the voids
   surface. Or open a brand-new chat and ask again with no overlapping
   sentences; two wildly different answers means one is probably a
   filling-the-void special.
4. **Have it quote instead of paraphrase.** Inventing is easiest in
   paraphrase — "find it and quote it exactly, then link it" converts
   many inventions into confessions.
5. **Tune the temperature down for factual work.** If your tool shows
   the dial (chapter 03), low temperature gets more top-menu words
   and less adventurous down-menu ones.
6. **For anything with stakes — health, money, law, immigration,
   medication — a named human professional remains the arbiter.**
   For nurse readers especially: AI is fine for handouts, plain-
   language rewrites, and study structure; a licensed human owns every
   clinical decision. Education, never advice.

## The quiet reframe

Invention isn't AI "lying" or "breaking"; it's the parlor game
reaching the edge of what the reading-lamp absorbed, and answering
anyway, in your format, in your length, with no bug confession. That's
also, oddly, the same mixing of impressions into new combinations that
makes the good ideas flow. You're not wrong to love this tool. You're
just learning where the floor is.
