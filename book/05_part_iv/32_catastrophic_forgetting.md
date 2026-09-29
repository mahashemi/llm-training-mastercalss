# Chapter 32 — Catastrophic Forgetting

**Part:** Part IV

## 1. The central trade-off

Adaptation can improve a target distribution while degrading previously useful behavior.

Let:

L_target(theta)

be target-domain loss and:

L_general(theta)

be retained/general loss.

A successful adaptation is not merely lower L_target. It is:

**target improvement subject to an acceptable regression constraint.**

## 2. What can cause forgetting?

| Cause | Example | Diagnostic |
|---|---|---|
| Narrow data | only specialist text | compare with mixed replay |
| High learning rate | aggressive update | LR sweep |
| Too many tokens/epochs | repeated small corpus | checkpoint trajectory |
| Distribution shift | domain far from base | mixture experiment |
| Strong adapter | high-rank/large update | rank/scale sweep |
| Objective shift | unusual labels/preferences | retained-task eval |

## 3. Evaluation matrix

Track at least:

| Model | Target | General | Language | Safety | Robustness |
|---|---:|---:|---:|---:|---:|
| Base | 70 | 88 | 76 | 91 | 80 |
| Adapted | 82 | 83 | 70 | 89 | 76 |

The target gain is real, but several regressions appear.

## 4. Replay/mixing experiment

Compare:

| Run | Target data | General replay | Target score | General score |
|---|---:|---:|---:|---:|
| A | 100% | 0% | measure | measure |
| B | 75% | 25% | measure | measure |
| C | 50% | 50% | measure | measure |

Keep total training budget comparable.

The result gives an empirical target-vs-retention curve.

## 5. Checkpoint trajectory matters

Do not evaluate only the final checkpoint.

Example:

| Step | Target | General |
|---:|---:|---:|
| 0 | 70 | 88 |
| 1k | 76 | 87 |
| 2k | 80 | 86 |
| 4k | 82 | 82 |
| 8k | 83 | 77 |

The trajectory suggests an earlier checkpoint may provide a better trade.

## 6. Forgetting vs intentional specialization

Not every regression is bad.

A model dedicated to one narrow task may intentionally sacrifice unrelated capabilities.

Therefore predeclare:

- which capabilities must be retained;
- which may change;
- acceptable regression.

## 7. Practical mitigation

Candidate mechanisms:

- mix general replay data;
- lower learning rate;
- reduce training duration;
- regularize updates;
- use PEFT;
- select an earlier checkpoint;
- distill retained capabilities where appropriate.

Test the mechanism rather than assuming it works.

## Research exercise

Design a 3×3 experiment across:

**adaptation strength × replay fraction**

Measure target score and retained capability.

Plot the frontier and identify the region where additional target gain begins to create unacceptable regression.

## Laboratory

[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Reference

https://cs336.stanford.edu/

## Deepening: regression must be measured explicitly

Catastrophic forgetting is not “the model got worse” in the abstract.

Define a protected evaluation suite representing capabilities that must remain acceptable.

### Experiment

Evaluate:

- base;
- adapted model;
- optionally a weaker/stronger adaptation.

Report target gain and protected-task regression together.

### Useful metric

For a protected metric M:

**regression = M_adapted − M_base**

with the sign interpreted according to the metric.

### Failure mode

The target score improves because the evaluation set is narrow while a protected capability quietly collapses.

### Engineering decision

Define a regression threshold before training. If exceeded, test:

- lower learning rate;
- fewer steps;
- broader data;
- replay/mixed data;
- weaker adapter capacity.
