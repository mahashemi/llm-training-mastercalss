# Course 1 — Deep Learning & Neural Computing Foundations

**Purpose:** teach the ideas, mathematics, architectures, training dynamics, and experimental habits that make modern deep learning understandable rather than mysterious.

This is a **standalone course**. It is not a 12-item prerequisite checklist for the LLM course.

## What this course teaches

By the end, a learner should be able to:

- derive and implement gradient-based learning;
- understand representations rather than treating layers as black boxes;
- explain why CNNs, recurrent networks, autoencoders, generative models, attention, and reinforcement learning were developed;
- train and debug models on real data;
- reason about memorization, generalization, optimization, capacity, and distribution shift;
- compare architectures under controlled budgets;
- read a deep-learning paper and reproduce its central claim;
- design a small research experiment.

## Teaching standard

Every lecture is a **chapter**, not a topic list.

A complete chapter contains:

1. **Motivating problem** — what real problem caused this idea to exist?
2. **Intuition** — a concrete example before notation.
3. **Conceptual model** — diagrams and a running example.
4. **Mathematics** — equations derived step by step.
5. **Worked example** — numbers or tensors traced by hand.
6. **Implementation** — from-scratch core mechanism.
7. **Modern implementation** — PyTorch/framework version.
8. **Real-world connection** — where the idea is useful and where it fails.
9. **Experiment** — real dataset, prediction, intervention, measurement.
10. **Failure analysis** — deliberately break something and explain why.
11. **Research extension** — turn the lesson into a falsifiable question.
12. **Mastery questions + answers**.

The learner should finish every chapter knowing **what the method does, why it works, when it fails, and how to measure it**.

## Course sequence

| # | Chapter | Core question |
|---|---|---|
| 1 | Neural computation | What does it mean for a machine to learn a function? |
| 2 | Feedforward networks + backpropagation | How do multilayer networks learn internal representations? |
| 3 | Competitive learning + SOM | Can learning organize structure without labels? |
| 4 | CNNs + residual/dense networks | How can architecture encode spatial structure and depth? |
| 5 | Autoencoders | What does it mean to learn a useful representation without labels? |
| 6 | VAE, GANs + diffusion | How can a model learn to generate new data? |
| 7 | RNNs, LSTM + GRU | How can neural networks represent sequences and memory? |
| 8 | Recurrent architectures + forecasting | How do sequence architecture and evaluation interact? |
| 9 | Boltzmann machines + DBNs | What is energy-based generative learning? |
| 10 | Attention + Transformer bridge | Why did attention change sequence modeling? |
| 11 | Deep reinforcement learning | How can an agent learn from actions and delayed rewards? |
| 12 | Research capstone | How do we turn a deep-learning idea into evidence? |

### Important boundary

Chapter 10 introduces Transformers because they are the natural historical endpoint of the sequence-modeling story. **The LLM course then teaches Transformers again from an LLM-engineering perspective**, including tokenization, decoder-only modeling, training objectives, systems, scaling, and production. The overlap is intentional but the purpose is different.

## Real-data thread

The course repeatedly uses real datasets rather than isolated toy examples. The same experiment is revisited when useful so students learn to distinguish a property of an algorithm from a property of a dataset.

## Relationship to Course 2

**Course 1:** understand deep learning.

**Course 2:** use that understanding to build, train, evaluate, optimize, serve, and manage LLMs.

→ [Course 2 — LLM Engineering & Training Masterclass](../01_what_is_an_llm/README.md)

[← Back to Masterclass](../../README.md)
