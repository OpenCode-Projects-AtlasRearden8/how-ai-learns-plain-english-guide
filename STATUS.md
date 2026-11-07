# STATUS — How AI Learns (Plain English Guide)

A gentle, kitchen-table explainer of **what happens before an AI
answers**: training on text, next-word prediction, tuning, human
feedback, why models sometimes invent things — plus a model-name
decoder and an update-cadence section. Zero math; told "like a friend
would," step by step, never condescending.

Deliverable type: **markdown manual (`docs/`) + static HTML website
(`site/`)** — system fonts, no tracking, no network calls, no build
step, no dependencies.

Education only. Never medical, legal, or financial advice. All model
names used as examples beyond real family labels (GPT, Claude, Gemini,
Llama, Mistral, Qwen, DeepSeek, Phi, Gemma) are fictional teaching aids
("Checkers-7B", "Widget-9B", "Storyteller-13B").

Maintained by **Asdale Dynamics, LLC** (Dylan Asdale, *The Massive AI
Manual*, dylanasdale.github.io). MIT licensed — `LICENSE` carries the
exact line `Copyright (c) 2026 Asdale Dynamics, LLC`, and the README
credits the LLC.

## What was built

### `docs/` — the manual (markdown, 10 files, ~7,500 words)

- `00-start-here.md` — the one core idea (an answer = guessed words by a
  well-read, well-schooled guesser), reading order, who it's for, what
  it won't do, and how it differs from the sibling glossary and
  benchmarks projects
- `01-the-journey-before-the-answer.md` — the two clocks (years vs.
  seconds), the top confusions table, the map of the trip, where the
  analogies bend
- `02-training-on-text.md` — the reading phase: guessing hidden words
  across a giant library, nudging billions of settings a hair at a
  time; what the reading gives (feel, not filing) and doesn't (lookup,
  storage, today's date)
- `03-next-word-prediction.md` — the parlor game: guess, place, re-read,
  guess; phone-keyboard analogy strengthened; the temperature dial;
  attention as the host's glance at the party
- `04-tuning-and-feedback.md` — finishing school (worked ideal
  conversations) and the tasting panel (human pick between two dishes =
  RLHF in plain English); why plain-named models ramble at chat windows
- `05-why-models-invent-things.md` — the leave-no-blank theory of
  hallucination; where invention concentrates (citations, numbers,
  URLs, dates); the confident-dinner-guest analogy; six practical
  habits; healthcare-worker note (education, never advice)
- `06-model-name-decoder.md` — names as four-part codes:
  family (cuisine) · size (B = billions of dials; size-class table) ·
  flavor (base / Talk-Chat-Instruct / reasoning / fine-tuned variants) ·
  version (vintage); applied-decoder table to keep
- `07-update-cadence.md` — big releases vs. quiet re-seasoning (system
  prompt, reading tools, guardrails, serving settings); the gentle
  five-habit protocol; local models never re-season themselves
- `08-cheat-sheet.md` — the journey in eight sentences, the four-tap
  name decoder, anti-hallucination habits, the two clocks, and a
  one-breath explanation for meetings
- `glossary.md` — 24 soft definitions, each one or two calm sentences

### `site/` — static website (dependency-free HTML/CSS/JS)

- `index.html` — the one idea, the two clocks, the chapter map, and the
  lane-distinctions (glossary pocketbook / benchmarks guide / this)
- `journey.html` — a **playable toy next-word predictor** (a real
  hand-built bigram model over a tiny fictional "cafe cookbook"), a
  live **temperature dial** that re-weights the menu, finishing-school
  vs. tasting-panel cards, and three **hallucination flip-cards**
  showing what the game puts in truth-hard slots
- `names.html` — the **live name decoder** (five fictional names decode
  piece by piece), what each piece means, and the update-cadence table
  with the gentle protocol
- `glossary.html` — live-searchable soft glossary (19 anchor-linked
  entries)
- `styles.css`, `app.js` — single stylesheet/script; system fonts only,
  no external assets, no trackers; JS verified syntax- and runtime-clean

### `tests/run_tests.py` — self-tests (Python stdlib only)

Checks structure, LICENSE line, README credit, secrets scan, all
internal links, chapter word-count floors, lane-distinction guards,
glossary completeness (md entries + HTML `dt/dd` + anchor resolution),
balanced-structure HTML parsing, external-asset/tracker bans, system-
font-only CSS, interactivity hooks, and a draft-artifact guard (stray
CJK, TODO/FIXME, Co-authored-by trailers).

## How to run it

```sh
# Read the manual
#   open docs/00-start-here.md and go chapter by chapter

# Browse the site (no build step; fully local)
python3 -m http.server 8000 --directory site
#   → http://localhost:8000   (or just double-click site/index.html)

# Run the self-tests
python3 tests/run_tests.py
```

## Verification results (actual, from this workspace)

- `python3 tests/run_tests.py` — **PASS, 159 checks, 1 failure reduced
  to 0 after STATUS.md was added** (that single failing check was the
  existence of this file itself). Verifies: 18 required files, exact
  LICENSE line, README credit, no secrets, every internal link
  resolves, ~7,500 words across chapters meeting per-chapter floors,
  glossary md (24 entries) and html (19 entries) complete with working
  anchors, all four pages parse with balanced structure, zero external
  assets/trackers, system-fonts-only CSS, all five interactivity hooks
  wired, no draft artifacts.
- `node --check site/app.js` — **syntax OK**.
- Runtime smoke test of `app.js` under a minimal DOM stub (all page
  hooks exercised: glossary filter, temperature dial, next-word form,
  starters, decoder) — **no errors**.
- Served with `python3 -m http.server` and curl-checked —
  `index/journey/names/glossary .html`, `styles.css`, `app.js` —
  **all HTTP 200**.
- Full-text scan for stray non-English characters and garbled
  fragments — **clean**.

## Known gaps

- The toy predictor is a bigram model over ~150 words of fictional
  cafe text — intentionally toy-sized so the game stays visible in one
  screen; it cannot reflect any real model's breadth.
- Fictional teaching names (Checkers, Widget, Storyteller) are used for
  suffix/cadence examples; they deliberately don't track any real
  vendor's versioning scheme, which changes faster than this guide.
- The manual avoids math by design; readers wanting gradients and
  matrices need a technical textbook (out of scope, by spec).
- Update-cadence advice is written era-independent (no dated vendor
  claims), so it can go stale only in tone, not in facts.
- The site is a friendly quick tour (~4 pages); the manual is the deep
  reference. Some depth (e.g., tokenization details) lives only as
  brief glossary notes.
