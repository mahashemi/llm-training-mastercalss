# Chapter 13 — Mixture of Experts

**Part:** Part I

## Core idea
1. **Sparse activation** — Only a subset of experts executes for each token.
2. **Router** — A learned or specified gate selects experts.
3. **Load balancing** — Uneven routing can waste capacity and create system bottlenecks.
4. **Expert parallelism** — Experts may be distributed across devices.

## Formal view
If k experts are activated from E total experts, nominal active compute can be much smaller than dense E-way computation, but routing and communication add cost.

## Practical method
Start with a baseline, change one major variable, measure quality and resource impact, inspect failures, and only then scale the experiment.

## Laboratory
[attention_and_moe_lab.ipynb](../../notebooks/attention_and_moe_lab.ipynb)

## Critical-thinking questions
**What is the tempting shortcut?** Apply the method before identifying the real bottleneck.  
**What is the answer?** Diagnose whether the limiting factor is data, objective, capacity, optimization, hardware, inference, or evaluation.  
**What evidence is required?** Versioned configuration, controlled comparison, target-specific metrics, representative failures, and explicit limitations.

## Research prompt
Design one controlled experiment that could falsify the central claim of this chapter.

## References
https://cs336.stanford.edu/
