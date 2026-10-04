# Course 1 · Chapter — CNNs + Residual/Dense Networks

**Track:** Neural Computing Foundation  
**Topics:** convolution, pooling, receptive fields, CNN extensions, residual and dense networks  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Start with the image problem: a detector for an edge should not need a completely different parameter for every pixel location. Convolution introduces a useful inductive bias: the same local detector can be reused across positions.

For a 1-D illustration,
y_i = Σ_k w_k x_{i+k}.
In 2-D the same idea becomes a sliding kernel over height and width. A feature map therefore answers questions such as “where does this learned pattern occur?”

Explain stride, padding, receptive field, channels, and parameter sharing with a 5×5 image and a 3×3 kernel. Count the parameters explicitly and compare them with a fully connected layer.

Then explain depth: early layers can detect edges/textures, later layers can combine them into more complex patterns. Residual networks change the optimization problem by learning a residual:
y = F(x) + x.
The shortcut gives information and gradients a direct path.

Dense networks instead concatenate earlier representations:
x_l = H_l([x_0,...,x_{l-1}]).

Real connection: CNNs power visual inspection, medical imaging, OCR, satellite imagery, and many multimodal encoders.

Failure experiment: compare a CNN with and without augmentation under a controlled background shift. Ask whether the model learned the object or a shortcut.

## Core concepts

This unit covers **convolution, pooling, receptive fields, CNN extensions, residual and dense networks**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advantage from a larger parameter count or better optimization.

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

<div align="center">[← Previous](../03_neural_computing/03_competitive_learning_and_som/lecture.md) · [Next →](../05_neural_computing/05_autoencoders/lecture.md)</div>
