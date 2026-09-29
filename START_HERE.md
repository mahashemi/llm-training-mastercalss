# Start Here

## Your first 90 minutes

### 1. Lecture — 25 min

Read:
[Lecture 01 — What Is an LLM?](lectures/01_what_is_an_llm/lecture.md)

### 2. Real model orientation — 10 min

Open:
[Open-Weight Training Ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md)

Understand the progression:

**tiny GPT → Qwen3-0.6B → larger open weights → H100 → multi-GPU**

The goal is to learn one workflow at multiple scales.

### 3. Video — selected segments

Open:
[Lecture 01 video companions](videos/01_lecture_01_video_companions.md)

Watch only the assigned segment, then return to the lab.

### 4. Laboratory — 30–45 min

Open:
[Notebook 01 — Next-token prediction and a tiny language model](notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

Use Colab or local Jupyter.

The lab starts with a bigram model so the objective and training loop are visible before Transformer abstractions.

### 5. Textbook — 15–20 min

Read:
[Chapter 1 — A Language Model Is a Probability Model](book/01_language_models_without_magic/01_a_language_model_is_a_probability_model.md)

See the full companion crosswalk:
[Book ↔ Lecture ↔ Laboratory Map](BOOK_LAB_MAP.md)

### 6. Exit test

Without looking back, explain:

1. token;
2. next-token objective;
3. logit;
4. cross-entropy;
5. training versus inference;
6. why generation is autoregressive;
7. why the tiny model is useful.

### What comes next

**language modeling → tokenization → resource accounting → Transformer → attention → GPU kernels → distributed training → scaling → data → open-weight SFT/PEFT → evaluation → serving → architecture decisions → program design**

Do not jump straight to LoRA. The course is designed so that by the time students use LoRA they understand the problem it is solving.
