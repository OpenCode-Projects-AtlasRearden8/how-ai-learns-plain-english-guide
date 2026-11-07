# 08 — Cheat Sheet

The whole guide on one page, for the day you're explaining this to
someone else.

## The journey in eight sentences

1. **Training** (ch. 02): The model read an enormous library — cookbooks,
   news, code, forums — and turned it into a feel for how language and
   facts flow, by playing guess-the-next-word on every page.
2. **Prediction** (ch. 03): At answer time it's still playing that game:
   guess the next word, place it, re-read the conversation, guess again.
3. **Temperature**: The dials behind "safe, starchy" vs. "vivid,
   risky" word choices are a seasoning setting.
4. **Attention**: Before each guess it re-reads the chat, noting what
   matters now; distant details can go faint in long conversations.
5. **Tuning** (ch. 04): Finishing school — thousands of ideal
   conversations — taught it to *answer* rather than *continue*.
6. **Feedback**: Human taste-testers picking between two replies
   taught it taste. Your thumbs-up is a (very small) contribution.
7. **Invention** (ch. 05): Because every word is a guess, missing
   facts get filled with plausible-shaped, confident-sounding
   fabrications — mostly in the slots where truth is hardest to guess
   (citations, numbers, URLs, dates, names).
8. **Releases** (ch. 06–07): The finished, frozen model ships as a
   named version; the chat kitchen around it re-seasons quietly; new
   vintages mean the whole schooling was re-run.

## Model names: four taps of a finger

> **Family** (whose kitchen) · **Size** (7B = 7 billion dials) ·
> **Flavor** (base vs. -Talk/-Chat/-Instruct vs. specialty) ·
> **Version** (which vintage)

- No suffix or "Base": raw reader; can ramble at a chat window.
- "-Talk/-Chat/-Instruct": finished school — start here.
- "-Think"/"-R...": does working notes before answering; slow, strong.
- Size classes: 1–3B phone-friendly · 4–9B everyday laptop ·
  10–40B strong machine · 70B+ serious hardware · cloud = rented seat.
- B-numbers compare within a family only, and size is not quality.

## Anti-hallucination habits

- Use AI where *fluency* matters; verify where *fact* matters.
- Ask for sources — then actually check them.
- Re-ask in a fresh chat; wildly different answers = one is invented.
- Have it quote exactly rather than paraphrase.
- "What would make this wrong?" surfaces the doubt.
- For health, money, law, medication: a trusted human professional
  decides. Education, never advice.

## The two clocks (the answer to most arguments about AI)

- **Years clock:** training and tuning — frozen into a release.
  Chats don't retrain it; updates re-run the school.
- **Seconds clock:** answering — word-by-word guessing at the table.
  Fast, fluent, and no new learning sticks to the model.

## One-breath explanation for a meeting or a dinner

> "It read a giant pile of text and learned to predict the next word,
> which forced it to absorb how the world is described. Then people
> coached it, with worked examples and taste tests, to answer
> helpfully. It writes one guessed word at a time, so it sometimes
> confidently fills gaps with plausible inventions. The finished
> model is frozen into a named version — family, size, flavor,
> vintage — and the chat service around it gets quietly re-seasoned
> between the big releases."

## Where to go next

- Definitions while reading: [Glossary](glossary.md).
- To *pick* and *test* models yourself: the `ai-model-picker-cli`
  and `mini-model-bench-cli` companion projects from the same family.
- To read quality *scores* like a pro: `ai-benchmarks-explained-guide`.
- For word-by-word definitions: `ai-glossary-pocketbook`.
- For a fictional worked storyline of models behaving badly:
  `when-ai-gets-it-wrong-guide`.
