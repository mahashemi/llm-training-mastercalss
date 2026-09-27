# Lecture 08 — Distributed Training

**Duration:** 25 minutes  
**Lab:** [08_ddp_and_sharding_simulation.ipynb](../../notebooks/08_ddp_and_sharding_simulation.ipynb)  
**Primary anchor:** https://pytorch.org/docs/main/distributed.fsdp.fully_shard.html

## Outcome

This lecture moves from conceptual understanding toward independent model-building judgment. The student should finish able to explain the mechanism, implement the central idea, predict resource behavior, identify failure modes, and decide when the method is appropriate.

## Learning objectives

- Explain the topic in plain language.
- State the governing equations or invariants.
- Trace the relevant tensor/data/system flow.
- Run and interpret the associated lab.
- Diagnose at least two failure modes.
- Make a resource-aware engineering decision.
- Form one testable research question.

## Core concepts

1. **DDP**
2. **tensor/model/pipeline parallelism**
3. **communication**
4. **FSDP2**
5. **ZeRO**
6. **topology**

## 25-minute script

### 0–3 — Problem first
Start from a real engineering problem. Ask the student to predict what should happen before giving the terminology.

### 3–8 — Intuition
Build a small example with as few moving parts as possible. Introduce the terminology only after the phenomenon is visible.

### 8–14 — Formal model
Derive the core quantities. Annotate every symbol and keep track of dimensions, assumptions, and approximations.

### 14–19 — Implementation
Open the linked notebook. Inspect the smallest implementation. Predict the result, execute it, then explain the observation.

### 19–22 — Break it
Deliberately violate one assumption. Compare the result with the baseline and explain the failure.

### 22–24 — Engineer it
Discuss how the choice changes with memory, data volume, latency, throughput, reliability, cost, or research novelty.

### 24–25 — Exit challenge
The student must explain the idea without using the lecture's main jargon term and propose the next experiment.

## Decision table

| Situation | First question |
|---|---|
| quality is poor | Is the issue data, model capacity, objective, or inference? |
| memory is insufficient | Can we reduce activation/optimizer memory or shard state? |
| throughput is poor | Are we compute-bound, memory-bound, or communication-bound? |
| results are surprising | Is the baseline valid and is evaluation contaminated? |
| budget is tight | What is the smallest experiment that reduces the most uncertainty? |

## Critical thinking

**Q1. What is the seductive but wrong shortcut?**

**Answer:** Treating this topic as a library feature instead of a system property that emerges from interacting data, mathematics, implementation, hardware, and evaluation.

**Q2. What evidence would justify spending more compute?**

**Answer:** A controlled baseline, a measured improvement tied to the target objective, stable evaluation, and evidence that the next experiment is likely to answer an important unresolved question.

**Q3. What can invalidate the conclusion?**

**Answer:** A change in dataset composition, model family, hyperparameters, sequence length, hardware/software path, evaluation set, or another hidden variable.

## Visuals to build

1. Mechanism diagram.
2. Tensor or data-flow diagram.
3. Resource-flow diagram.
4. Engineering decision tree.

Each visual should have a one-sentence “notice this” caption.

## Lab requirements

Run:

notebooks/08_ddp_and_sharding_simulation.ipynb

Produce:
- baseline;
- changed-condition run;
- plot/table;
- interpretation;
- failure note;
- next-experiment proposal.

## Research bridge

Read the cited primary/official material after completing the lab.

Ask:

> Which claim is experimentally demonstrated, which is an implementation choice, and which is an inference made by us?

## Deliverable

One-page experiment report:

**Hypothesis → Setup → Baseline → Intervention → Result → Failure → Interpretation → Next step**

