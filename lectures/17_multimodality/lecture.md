# Lecture 17 — Multimodality

**Duration:** 25 minutes  
**Primary anchor:** https://cs336.stanford.edu/

## Learning objectives
- Explain the central mechanism in plain language.
- Derive the key quantities and track dimensions.
- Implement or inspect the mechanism in the practical lab.
- Predict memory, compute, quality, or failure behavior.
- Decide when the method is justified.
- Propose a research experiment.

## Teaching sequence

### 0–3 — Problem first
State a realistic problem. Ask students for a prediction before introducing terminology.

### 3–8 — Intuition
Use a small visual example. Show what information moves where and what the method changes.

### 8–14 — Mathematics
Write the governing equations. Define all symbols and assumptions. Highlight approximations that will matter at scale.

### 14–19 — Implementation
Run the associated notebook. Inspect shapes, intermediate values, timing, and metrics. Students predict results before execution.

### 19–22 — Break it
Change exactly one assumption. Classify the resulting failure as statistical, numerical, algorithmic, or systems-level.

### 22–24 — Engineering judgment
Compare choices under quality, memory, throughput/latency, reliability, privacy, and cost.

### 24–25 — Exit challenge
Explain the concept without the main jargon word. State what evidence would justify a more expensive next step.

## Core concepts
1. vision-language interfaces
2. modality encoders
3. token budgets
4. alignment
5. multimodal evaluation

## Decision table

| Constraint | First thing to investigate |
|---|---|
| quality gap | data quality, objective, capacity, evaluation validity |
| memory gap | precision, activations, optimizer state, sharding, PEFT |
| speed gap | profiling first: compute-bound, memory-bound, or communication-bound |
| data gap | provenance, filtering, deduplication, sampling, domain coverage |
| evidence gap | improve the evaluation set and baseline before scaling |

## Critical-thinking questions

**Q1. What is the tempting shortcut?**

**Answer:** Changing many variables simultaneously and then attributing the observed result to one technique.

**Q2. What should be recorded?**

**Answer:** Code version, data/model versions, configuration, environment, hardware, evaluation protocol, results, and limitations.

**Q3. When should we stop scaling?**

**Answer:** When the marginal experiment no longer reduces an important uncertainty or improves the target objective enough to justify its resource cost.

## Visuals

Create:
1. mechanism/data-flow diagram;
2. tensor/system diagram;
3. resource diagram;
4. decision tree.

## Practical work

Use the linked course notebook for the hands-on experiment. Produce:
- a baseline;
- an intervention;
- a quantitative comparison;
- one failure case;
- a short interpretation;
- a next experiment.

## Research connection

Read the primary anchor and classify statements into **measured evidence, method choice, heuristic, and inference**.
