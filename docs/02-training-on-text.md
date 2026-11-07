# 02 — Training on Text

The first phase of the journey is the years clock: training.

> **Training is a very long, very repetitive guess-the-next-word
> session across an enormous library of text.** Every guess that misses
> nudges the model's internal settings slightly closer to guessing
> right *next time*.

That's the entire mechanism. Everything impressive grew out of it.

## The reading, in kitchen-table terms

Imagine a guest who read the entire neighborhood library — cookbooks,
newspapers, encyclopedias, fiction, forums, repair manuals — not to
memorize each book, but to become the sort of person who knows how a
cookbook sounds, how a news story is built, how a recipe ends, what
questions people ask about insurance, and how sixteen kinds of experts
explain the same thing.

Now the twist that separates this from any human reader: **the guest's
memory isn't words.** After the reading, what's left is one enormous
set of adjustable settings — billions of them. Reading was the
process of twisting those settings, a very tiny amount, billions of
times, until they hold a *feel* for language instead of a filing
cabinet of sentences.

That feel is hard to write down and easy to use. It's why the model
can write an apology email from the perspective of a wedding planner
having a difficult week — it absorbed how apologies sound, how wedding
planners sound, and how "difficult week" emails go — without ever
storing one as an email.

## How a training step actually goes

Stripped of all math, one training step looks like this:

1. Grab a fragment of text — say, the middle of an old newspaper story
   about a marathon.
2. Hide the next few words.
3. Ask the model to guess them: *"Runners waited at the starting line,
   stretching, sipping water, and…"* — the guess is *"chatting"* or
   *"nervously"* — both plausible.
4. Reveal the truth: *"shivering."*
5. Nudge every setting the tiniest amount toward "shivering."

Multiply that by a very big number — the whole process is billions of
these games — and you get a model.

Two honest simplifications, flagged so we're not pulling wool:

- Real training shows the model *several* hidden words at a time and
  scores its whole arrangement of guesses at once. The kitchen-table
  version is "guess what comes next"; the real version is "guess what
  comes next, from every direction at once."
- The "nudge" isn't magic — it's arithmetic that says "settings that
  helped guess correctly move a hair upward." That's the one place
  math sneaks in, and you can safely leave it to the machines.

## What the reading actually gives the model

After the years clock runs down, the model has absorbed — as feel,
not as facts in folders:

- **Language itself:** grammar that feels effortless, tone-shifting,
  the shape of a question and the shape of an answer.
- **Descriptions of the world:** what a marathon is, why bread rises,
  what 1099 paperwork is, how nurses talk to patients. Notice the
  careful wording — it knows how the world is *described*, which is
  nearly the same as knowing the world, but not quite. Remember this;
  chapter 05 leans on it hard.
- **Styles and genres:** lab reports, bedtime stories, legal boilerplate,
  forum arguments, soured recipe-review comments.
- **Skills without lessons:** nobody "taught" it to summarize, translate,
  outline, or write code. Those abilities emerge because the library
  contained ten million examples of documents beside their summaries,
  one language beside another, code beside its error messages.

## What it does *not* get from the reading

- **It doesn't look anything up.** There's no filing cabinet, no
  library card, no browsing. Later, when you *ask* it a question, it
  answers from the feel it baked in — impressions with edges as fuzzy
  as memory.
- **It doesn't store copies of the books.** The training result is
  far too small to hold the library; it holds patterns *learned from*
  the library. (When a model recites something word-for-word, it's a
  pattern worn very deep, like a highway groove, not a quoted file.)
- **It doesn't know today's date.** The library has a back inscription:
  the last page of text it trained on. Everything after that is a
  mystery — chapter 07 is all about that edge.

## The kitchen-table summary

Before an AI can answer you, it had to become something like a well-read
guest who absorbed the whole library as *feel*, not as filing. The next
chapter shows what that guest is actually doing when you ask a question:
playing one game, lightning fast, over and over — guess the next word.
