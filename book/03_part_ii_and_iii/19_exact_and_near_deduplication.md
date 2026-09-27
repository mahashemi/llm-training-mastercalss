# Chapter 19 — Exact and Near Deduplication

**Part:** Part III

## Core idea
1. **Exact dedup** — Remove identical documents or segments.
2. **Near dedup** — Cluster highly similar content.
3. **Contamination** — Train/evaluation overlap can inflate benchmark results.
4. **Memorization** — Repeated exposure changes the learning dynamics.

## Formal view
Deduplication changes sample frequency. For repeated document frequency f_i, the empirical gradient contribution can be distorted approximately in proportion to f_i.

## Practical method
Start with a baseline, change one major variable, measure quality and resource impact, inspect failures, and only then scale the experiment.

## Laboratory
[dedup_and_data_mixing.ipynb](../../notebooks/dedup_and_data_mixing.ipynb)

## Critical-thinking questions
**What is the tempting shortcut?** Apply the method before identifying the real bottleneck.  
**What is the answer?** Diagnose whether the limiting factor is data, objective, capacity, optimization, hardware, inference, or evaluation.  
**What evidence is required?** Versioned configuration, controlled comparison, target-specific metrics, representative failures, and explicit limitations.

## Research prompt
Design one controlled experiment that could falsify the central claim of this chapter.

## References
https://arxiv.org/abs/2402.00159
