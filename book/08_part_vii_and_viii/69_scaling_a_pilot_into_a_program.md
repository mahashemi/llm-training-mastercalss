# Chapter 69 — Scaling a Pilot Into a Program

**Part:** Part VIII

## Core concepts
1. **Pilot** — Prove the target capability and measurement protocol.
2. **Ablation** — Determine what actually drives the improvement.
3. **Scale decision** — Spend more compute only after the pilot reduces key uncertainty.
4. **Milestones** — Attach resources to measurable outputs.

## Formal view
A good program increases scale only when evidence supports it. This is an adaptive experiment budget, not a fixed hardware shopping list.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://cs336.stanford.edu/
