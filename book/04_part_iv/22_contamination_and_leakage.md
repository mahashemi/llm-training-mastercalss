# Chapter 22 — Contamination and Leakage

**Part:** Part III

## Core concepts
1. **Train-test overlap** — Shared examples can inflate evaluation.
2. **Benchmark leakage** — Public benchmark text can enter training corpora.
3. **Temporal splits** — Time-based evaluation can test freshness better than random splits.
4. **Provenance tracing** — Record sources and exclusion rules.

## Formal view
If E_train∩E_eval is non-negligible, measured generalization can be biased upward. The practical remedy is detection, exclusion, and robust evaluation design.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://cs336.stanford.edu/
