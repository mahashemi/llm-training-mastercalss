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
