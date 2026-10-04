# Lecture Authoring Standard

This document is the quality gate for every chapter in Course 1 and Course 2.

## A lecture is a teaching chapter

A list of topics, learning objectives, links, or research prompts is **not** a lecture.

A learner should be able to read the chapter without external explanation and come away understanding the central mechanism well enough to implement and reason about it.

## Required teaching sequence

### 1. Motivation

Start with a concrete problem.

Bad:

> “This lecture covers attention.”

Good:

> “A recurrent model processes a long sequence step by step. What if we need one position to directly use information from a distant position?”

The reader should understand **why the idea was needed** before seeing its name.

### 2. Intuition

Explain the mechanism using a concrete example, analogy, diagram, or tiny dataset.

The intuition must map to the mathematics that follows.

### 3. Formal concept

Define every new object.

If introducing:

$$
z = Wx+b
$$

explain what $z$, $W$, $x$, and $b$ mean, their shapes, and why the operation is useful.

### 4. Worked example

Use actual numbers or a tiny tensor.

The reader should be able to calculate the result manually.

For a Transformer this could mean:

- a four-token sequence;
- explicit $Q$, $K$, $V$;
- attention scores;
- causal mask;
- softmax;
- weighted sum.

For backpropagation it could mean:

- one input;
- one hidden unit;
- one output;
- explicit loss;
- explicit chain-rule derivatives.

### 5. Mathematics

Derive the important equations rather than dropping them into the page.

Explain what each term contributes.

### 6. Implementation

Show the mechanism in code.

Whenever reasonable:

**from scratch → framework implementation → real model implementation**

The learner should understand what the abstraction is hiding.

### 7. Real-world connection

Answer:

- where is this used?
- what does it buy us?
- what does it cost?
- what can go wrong?
- what would an engineer monitor?

### 8. Experiment

The reader makes a prediction before executing the experiment.

Then the lab tests that prediction.

A minimum experiment contains:

**baseline → one controlled change → measurement → interpretation**

### 9. Failure analysis

Every major chapter deliberately breaks something.

Examples:

- remove the causal mask;
- corrupt labels;
- create train/test leakage;
- use a bad tokenizer;
- exceed memory;
- increase learning rate;
- introduce duplicate data;
- evaluate outside the training distribution.

The student must explain the mechanism of failure.

### 10. Engineering decision

Convert the lesson into a decision.

For example:

> “If the workload has long contexts and latency is the constraint, configuration A is preferable because…”

### 11. Research extension

Only after understanding the method should the student formulate a research question.

The question must contain:

**variable + comparison + outcome + controlled setting**

### 12. Mastery questions and answers

Questions should test understanding, not recall.

Include numerical, conceptual, debugging, and engineering questions.

## Required connection density

Every chapter should connect at least:

**concept ↔ previous concept ↔ real system ↔ experiment ↔ next concept**

The learner should never encounter an isolated definition.

## Forbidden lecture patterns

Do not use these as the main content:

- “Why this belongs before LLM training”
- lists of topics with one-sentence descriptions
- repeated generic research-workflow instructions
- links presented instead of explanations
- “run the notebook” without teaching what the notebook demonstrates
- unexplained equations
- unexplained architecture diagrams
- benchmark tables without interpretation
- a research question before the underlying mechanism has been taught

## Lab standard

The notebook is a laboratory for the chapter, not a substitute for it.

The chapter teaches the mechanism.

The notebook lets the learner manipulate the mechanism.

## Answer-key standard

Where the lab asks the learner to predict, calculate, measure, or interpret something, the repository should provide an answer key or reference result.

For expensive experiments, provide expected trends and explain what deviations might mean.

## Production connection

By Course 2, every major concept should eventually connect to:

**quality → memory → latency → throughput → cost → reliability → maintainability**

The goal is not merely to know how an algorithm works.

The goal is to know **when and why to use it**.


## Mathematical notation quality gate

Mathematics must be both **renderable and teachable**.

### Renderability rules

- Use GitHub-compatible LaTeX inside `$...$` for inline mathematics and `$$...$$` for display mathematics.
- Every LaTeX command must begin with its backslash: `\nabla`, `\frac`, `\theta`, `\eta`, `\partial`, `\sigma`, `\sum`, `\rightarrow`, etc.
- Never allow corrupted forms such as `abla`, `frac`, `theta`, `eta`, `ightarrow`, or `\frac` when a single LaTeX command is intended.
- Never put unexplained LaTeX-like text into equations.
- After editing, inspect rendered Markdown rather than relying only on source appearance.

### Beginner-first notation rules

A mathematical symbol is not an explanation.

Before using a new symbol, explain it in plain English. For example, do not write

$$
w_{new}=w_{old}-\eta\nabla_w L
$$

and move on.

First explain:

- **$w$** — the weight(s) we are learning;
- **$L$** — the loss, a number saying how wrong the model is;
- **$\partial L/\partial w$** — how the loss changes when this weight changes;
- **$\nabla_w L$** — all of those individual slopes collected together;
- **$\eta$** — the learning rate, which controls how large a step we take;
- **the minus sign** — move opposite the direction in which the loss increases.

Then show the equation and a numerical example.

### The “read the equation in English” test

For every important equation, a beginner should be able to answer:

1. What does every symbol mean?
2. What are the shapes of the objects, when applicable?
3. What operation is being performed?
4. Why are we performing it?
5. What would happen if one term became larger or smaller?
6. How does this equation connect to the previous computation?

If those questions cannot be answered from the chapter, the equation is not yet sufficiently taught.

### Derivative and gradient vocabulary

Use the following conceptual progression:

**change → slope → derivative → partial derivative → gradient → update**

Explain that:

- a derivative is a local slope/sensitivity;
- a partial derivative asks about one variable while holding the others fixed;
- a gradient collects partial derivatives;
- an optimizer uses gradients to change parameters.

Do not introduce “nabla” as vocabulary without explaining that it is simply notation for the vector of these slopes.

### Equation-to-code consistency

Whenever an equation appears, the surrounding code should use the same names where practical. If the mathematics says $\theta$, explain what concrete object in the code corresponds to $\theta$.

