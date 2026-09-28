# Chapter 44 — Model-as-Judge Evaluation

**Part:** Part V

## 1. A judge is another model, not ground truth

A model-as-judge maps:

J(x, y, rubric) → score or preference

It can scale evaluation, but it may share biases with the candidate model or reward properties unrelated to the real task.

Therefore judge evaluation must be **calibrated against trusted human labels**.

## 2. Judge design

| Decision | Options | Risk |
|---|---|---|
| Output | score / pairwise / ranking | scale instability |
| Prompt | fixed rubric | prompt sensitivity |
| Model | one judge / multiple | correlated bias |
| Context | blinded / unblinded | identity leakage |
| Evidence | answer only / source + answer | judge may infer unsupported facts |
| Aggregation | mean / majority / calibrated probability | hides uncertainty |

## 3. Calibration protocol

Create a human-labeled calibration set.

Then measure:

- judge-human agreement;
- false-positive rate;
- false-negative rate;
- agreement by language;
- agreement by task;
- sensitivity to verbosity;
- sensitivity to answer order.

If the judge disagrees systematically on one slice, do not silently use the aggregate judge score.

## 4. Pairwise judging

For model A and B on the same prompt x:

judge(x, A(x), B(x)) → A wins / B wins / tie

Use randomized ordering.

A useful report is:

| Slice | A wins | B wins | Tie |
|---|---:|---:|---:|
| General | 52% | 43% | 5% |
| Target language | 41% | 55% | 4% |
| Safety | 38% | 57% | 5% |

An overall number can hide systematic slice differences.

## 5. Position and verbosity bias

Potential confounders:

- first-answer preference;
- longer-answer preference;
- formatting preference;
- model-family familiarity.

Mitigations:

- randomize order;
- normalize presentation where appropriate;
- test short vs long answers;
- include controlled synthetic pairs.

## 6. Worked calibration

Suppose 1,000 human-labeled pairwise cases exist.

The judge agrees on 870:

agreement = 87%

But by language:

| Language | Agreement |
|---|---:|
| L1 | 93% |
| L2 | 91% |
| L3 | 74% |
| L4 | 89% |

The judge may be unsuitable as the sole evaluator for L3.

## 7. Judge ensembles

Using multiple judges can reduce one-model idiosyncrasies, but judges can share the same bias.

Therefore compare:

**one judge → multiple judges → human subset**

and measure marginal benefit per evaluation cost.

## 8. Judge cost

Judge TCO is:

C_judge =
judge inference
+ prompt/context tokens
+ engineering
+ calibration
+ human auditing

For millions of evaluations, judge cost can become substantial.

## 9. Appropriate use

Model-as-judge is valuable for:

- rapid iteration;
- large-scale candidate filtering;
- error triage;
- continuous regression monitoring.

It should not be the only source of truth for high-stakes release decisions unless validated for the specific task.

## Research exercise

Create 500 human-labeled pairwise cases.

Calibrate two judge models.

Report:

- agreement;
- disagreement by language/task;
- cost/evaluation;
- sensitivity to answer ordering.

Then design a hybrid human + judge evaluation strategy.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
