# Chapter 47 — Statistical Thinking for LLM Evaluation

**Part:** Part V

## 1. A benchmark score is an estimate

If a model solves 80 of 100 evaluation examples, the observed accuracy is 80%.

It is not “the true model accuracy.” It is an estimate under a sampling and measurement process.

That distinction becomes important when comparing small improvements.

## 2. Standard error for a proportion

For a proportion p measured over n approximately independent examples:

SE ≈ sqrt[p(1-p)/n]

Example:

p = 0.80, n = 400

SE ≈ 0.02

A rough 95% interval using ±1.96 SE is approximately:

0.80 ± 0.039

The independence assumption may fail when examples are clustered or related. Use bootstrap or clustered methods when appropriate.

## 3. Paired evaluation is powerful

When models A and B answer the same examples, use the paired differences.

For a binary metric:

d_i = score_B(i) - score_A(i)

Then analyze the distribution of d_i.

Benefits:

- controls for example difficulty;
- reduces irrelevant sampling variation;
- directly measures improvement on shared cases.

## 4. Bootstrap

A simple paired bootstrap:

1. sample evaluation examples with replacement;
2. calculate mean paired difference;
3. repeat many times;
4. take empirical quantiles.

The resulting interval estimates uncertainty in the observed effect under the sampled population.

## 5. Statistical vs practical significance

Suppose:

- baseline = 80.0%;
- candidate = 80.4%;
- many millions of examples make the difference statistically detectable.

That does not mean the 0.4-point gain justifies:

- retraining;
- higher serving cost;
- added latency;
- operational complexity.

Decision-making needs both:

**statistical evidence + practical value**

## 6. Multiple slices

Suppose a model improves:

| Slice | Delta |
|---|---:|
| English | +2.0 |
| Language A | +1.0 |
| Language B | −3.0 |
| Safety | −1.5 |

The aggregate may improve while an important slice regresses.

Correct for multiple comparisons where appropriate, but more importantly, predefine critical slices that have their own release gates.

## 7. Paired example

Suppose 200 paired cases are evaluated:

- candidate wins on 112;
- baseline wins on 78;
- tie on 10.

Ignoring ties for a simple illustration:

candidate win rate = 112 / (112 + 78) = 58.9%

Then inspect uncertainty and the examples responsible for the difference.

## 8. Human annotation uncertainty

For subjective evaluation, uncertainty includes:

- sampling uncertainty;
- annotator disagreement;
- rubric ambiguity;
- judge/model variance.

Do not pretend a score has one source of error.

## 9. Sequential evaluation

Repeatedly checking a benchmark during training can bias interpretation if the same set guides many decisions.

Use:

- development set for iteration;
- validation set for selection;
- protected test set for final claims.

This helps prevent overfitting the research process to the measurement instrument.

## Research exercise

Create a paired evaluation with 500 examples.

Compute:

- score A;
- score B;
- mean paired difference;
- bootstrap interval;
- slice-specific differences.

Then write two conclusions:

1. statistical conclusion;
2. engineering conclusion.

They should not automatically be identical.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
