# 06 — Model Name Decoder

Once you know the journey (train in chapter 02, tune in chapter 04,
release to the world), model names stop being alphabet soup. Take a
fictional one: **Checkers-7B-Talk-v2**. Four puzzle pieces —
*Checkers*, *7B*, *Talk*, *v2* — and each one tells you something
different. By the end of this chapter you'll be able to read any model
name, real or imaginary, as those four pieces.

## The decoder in one breath

> A model name is usually a **four-part code**: family, size, flavor,
> version — in that order.

- **Family** — which "cuisine" it belongs to: who built it, and which
  training recipe.
- **Size** — roughly how big the model is, counted in billions of
  adjustable settings (the "dials" from chapter 01).
- **Flavor** — which finishing school it went through: raw
  text-player or polished conversationalist.
- **Version** — which vintage: which edition of that recipe you're
  talking to.

Now each piece in detail.

## Part 1: Family — the cuisine

The family name is the label of the kitchen that made it: **GPT**,
**Claude**, **Gemini**, **Llama**, **Mistral**, **Qwen**,
**DeepSeek**, **Phi**, **Gemma** — and in this guide's examples,
fictional families like **Checkers** and **Widget**.

Models within a family share a training recipe the way siblings share
a house seasoning. Moving across families is a different kitchen:
different pantry, different pan-handling, and a personality that can
surprise you a little on first reading.

What the family *doesn't* mean: it isn't a quality score. All major
families passed similar schools (chapter 04). The biggest *felt*
difference across families is personality — tone, length, hedging
style — not raw smartness. (Judging quality from scores is another
skill entirely; that's the `ai-benchmarks-explained-guide` project.
This guide sticks to what a name tells you.)

## Part 2: Size — the "7B" question

The odd string **7B** means **seven billion** — the count of
adjustable settings ("parameters," glossary-speak) inside the model:
the dials that training, in chapter 02, tightened billions of times
until they held a feel for the whole library.

What size actually predicts, day to day:

| Size class | Typical feel | Runs on |
| --- | --- | --- |
| Very small (1–3B) | Snappy chat, thinner world-knowledge | a phone, an old laptop |
| Small (4–9B) | The everyday sweet spot: good manners, decent recall | a regular laptop, modest local setup |
| Medium (10–40B) | Noticeably deeper reasoning and recall | strong laptop or desktop |
| Large (70B+) | The heavyweight: rarer stumbles, more nuance | high-end hardware or a lab's server |
| Frontier (cloud) | The most capable class available | someone else's data center; you rent the seat |

Two cautions worth a sticky note:

- **Size is not a quality score.** A small model fine-tuned for one
  job can beat a giant at that one job.
- **B-numbers compare well only within one family.** Different
  kitchens pack their spices differently. Treat the B-number as a
  rough size class, never a ranking.

## Part 3: Flavor — which finishing school

The suffix – and this is where newcomers most often grab the wrong
jar; chapter 04 explained why. In names:

- **No suffix, "Base," or "Raw"** — the guest straight from the
  library, before finishing school
  ([glossary](glossary.md#base-model)). Ask it a question and it may
  reply with *more question-shaped text* ("Question two: why is the
  sky blue? Answer: ..."), because continuing documents is its skill.
  Legitimate and even useful for study and building — but not what
  you want at a chat window.
- **Instruct / Chat / Talk** — finished school. Answers questions,
  follows instructions, asks clarifying questions, knows how to
  decline. This is what every chat service serves and what you
  almost always want when downloading a local model.
- **Reasoning-class markers** ("-Think," "R1"-style, "o"-series
  names) — a model trained to write working notes before its final
  answer. Better for multi-step problems and tangled code; slower,
  and overkill for a friendly email.
- **Fine-tuned variants** — a standard model with an extra, narrower
  finishing school stacked on top: "Storyteller-13B-Talk-Chef"
  (fictional) would be Storyteller-13B-Talk with a cookbook
  specialty. Community fine-tunes on download sites carry the base
  name plus the author's tag.

Rule of thumb: **plain name = base; -Talk/-Chat/-Instruct =
chat-ready; extra tag = specialty stacked on top.** If in doubt,
start on the -Talk shelf.

## Part 4: Version — the vintage

The trailing bit ("2," "3.5," "4," "v3.1," a date, a codename) marks
which **vintage** ([glossary](glossary.md#vintage)) of the recipe
you're talking to. Because a new
version means the *entire* schooling was re-run (that's chapter 07),
new editions arrive as new names rather than as a slowly improving
same-model — the restaurant doesn't re-cook a sold dish; it cooks the
next one.

What a version tells you in real terms:

- It's a vintage, not a promise: "v3" isn't automatically better
  *for you*. Temperaments shift, and gains in one area can cost
  somewhere you cared about.
- Version numbers aren't a tidy ladder: "4," "4-minor," and "4 mini"
  coexist as different objects on the shelf, not one improving thing.
- Your prompts and habits survive the change. A new vintage doesn't
  delete your kitchen mitts.

## The decoder, applied — a table to keep

| Name (fictional) | Decoded |
| --- | --- |
| **Checkers-7B** | Family Checkers, seven billion settings, no suffix — almost certainly a **base**: the raw reader. |
| **Checkers-7B-Talk** | Same size, finishing school done: chat-ready. |
| **Checkers-7B-Talk-v2** | Same size and flavor, later vintage (schools re-run). |
| **Checkers-70B-Talk-v2** | Ten times the settings: deeper recall, needs serious hardware. |
| **Checkers-7B-Talk-v2-Think** | Plus the "work it out on paper first" training. Slow but methodical. |
| **Widget-9B vs. Widget-9B-Talk** | Same student, before and after finishing school. |
| **Widget-mini-4** | A small member of the Widget family's 4th vintage: cheap and fast, less deep. |

A five-second exercise for next time you meet any model name — cloud
picker, download page, or a friend's mention: tap four fingers and
name each piece — family, size, flavor, version — then answer the one
question that matters: **right job? right machine?**

Not bad for a four-part code. One honest question is left, and it
gets its own chapter: **how often does this whole shelf change, and
who's keeping up?**
