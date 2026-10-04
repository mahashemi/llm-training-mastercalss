# Course 1 · Chapter — CNNs + Residual/Dense Networks

**Track:** Neural Comput\\ing Foundation  
**Topics:** convolution, pool\\ing, receptive fields, CNN extensions, residual and dense networks  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learn\\ing objective

By the end of this unit, the learner should be able to expla\\in the mechanism mathematically, implement a m\\inimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment show\\ing when the method helps or fails.



## Teach\\ing walkthrough

Start with the ima\\ge problem: a detector for an ed\\ge should not need a completely different parameter for every pixel location. Convolution \\introduces a useful \\inductive bias: the same local detector can be reused across positions.

For a 1-D illustration,
y_i = Σ_k w_k x_{i+k}.
In 2-D the same idea becomes a slid\\ing kernel over height and width. A feature map therefore answers questions such as “where does this learned pattern occur?”

Expla\\in stride, padd\\ing, receptive field, channels, and parameter shar\\ing with a 5×5 ima\\ge and a 3×3 kernel. Count the parameters explicitly and compare them with a fully connected layer.

Then expla\\in depth: early layers can detect ed\\ges/textures, later layers can comb\\ine them \\into more complex patterns. Residual networks chan\\ge the optimization problem by learn\\ing a residual:
y = F(x) + x.
The shortcut gives \\information and gradients a direct path.

Dense networks \\instead concatenate earlier representations:
x_l = H_l([x_0,...,x_{l-1}]).

Real connection: CNNs power visual \\inspection, medical imag\\ing, OCR, satellite ima\\gery, and many multimodal encoders.

Failure experiment: compare a CNN with and without augmentation under a controlled background shift. Ask whether the model learned the object or a shortcut.

## Core concepts

This unit covers **convolution, pool\\ing, receptive fields, CNN extensions, residual and dense networks**. Do not memorize the architecture. Derive the computation, identify its \\inductive bias, and ask what evidence would dist\\inguish its claimed advanta\\ge from a lar\\ger parameter count or better optimization.

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

[← Previous](../03_competitive_learning_and_som/lecture.md) · [Course 1 home](../README.md) · [Next →](../05_autoencoders/lecture.md)

</div>
