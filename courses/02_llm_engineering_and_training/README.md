# Course 2 — LLM Engineering & Training Masterclass

**Purpose:** take a learner from understanding neural networks to being able to build, train, evaluate, optimize, serve, and plan modern language-model systems.

**Recommended prerequisite:** Course 1 — Deep Learning & Neural Computing Foundations.

This course is **not** a collection of Transformer topics. It is a guided engineering progression:

> **text → tokens → objective → Transformer → compute → data → pretraining → adaptation → alignment → evaluation → serving → research → program design**

## What this course teaches

A graduate should be able to:

- build a tiny GPT and explain every major tensor operation;
- train and debug an open-weight model;
- construct and audit language-model datasets;
- understand the compute/memory economics of training;
- choose between prompting, RAG, tools, SFT, PEFT, continued pretraining, preference optimization, distillation, and pretraining;
- design evaluations before changing a model;
- diagnose failures and regressions;
- benchmark inference systems;
- reproduce research and turn observations into experiments;
- create a defensible model/data/compute proposal.

## Chapter standard

A chapter must **teach**, not merely enumerate.

Every chapter should answer:

**What problem are we solving? → How does the mechanism work? → Can I see it on a concrete example? → Can I derive it? → Can I implement it? → What happens on real data? → How does it fail? → What engineering decision follows? → What research question remains?**

The notebook is part of the chapter rather than a detached assignment.

## Course sequence

| # | Chapter | Learner question |
|---|---|---|
| 1 | What is a language model? | What exactly is being learned? |
| 2 | Tokenization | How does text become the computational units the model sees? |
| 3 | PyTorch + resource accounting | How do tensors, autograd, memory, FLOPs, and hardware meet? |
| 4 | Transformer architecture | How does a decoder-only model turn context into next-token probabilities? |
| 5 | Attention alternatives + MoE | What changes when we redesign attention or sparsify computation? |
| 6 | GPUs + kernels | Why does the same mathematical model run at very different speeds? |
| 7 | Efficient attention + Triton | How do implementation details change memory and latency? |
| 8 | Distributed training | How do we train beyond one GPU? |
| 9 | Scaling laws | How do model size, data, and compute interact? |
| 10 | Inference systems | What actually determines serving cost and latency? |
| 11 | Training-system design | How do we run a reliable training campaign? |
| 12 | Evaluation | How do we know a model improved? |
| 13 | Data sources + construction | Where does training data come from and how do we make it usable? |
| 14 | Filtering, deduplication, mixing + synthetic data | What makes a training mixture useful? |
| 15 | SFT + RLHF | How do we turn a base model into a useful assistant? |
| 16 | RL with verifiable rewards | When can correctness become a training signal? |
| 17 | Multimodality | How do language models connect to other modalities? |
| 18 | LoRA + QLoRA + PEFT | How can we adapt models cheaply? |
| 19 | Full fine-tuning + continued pretraining | When should we update all weights or change the model's knowledge? |
| 20 | Preference optimization + distillation | How do we shape behavior and transfer capability? |
| 21 | Safety, robustness + failure analysis | Where does the model fail and how do we release responsibly? |
| 22 | API vs RAG vs tools vs training | What is the right intervention for a real product problem? |
| 23 | Building an LLM program | How do experiments become an engineering program? |
| 24 | From experiment to fundable model | How do evidence, resources, people, risk, and milestones become a plan? |

## Production-grade learning loop

Every major chapter follows:

**Understand → Implement → Run → Measure → Break → Diagnose → Decide → Reproduce**

The research track then adds:

**Intervene → Ablate → Generalize → Communicate → Release**

## Two levels of examples

Each concept should be taught through both:

- a **small transparent example** where every tensor/calculation can be inspected;
- a **real open-weight or real-data example** where engineering constraints become visible.

That is how the learner moves from “I know the definition” to “I can use this in a production system.”

← Course 1 — Deep Learning & Neural Computing Foundations
