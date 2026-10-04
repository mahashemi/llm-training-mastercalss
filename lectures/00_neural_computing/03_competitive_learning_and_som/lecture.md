# Course 1 · Chapter — Competitive Learn\\ing + SOM

**Track:** Neural Comput\\ing Foundation  
**Topics:** w\\inner-take-all, SOM topology, Evolv\\ing SOM, representation discovery  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learn\\ing objective

By the end of this unit, the learner should be able to expla\\in the mechanism mathematically, implement a m\\inimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment show\\ing when the method helps or fails.



## Teach\\ing walkthrough

Start with a cluster\\ing problem where labels do not exist. Competitive learn\\ing asks which prototype is closest to an \\input and lets that prototype move toward the example. For SOM, the w\\inner is not alone: nearby units move too, creat\\ing a topology-preserv\\ing map.

For an \\input x and prototype w_j, choose
j* = argm\\in_j ||x-w_j||².
Then update the w\\inner:
w_j* ← w_j* + η(x-w_j*).
SOM extends this with a neighborhood h(j,j*,t):
w_j ← w_j + η h(j,j*,t)(x-w_j).

The important \\intuition is that learn\\ing is simultaneously do\\ing two th\\ings: fitt\\ing prototypes to data and organiz\\ing nearby prototypes to represent nearby regions of the \\input space.

Worked example: place four 2-D prototypes on the corners of a square and feed po\\ints from two clusters. Calculate the w\\inner for one po\\int and move the w\\inner. Then activate its neighbors and observe how the map chan\\ges.

Real connection: SOMs are useful for exploratory visualization, sensor regimes, customer segmentation, and \\inspect\\ing high-dimensional structure. They are not magic cluster\\ing algorithms; topology preservation and neighborhood choices matter.

Failure experiment: create two clusters with very different densities. Ask whether the map represents density faithfully or spreads prototypes accord\\ing to its tra\\in\\ing dynamics.

## Core concepts

This unit covers **w\\inner-take-all, SOM topology, Evolv\\ing SOM, representation discovery**. Do not memorize the architecture. Derive the computation, identify its \\inductive bias, and ask what evidence would dist\\inguish its claimed advanta\\ge from a lar\\ger parameter count or better optimization.

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

[← Previous](../02_feedforward_and_backprop/lecture.md) · [Course 1 home](../README.md) · [Next →](../04_convolutional_networks/lecture.md)

</div>
