# Chapter 49 — Robustness and Distribution Shift

**Part:** Part V

## 1. Robustness is degradation under changed conditions

A model is robust when its capability degrades acceptably under relevant changes.

Let m(x) be the metric on the original distribution and m_delta(x) after transformation delta.

A simple degradation measure is:

D(delta) = m_original - m_delta

The useful question is not “is the model robust?” but:

**robust to what change, by how much, on which population?**

## 2. Stress dimensions

| Dimension | Example transformation | Metric |
|---|---|---|
| Spelling | typos | task score delta |
| Paraphrase | same meaning, new wording | score delta |
| Length | 1k → 16k tokens | quality + latency |
| Language | low-resource language | per-language score |
| Domain | general → specialist | domain score |
| Time | old → new information | freshness |
| Adversarial | confusing/malicious input | safety/task score |
| Conversation | 1 turn → 20 turns | task success |

## 3. Distribution shift types

### Covariate shift
Inputs change.

### Label/task shift
The relationship between input and desired output changes.

### Concept drift
The underlying world changes over time.

The intervention differs:

- input normalization;
- retraining;
- retrieval;
- tools;
- monitoring.

## 4. Robustness matrix

| Model | Clean | Typos | Long context | Low-resource | Domain shift |
|---|---:|---:|---:|---:|---:|
| Baseline | 82 | 76 | 70 | 55 | 61 |
| Candidate | 84 | 79 | 73 | 53 | 68 |

The candidate gains on the clean set but regresses on the low-resource slice.

That regression must be visible.

## 5. Perturbation budget

Perturbations should be controlled.

Examples:

- 1 typo per 100 characters;
- 2 paraphrases/item;
- context length ×2;
- domain mixture shifted by defined amount.

This makes comparisons reproducible.

## 6. Stress testing and resource costs

Longer inputs can increase:

- prefill latency;
- memory;
- retrieval cost;
- KV-cache memory.

Therefore robustness testing should report **quality + resource degradation**.

## 7. Worked example

Suppose:

clean accuracy = 90%  
typo accuracy = 82%

Degradation = 8 points.

After training:

clean = 92%  
typo = 90%

Now the intervention improved both central performance and robustness.

But test additional perturbations before generalizing the result.

## 8. Out-of-distribution evaluation

Do not define OOD merely as “harder.”

Build a distribution different in a specified way:

**source, domain, language, time, format, user population, or task composition**

Then measure the change.

## Research exercise

Create four perturbation families.

For each model version, report:

- clean score;
- perturbed score;
- degradation;
- p95 latency;
- cost/task.

Then identify whether one intervention helps one perturbation while harming another.

## Laboratory

[failure_analysis_and_safety_eval.ipynb](../../notebooks/failure_analysis_and_safety_eval.ipynb)

## Reference

https://cs336.stanford.edu/
