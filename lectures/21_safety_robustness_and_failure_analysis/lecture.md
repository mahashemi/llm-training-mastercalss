# Lecture 21 — Safety, Robustness, and Failure Analysis

**Lab:** [failure_analysis_and_safety_eval.ipynb](./lab.ipynb)
**Primary anchor:** https://arxiv.org/abs/2203.02155

## Learning outcome

The learner can turn vague “safety concerns” into measurable failure categories, test them under realistic conditions, and use the results to drive engineering changes.

## Start from failures

Give five outputs:

1. wrong answer;
2. unsafe answer;
3. correct answer with unsupported citation;
4. correct answer but invalid JSON;
5. correct answer that becomes wrong after a typo.

Ask: “Are these the same failure?”

No. They occur at different layers.

## Failure taxonomy

| Failure | Example | Likely layer |
|---|---|---|
| Capability | cannot solve task | model/data |
| Grounding | contradicts source | retrieval/generation |
| Safety | harmful response | policy/model/system |
| Format | invalid schema | interface/behavior |
| Robustness | fails after perturbation | data/model |
| Tool | unsafe/wrong action | agent/system |

This taxonomy turns evaluation into an intervention map.

## Safety evaluation design

A serious safety set should specify:

- threat model;
- user population;
- attack/edge-case families;
- expected safe behavior;
- severity levels;
- scoring rubric;
- human audit process.

Example severity:

| Severity | Meaning | Release treatment |
|---|---|---|
| S0 | harmless quality issue | monitor |
| S1 | minor failure | fix |
| S2 | meaningful harm potential | release gate |
| S3 | severe/critical | blocker |

The exact definitions are domain-specific.

## Robustness

Build perturbations:

- typos;
- paraphrases;
- long context;
- multilingual variation;
- conflicting evidence;
- malformed tool arguments.

Measure degradation:

clean score − perturbed score

Also record latency/cost changes.

## Worked failure analysis

Observed:

“The assistant gives unsafe medical advice.”

Test 1: Was correct policy/evidence retrieved?

Test 2: Was the evidence sufficient?

Test 3: Does the model behave correctly with oracle context?

Test 4: Is the failure isolated to one language/intent?

This converts a scary symptom into a causal debugging tree.

## Red-team vs benchmark

| Benchmark | Red-team |
|---|---|
| fixed, repeatable | adaptive |
| known categories | searches for unknown failure modes |
| easier to regress | can discover novel failures |
| quantitative | often exploratory + quantitative |

Use both.

## Release decision

A release scorecard should include:

**capability + safety + robustness + language + product SLO**

Do not allow a large aggregate benchmark gain to silently override a critical failure.

## Exit challenge

Give the learner one failure and require:

**failure → taxonomy → confirming experiment → intervention → release gate**

### Research bridge

Read the primary post-training/safety literature and compare automated evaluation with human audit.

Reference:
https://arxiv.org/abs/2203.02155


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Deepening — turn safety into a test matrix

Create a matrix:

**failure family × severity × language × context × system layer**

For every severe failure define:

1. confirming experiment;
2. immediate mitigation;
3. regression test;
4. release gate.

### Robustness experiment

Start with a clean evaluation set. Generate controlled perturbations:

- typo;
- paraphrase;
- long context;
- conflicting evidence;
- tool argument corruption;
- language switch.

Report both score and degradation relative to clean inputs.

### H100/production transfer

Safety evaluation is not cheaper simply because inference is cheap. At production scale the suite becomes an operational workload with queueing, evaluator cost, and release cadence.



## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 20 — Multimodality](../17_multimodality/lecture.md) · [Next: Lecture 22 — API vs RAG vs Tools vs Training →](../22_api_vs_rag_vs_tools_vs_training/lecture.md)

</div>