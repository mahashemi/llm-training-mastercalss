# Course 1 — Deep Learning & Neural Computing Foundations

**Purpose:** teach the ideas, mathematics, architectures, training dynamics, and experimental habits that make modern deep learning understandable rather than mysterious.

**Instructor-led delivery:** [35-day teaching plan (70 contact hours)](./35_DAY_TEACHING_PLAN.md)

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

The table is the learner's navigation map: every chapter links directly to its teaching chapter **and its executable laboratory**.

| # | Chapter | Core question | Laboratory |
|---|---|---|---|
| 1 | [Neural computation](../../lectures/00_neural_computing/01_neural_computing_foundations/lecture.md) | What does it mean for a machine to learn a function? | [Lab](../../lectures/00_neural_computing/01_neural_computing_foundations/lab.ipynb) |
| 2 | [Feedforward networks + backpropagation](../../lectures/00_neural_computing/02_feedforward_and_backprop/lecture.md) | How do multilayer networks learn internal representations? | [Lab](../../lectures/00_neural_computing/02_feedforward_and_backprop/lab.ipynb) |
| 3 | [Competitive learning + SOM](../../lectures/00_neural_computing/03_competitive_learning_and_som/lecture.md) | Can learning organize structure without labels? | [Lab](../../lectures/00_neural_computing/03_competitive_learning_and_som/lab.ipynb) |
| 4 | [CNNs + residual/dense networks](../../lectures/00_neural_computing/04_convolutional_networks/lecture.md) | How can architecture encode spatial structure and depth? | [Lab](../../lectures/00_neural_computing/04_convolutional_networks/lab.ipynb) |
| 5 | [Autoencoders](../../lectures/00_neural_computing/05_autoencoders/lecture.md) | What does it mean to learn a useful representation without labels? | [Lab](../../lectures/00_neural_computing/05_autoencoders/lab.ipynb) |
| 6 | [VAE, GANs + diffusion](../../lectures/00_neural_computing/06_generative_models/lecture.md) | How can a model learn to generate new data? | [Lab](../../lectures/00_neural_computing/06_generative_models/lab.ipynb) |
| 7 | [RNNs, LSTM + GRU](../../lectures/00_neural_computing/07_recurrent_networks/lecture.md) | How can neural networks represent sequences and memory? | [Lab](../../lectures/00_neural_computing/07_recurrent_networks/lab.ipynb) |
| 8 | [Recurrent architectures + forecasting](../../lectures/00_neural_computing/08_sequence_architectures_and_forecasting/lecture.md) | How do sequence architecture and evaluation interact? | [Lab](../../lectures/00_neural_computing/08_sequence_architectures_and_forecasting/lab.ipynb) |
| 9 | [Boltzmann machines + DBNs](../../lectures/00_neural_computing/09_boltzmann_machines/lecture.md) | What is energy-based generative learning? | [Lab](../../lectures/00_neural_computing/09_boltzmann_machines/lab.ipynb) |
| 10 | [Attention + Transformer bridge](../../lectures/00_neural_computing/10_attention_transformers_and_llms/lecture.md) | Why did attention change sequence modeling? | [Lab](../../lectures/00_neural_computing/10_attention_transformers_and_llms/lab.ipynb) |
| 11 | [Deep reinforcement learning](../../lectures/00_neural_computing/11_deep_reinforcement_learning/lecture.md) | How can an agent learn from actions and delayed rewards? | [Lab](../../lectures/00_neural_computing/11_deep_reinforcement_learning/lab.ipynb) |
| 12 | [Research capstone](../../lectures/00_neural_computing/12_research_capstone/lecture.md) | How do we turn a deep-learning idea into evidence? | [Lab](../../lectures/00_neural_computing/12_research_capstone/lab.ipynb) |

### Important boundary

Chapter 10 introduces Transformers because they are the natural historical endpoint of the sequence-modeling story. **The LLM course then teaches Transformers again from an LLM-engineering perspective**, including tokenization, decoder-only modeling, training objectives, systems, scaling, and production. The overlap is intentional but the purpose is different.

## Real-data thread

The course repeatedly uses real datasets rather than isolated toy examples. The same experiment is revisited when useful so students learn to distinguish a property of an algorithm from a property of a dataset.

## Relationship to Course 2

**Course 1:** understand deep learning.

**Course 2:** use that understanding to build, train, evaluate, optimize, serve, and manage LLMs.

→ [Course 2 — LLM Engineering & Training Masterclass](../02_llm_engineering_and_training/README.md)
