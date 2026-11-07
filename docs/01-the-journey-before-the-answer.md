# 01 — The Journey Before the Answer

Let's begin at the moment you already know, and then walk backward.

You type a question. A few seconds later, a well-formed, genuinely
helpful answer appears. Most explanations of AI either skip this or
wave a magic wand at it. We're not going to wave the wand. Here's the
whole journey in one paragraph:

> **Months or years ago**, the model read an enormous amount of text and
> turned it into a deep feel for how language and facts flow. Then it
> went through finishing school, where people coached it on being
> helpful instead of just... continuing sentences. Then it was frozen,
> boxed, and connected to a chat window. **Now**, when you ask a
> question, it plays a lightning-fast game of guess-the-next-word —
> again and again — until a complete answer stands there.

That's it. No magic. Two very different clocks.

## The two clocks

Kitchen-table analogy time: think of a really good line cook.

- **The years clock:** apprenticeship, culinary school, a thousand
  Thursday services, tasting disasters, learning how heat behaves.
  This is slow. It happened *before* tonight. You cannot speed it up
  by ordering more food.
- **The seconds clock:** tonight, ticket comes in — "one risotto, no
  cream." The cook uses everything from the years clock to produce a
  dish in minutes.

An AI has both clocks, and mixing them up is the number-one source of
confusion in everyday conversations about AI:

| Confusion | Reality |
| --- | --- |
| "It learned that yesterday, from my chat!" | The *model* hasn't re-read anything since it finished school; your chats are tonight's service, not new coursework. |
| "It knows this — it must have looked it up." | For most chat models, no: it's working from impressions formed years ago, not a filing cabinet. (Some chat systems bolt on a real reading tool — explained in chapter 07.) |
| "They fixed it last week with an update." | Updates rebuild the *schooling*, not yesterday's homework — they take months, which is why fixes feel slow. |

## The map of the trip

Here's the full journey with its chapter numbers, so you always know
where you are:

1. **Training on text** (chapter 02) — the raw model reads a vast
   library and absorbs patterns: how sentences go, how facts connect,
   how code looks, how recipes are written. This is the years clock.
2. **Next-word prediction** (chapter 03) — the one game it learned to
   play: given everything so far, guess what comes next. Every answer
   you've ever seen was built one guessed word at a time.
3. **Tuning and feedback** (chapter 04) — finishing school: worked
   examples of good answers, plus human taste-testers picking between
   two replies. This turns a babbling word-completion engine into
   something that answers, asks clarifying questions, and apologizes.
4. **Invention, honestly labeled** (chapter 05) — because the model is
   *always* playing the guess-the-next-word game, sometimes it fills
   gaps with plausible-seeming fabrications. This is a feature of the
   game, not a bug you can patch away.
5. **Names and versions** (chapter 06) — once you know the journey,
   model names stop being alphabet soup and start being a tiny puzzle
   with four pieces: family, size, flavor, version.
6. **Update cadence** (chapter 07) — how the meal gets re-cooked: big
   re-releases, quiet behind-the-scenes seasoning, and the polite
   habit of not chasing every update.

## What the analogy bends on

We promised to flag where the kitchen-table picture bends. Two spots:

- The cook slowly improves *during* tonight's service. The model never
  does; its schooling is frozen. (Chat systems can add tools — a real
  search bar, your own documents — but that's the restaurant hiring a
  forager, not the cook going back to school mid-shift.)
- A deep feel for language is a metaphor for a very large pattern of
  numbers. Nothing inside the model is a sentence, a photo, or a
  thought. It's all one big set of adjustable settings — and chapter 06
  uses that to explain why "7B" is a size, not a speed.

## The office-hours answer

If someone at a meeting says "how does this thing even work," you'll
soon be able to answer in one calm breath:

> "It took a lot of text, trained itself to predict the next word over
> and over, absorbed a huge amount about how the world is described,
> then got coached by people on how to answer helpfully. That coaching
> is frozen into a version you can use. It writes one word at a time,
> which is why it sometimes confidently invents things — and why the
> releases have version names."

Not a bad answer, and every word of it gets unpacked in the next three
chapters.
