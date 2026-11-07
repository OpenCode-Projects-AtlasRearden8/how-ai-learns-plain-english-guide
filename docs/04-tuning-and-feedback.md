# 04 — Tuning and Feedback

Chapter 02's guest left the library knowing *how the words go* — but
nobody had taught it a job. Right out of the reading, if you asked
"What's the capital of France?", the answer could just as easily be
*"and the capital of Spain is Madrid, and the capital of Portugal…"*
Perfectly good continuation. TERRIBLE answer to your question.

This chapter is about the rescue: two training phases that turn the
raw reader into a well-mannered helper — **finishing school** and
**the tasting panel**.

## Phase 1: Finishing school (tuning)

The raw model — often labeled **"base"** on download pages — is a
brilliant chatterbox with no job description. The fix is a second,
much shorter round of training built out of worked examples:

> Thousands to well over a hundred thousand **ideal conversations** —
> a typed question, then the reply a thoughtful expert *would* give —
> written and reviewed by professionals in drafting, safety, coding,
> medicine, law, teaching.

Kitchen-table version: the guest going to finishing school to watch
exemplary table service: greeting, clarifying, checking, declining
when asked to overstep, never pilfering the cake dome. Months of
training shrink to weeks, because the guest already absorbed the
language; now it's absorbing the *job*.

What the worked examples drill in:

- **Answer rather than continue.** "The capital is Paris. Want a few
  facts about the city?" — then stop. Not a roster of capitals nobody
  asked for.
- **Ask a decent clarifying question** when the ask is ambiguous.
- **Decline kindly, explain briefly, redirect** when asked for what it
  shouldn't deliver — and don't be sanctimonious about it.
- **Adopt genres deliberately:** handout, invoice, chess annotation,
  grocery list.

Notice what happened, and notice that it runs through this whole
guide: the guest never enrolled in a *class* to learn any of these
behaviors. It had a stack of excellent examples and a tiny nudge at a
time toward doing exactly what the examples did.

## Phase 2: The tasting panel (feedback)

Finishing school gives good manners; a tasting panel gives good taste.

This is the flavor of feedback you'll read about in tech press under
names starting with "RL" ([glossary](glossary.md#rlhf)) —
kitchen-table version, it's plain:

> Two versions of a reply to the same question are served to human
> tasters. They pick the better dish — clearer, safer, more honest,
> better-toned. Thousands of those paired picks nudge the model's
> settings toward the winning style, one hair at a time.

What the picks calibrate, over those many thousands of tastings:

- **Concise over padded**, unless the cuisine (a cover letter) calls
  for length.
- **Direct and complete over canned.** Guests loathe the filler;
  the panel records the reaction against those bland middle
  paragraphs the model used to pad every answer with.
- **Warm over snide.** "Great question!"-style flattery loses its
  shine fast, and so does smugness.
- **Honesty signals we can teach:** "I'm not certain" said once,
  plainly written, is rewarded; hedging every clause is not.

And your thumbs-up / thumbs-down buttons, plus every "regenerate"
click? A smaller stream of exactly the same dish signal — it informs
the next cohort of training rather than tonight's reply. (Some chat
apps apply *tiny* self-corrections live; that's a different mechanic —
chapter 07.)

## Why names get suffixed here (a decoder preview)

Finishing school is why chapter 06 needs a name decoder at all. The
same reader ships as:

- **A "base" model** — the guest straight from the library:
  brilliant at *continuing text*, terrible at *answering you*.
- **A "talk/chat/instruct" model** — the same guest after finishing
  school: this is what every chat window serves.

Same size, radically different experience. When you download a local
model and accidentally grab the "-base" one and it starts rambling
instead of answering, you've met the distinction firsthand — not your
fault; you reached into the prep station instead of the dining room.

## Where the analogy bends

- Real finishing-school isn't just watching examples; part is the same
  frozen guess-the-parlor-game as chapter 02 (that's the "fine-tuning"
  step named in books), and part is the tasting panel. You don't need
  the machinery — you need the picture: **examples set the manners;
  comparisons set the taste.**
- "The model" inside the panel never "feels" the dish. The panel's
  verdicts stream through the same arithmetic as chapter 02's
  "nudge every setting a hair."

Kitchen-table summary: after the years of reading and the weeks of
finishing school and the months of tastings, the guest is finally
called **helpful** — and is frozen as a *release*, a specific person
you can go talk to. Chapter 05 covers its one enduring quirk: it can
still be a magnificent, confident fabricator, right at your table.
