# Chapter 34 — Preference Data

**Part:** Part IV

## 1. Preference data defines what “better” means

A preference dataset contains a prompt x and two or more candidate responses.

The annotation answers a question such as:

**Which response better satisfies the stated rubric?**

Without a precise rubric, the model learns whatever correlates with the label.

## 2. Preference dimensions

| Dimension | Better response | Common annotation failure |
|---|---|---|
| Correctness | factually accurate | chooses confident wording |
| Helpfulness | solves the task | rewards verbosity |
| Grounding | supported by evidence | rewards citations regardless of support |
| Safety | appropriate safeguards | over-rewards refusal |
| Style | desired format/tone | style dominates substance |
| Concision | sufficient information | short but incomplete wins |

The rubric must state which dimensions dominate when they conflict.

## 3. Pair construction

Strong pair:

**chosen:** correct + concise + supported  
**rejected:** plausible + unsupported

Weak pair:

**chosen:** 400 words  
**rejected:** 100 words

The weak pair teaches length, not quality.

## 4. Annotation protocol

Document:

- task definition;
- rubric;
- anchor examples;
- tie policy;
- annotator training;
- sampling;
- blinding/order randomization;
- disagreement handling.

## 5. Agreement and uncertainty

Do not force a preference when the difference is genuinely ambiguous.

Track:

- agreement;
- tie rate;
- disagreement by language/task;
- examples requiring adjudication.

High disagreement can indicate that the rubric is not operationally clear.

## 6. Worked example

500 examples:

- chosen = safety-correct;
- rejected = more direct but unsafe.

If annotators agree 92%, the preference signal is relatively clear.

Now build a second set where both responses are safe but differ in helpfulness. If agreement falls to 62%, the rubric may need refinement.

The model should not be trained as though both datasets have equal label reliability.

## 7. Dataset balance

Track the distribution of preferences:

- safety;
- correctness;
- verbosity;
- style;
- refusal;
- language;
- difficulty.

Otherwise one easy-to-annotate preference dimension can dominate training.

## 8. Research exercise

Create 2,000 preference pairs.

Stratify them by:

**correctness / safety / helpfulness / style**

Then run a small DPO experiment with:

- balanced mixture;
- correctness-heavy mixture;
- style-heavy mixture.

Measure which behavioral dimensions move.

## Laboratory

[dpo_and_distillation_concepts.ipynb](../../notebooks/dpo_and_distillation_concepts.ipynb)

## Reference

https://arxiv.org/abs/2305.18290

## Deepening: preference datasets are measurement instruments

A preference label is a claim:

**chosen response is preferable under a rubric**

Therefore dataset construction must define the rubric.

### Pair taxonomy

Annotate why one response wins:

- correctness;
- groundedness;
- safety;
- concision;
- formatting;
- reasoning quality;
- style.

A pair can encode multiple correlated attributes.

### Experiment

Create two preference sets:

1. balanced multi-attribute rubric;
2. style-heavy rubric.

Train under similar budgets.

Measure:

- target quality;
- verbosity;
- factuality;
- safety;
- refusal behavior.

### Failure mode

The model learns the easiest observable proxy, such as length or politeness, rather than the intended quality criterion.
