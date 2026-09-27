# Chapter 16 — Gradient Accumulation and Effective Batch Size

**Part:** Part I

## Core idea
1. **Micro-batch** — Batch that fits on one accelerator step.
2. **Accumulation** — Sum/average gradients over several micro-batches before updating.
3. **Global batch** — Effective batch across devices and accumulation steps.

## Formal view
Effective batch size ≈ micro_batch × data_parallel_world_size × accumulation_steps, subject to padding/packing conventions.

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
https://cs336.stanford.edu/
