# Start Here

The repository is intentionally large because it contains the **textbook, 24 lectures, executable laboratories, operational runbooks, research materials, and projects**. You should not approach these as six separate courses.

Start from the **[Master Course Flow in the README](README.md#master-course-flow--the-one-path-through-the-repository)**. It gives the natural dependency order and tells you which book chapters, lecture IDs, and primary labs belong to each stage.

## Your first 90 minutes

### 1. Orient — 10 min

Read:
[Chapter 00 — The Open-Weight Training Path](book/00_open_weight_training_path.md)

Then open:
[Open-Weight Model Audit](notebooks/open_weight_model_audit.ipynb)

The goal is to learn the recurring workflow:

**inspect → estimate → load → baseline → smoke test → train → evaluate → break → report → scale**

### 2. Lecture 01 — 25 min

Read:
[Lecture 01 — What Is an LLM?](lectures/01_what_is_an_llm/lecture.md)

### 3. Laboratory — 30–45 min

Open:
[Notebook 01 — Next-token prediction and a tiny language model](notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

The lab starts with a bigram model so the objective and training loop are visible before Transformer abstractions.

### 4. Textbook — 15–20 min

Read:
[Chapter 01 — A Language Model Is a Probability Model](book/01_language_models_without_magic/01_a_language_model_is_a_probability_model.md)

### 5. Exit test

Without looking back, explain:

1. token;
2. next-token objective;
3. logit;
4. cross-entropy;
5. training versus inference;
6. why generation is autoregressive;
7. why the tiny model is useful.

## What comes next

Follow the README's stage order:

**foundations → training systems → evaluation contract → real data → train/adapt → alignment → safety/multimodality → serving/engineering decisions → program/research**

Do not jump straight to LoRA. By the time you reach parameter-efficient fine-tuning, you should understand the model, data, resource, evaluation, and failure trade-offs that make the technique useful.
