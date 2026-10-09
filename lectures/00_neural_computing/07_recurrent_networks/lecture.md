# Course 1 · Chapter 7 — RNNs, LSTM, and GRU: Learning from Sequences

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the executable laboratory](./lab.ipynb)

## Why this chapter exists

Language, sensor streams, transactions, and speech arrive as sequences. A recurrent model carries information from earlier steps into later decisions.

A vanilla RNN repeatedly applies the same transition. LSTM and GRU introduce gates that learn what to keep, forget, and expose, addressing long-range gradient problems.

You will see the failure before learning why the gates were invented.

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Start with a sequence whose interpretation depends on earlier context. A recurrent model maintains a hidden state:

$$
h_t=\phi(W_xx_t+W_hh_{t-1}+b).
$$

Read this from right to left as a recipe: combine the current input $x_t$ with the previous memory $h_{t-1}$, apply learned weights $W_x$ and $W_h$, add bias $b$, then pass the result through activation $\phi$ to obtain the new state $h_t$. The same weights are reused at every time step.

Unroll the recurrence for three tokens and calculate the hidden state symbolically. This makes an important fact visible: the gradient from a later time step passes through repeated transformations.

Explain vanishing and exploding gradients. If the relevant Jacobian repeatedly shrinks, early information becomes difficult to learn; if it grows, optimization can become unstable.

An LSTM introduces gates—learned values between 0 and 1—that regulate information flow. A simplified view is

$$
i_t=\sigma(\cdots),\qquad f_t=\sigma(\cdots),\qquad o_t=\sigma(\cdots).
$$

The input gate $i_t$ controls what new information may enter the memory, the forget gate $f_t$ controls what old memory to retain, and the output gate $o_t$ controls what part of the memory is exposed as the hidden state. The sigmoid $\sigma$ maps each gate value into the interval $(0,1)$. The ellipses stand for learned affine combinations of the current input and previous hidden state; the full equations and a numerical cell-state trace follow below.

### Full LSTM equations: what the gates actually compute

The ellipses above hide learned weighted sums. In one common LSTM convention, the gates and candidate memory are

$$
\begin{aligned}
i_t &= \sigma(W_i x_t+U_i h_{t-1}+b_i),\\
f_t &= \sigma(W_f x_t+U_f h_{t-1}+b_f),\\
o_t &= \sigma(W_o x_t+U_o h_{t-1}+b_o),\\
g_t &= \tanh(W_g x_t+U_g h_{t-1}+b_g).
\end{aligned}
$$

Here $x_t$ is the current input, $h_{t-1}$ is the previous exposed hidden state, each $W$ and $U$ is a learned weight matrix, and each $b$ is a bias. The sigmoid makes each gate a value between 0 and 1; $\tanh$ makes candidate content lie between -1 and 1.

The cell memory and hidden state are then updated:

$$
c_t=f_t\odot c_{t-1}+i_t\odot g_t,
\qquad
h_t=o_t\odot\tanh(c_t).
$$

The symbol $\odot$ means element-by-element multiplication. Read the cell update as **keep some old memory + write some candidate memory**. The output gate decides how much of the updated cell to expose as $h_t$. Implementations differ in details and gate ordering, but this is a standard formulation.

#### Trace one cell update by hand

For one memory component, suppose the previous cell value is $c_{t-1}=0.5$, the forget gate is $f_t=0.8$, the input gate is $i_t=0.25$, and the candidate is $g_t=0.4$. Then

$$
c_t=(0.8)(0.5)+(0.25)(0.4)=0.4+0.1=0.5.
$$

The old memory contributes 0.4 and the new candidate contributes 0.1. If $o_t=0.9$, the exposed state is

$$
h_t=0.9\tanh(0.5)\approx0.416.
$$

This is the point of the gates: the model learns separate controls for retaining memory, writing candidate content, and exposing information.

### GRU equations and how they differ

A common GRU formulation uses an update gate $z_t$, reset gate $r_t$, and candidate state $\tilde h_t$:

