# Experiment → Program

A serious LLM initiative grows through progressively more expensive evidence.

## Stage 0 — Hypothesis

Define:

**capability → population → metric → constraint**

## Stage 1 — Baseline

Measure the strongest existing practical approach.

Record model, prompt, retrieval/tools where applicable, evaluation, latency, and cost.

## Stage 2 — Cheap intervention

Try:

**prompting / structured output / RAG / tools**

This isolates whether the gap is contextual or behavioral.

## Stage 3 — Small open-weight training

Use a real small checkpoint on free Colab or a small GPU.

Run:

**baseline → SFT/PEFT → regression evaluation**

## Stage 4 — Representation/data study

When evidence suggests domain/language exposure is the bottleneck, test continued pretraining and tokenizer/data hypotheses on a small controlled model.

## Stage 5 — Scaling experiment

Move the same workload to larger checkpoints/H100s.

Measure:

**tokens/sec + memory + scaling efficiency + quality + cost**

## Stage 6 — Pilot system

Integrate:

**data + model + evaluation + serving + monitoring + governance**

## Stage 7 — Program

Only after earlier evidence exists should the proposal include:

**large infrastructure + staffing + multi-year budget + from-scratch pretraining**

## Gate principle

At each stage ask:

> What evidence must exist before we release more resources?

Also define what evidence would stop the program.

This converts a hardware acquisition exercise into an evidence-generating engineering program.
