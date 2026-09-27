# Chapter 61 — API Privacy and Data Governance

**Part:** Part VII

## Core concepts
1. **Data boundary** — Know what data leaves the organization and where it is stored.
2. **Retention** — Understand provider and internal retention terms before deployment.
3. **Access control** — Restrict tools and retrieved documents by identity and policy.
4. **Auditability** — Log inputs/outputs safely enough to investigate failures.

## Formal view
Risk exposure is a function of data sensitivity, provider controls, retention, access patterns, and application architecture. These must be assessed together.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://cs336.stanford.edu/
