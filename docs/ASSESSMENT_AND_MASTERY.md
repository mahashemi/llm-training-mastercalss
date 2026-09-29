# Assessment and Mastery Rubric

## Principle

A learner does not pass because code executed.

The course uses:

**Understand → Implement → Measure → Break → Explain → Decide → Reproduce → Research**

## Practical mastery levels

| Level | Observable evidence |
|---|---|
| 0 — Exposure | defines the concept |
| 1 — Understanding | explains mechanism + equations |
| 2 — Implementation | modifies/implements it |
| 3 — Measurement | produces a valid baseline + intervention |
| 4 — Diagnosis | reproduces a failure and identifies cause |
| 5 — Engineering | chooses under resource constraints |
| 6 — Research | formulates/tests a falsifiable hypothesis |
| 7 — Program | converts evidence into staged resource plan |

## Required model-training gates

### Gate A — Tiny model

Can explain every training-loop operation and trace tensor shapes.

### Gate B — Open-weight checkpoint

Can download a real model, identify architecture/tokenizer/revision, estimate weight memory, and run inference.

### Gate C — SFT

Can establish a baseline, run a smoke test, train on controlled data, and evaluate target + regression.

### Gate D — PEFT

Can explain and experimentally compare LoRA/QLoRA, including rank, target modules, memory, and adapter artifacts.

### Gate E — Systems

Can calculate resource requirements and explain throughput, memory, checkpointing, and distributed scaling.

### Gate F — Evaluation

Can create a benchmark before training, slice it, quantify uncertainty, and create release blockers.

### Gate G — Serving

Can benchmark TTFT, inter-token latency, throughput, concurrency, and KV-cache growth.

### Gate H — Architecture decision

Can map knowledge/behavior/action/representation failures to the least invasive useful experiment.

### Gate I — Program

Can defend a staged model program with baseline, data, compute, people, TCO, gates, risks, and fallback.

## Open-weight practical exam

Give the learner:

**an unfamiliar open-weight model + a small dataset + a single GPU constraint.**

Require:

1. model audit;
2. resource estimate;
3. baseline;
4. smoke test;
5. training method choice;
6. controlled run;
7. evaluation;
8. failure analysis;
9. checkpoint/reproduction package;
10. next-scale plan.

## Grading emphasis

Reward evidence over confidence.

A smaller, well-controlled experiment should score higher than a larger run with hidden variables or no reliable baseline.
