# Chapter 37 — Distillation

**Part:** Part IV

## 1. Distillation is an economic transformation

The goal is often:

**large/expensive teacher → smaller/cheaper student**

while preserving enough task quality.

This changes the optimization target from “maximum score” to a frontier:

**quality ↔ latency ↔ memory ↔ cost**

## 2. Distillation signals

| Signal | What the student sees | Cost | Strength |
|---|---|---|---|
| Hard labels | target answer | low | task-specific |
| Teacher responses | generated text | medium | broad |
| Teacher logits | probability distribution | high | richer |
| Hidden states | internal representations | high | architecture-dependent |
| Mixed | several signals | highest | flexible |

Response distillation is easier to deploy because the teacher only needs to generate training data.

## 3. Why a small model can become useful

The teacher converts difficult inference into supervision.

For input x:

teacher → y_teacher

student learns:

p_student(y|x) ≈ y_teacher

The student still needs evaluation against the **real target**, not merely similarity to teacher outputs.

## 4. Teacher quality does not guarantee student quality

Teacher errors can be transferred.

Track:

- teacher accuracy;
- student accuracy;
- teacher uncertainty;
- disagreement;
- hard cases.

Filter low-quality teacher samples.

## 5. Worked deployment decision

Suppose:

| Model | Quality | Latency | Cost/task |
|---|---:|---:|---:|
| Teacher | 90 | 500 ms | 1.00 |
| Student A | 86 | 180 ms | 0.30 |
| Student B | 88 | 240 ms | 0.45 |

The decision depends on the required quality threshold and latency budget.

If the product requires ≥87 quality, Student A fails the requirement despite lower cost. Student B is a candidate for further evaluation.

This is a constraint problem, not a single-score ranking.

## 6. Compression experiment

Train several students with:

- different parameter counts;
- different distillation data sizes;
- different teacher sampling temperatures.

Plot:

**quality vs cost/task**

The useful artifact is a Pareto-style frontier, not a single “best” student.

## 7. Long-tail preservation

A student may match common cases while failing rare ones.

Create buckets:

- common;
- hard;
- safety-critical;
- multilingual;
- long-context;
- adversarial.

Report each separately.

## 8. Distillation plus post-training

A practical lifecycle can be:

teacher → distill → SFT → preference optimization → quantize → serve

But every stage should be measured because later stages can erase or recover capabilities.

## 9. Research exercise

Generate a teacher dataset for 10k prompts.

Train three student sizes.

Measure:

- quality;
- p95 latency;
- peak memory;
- cost per successful task;
- rare-case failure rate.

Then identify where the student stops being economically attractive.

## Laboratory

[dpo_and_distillation_concepts.ipynb](../../notebooks/dpo_and_distillation_concepts.ipynb)

## Reference

Hinton et al., Distilling the Knowledge in a Neural Network:
https://arxiv.org/abs/1503.02531

## Deepening: distillation is an economic frontier

A large teacher may be capable but expensive. A smaller student can trade quality for lower latency and memory.

The objective is:

**quality ↔ latency ↔ memory ↔ cost**

### Experiment

Compare at least two student capacities.

Measure task quality, latency, peak memory, cost/request, and rare-case failures.

### Failure mode

Teacher agreement remains high while the student loses rare capabilities because the distillation data underrepresents them.

Evaluate against the real workload, not only teacher imitation.