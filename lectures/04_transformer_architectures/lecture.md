# Lecture 04 — Transformer Architectures

**Duration:** 25 minutes  
**Lab:** [Build a Tiny Transformer](`./lab.ipynb`)  
**Primary anchor:** *Attention Is All You Need* — https://arxiv.org/abs/1706.03762

## Outcome

Students can trace a decoder-only Transformer from token IDs to logits and explain why residual paths, normalization, positional information, attention, and the MLP exist.

## 0–4 — Assemble before naming

Start with:

**token IDs → embeddings → blocks → logits**

Ask what each stage must provide for the next stage.

## 4–9 — One Transformer block

Draw:

**x → norm → attention → residual → norm → MLP → residual**

Then explain that the residual stream carries information forward while sublayers transform it.

## 9–14 — Attention and MLP are different jobs

Attention allows positions to exchange information.

The MLP transforms each position's representation after contextualization.

Students should be able to state:

> Attention mixes across positions; the MLP transforms features within a position.

Then introduce RoPE and normalization as components that affect the representation flow rather than optional decoration.

## 14–19 — Tensor walkthrough

Use concrete shapes:

**B × L × d_model**

and one small configuration.

Track:

- Q/K/V;
- attention scores;
- attention output;
- MLP expansion;
- final logits.

Students calculate parameter counts for one attention block.

## 19–22 — Laboratory

Run the tiny Transformer notebook.

Required experiment:

- baseline depth;
- change depth;
- compare validation loss and parameter count.

Then break causal masking and observe leakage.

## 22–24 — Engineering decision

Architecture is a coupled system:

**depth × width × context × attention structure × MLP × normalization × positional method**

Changing one term can alter memory and optimization behavior elsewhere.

## 24–25 — Exit challenge

Without naming a Transformer component, explain why the model needs:

1. a way to represent tokens;
2. a way to mix information across positions;
3. a way to transform each position;
4. a path that preserves earlier information.

## Research bridge

Connect the implementation to the original Transformer paper, then identify which modern decoder-only choices are inherited, modified, or newly introduced.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
