# Course 1 · Chapter — Recurrent Architectures + Forecasting

**Track:** Neural Computing Foundation  
**Topics:** Elman, Jordan, fully recurrent networks, forecasting protocol, leaka\ge  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Forecasting exposes a critical distinction between fitting a sequence and evaluating a future prediction system.

In an Elman-style network, the hidden state summarizes previous observations. Jordan-style recurrence feeds previous outputs into the state. A fully recurrent architecture can allow richer recurrent connectivity but increases optimization complexity.

For forecasting, suppose we observe
x_1,...,x_t
and predict
x_{t+1}.
For a multi-step forecast we may recursively feed predictions back into the model:
x̂_{t+1} → x̂_{t+2} → ... .
This creates error accumulation.

Work through a three-step forecast with a simple autoregressive baseline before using a neural network. Explain why a chronological split is mandatory for time series: random splitting can place future information in the training set.

Real connection: electricity demand, traffic, sensors, finance, and operations.

Failure experiment: intentionally randomize the train/test split and compare the apparently excellent result with a proper chronological evaluation. This demonstrates leaka\ge more effectively than a warning paragraph.

## Core concepts

This unit covers **Elman, Jordan, fully recurrent networks, forecasting protocol, leaka\ge**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advanta\ge from a lar\ger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible baseline.
3. Implement the central mechanism once from first principles.
4. Run the framework implementation.
5. Keep the primary bud\get fixed while changing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncertainty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short interpr\etation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Research exercise

The lab must end with a research question. A good question has a measurable independent variable, a defined outcome, a baseline, and a reason the result would matter. Examples include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same training bud\get?
- Does it improve robustness under distribution shift?
- Does it reduce inference memory or latency?
- Which failure mode becomes more or less common?

## Paper-ready deliverable

Every learner produces a **mini research packa\ge**: hypothesis, related-work note, dataset card, method description, experiment matrix, baseline, results table, one figure, error analysis, limitations, reproducibility block, and next-work proposal. These artifacts accumulate toward the final publication capstone.

## Exit questions

1. What problem does the method solve?
2. What inductive bias does it introduce?
3. Which tensor operations implement it?
4. What is the simplest credible baseline?
5. Which metric and split answer the research question?
6. What failure would falsify your hypothesis?

## Laboratory

The notebook is intentionally part of this lecture. It uses a real dataset and requires a baseline, controlled intervention, ablation/error analysis, and a paper-ready result rather than a “hello world” demo.




## Laboratory — run this experiment end to end

**[Open the executable lab notebook](./lab.ipynb)**

The notebook is part of this chapter, not optional homework. Work through it in order: **predict → establish baseline → run → chan\ge one factor → measure → inspect failures → produce the results table → write the conclusion**. The final cells include an answer key and a research extension.

## Laboratory — run this experiment end to end

**[Open the executable lab notebook](./lab.ipynb)**

Work through the notebook in order: **predict → baseline → run → change one factor → measure → inspect failures → produce the results table → conclude**. The final cells include the answer key and a research extension.

<div align="center">

[← Previous](../07_recurrent_networks/lecture.md) · [Course 1 home](../README.md) · [Next →](../09_boltzmann_machines/lecture.md)

</div>
