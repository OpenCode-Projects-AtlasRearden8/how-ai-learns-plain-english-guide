# Glossary

Soft definitions in one or two calm sentences. The HTML version at
`site/glossary.html` has the same list, live-searchable.

- **Attention** — The reading step the model takes before each guess:
  it re-reads the whole conversation and weighs which parts matter
  right now. Like a good host glancing across the room before
  answering you.
- **Base model** — The raw, pre–finishing-school model: brilliant at
  continuing text, unreliable at answering questions. Plain model
  names (no suffix) usually mean this.
- **Benchmark** — A fixed exam with known answers used to score
  models. Covered properly by the companion project
  `ai-benchmarks-explained-guide`.
- **Cadence** — The rhythm of releases: big new vintages every few
  months per family, quiet kitchen re-seasoning in between (chapter 07).
- **Chat tuning** — The finishing-school training that turns a raw
  text-player into something that answers, clarifies, and declines.
- **Cloud model** — A model running on the provider's hardware; you
  send words to it and rent the seat. The counterpart is a local
  model on your own machine.
- **Context window** — How much text the model can re-read at once
  when making its guesses. Long conversations can leave early details
  faint.
- **Cutoff date** — The "last page" of the training library:
  everything after it is unknown to the model unless it's given a
  reading tool.
- **Fine-tune** — A narrower extra round of finishing school on top
  of an existing model, teaching a specialty (a style, a domain, a
  genre).
- **Frontier model** — Informal label for the most capable class
  available, which currently means cloud models.
- **Hallucination** — A confident, plausible answer where the truth
  was missing: the guess-the-next-word game filling an empty slot
  with a well-formed thing that doesn't exist.
- **Inference** — The seconds clock: the model answering, guess by
  guess, after its training clock has stopped.
- **Instruct model** — Same as a chat/Talk model: finished school.
  Usually the suffix `-Talk`/`-Chat`/`-Instruct` in a name.
- **Local model** — A model running on your own computer (e.g., via
  Ollama). It never re-seasons itself; updates are new downloads.
- **Parameter** — One adjustable setting inside the model; training
  nudged billions of them. The "dials" of the kitchen analogy.
- **Parameters (size)** — The B-number in a name: 7B ≈ seven billion
  settings. A size class, not a quality score.
- **Pretraining** — Chapter 02 in one word: the reading phase.
- **Prompt** — The words you send. Drafted well, they're your most
  durable tool, surviving model changes.
- **RLHF** — Reinforcement learning from human feedback; the tasting
  panel of chapter 04: humans pick between two replies, and the
  verdicts nudge the model's taste.
- **Release** — A finished, frozen model shipped under a name:
  the years clock boxed and labeled.
- **System prompt** — The hidden instructions that set a chat
  service's tone and rules, adjustable by the provider without
  announcing it.
- **Temperature** — The seasoning dial for word-choice adventure:
  low = predictable and starchy, high = lively and risky.
- **Token** — A word-chunk; models read and write in tokens, which is
  why they don't count letters well.
- **Training** — The years clock: billions of guess-the-next-word
  rounds across a giant library, nudging every parameter a hair at a
  time.
- **Version / vintage** — Which edition of the recipe you're talking
  to; a bump means the whole schooling was re-run (chapter 07).
