# Course 1 · Chapter — RNNs, LSTM + GRU

**Track:** Neural Computing Foundation  
**Topics:** SRU-style recurrence, LSTM, GRU, sequence modeling and teacher forcing  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Start with a sequence whose interpretation depends on earlier context. A recurrent model maintains a state:
h_t = φ(W_x x_t + W_h h_{t-1}+b).
The same parameters are reused at every time step.

Unroll the recurrence for three tokens and calculate the hidden state symbolically. This makes an important fact visible: the gradient from a later time step passes through repeated transformations.

Explain vanishing and exploding gradients. If the relevant Jacobian repeatedly shrinks, early information becomes difficult to learn; if it grows, optimization can become unstable.

LSTM introduces gates to control information flow:
i_t = σ(...), f_t = σ(...), o_t = σ(...).
Its cell state provides a more controlled path for long-range information.

GRU simplifies the gating structure while retaining explicit control over updates.

Real connection: speech, forecasting, event streams, and historical sequence models. Transformers later replace recurrence with direct content-based interactions across positions.

Failure experiment: train RNN/LSTM/GRU on a task requiring long-range dependency and measure performance as the dependency length increases.

## Core concepts

This unit covers **SRU-style recurrence, LSTM, GRU, sequence modeling and teacher forcing**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advantage from a larger parameter count or better optimization.

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

<div align="center">[← Previous](../06_neural_computing/06_generative_models/lecture.md) · [Next →](../08_neural_computing/08_sequence_architectures_and_forecasting/lecture.md)</div>
