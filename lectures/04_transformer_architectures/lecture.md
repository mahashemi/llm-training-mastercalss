# Course 2 · Chapter 4 — Transformer Architecture: From Tokens to a Tiny GPT

**Course:** LLM Engineering & Training Masterclass  
**Lab:** [Build a Tiny Transformer](./lab.ipynb)

## 1. The problem

A language model must answer:

> Given the tokens before position $t$, what probability should it assign to the next token?

For

`The cat sat on the`

the model should assign a high probability to plausible continuations such as “mat”.

But the representation of “the” may need information from “cat”, “sat”, or much earlier context.

The central Transformer question is:

> **How can every position selectively retrieve useful information from the other positions while remaining highly parallelizable during training?**

---

## 2. Start from the computation we already understand

Suppose token IDs are:

$$
[12, 91, 7, 43].
$$

An embedding table

$$
Einmathbb{R}^{|V|	imes d}
$$

maps each ID to a vector.

For sequence length $L$:

$$
Xinmathbb{R}^{L	imes d}.
$$

At this point the model has vectors, but each position does not yet have contextual information.

We need a mechanism for positions to communicate.

---

## 3. Attention as learned information retrieval

For every position we create:

$$
Q=XW_Q,qquad K=XW_K,qquad V=XW_V.
$$

Think of:

- **Query:** what information does this position need?
- **Key:** what kind of information does this position contain?
- **Value:** what information should actually be retrieved?

Similarity is computed by:

$$
S=rac{QK^	op}{sqrt{d_k}}.
$$

The scale factor prevents dot products from becoming too large as the dimension grows.

Then:

$$
A=operatorname{softmax}(S)
$$

and:

$$
Y=AV.
$$

---

## 4. Numerical attention example

Take three positions and one-dimensional keys/queries for intuition.

Suppose the current position has query:

$$
q=2
$$

and previous positions have keys:

$$
k=[1,2,0.5].
$$

Raw similarities are:

$$
[2,4,1].
$$

The largest score corresponds to the second position.

After softmax, the attention weights are approximately:

$$
[0.114,0.844,0.042].
$$

So the output is approximately:

$$
0.114v_1+0.844v_2+0.042v_3.
$$

The important point is not the exact numbers.

It is:

> **The model has learned a differentiable way to decide where information should come from.**

---

## 5. Why the causal mask is essential for GPT

During training, the complete sentence is already present.

That creates a dangerous possibility.

For:

$$
x_1,x_2,x_3,x_4
$$

position 2 must not be allowed to look at positions 3 or 4 when predicting the next token.

We therefore apply a causal mask:

$$
M_{ij}=
egin{cases}
0 & jle i\
-infty & j>i.
end{cases}
$$

Then:

$$
A=operatorname{softmax}left(
rac{QK^	op}{sqrt{d_k}}+M
ight).
$$

The masked positions receive probability approximately zero.

### Critical experiment

Train once with the causal mask.

Train once with it accidentally removed.

If the unmasked model performs suspiciously well, that is not a breakthrough.

It is **future-token leakage**.

This is one of the most important debugging experiments in the entire course.

---

## 6. Multi-head attention

One attention operation has one learned projection space.

Multi-head attention creates several:

$$
head_i =
Attention(XW_Q^i,XW_K^i,XW_V^i).
$$

Then:

$$
MultiHead(X)=Concat(head_1,ldots,head_h)W_O.
$$

Different heads can learn different relationships.

For example, one head may strongly connect a pronoun to an earlier noun while another attends to nearby syntax.

Do not interpret individual heads too literally, however. Head visualizations are evidence for analysis, not proof of a human-readable semantic role.

---

## 7. Attention is only half of a Transformer block

A decoder block typically contains:

1. normalization;
2. causal self-attention;
3. residual connection;
4. normalization;
5. feed-forward network;
6. residual connection.

A simplified pre-norm block is:

$$
x' = x + Attention(Norm(x))
$$

then

$$
x'' = x' + MLP(Norm(x')).
$$

The residual stream is important because information can flow through many layers without being repeatedly transformed.

---

## 8. What does the MLP do?

Attention mixes information **between positions**.

The MLP transforms features **within each position**.

A typical feed-forward network expands the hidden dimension:

$$
MLP(x)=W_2,sigma(W_1x+b_1)+b_2.
$$

If:

$$
d_{model}=512
$$

and:

$$
d_{ff}=2048,
$$

the intermediate representation is four times wider.

This expansion provides substantial nonlinear computation at every position.

A useful mental model is:

> **Attention decides what information to bring together; the MLP transforms the resulting representation.**

---

## 9. Position information

Self-attention by itself does not inherently know whether a token came first or last.

The sequence:

> dog bites man

must not have the same representation as:

> man bites dog.

Transformers therefore require positional information.

Modern decoder-only models commonly use methods such as rotary positional embeddings (RoPE).

The important engineering question is not memorizing one formula.

It is understanding that:

> **Content identity and position are different pieces of information that the architecture must combine.**

---

## 10. From block to language model

Stack $N$ decoder blocks:

$$
X_0 ightarrow Block_1 ightarrow Block_2
ightarrowcdotsightarrow Block_N.
$$

The final representation is projected into vocabulary logits:

$$
Z=X_NW_U.
$$

For each position, the model now has one score for every vocabulary token.

Softmax gives:

$$
P(x_{t+1}|x_{le t}).
$$

The training loss is:

$$
L=-rac{1}{T}sum_t
log P(x_{t+1}|x_{le t}).
$$

So the entire GPT training problem can be viewed as:

