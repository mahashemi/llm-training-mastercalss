# Chapter 26 — Continued Pretraining

**Part:** Part IV

## Core concepts
1. **Domain adaptation** — Continue language-model training on a new distribution.
2. **Learning rate** — Usually lower than an aggressive from-scratch recipe.
3. **Forgetting** — Strong domain adaptation can reduce performance outside the target domain.
4. **Mixture retention** — Mix general and domain data when maintaining broad capability matters.

## Formal view
Continued pretraining minimizes the same or related language-model loss on a new corpus, changing θ from θ_0 to θ_1 under a new data distribution.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://cs336.stanford.edu/
