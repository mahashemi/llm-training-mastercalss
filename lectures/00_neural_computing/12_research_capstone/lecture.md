# Course 1 · Chapter 12 — Research Capstone: From Observation to Evidence

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the publication capstone](./lab.ipynb)

## 1. Start with a falsifiable question

“Try a bigger model” is not a research question.

A defensible question identifies an independent variable and measurable outcome:

$$
\text{intervention}
\rightarrow
\text{measurable outcome}.
$$

Example:

> At approximately equal parameter count, does adding a nonlinear hidden representation improve held-out accuracy?

That can be contradicted by evidence.

## 2. Freeze the evaluation contract

Before changing the model, specify:

- dataset and provenance;
- train/validation/test split;
- primary metric;
- baseline;
- intervention;
- compute/training budget;
- seeds;
- stopping rule.

This prevents the evaluation from drifting toward whichever result looks best.

## 3. Observation, explanation, claim

Suppose Model B scores 91% and Model A scores 89%.

**Observation:** B scored higher under the measured protocol.

**Explanation:** perhaps its representation is better, but this is a mechanism hypothesis.

**Claim:** B improves this task under the stated conditions.

Do not silently jump from the first statement to the third.

## 4. Intervention and ablation

A useful experiment has a baseline

$$
B
$$

and a controlled intervention

$$
B+\Delta.
$$

An ablation removes the proposed mechanism while preserving as much else as possible.

If the effect disappears under the ablation, the evidence that the mechanism mattered becomes stronger.

## 5. Uncertainty

For repeated measurements $x_1,\ldots,x_n$, report the mean

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

and sample standard deviation

$$
s=
\sqrt{
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
}.
$$

A table containing only the best seed hides important uncertainty.

## 6. Error analysis

Aggregate metrics hide mechanisms.

Inspect:

- false positives and false negatives;
- difficult examples;
- distribution-shift failures;
- confidence/calibration;
- resource regressions.

An error table should classify failures by mechanism rather than merely listing examples.

## 7. Paper-ready structure

A compact research report follows:

**Abstract → Introduction → Related Work → Method → Experimental Setup → Results → Error Analysis → Limitations → Conclusion → Reproducibility.**

A result does not need to be novel to be useful. A careful reproduction, negative result, benchmark, ablation, or efficiency study can be a legitimate research contribution when the question and evidence are clear.

## Laboratory — run the experiment end to end

**[Open the executable laboratory](./lab.ipynb)**

This notebook is the chapter's final research artifact, not optional homework. Follow the complete research loop: **state a question → freeze the protocol → establish a baseline → intervene → measure → inspect errors → produce the results table → bound the claim → propose the next falsifiable experiment.**

You will leave with a reproducible mini-study rather than a single model score. The final cells contain the answer key and a research extension.

## Mastery questions

1. What makes a research question falsifiable?
2. Why freeze the evaluation contract?
3. What is the difference between observation and explanation?
4. Why are ablations valuable?
5. Why report uncertainty?

### Answers

1. A plausible outcome can be contradicted by a defined measurement.
2. Otherwise the evaluation can drift toward the result that looks best.
3. Observation is what happened; explanation is a proposed mechanism for why.
4. Ablations test whether the proposed mechanism contributes to the observed effect.
5. To distinguish systematic effects from stochastic variation.

## Final Course 1 standard

A learner is ready for Course 2 when they can:

**derive → implement → measure → break → explain → decide → reproduce.**

[← Previous](../11_deep_reinforcement_learning/lecture.md) · [Course 1 home](../README.md) · [Continue to Course 2 →](../../02_llm_engineering_and_training/README.md)
