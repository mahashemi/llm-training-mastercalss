# Chapter 67 — Team Design for LLM Programs

**Part:** Part VIII

## Core concepts
1. **Research** — Architecture, data, optimization, and evaluation scientists.
2. **Engineering** — Training systems, data pipelines, serving, reliability.
3. **Language/domain experts** — Quality, cultural context, terminology, evaluation.
4. **Program management** — Budget, vendors, milestones, compliance, communication.

## Formal view
Organizational capacity is a resource constraint just like GPU memory. Critical single points of failure should be identified and mitigated.

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
