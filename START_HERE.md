# Start Here

The repository contains deep reference material, but the learner path is intentionally simple: **README → Lecture 01 → Lecture 02 → … → Lecture 24**. Each lecture owns its primary laboratory, real-data connection, decision exercise, and evidence.

You do not need to open the textbook, notebook index, or runbook to complete the core course. Those are optional reference layers.

## Your first 90 minutes

### 1. Orient — 10 min

Read:
Start directly with [Lecture 01 — What Is an LLM?](lectures/01_what_is_an_llm/lecture.md).

The goal is to learn the recurring workflow:

**inspect → estimate → load → baseline → smoke test → train → evaluate → break → report → scale**

### 2. Lecture 01 — 25 min

Read:
[Lecture 01 — What Is an LLM?](lectures/01_what_is_an_llm/lecture.md)

### 3. Run the embedded laboratory

Open the lab directly from Lecture 01: [run the Lecture 01 lab](lectures/01_what_is_an_llm/lab.ipynb).

The lab is part of the lecture—not a separate course resource.

### 4. Exit test

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
