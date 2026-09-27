# Start Here

## Your first 90 minutes

### 1. Lecture — 25 min
Read:
[Lecture 01 — What Is an LLM?](lectures/01_what_is_an_llm/lecture.md)

Goal: understand language modeling, next-token prediction, logits, cross-entropy, training versus inference.

### 2. Video — selected segments
Open:
[Lecture 01 video companions](videos/01_lecture_01_video_companions.md)

Primary video: Andrej Karpathy, *Let's build GPT from scratch*.

Recommended first segment: 00:00–35:00, then return to the lab.

### 3. Laboratory — 30–45 min
Open:
[Notebook 01 — Next-token prediction and a tiny language model](notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

Use Google Colab or a local Jupyter environment.

The lab intentionally starts with a bigram model. Do not skip it: it makes the objective and training loop visible before Transformer abstractions are introduced.

### 4. Textbook — 15–20 min
Read:
[Chapter 1 — A Language Model Is a Probability Model](book/01_language_models_without_magic/01_a_language_model_is_a_probability_model.md)

### 5. Exit test

Without looking back, explain:

1. What is a token?
2. What does the model predict?
3. What is a logit?
4. Why do we use cross-entropy?
5. What changes during training?
6. Why is generation autoregressive?
7. Why is a bigram model useful even though it is not an LLM?

If you cannot explain these cleanly, repeat the lab before moving on.

## What comes next

The sequence is deliberate:

**language modeling → tokenization → embeddings → attention → Transformer → tiny GPT → data engineering → pretraining → scaling → fine-tuning → evaluation → serving → build-vs-buy → LLM program design**

Do not jump straight to LoRA. We are building the mental model needed to know when LoRA is, and is not, the right answer.
