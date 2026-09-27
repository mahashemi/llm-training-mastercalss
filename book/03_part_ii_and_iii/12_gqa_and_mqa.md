# Chapter 12 — GQA and MQA

**Part:** Part I

## Core idea
1. **KV sharing** — Multiple query heads can share fewer key/value heads.
2. **Serving tradeoff** — Fewer KV heads reduce cache size and memory bandwidth requirements.
3. **Quality tradeoff** — Sharing changes the representational degrees of freedom and must be evaluated.

## Formal view
KV cache scales roughly with 2·B·H_kv·T·d_head·bytes. Reducing H_kv reduces inference memory for a fixed query-head count.

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
https://arxiv.org/abs/1911.02150
