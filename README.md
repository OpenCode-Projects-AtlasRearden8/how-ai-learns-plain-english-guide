# How AI Learns — a plain-English guide to what happens before your AI answers

*Explain AI "like a friend would" — plain English, step by step, never
condescending.*

You type a question, and seconds later a tidy, helpful answer appears.
What actually happened in between? This gentle, kitchen-table guide
walks the whole journey: **training on text, next-word prediction,
tuning, human feedback, and why models sometimes confidently invent
things** — plus a model-name decoder and an update-cadence chapter, with
zero math.

**This is an education project. It is never an endorsement of hype, and
it is never medical, legal, or financial advice.**

## What's inside

| Path | What it is |
| --- | --- |
| `docs/00-start-here.md` | How to use the guide: the one core idea, reading order |
| `docs/01-the-journey-before-the-answer.md` | The map: the years clock (training) vs. the seconds clock (answering) |
| `docs/02-training-on-text.md` | The reading phase — absorbing the whole library as *feel* |
| `docs/03-next-word-prediction.md` | The parlor game: every answer written one guessed word at a time |
| `docs/04-tuning-and-feedback.md` | Finishing school and the tasting panel (RLHF, in plain English) |
| `docs/05-why-models-invent-things.md` | Where hallucinations come from, and six habits that keep them visible |
| `docs/06-model-name-decoder.md` | Family · size · flavor · version — any model name in four pieces |
| `docs/07-update-cadence.md` | Big vintages, quiet re-seasoning, and the gentle way to keep up |
| `docs/08-cheat-sheet.md` | The whole guide on one page |
| `docs/glossary.md` | Soft glossary — calm one-liner definitions |
| `site/` | A static website version with a playable toy next-word predictor, a temperature dial, hallucination flip-cards, and a live name decoder |

## Run the website

No build step, no dependencies, no network calls, no tracking. The site
is plain HTML/CSS/JS with system fonts only.

```sh
python3 -m http.server 8000 --directory site
# then open http://localhost:8000
```

(You can just double-click `site/index.html` too — everything is local.)

## Run the self-tests

```sh
python3 tests/run_tests.py
```

The tests verify project structure, internal links, glossary anchors,
site HTML structure, and the exact LICENSE copyright line.

## How this differs from its siblings

- **`ai-glossary-pocketbook`** defines words. This guide *tells a
  story* — how learning happens end to end. It defines only enough
  terms to keep the story flowing.
- **`ai-benchmarks-explained-guide`** teaches you to *read quality
  scores*. This guide explains where the ability being scored came
  from — and never ranks or scores anything itself.
- **`context-and-memory-ai-guide`** goes deep on what the model can
  re-read in the moment; this guide covers the whole journey lightly.

## Who made this

Built and maintained by **Asdale Dynamics, LLC** — the company behind
Registered Nurse turned AI author Dylan Asdale, his book *The Massive
AI Manual*, and the hub site `dylanasdale.github.io`. Beginner-first
AI education: books, guides, and practical tools published with a
local-first, no-secrets, no-tracking ethos.

## License

MIT — see [LICENSE](LICENSE). `Copyright (c) 2026 Asdale Dynamics, LLC`

## Editorial promise

Model names, scores, and release news go out of date; the *shape of the
story* doesn't. Nothing here tells you which model to buy — it teaches
you what the machine really is, so its confident nonsense stops being
scary and starts being workable. Fictional model names (Checkers-7B,
Widget-9B) appear throughout as teaching aids. Use AI to assist your
thinking, especially for anything involving health, money, or law —
and always confirm important things with your own trusted sources.
