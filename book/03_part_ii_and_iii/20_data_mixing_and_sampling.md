# Chapter 20 — Data Mixing and Sampling

**Part:** Part III

## Core idea
1. **Mixture weights** — Control how often source families appear.
2. **Temperature sampling** — Flatten or sharpen category probabilities.
3. **Epochs over a corpus** — Repeatedly sampling a small corpus increases exposure.
4. **Low-resource languages** — Need explicit measurement so representation is not dominated by high-resource data.

## Formal view
A temperature-style mixture can be written q_i∝p_i^α. α<1 flattens the distribution; α>1 sharpens it.

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
