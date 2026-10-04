# Course 1 · Chapter — Boltzmann Machines + RBMs + DBNs

**Track:** Neural Computing Foundation  
**Topics:** energy-based learning, RBM, contrastive divergence, DBN intuition  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Begin with an energy function rather than a neural-network layer. An energy-based model assigns lower energy to configurations it considers more compatible.

For a restricted Boltzmann machine with visible v and hidden h:
E(v,h) = -aᵀv - bᵀh - vᵀWh.
The probability is proportional to exp(-E).

The restriction—no visible-visible or hidden-hidden edges—makes conditional sampling tractable:
P(h_j=1|v)=σ(b_j+W_jv).
Similarly for visible units.

Explain contrastive divergence: start from observed data, sample hidden states, reconstruct visible states, sample again, and use the difference between data and reconstruction statistics as an approximate learning signal.

Deep belief networks stack RBM-like representations.

Real connection: these models are historically important because they illustrate latent-variable learning, energy-based modeling, and pre-deep-learning representation learning.

Failure experiment: compare reconstruction statistics after different numbers of Gibbs steps and observe why approximate sampling can bias learning.

## Core concepts

This unit covers **energy-based learning, RBM, contrastive divergence, DBN intuition**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advantage from a larger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible baseline.
3. Implement the central mechanism once from first principles.
4. Run the framework implementation.
5. Keep the primary budget fixed while changing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncertainty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short interpretation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Research exercise

The lab must end with a research question. A good question has a measurable independent variable, a defined outcome, a baseline, and a reason the result would matter. Examples include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same training budget?
- Does it improve robustness under distribution shift?
- Does it reduce inference memory or latency?
- Which failure mode becomes more or less common?

## Paper-ready deliverable

Every learner produces a **mini research package**: hypothesis, related-work note, dataset card, method description, experiment matrix, baseline, results table, one figure, error analysis, limitations, reproducibility block, and next-work proposal. These artifacts accumulate toward the final publication capstone.

## Exit questions

1. What problem does the method solve?
2. What inductive bias does it introduce?
3. Which tensor operations implement it?
4. What is the simplest credible baseline?
5. Which metric and split answer the research question?
6. What failure would falsify your hypothesis?

## Laboratory

The notebook is intentionally part of this lecture. It uses a real dataset and requires a baseline, controlled intervention, ablation/error analysis, and a paper-ready result rather than a “hello world” demo.

<div align="center">[← Previous](../08_neural_computing/08_sequence_architectures_and_forecasting/lecture.md) · [Next →](../10_neural_computing/10_attention_transformers_and_llms/lecture.md)</div>
