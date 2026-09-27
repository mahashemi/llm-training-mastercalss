# Chapter 59 — Tool Use and Agents

**Part:** Part VII

## Core concepts
1. **Tool specification** — Define schemas and valid arguments.
2. **Execution** — Perform actions outside the model.
3. **Observation loop** — Feed tool results back into the context.
4. **Reliability** — Validate arguments, permissions, and side effects.

## Formal view
An agent can be represented as a policy over actions a_t conditioned on state/context s_t. Tool correctness therefore becomes part of system evaluation.

## Practice
Define the operational objective, freeze the baseline, run the smallest informative experiment, record resource use, inspect failures, and decide whether the next intervention is justified.

## Laboratory
[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Critical thinking
**Question:** What can a benchmark or metric hide?  
**Answer:** Distribution shift, severe but rare failures, cost/latency regressions, and behavior outside the tested task.

**Question:** What makes this research-grade?  
**Answer:** Clear hypothesis, controlled comparison, versioned inputs, reproducible procedure, quantitative evidence, uncertainty/limitations, and enough detail for another team to repeat it.

## Research prompt
Propose one ablation and one failure-analysis experiment.

## References
https://docs.vllm.ai/en/stable/
