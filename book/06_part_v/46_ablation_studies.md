# Chapter 46 — Ablation Studies

**Part:** Part V

## 1. An ablation asks “what caused the gain?”

Suppose a new model improves benchmark score by 4%.

Without an ablation, you do not know whether the gain came from:

- more data;
- better filtering;
- larger model;
- longer training;
- different tokenizer;
- better optimizer;
- better post-training.

An ablation removes or changes one cause while holding the rest as constant as practical.

## 2. Basic design

| Run | Data | Model | Training | Intervention |
|---|---|---|---|---|
| Baseline | D | M | T | none |
| A | D' | M | T | data change |
| B | D | M' | T | model change |
| C | D | M | T' | training change |

Compare each against the baseline.

## 3. Keep the comparison fair

Record:

- dataset version;
- token count;
- model parameters;
- tokenizer;
- training tokens;
- optimizer;
- learning-rate schedule;
- batch size;
- sequence length;
- precision;
- compute budget;
- evaluation protocol.

If several variables change, causal interpretation weakens.

## 4. Compute-aware ablation

A quality-only table is incomplete.

| Run | Quality | GPU-hours | Cost | p95 latency |
|---|---:|---:|---:|---:|
| Baseline | 78 | 10 | 50 | 180 ms |
| A | 80 | 12 | 60 | 190 ms |
| B | 81 | 30 | 150 | 180 ms |
| C | 79.5 | 11 | 55 | 140 ms |

A gives +2 points for small cost; B gives +3 but at much higher training cost; C trades quality for serving speed.

The useful analysis is **quality vs resources**, not quality alone.

## 5. Interaction effects

When two factors may interact, use a small factorial design.

For factors A and B:

interaction ≈
f(A,B) - f(A,baseline) - f(baseline,B) + f(baseline,baseline)

A positive interaction means the combination produces more gain than the simple sum of the individual effects.

## 6. Example — data filtering × model size

| Run | Model | Filter | Score |
|---|---|---|---:|
| 1 | small | off | 70 |
| 2 | small | on | 73 |
| 3 | large | off | 76 |
| 4 | large | on | 80 |

The filtering gain is 3 points for the small model but 4 for the large model.

That suggests an interaction worth investigating.

## 7. Repeated runs

Training has randomness.

When the expected effect is small, repeat runs with controlled seeds or report uncertainty.

Do not infer a strong effect from one run differing by 0.3 points when run-to-run variation is 0.4 points.

## 8. Negative ablations are valuable

A failed intervention can eliminate a bad hypothesis.

Example:

**Hypothesis:** adding 20% synthetic data improves reasoning.

Result:

- benchmark unchanged;
- rare-case failures increase.

The negative result prevents spending more compute on the same assumption.

## 9. Research exercise

Design a 2×2 experiment:

- factor A = dataset filtering;
- factor B = model size.

Measure:

- target score;
- validation loss;
- GPU-hours;
- cost;
- p95 latency.

Estimate the interaction and explain whether the larger model changes the value of filtering.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
