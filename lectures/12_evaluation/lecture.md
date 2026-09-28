# Lecture 12 — Evaluation

**Duration:** 25 minutes

## Outcome

Design an evaluation system that measures the real task, separates retrieval/model/system failures, quantifies uncertainty, and can block a bad release.

## 0–4 — Start with a dangerous claim

“Model B scores 3 points higher than Model A.”

Ask:

**Higher on what?**

Then expose five possible hidden changes:

- benchmark;
- prompt;
- decoding;
- evaluator;
- data distribution.

A score is meaningful only with a defined protocol.

## 4–8 — Evaluation stack

Draw:

**benchmark design → automatic metrics → human evaluation → failure taxonomy → statistical analysis → release gates**

Each answers a different question.

## 8–13 — Build a benchmark from the requirement

Example requirement:

“Answer internal policy questions correctly, cite evidence, and abstain when evidence is insufficient.”

| Requirement | Metric |
|---|---|
| correctness | task accuracy |
| evidence | citation support / groundedness |
| abstention | unsupported-answer rate |
| language | per-language score |
| latency | p95 |
| cost | cost per successful task |

Then create slices:

**language × difficulty × task type × safety/failure class**

## 13–17 — Human and model judges

| Approach | Strength | Risk |
|---|---|---|
| automatic | cheap/fast | metric mismatch |
| model-as-judge | scalable | judge bias |
| human | richer | expensive |
| hybrid | scalable + audited | operational complexity |

Calibrate judges on a human-labeled subset.

## 17–20 — Statistical reasoning

When two models use the same test items, compare paired outcomes.

For proportion p over n approximately independent examples:

SE ≈ sqrt[p(1-p)/n]

For paired open-ended evaluation, bootstrap per-example differences.

Then separate:

**statistical significance** from **engineering significance**.

A 0.3-point gain may be detectable but not worth extra cost.

## 20–22 — Failure analysis

Example:

Wrong answer in RAG.

Ask:

1. Was correct evidence retrieved?
2. Was evidence sufficient?
3. Did model use it?
4. Was citation correct?

This maps evaluation to the next engineering action.

## 22–24 — Release gate

Example:

| Metric | Gate |
|---|---:|
| target quality | ≥90 |
| critical safety failures | 0 |
| L3 language | ≥75 |
| p95 latency | ≤2s |
| cost/task | ≤0.20 |

A candidate can improve overall score and still fail release.

## 24–25 — Exit challenge

Write:

**metric → sampling → uncertainty → failure taxonomy → release gate**

### Research bridge

Use the evaluation chapters and harness in the repository to build a reproducible scorecard.

