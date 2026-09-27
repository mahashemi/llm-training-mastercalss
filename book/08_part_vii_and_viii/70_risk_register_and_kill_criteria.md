# Chapter 70 — Risk Register and Kill Criteria

**Part:** Part VIII

## Core concepts
1. **Technical risk** — Training instability, data quality, or insufficient capability.
2. **Program risk** — Staffing, schedule, procurement, or budget.
3. **Evaluation risk** — Cannot demonstrate progress credibly.
4. **Kill criteria** — Predefined conditions that stop or redirect spending.

## Formal view
Define risk r_i with probability p_i and impact I_i, then prioritize mitigation by expected exposure p_iI_i while recognizing that rare catastrophic risks need separate handling.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[capstone_model_program.ipynb](../../notebooks/capstone_model_program.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://cs336.stanford.edu/
