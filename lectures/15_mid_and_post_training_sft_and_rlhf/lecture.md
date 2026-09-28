# Lecture 15 — Mid and Post Training: SFT, RLHF, and the Post-Training Stack

**Duration:** 25 minutes  
**Primary anchor:** https://arxiv.org/abs/2203.02155

## Learning outcome

By the end, the learner can distinguish:

**continued pretraining → SFT → preference optimization/RLHF**

and decide which stage addresses a measured failure.

## 0–4 — Why “train the model more” is ambiguous

Start with three failures:

1. The model does not know a specialist domain.
2. The model knows the domain but ignores the required response format.
3. The model follows the format but prefers unsafe or unhelpful responses.

Ask whether one training method should solve all three.

Reveal:

| Failure | Likely intervention |
|---|---|
| Broad domain/language exposure | continued pretraining |
| Stable behavior | SFT / PEFT |
| Preference trade-offs | DPO / RLHF-style methods |

## 4–8 — The post-training stack

Draw:

**base model**  
↓  
**continued pretraining (optional)**  
↓  
**SFT**  
↓  
**preference optimization**  
↓  
**evaluation + safety**  
↓  
**serving**

Explain that stages are composable, not mandatory.

## 8–13 — SFT in concrete terms

SFT learns from:

**input → desired response**

Show a bad dataset:

- repetitive prompts;
- low-quality answers;
- only easy cases;
- no refusal/uncertainty examples.

Then a good coverage matrix:

| Dimension | Examples |
|---|---|
| intent | factual / advisory / procedural |
| difficulty | easy / medium / hard |
| language | L1 / L2 / L3 |
| output | prose / JSON / table |
| safety | ordinary / edge / refusal |

Explain:

**dataset composition = gradient pressure on behavior.**

## 13–17 — Preference optimization vs RLHF

| Property | SFT | DPO-style preference optimization | Classic RLHF |
|---|---|---|---|
| Data | targets | chosen/rejected | preferences + rollouts |
| Reward model | no | no | yes |
| Online loop | no | usually no | yes |
| Complexity | low | medium | high |
| Main risk | imitation errors | preference bias | reward hacking/stability |

Key lesson:

A more complex training loop is justified only when it solves a problem the simpler loop cannot.

## 17–20 — Worked example

Target: “safe, concise, grounded medical responses.”

Baseline:

- correctness = 84%;
- schema validity = 96%;
- unnecessary refusal = 12%.

SFT improves:

- correctness = 88%;
- schema validity = 98%;
- refusal = 12%.

Preference optimization then tests whether the preference data can reduce verbosity/refusal without harming correctness.

Measure:

| Metric | Before | After |
|---|---:|---:|
| Correctness | 84 | measure |
| Groundedness | 82 | measure |
| Refusal rate | 12 | measure |
| Mean output tokens | 240 | measure |
| Safety failures | measure | measure |

## 20–22 — Break it

Give a preference dataset where chosen responses are always longer.

Predict:

- verbosity increases;
- serving cost increases;
- human helpfulness may not improve.

Then inspect the preference data.

## 22–24 — Engineering judgment

The learner must answer:

**When is another training stage justified?**

Require:

- stable failure;
- measurable target metric;
- representative data;
- protected evaluation;
- known resource cost;
- acceptable regression.

## 24–25 — Exit challenge

Complete:

> “We should use ___ rather than ___ because the dominant failure is ___, and the cheapest experiment is ___.”

### Research bridge

- InstructGPT: https://arxiv.org/abs/2203.02155
- DPO: https://arxiv.org/abs/2305.18290
