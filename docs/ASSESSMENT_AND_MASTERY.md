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


## Course 1 grading policy (35 teaching days)

The percentages below sum to 100%. They are published at course launch so students can plan effort across the full course.

| Component | Weight | Timeline | Required evidence |
|---|---:|---|---|
| Assignments and research project | **40%** | Small assignments begin Day 1; project question Day 3; proposal Day 7; baseline by Day 29; final package Day 34 | Individual concept/lab assignments plus team research artifact, controlled experiment, error analysis, reproducibility and contribution statement |
| Critical study report | **15%** | Topic and references Day 5; outline Day 17; draft Day 30; final Day 34 | Critical synthesis of one substantial paper or a tightly related small set; explain the question, method, evidence, limitations and relation to the project |
| Midterm examination | **15%** | **Day 18** | Individual assessment covering Days 1–14: neural computation, gradients/backprop, optimization/generalization, SOM, CNN/residual/dense architectures, autoencoders and experimental reasoning |
| Final examination | **30%** | **Day 35** | Individual cumulative assessment emphasizing mechanism, mathematical reasoning, model/experiment diagnosis and defensible research decisions |

### Assignment/project timeline

- **Days 1–3:** start low-stakes assignments; browse the project catalogue and choose a research direction.
- **Day 7:** proposal approved or narrowed by the instructor.
- **Day 14:** feasible baseline and evaluation plan.
- **Day 17:** project progress check; study-report outline due.
- **Day 27:** interim results table.
- **Day 29:** reproducible baseline and frozen evaluation contract.
- **Day 31–32:** controlled intervention, error analysis and figure.
- **Day 33:** presentation and peer feedback.
- **Day 34:** project package and study report due.

### Fairness and individual accountability

Group projects are encouraged, but group output must not hide individual learning. Each learner submits individual mastery checks, identifies their contributions, and must be able to explain the project's method and evidence. Grades reward sound reasoning and transparent evidence, not simply the highest score or most expensive model. A well-supported negative result can earn full research credit.

### Study report versus project report

These are different artifacts. The **study report** critically explains existing literature and is due on Day 34. The **project report/paper draft** explains the team's own question, experiment, results, limitations and reproducibility package. They may inform each other, but one cannot be substituted for the other.