$$
\begin{aligned}
z_t &= \sigma(W_zx_t+U_zh_{t-1}+b_z),\\
r_t &= \sigma(W_rx_t+U_rh_{t-1}+b_r),\\
\tilde h_t &= \tanh\!\left(W_hx_t+U_h(r_t\odot h_{t-1})+b_h\right),\\
h_t &= (1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t.
\end{aligned}
$$

In this convention, $z_t$ mixes the previous state with the candidate state, while $r_t$ controls how much previous state contributes when forming the candidate. Some libraries use the complementary update-gate convention, so always check the implementation's definition before comparing equations.

A GRU has no separate cell state $c_t$ or output gate. This can make it simpler, but fewer gates do not guarantee better performance. Compare RNN, LSTM, and GRU with the same data split, parameter/training budget, and repeated seeds.



Real connection: speech, forecasting, event streams, and historical sequence models. Transformers later replace recurrence with direct content-based interactions across positions.

Failure experiment: train RNN/LSTM/GRU on a task requiring long-range dependency and measure performance as the dependency length increases.

## Build the intuition before the notation

Imagine reading a sentence one word at a time while carrying a small notebook.

After each word, you update the notebook.

That notebook is the hidden state $h_t$.

An RNN says:

> “Use the current input plus the notebook from the previous step to create the next notebook.”

The difficulty is that the notebook must preserve the right information for potentially hundreds or thousands of steps.

### See the gradient problem numerically

Suppose the relevant gradient factor is approximately $0.8$ at each step.

After 50 steps:

$$
0.8^{50}\approx1.43\times10^{-5}.
$$

The signal is tiny.

If the factor is $1.2$:

$$
1.2^{50}\approx9,100.
$$

The signal can become enormous.

These are simplified examples, not exact descriptions of every RNN. Their purpose is to make the words **vanishing** and **exploding** concrete.

### Why gates help

A gate can learn to preserve information rather than repeatedly transforming it.

The LSTM cell-state update

$$
c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t
$$

contains an additive path.

If $f_t$ is close to 1 and the new contribution is small, information can persist with much less destructive transformation.

That is the conceptual reason gating helps long-range credit assignment.

### Controlled comparison

Do not compare RNN, LSTM, and GRU using different hidden sizes or different training budgets and then attribute every difference to the architecture.

Keep the important variables fixed, vary the recurrent cell, and repeat across seeds.


## Work a recurrent update by hand

A simple RNN updates its hidden state using the current input and previous state:

$$
h_t=\tanh(0.5x_t+0.8h_{t-1}).
$$

Let $h_0=0$ and feed $x_1=1, x_2=0, x_3=1$.

- Step 1: $h_1=\tanh(0.5)\approx0.462$.
- Step 2: $h_2=\tanh(0+0.8\times0.462)\approx0.354$.
- Step 3: $h_3=\tanh(0.5+0.8\times0.354)\approx0.654$.

The second input is zero, but the state remains nonzero because it carries information from the first step. This is useful memory, but it is also a path through which gradients must travel.

### Why long-range learning is hard

If a simplified gradient multiplier is $0.8$ at each step, after 10 repeated steps its contribution is $0.8^{10}\approx0.107$; after 50 steps it is $0.8^{50}\approx1.43\times10^{-5}$. If the multiplier is $1.2$, then $1.2^{50}\approx9,100$. Repeated shrinkage makes early events hard to learn; repeated growth can destabilize updates. Real RNN gradients involve matrix Jacobians, so these scalar examples illustrate the mechanism rather than model every case.

LSTM introduces a cell-state path:

$$
c_t=f_t\odot c_{t-1}+i_t\odot\tilde{c}_t.
$$

The forget gate $f_t$ controls retained memory; the input gate $i_t$ controls new content. When $f_t$ is near 1, information can persist without being repeatedly overwritten. GRU uses a simpler gating design with related goals.

**Check yourself:** if the same input sequence is processed twice from different initial states, should the hidden states necessarily match? Explain which condition would make them match and why this matters when resetting state between independent sequences.


## Failure analysis: when recurrence stops helping

A recurrent model can fail for different reasons that require different responses:

- **Long dependencies are forgotten:** plot performance against dependency length and compare the vanilla RNN with LSTM/GRU. Do not infer vanishing gradients from accuracy alone; inspect gradient norms or controlled synthetic tasks too.
- **Training becomes unstable:** log gradient norms and loss; gradient clipping may limit extreme updates, but it cannot restore information that has already vanished.
- **State leaks across unrelated examples:** reset the hidden/cell state at sequence boundaries unless the examples are intentionally contiguous streams. Otherwise the model can use information from a previous sample.
- **A gated model appears better:** compare parameter counts, training steps, and tuning budget; the extra capacity or optimization may explain part of the gain.

### Answer to the state-reset question

The same input sequence does **not** necessarily produce the same hidden states from different initial states: the recurrence explicitly depends on $h_0$ (and, for LSTM, $c_0$). With identical inputs, parameters, and initial states, a deterministic evaluation pass should reproduce the same states. Resetting state is therefore part of the experimental protocol, not just a coding detail.

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

### Answers

1. An RNN updates a hidden state using the current input and previous state; the same transition parameters are reused over time.
2. Vanishing gradients shrink signals through repeated Jacobian products; exploding gradients grow them and can destabilize optimization.
3. The LSTM forget gate controls retained cell memory, the input gate controls candidate content written, and the output gate controls exposed state.
4. A GRU uses update/reset gates and a candidate state but has no separate LSTM-style cell state; exact gate conventions vary by implementation.
5. Compare at a declared budget, test a task with controlled dependency lengths, and inspect gradient behavior as well as predictive quality.
6. The initial state influences later states, so state must be reset or deliberately carried according to the real sequence boundaries.

## Visual intuition

![Recurrent networks carry state through time](../../../visuals/course1/07-recurrent-networks.svg)

*Figure: Each step reads the current input and updates a memory state.*

— recurrent state and gated memory

A recurrent network reuses the same cell at each time step. The hidden state carries information forward. LSTM and GRU add gates that control how much information is retained, overwritten, or exposed.

```mermaid
flowchart LR
    X1["Input xₜ₋₁"] --> C1["Recurrent cell"]
    H0["State hₜ₋₂"] --> C1
    C1 --> H1["State hₜ₋₁"]
    X2["Input xₜ"] --> C2["Same cell parameters"]
    H1 --> C2
    C2 --> H2["State hₜ"]
    H2 --> Y["Prediction"]
```

```mermaid
flowchart TB
    X["Current input xₜ"] --> G["Gates"]
    H["Previous state hₜ₋₁ / cell state cₜ₋₁"] --> G
    G --> KEEP["Keep useful information"]
    G --> FORGET["Forget or overwrite stale information"]
    G --> OUT["Expose state for prediction"]
```

The gates are learned, not manually programmed rules. A fair comparison tests whether the extra gating helps on the chosen sequence task under a comparable data and training budget.

## Laboratory — run the experiment end to end

**[Open the executable laboratory](./lab.ipynb)**

This notebook is part of the chapter, not optional homework. Follow the same scientific loop used in real ML work:

**predict → establish a baseline → run → change one factor → measure → inspect failures → produce the results table → conclude → propose the next experiment.**

The notebook uses a real dataset or environment, records quantitative results, and ends with an answer key and a research extension.

## Video companions

**Recommended starting point:** [Long Short-Term Memory (LSTM) — gates and long-range memory](https://www.youtube.com/watch?v=YCzL96nL7j0)

For a broader selection, [browse more RNNs, LSTM, and GRU videos](https://www.youtube.com/results?search_query=RNNs%2C+LSTM%2C+and+GRU).

## Navigation

[← Previous](../06_generative_models/lecture.md) · [Course 1 home](../README.md) · [Next →](../08_sequence_architectures_and_forecasting/lecture.md)
