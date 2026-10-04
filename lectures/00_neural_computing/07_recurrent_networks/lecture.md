# Course 1 · Chapter — RNNs, LSTM + GRU

**Track:** Neural Comput\\ing Foundation  
**Topics:** SRU-style recurrence, LSTM, GRU, sequence model\\ing and teacher forc\\ing  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learn\\ing objective

By the end of this unit, the learner should be able to expla\\in the mechanism mathematically, implement a m\\inimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment show\\ing when the method helps or fails.



## Teach\\ing walkthrough

Start with a sequence whose \\interpr\\etation depends on earlier context. A recurrent model ma\\inta\\ins a state:
h_t = φ(W_x x_t + W_h h_{t-1}+b).
The same parameters are reused at every time step.

Unroll the recurrence for three tokens and calculate the hidden state symbolically. This makes an important fact visible: the gradient from a later time step passes through repeated transformations.

Expla\\in vanish\\ing and explod\\ing gradients. If the relevant Jacobian repeatedly shr\\inks, early \\information becomes difficult to learn; if it grows, optimization can become unstable.

LSTM \\introduces gates to control \\information flow:
i_t = σ(...), f_t = σ(...), o_t = σ(...).
Its cell state provides a more controlled path for long-ran\\ge \\information.

GRU simplifies the gat\\ing structure while r\\eta\\in\\ing explicit control over updates.

Real connection: speech, forecast\\ing, event streams, and historical sequence models. Transformers later replace recurrence with direct content-based \\interactions across positions.

Failure experiment: tra\\in RNN/LSTM/GRU on a task requir\\ing long-ran\\ge dependency and measure performance as the dependency length \\increases.

## Core concepts

This unit covers **SRU-style recurrence, LSTM, GRU, sequence model\\ing and teacher forc\\ing**. Do not memorize the architecture. Derive the computation, identify its \\inductive bias, and ask what evidence would dist\\inguish its claimed advanta\\ge from a lar\\ger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset \\in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible basel\\ine.
3. Implement the central mechanism once from first pr\\inciples.
4. Run the framework implementation.
5. Keep the primary bud\\get fixed while chang\\ing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncerta\\inty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short \\interpr\\etation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Research exercise

The lab must end with a research question. A good question has a measurable \\independent variable, a def\\ined outcome, a basel\\ine, and a reason the result would matter. Examples \\include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same tra\\in\\ing bud\\get?
- Does it improve robustness under distribution shift?
- Does it reduce \\inference memory or latency?
- Which failure mode becomes more or less common?

## Paper-ready deliverable

Every learner produces a **m\\ini research packa\\ge**: hypothesis, related-work note, dataset card, method description, experiment matrix, basel\\ine, results table, one figure, error analysis, limitations, reproducibility block, and next-work proposal. These artifacts accumulate toward the f\\inal publication capstone.

## Exit questions

1. What problem does the method solve?
2. What \\inductive bias does it \\introduce?
3. Which tensor operations implement it?
4. What is the simplest credible basel\\ine?
5. Which metric and split answer the research question?
6. What failure would falsify your hypothesis?

## Laboratory

The notebook is \\intentionally part of this lecture. It uses a real dataset and requires a basel\\ine, controlled \\intervention, ablation/error analysis, and a paper-ready result rather than a “hello world” demo.




## Laboratory — run this experiment end to end

**[Open the executable lab notebook](./lab.ipynb)**

The notebook is part of this chapter, not optional homework. Work through it in order: **predict → establish baseline → run → change one factor → measure → inspect failures → produce the results table → write the conclusion**. The final cells include an answer key and a research extension.

<div align="center">

[← Previous](../06_generative_models/lecture.md) · [Course 1 home](../README.md) · [Next →](../08_sequence_architectures_and_forecasting/lecture.md)

</div>
