# Chapter 32 — Catastrophic Forgetting

**Part:** Part IV

## Core concepts
1. **Domain overfitting** — A model can become better on a domain while losing general capability.
2. **Replay** — Mix representative general data during adaptation.
3. **Evaluation matrix** — Evaluate both target and retained capabilities.
4. **Checkpoint comparison** — Compare base, intermediate, and final checkpoints.

## Formal view
Let L_target(θ) and L_general(θ) be losses on target and general distributions. Adaptation is successful only if the target improvement outweighs unacceptable general regressions for the stated objective.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://cs336.stanford.edu/
