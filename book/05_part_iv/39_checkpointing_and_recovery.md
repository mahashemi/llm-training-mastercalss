# Chapter 39 — Checkpointing and Recovery

**Part:** Part III

## Core concepts
1. **State capture** — Save model, optimizer, scheduler, scaler, and progress state as required.
2. **Frequency** — Checkpoint cadence trades storage/overhead against recovery loss.
3. **Integrity** — Verify that checkpoints can actually be restored.
4. **Resume tests** — A checkpoint that cannot resume is not a reliable checkpoint.

## Formal view
Expected lost work under random failure is roughly related to checkpoint interval; optimal cadence balances recompute cost and checkpoint overhead.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://cs336.stanford.edu/
