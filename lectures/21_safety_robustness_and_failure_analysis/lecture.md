# Lecture 21 — Safety, Robustness, and Failure Analysis

**Duration:** 25 minutes  
**Primary anchor:** https://arxiv.org/abs/2203.02155

## Learning outcome

The learner can turn vague “safety concerns” into measurable failure categories, test them under realistic conditions, and use the results to drive engineering changes.

## 0–4 — Start from failures

Give five outputs:

1. wrong answer;
2. unsafe answer;
3. correct answer with unsupported citation;
4. correct answer but invalid JSON;
5. correct answer that becomes wrong after a typo.

Ask: “Are these the same failure?”

No. They occur at different layers.

## 4–8 — Failure taxonomy

| Failure | Example | Likely layer |
|---|---|---|
| Capability | cannot solve task | model/data |
| Grounding | contradicts source | retrieval/generation |
| Safety | harmful response | policy/model/system |
| Format | invalid schema | interface/behavior |
| Robustness | fails after perturbation | data/model |
| Tool | unsafe/wrong action | agent/system |

This taxonomy turns evaluation into an intervention map.

## 8–13 — Safety evaluation design

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

## 13–17 — Robustness

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

## 17–20 — Worked failure analysis

Observed:

“The assistant gives unsafe medical advice.”

Test 1: Was correct policy/evidence retrieved?

Test 2: Was the evidence sufficient?

Test 3: Does the model behave correctly with oracle context?

Test 4: Is the failure isolated to one language/intent?

This converts a scary symptom into a causal debugging tree.

## 20–22 — Red-team vs benchmark

| Benchmark | Red-team |
|---|---|
| fixed, repeatable | adaptive |
| known categories | searches for unknown failure modes |
| easier to regress | can discover novel failures |
| quantitative | often exploratory + quantitative |

Use both.

## 22–24 — Release decision

A release scorecard should include:

**capability + safety + robustness + language + product SLO**

Do not allow a large aggregate benchmark gain to silently override a critical failure.

## 24–25 — Exit challenge

Give the learner one failure and require:

**failure → taxonomy → confirming experiment → intervention → release gate**

### Research bridge

Read the primary post-training/safety literature and compare automated evaluation with human audit.

Reference:
https://arxiv.org/abs/2203.02155
