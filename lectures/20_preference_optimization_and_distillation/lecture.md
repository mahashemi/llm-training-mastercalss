# Lecture 20 — Preference Optimization and Distillation

**Duration:** 25 minutes  
**Primary anchors:** https://arxiv.org/abs/2305.18290 · https://arxiv.org/abs/1503.02531

## Learning outcome

The learner can explain two different goals:

**preference optimization changes what the model prefers**  
**distillation changes the economics of serving a capability**

## 0–4 — Start with the product problem

Suppose a model is accurate but:

- too verbose;
- expensive to serve;
- inconsistent with user preferences.

Ask: is one method the answer?

Reveal two separate hypotheses:

| Problem | Candidate |
|---|---|
| behavior/preference | DPO-style preference optimization |
| cost/latency/model size | distillation |

They can be combined later.

## 4–8 — Preference data

A preference example contains:

**prompt x + chosen y_w + rejected y_l**

The quality of the pair is critical.

Bad pair:

chosen = 500 words  
rejected = 100 words

This teaches length if length correlates with the label.

Better pair:

chosen = correct + concise + grounded  
rejected = plausible + unsupported

## 8–13 — DPO mechanics

A common DPO objective compares policy and reference log-probability differences.

The important intuition:

**increase relative preference for the chosen answer while anchoring against the reference policy.**

Parameters such as beta control how strongly preference differences affect optimization.

Do not treat beta as a universal magic number; sweep it.

## 13–17 — Distillation

Teacher → student.

| Signal | Student learns from | Cost |
|---|---|---|
| Hard labels | target answer | low |
| Teacher responses | generated output | medium |
| Teacher logits | full distribution | higher |
| Hidden states | representations | higher |

The student must be evaluated against the real task, not only teacher imitation.

## 17–20 — Worked decision

| Model | Quality | p95 latency | Cost/task |
|---|---:|---:|---:|
| Teacher | 90 | 500 ms | 1.00 |
| Student A | 86 | 180 ms | 0.30 |
| Student B | 88 | 240 ms | 0.45 |

If the release threshold is quality ≥87 and latency ≤300 ms:

Student A does not satisfy the quality constraint.

Student B is a candidate for further testing.

This is constraint satisfaction, not a “best model” ranking.

## 20–22 — Failure analysis

**Preference win rate rises but factuality falls**  
→ preference proxy mismatch.

**Student matches teacher but product score falls**  
→ teacher behavior was not aligned with the actual objective.

**Student is cheaper but misses latency target**  
→ compression did not solve the relevant bottleneck.

## 22–24 — Experiment design

Run:

1. SFT baseline;
2. DPO on balanced preferences;
3. DPO on style-heavy preferences;
4. teacher → student distillation.

Measure:

- target quality;
- safety;
- verbosity;
- refusal;
- latency;
- cost;
- rare-case failures.

## 24–25 — Exit challenge

State one sentence each:

> “Preference optimization is justified because ___.”

> “Distillation is justified because ___.”

### References

DPO: https://arxiv.org/abs/2305.18290  
Knowledge distillation: https://arxiv.org/abs/1503.02531
