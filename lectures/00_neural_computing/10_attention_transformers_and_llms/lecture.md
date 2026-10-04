# Course 1 · Chapter — Attention + Transformer Brid\ge

**Track:** Neural Computing Foundation  
**Topics:** attention types, Transformer, encoder/decoder, BERT, GPT, brid\ge to LLM training  
**Primary lab:** [Open the executable laboratory](./lab.ipynb)

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Begin with a sentence containing a long dependency:

“The scientist who had worked in Tehran for ten years finally published the paper.”

Suppose we want the representation of “published” to use information about “scientist.” A recurrent model can carry that information through many steps. Attention asks a different question:

> Which positions should this position directly use right now?

Given queries Q, keys K, and values V:
Attention(Q,K,V)=softmax(QKᵀ/√d_k)V.

Use a three-token numerical example and calculate one attention row. Then apply a causal mask and show why token t cannot use future tokens during autoregressive langua\ge modeling.

Explain the roles separately:
- Q: what this position is looking for;
- K: what each position offers for matching;
- V: what information is retrieved after matching.

Then introduce multi-head attention as several learned projections that can specialize in different relationships.

The Transformer combines attention with positional information, residual connections, normalization, and feed-forward transformations.

Real connection: machine translation, BERT-style encoders, GPT-style decoders, retrieval, multimodal models.

Failure experiment: remove the causal mask in a next-token training task. The model may appear to learn extraordinarily well because it can see the answer. This is data leaka\ge inside the architecture.

The next course uses this brid\ge to derive decoder-only LLMs in much greater d\etail.

## Core concepts

This unit covers **attention types, Transformer, encoder/decoder, BERT, GPT, brid\ge to LLM training**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advanta\ge from a lar\ger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible baseline.
3. Implement the central mechanism once from first principles.
4. Run the framework implementation.
5. Keep the primary budget fixed while changing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncertainty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short interpr\etation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Research exercise

The lab must end with a research question. A good question has a measurable independent variable, a defined outcome, a baseline, and a reason the result would matter. Examples include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same training budget?
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

[← Previous](../undefined/lecture.md) · [Course 1 home](../README.md) · [Next →](../11_deep_reinforcement_learning/lecture.md)

</div>