**tokens → contextual representations → vocabulary logits → next-token loss → gradients → parameter updates.**

---

## 11. Why training is parallel but generation is sequential

This distinction matters enormously for systems engineering.

During training, the entire target sequence is available.

A causal mask prevents illegal information flow, so all positions can be computed in parallel.

During generation:

1. predict token $t+1$;
2. append it;
3. predict token $t+2$;
4. repeat.

The future token does not exist yet.

This is why training and serving have very different hardware bottlenecks.

Later we will see how the **KV cache** avoids recomputing all previous keys and values during generation.

---

## 12. Build a tiny GPT

The laboratory should now feel like an implementation of everything above.

Build:

1. tokenizer;
2. embedding table;
3. positional mechanism;
4. causal self-attention;
5. multi-head attention;
6. MLP;
7. residual connections;
8. normalization;
9. vocabulary projection;
10. cross-entropy loss;
11. optimizer;
12. autoregressive generation.

Start with a tiny configuration.

For example:

- vocabulary: a few thousand tokens;
- context: 64–256;
- layers: 2–4;
- hidden size: 128–256;
- heads: 4;
- batch size: small enough for Colab/CPU fallback.

The goal is not quality.

The goal is **complete causal understanding**.

---

## 13. Tensor-shape audit

For:

$$
B	imes L	imes d
$$

track every tensor.

| Object | Shape |
|---|---|
| token IDs | $B	imes L$ |
| embeddings | $B	imes L	imes d$ |
| Q/K/V | $B	imes L	imes d$ |
| attention scores | $B	imes h	imes L	imes L$ |
| attention output | $B	imes L	imes d$ |
| logits | $B	imes L	imes |V|$ |

Now notice the important systems consequence:

> Attention scores contain an $L	imes L$ interaction.

That is why long context is expensive.

---

## 14. Parameter-count reasoning

For a simplified attention projection with model width $d$:

$$
W_Q,W_K,W_V,W_O
$$

contain roughly:

$$
4d^2
$$

parameters, ignoring biases.

A two-layer MLP with intermediate width $d_{ff}$ contains roughly:

$$
2dd_{ff}.
$$

If $d_{ff}=4d$, the MLP has roughly:

$$
8d^2
$$

parameters.

This explains why the MLP can represent a substantial fraction of the parameters and compute in a Transformer block.

Do not memorize these formulas blindly. Derive them from matrix shapes.

---

## 15. Real-world connection

A production LLM is this basic computation plus enormous engineering infrastructure:

- high-quality training data;
- distributed optimization;
- memory management;
- efficient kernels;
- checkpointing;
- evaluation;
- post-training;
- inference optimization;
- monitoring;
- safety controls.

The architecture is necessary, but architecture alone is not the product.

---

## 16. Failure laboratory

Run these controlled failures:

### A. Remove the causal mask

Expected: suspiciously strong training performance.

Diagnosis: future information leakage.

### B. Shift targets incorrectly

Expected: poor learning despite apparently correct code.

Diagnosis: input/target alignment error.

### C. Use an excessively high learning rate

Expected: unstable or divergent loss.

Diagnosis: optimization failure.

### D. Reduce context length

Expected: degradation on tasks requiring longer dependencies.

Diagnosis: information cannot enter the receptive context.

### E. Compare parameter count and latency

Expected: more parameters generally increase computation, but actual latency also depends on kernels, hardware, batch size, and memory behavior.

---

## 17. Engineering decision

When choosing an LLM architecture, ask:

**What quality do we need? What context length? What latency? What memory? What throughput? What training budget?**

Architecture is a system trade-off, not a leaderboard number.

---

## 18. Mastery questions

1. Why does attention need Q, K, and V rather than a single projection?
2. Why divide by $sqrt{d_k}$?
3. Why is the causal mask necessary?
4. Why can training be parallelized?
5. Why is generation sequential?
6. What does the residual stream accomplish?
7. What is the difference between attention and the MLP?
8. Why does context length affect memory?
9. What would future-token leakage look like experimentally?
10. Why does a tiny GPT teach something a downloaded 7B model cannot?

### Answers

1. They separate the matching signal from the information retrieved after matching.
2. To control the scale of dot products as key/query dimension grows.
3. GPT must predict future tokens without seeing them.
4. All target positions are known during training and can be computed simultaneously under a causal mask.
5. Each new token depends on the token generated immediately before it.
6. It provides a relatively direct information/gradient path across layers.
7. Attention mixes information across positions; the MLP performs nonlinear feature transformation at each position.
8. Attention forms pairwise interactions between positions, producing an $L	imes L$ structure.
9. A model with the mask removed can obtain unrealistically low loss or unusually high next-token accuracy.
10. Because every tensor and dependency can be inspected, modified, and deliberately broken.

---

## Research extension

Choose one:

- context length versus loss;
- number of heads versus quality;
- depth versus width at fixed parameter count;
- MLP expansion ratio;
- positional encoding;
- causal-mask ablation;
- attention-head pruning;
- parameter count versus inference latency.

State the hypothesis before running the experiment.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 03 — PyTorch and Resource Accounting](../03_pytorch_and_resource_accounting/lecture.md) · [Next: Lecture 05 — Attention Alternatives and MoE →](../05_attention_alternatives_and_moe/lecture.md)

</div>
## Video companions

[Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) · [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## Navigation

[← Previous](../03_pytorch_and_resource_accounting/lecture.md) · [Course 2 home](../courses/02_llm_engineering_and_training/README.md) · [Next →](../05_attention_alternatives_and_moe/lecture.md)
