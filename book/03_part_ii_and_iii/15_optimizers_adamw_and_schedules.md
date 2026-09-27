# Chapter 15 — Optimizers: AdamW and Schedules

**Part:** Part I

## Core idea
1. **Adam moments** — Track running first and second moments of gradients.
2. **Decoupled weight decay** — AdamW separates weight decay from the adaptive update.
3. **Warmup** — Avoid overly large early updates.
4. **Cosine decay** — Commonly reduces learning rate over a long training run.

## Formal view
Adam maintains m_t and v_t; AdamW applies decoupled decay. Schedules turn one hyperparameter into a time-varying control signal.

## Practical method
Start with a baseline, change one major variable, measure quality and resource impact, inspect failures, and only then scale the experiment.

## Laboratory
[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Critical-thinking questions
**What is the tempting shortcut?** Apply the method before identifying the real bottleneck.  
**What is the answer?** Diagnose whether the limiting factor is data, objective, capacity, optimization, hardware, inference, or evaluation.  
**What evidence is required?** Versioned configuration, controlled comparison, target-specific metrics, representative failures, and explicit limitations.

## Research prompt
Design one controlled experiment that could falsify the central claim of this chapter.

## References
https://arxiv.org/abs/1711.05101
