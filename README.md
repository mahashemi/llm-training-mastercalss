# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to **understand, build, train, evaluate, optimize, deploy, and manage large language models**—from a tiny GPT and real open-weight checkpoints to H100-scale systems, research, economics, and program design.

**Audience:** high-school graduates, engineers, researchers, and organizations.

## Two-course structure

This repository now contains **two coherent courses**, not one 36-lecture prerequisite chain.

### Course 1 — Deep Learning & Neural Computing Foundations

A standalone deep-learning course covering the mechanisms that make modern neural networks understandable.

**[Open Course 1](courses/01_deep_learning_and_neural_computing/README.md)**

| # | Course 1 chapter | Main practical outcome |
|---|---|---|
| 1 | Neural computation | Build and reason about a perceptron/Adaline |
| 2 | Feedforward networks + backpropagation | Derive gradients and train an MLP |
| 3 | Competitive learning + SOM | Analyze unsupervised topology |
| 4 | CNNs + residual/dense networks | Understand spatial inductive bias and depth |
| 5 | Autoencoders | Learn and probe latent representations |
| 6 | VAE, GANs + diffusion | Understand and compare generative learning |
| 7 | RNNs, LSTM + GRU | Understand neural sequence memory |
| 8 | Recurrent architectures + forecasting | Build and correctly evaluate sequence predictors |
| 9 | Boltzmann machines + DBNs | Understand energy-based representation learning |
| 10 | Attention + Transformer bridge | Understand why attention changed sequence modeling |
| 11 | Deep reinforcement learning | Learn from actions and delayed rewards |
| 12 | Research capstone | Reproduce, intervene, ablate, and communicate evidence |

### Course 2 — LLM Engineering & Training Masterclass

A standalone LLM course that takes the learner from text and tokens through a tiny GPT, real data, training systems, adaptation, evaluation, serving, and research/program design.

**[Open Course 2](courses/02_llm_engineering_and_training/README.md)**

| # | Course 2 chapter | Main practical outcome |
|---|---|---|
| 1 | What is a language model? | Build a language-model mental model |
| 2 | Tokenization | Measure tokenizer/computation consequences |
| 3 | PyTorch + resource accounting | Reason about tensors, autograd, memory, and FLOPs |
| 4 | Transformer architecture | Trace a decoder-only model end to end |
| 5 | Build a tiny GPT | Train a real miniature language model |
| 6 | Data sources + construction | Build a defensible corpus |
| 7 | Filtering + deduplication + mixing | Run controlled data interventions |
| 8 | Pretraining systems | Turn a training loop into a reliable experiment |
| 9 | Scaling laws | Connect model/data/compute budgets |
| 10 | GPUs + kernels | Understand hardware-level performance |
| 11 | Efficient attention + Triton | Optimize memory and latency |
| 12 | Distributed training | Scale beyond one GPU |
| 13 | Evaluation | Design evaluation before changing the model |
| 14 | Inference systems | Measure latency, throughput, and KV-cache economics |
| 15 | SFT + post-training | Turn a base model into a useful assistant |
| 16 | LoRA + QLoRA + PEFT | Adapt models under tight resource budgets |
| 17 | Continued pretraining + full FT | Change knowledge and compare update strategies |
| 18 | Preference optimization + distillation | Shape behavior and transfer capability |
| 19 | RL with verifiable rewards | Train against automatically checkable outcomes |
| 20 | Multimodality | Extend language-model training beyond text |
| 21 | Safety + robustness + failure analysis | Find and characterize failures |
| 22 | API vs RAG vs tools vs training | Make the right product intervention |
| 23 | Building an LLM program | Turn evidence into a technical program |
| 24 | From experiment to fundable model | Turn evidence into resources, milestones, and risk |

### One relationship, not one course

**Course 1 teaches deep learning. Course 2 applies that foundation specifically to language-model engineering.**

Course 1 is recommended preparation for Course 2, but the two have separate learning goals, navigation, labs, and completion criteria.

## Learning Graph

**[Open the complete Learning Graph](docs/LEARNING_GRAPH.md)** · **[Dataset Learning Matrix](data/REAL_DATASET_REGISTRY.md)** · **[Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)**

The repository is organized so that a learner follows one course at a time. Supporting books, runbooks, papers, and references deepen the chapter rather than defining a competing learning order.

### The new lecture standard

A lecture is not a list of topics.

Every chapter must contain:

**Motivating problem → intuition → worked example → concept → mathematics → implementation → real-world connection → real dataset → experiment → failure analysis → engineering decision → research extension → mastery questions**

The lab is embedded in that story.

The standard is deliberately similar to learning from a good textbook with a laboratory beside it: the reader should understand the idea **before** being asked to run code.

## North-star outcome

A graduate of this curriculum should be able to:

- explain a language model from tokens to distributed training;
- build a tiny GPT from scratch and understand every major tensor operation;
- construct and audit a pretraining dataset;
- select between prompting, RAG, tool use, SFT, LoRA, QLoRA, continued pretraining, preference optimization, distillation, or training from scratch;
- estimate model/data/compute requirements and turn them into a resource proposal;
- run reproducible experiments and generate paper-ready tables and figures;
- design evaluation suites before training rather than after;
- diagnose training failures and scaling bottlenecks;
- design a multilingual/national-language data and model program;
- produce a technical + organizational + funding proposal for an LLM initiative.



## Practical Open-Weight Training Track

Course 2 now has an explicit hardware-to-training ladder. Start with a real open-weight model on free Colab, then move the same experiment to larger single-GPU and H100 environments.

**Practical progression:**

CPU tiny GPT → Qwen3-0.6B on free Colab → Qwen3-1.7B/4B experiments → 7B/8B on H100 → Qwen3.8-27B adaptation → multi-GPU training → foundation-model planning.

See **[Open-Weight Training Ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md)** and **[Open-Weight Training Path](book/00_open_weight_training_path.md)**.

The current classroom anchor is Qwen3-0.6B because the official checkpoint is small enough to make a real open-weight workflow practical in a free-first course. The larger-model path is deliberately the same workflow with different resource constraints.

The course distinguishes four different activities that are often incorrectly called “training”: **inference, supervised fine-tuning, continued pretraining, and pretraining from scratch**. It also treats **full FT, LoRA, and QLoRA as parameter-update strategies**, not as alternatives to the training objective itself.

### Open-weight model ladder

The practical hardware/model progression is maintained in the dedicated [Open-Weight Training Ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md). The curriculum matrix above tells you **when** to use that ladder; the ladder contains the detailed hardware and model sizing reference.

This is intentionally **not another curriculum table**. The same workflow is applied at different resource scales:

**CPU tiny GPT → Qwen3-0.6B on free Colab → 1.7B/4B experiments → 7B–8B on H100 → 27B adaptation → multi-GPU training → foundation-model planning.**

## Learning engine

Every lesson follows:

**Intuition → visual → mathematics → code → systems → experiment → failure analysis → decision → research question**

Every important concept is taught twice: once for understanding and once for engineering judgment.

## Free-first rule

Practical labs target free Google Colab or CPU fallbacks whenever possible. Colab's free tier provides access to compute resources, including GPUs/TPUs, but availability and limits are dynamic and not guaranteed. Therefore no lab assumes a particular accelerator will always be available.

For large-scale training, the course uses small reproducible runs to teach the method and then converts the same experiment into a scaling proposal with explicit assumptions.

## Repository architecture

- `lectures/` — the chapter implementations and embedded laboratories for Course 1 and Course 2
- `book/` — optional deep-reference chapters; not required for the learner path
- `runbooks/` — reusable operational procedures for instructors/advanced practitioners
- `visuals/` — diagrams and visual teaching assets
- `videos/` — curated public lectures with timestamps, purpose, and critical questions
- `papers/` — paper-reading guides and reproduction plans
- `cheat_sheets/` — compact references
- `projects/` — research projects, graded/capstone work, and the publication path
- `templates/` — experiment cards, research-project specifications, paper reports, technical proposals, funding proposals
- `references/` — canonical sources and citations

## Research philosophy

The course treats model training as an experimental science and an engineering discipline. Claims are tied to evidence, configurations are recorded, and every major result is accompanied by a failure analysis and a reproducibility checklist. The [Student Research Project Catalog](projects/06_student_research_project_catalog.md) turns the curriculum into a progression from first experiment to benchmark, dataset contribution, reproducibility study, efficiency study, or paper-quality research.

## Canonical external foundations

- Stanford CS336, *Language Modeling from Scratch* — full lifecycle: data, architecture, training, evaluation, deployment.
- Andrej Karpathy, *Let's build GPT* and *Let's reproduce GPT-2* — highly practical implementation walkthroughs.
- 3Blue1Brown, attention/transformer visual explanations — mathematical intuition.
- Sebastian Raschka, end-to-end LLM coding workshop — from tokenizer and architecture to pretraining and instruction tuning.
- OLMo / OLMo 2 — open model lifecycle, training data, code, evaluation, and reproducible artifacts.
- Llama 3 technical report — case study in modern large-scale training.
- BLOOM — case study in multilingual, collaborative, large-scale training.
- Dolma / FineWeb / DataComp-LM — case studies in data curation.


## Open research and development resource

This repository is intended to be a living, citable knowledge base for LLM engineering. It is designed for teaching, experimentation, research reproduction, technical planning, and real-world model-development programs.

Readers are encouraged to explore the material, reproduce experiments, report failures, propose corrections, add new experiments, translate explanations, and contribute improved teaching material.

The project values scientific traceability: important claims should point to evidence; experimental results should include configurations and limitations; changing recommendations should be dated; and historical releases should remain referenceable.

## How to Cite This Repository

### For papers, reports, and research derived from this repository

Cite the **specific release or Git commit** you used whenever possible. If the work also relies on an underlying paper, dataset, model, or software project, cite that original source as well. This repository citation identifies the curriculum, notebook, runbook, experiment, or proposal framework that contributed to your work.

For long-lived academic references, prefer a **release DOI** once the corresponding GitHub release has been archived. Until a DOI release exists, cite the repository URL together with the exact commit or tag.

### Recommended BibTeX

The machine-readable citation file is available at [CITATION.cff](CITATION.cff), and a ready-to-copy BibTeX record is available at [CITATION.bib](CITATION.bib).

```bibtex
@misc{hashemi2026llmtrainer,
  author       = {Hashemi, Seyed Mohammad Abuzar},
  title        = {LLM Trainer Masterclass},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/mahashemi/llm-training-mastercalss},
  note         = {Free-first, research-oriented curriculum for understanding, building, training, evaluating, optimizing, deploying, and managing large language models}
}
```

For reproducibility, add the release or commit used, for example:

```text
https://github.com/mahashemi/llm-training-mastercalss/tree/<TAG>
```

or

```text
https://github.com/mahashemi/llm-training-mastercalss/commit/<COMMIT>
```

## Quality bar

The target is not simply a large collection of tutorials. The target is a durable engineering curriculum in which a learner can progress from intuition to implementation, from implementation to controlled experimentation, and from experimentation to resource planning and organizational decision-making.

The project explicitly aims to teach learners how to build evidence for a model proposal: mission, users, data, architecture, training method, compute, people, evaluation, safety, deployment, budget, milestones, risks, and measurable outcomes.

## Project status

The curriculum is under active development. The field changes quickly, so material may be revised as new papers, models, datasets, training techniques, hardware, and evaluation practices become available. Substantive updates should be recorded in the changelog and associated with a release or commit whenever practical.

## Open licensing

Original educational material is intended to be shared under CC BY 4.0, while source code and code examples are intended to be shared under the MIT License. Third-party material remains under its original terms. See LICENSE.md and LICENSE-CODE.

## Repository health

The project includes contribution guidelines, a code of conduct, security guidance, issue templates, code ownership, a reproducibility standard, maintenance policy, and release checklist. These are designed to keep the repository useful as a living research and engineering reference.

## Current build status

The repository currently contains:

- two standalone courses with 12 deep-learning chapters and 24 LLM-engineering chapters;
- an optional 76-chapter deep-reference textbook;
- primary laboratories attached to the course chapters, with real datasets, worked experiments, answer keys, and research extensions;
- 14 optional operational runbooks;
- a research project catalog spanning 48 project tracks from foundational experiments to publication-grade capstones;
- research, proposal, model-card, dataset-card, and experiment templates;
- curated lecture/video and paper-reading paths;
- citation, reproducibility, maintenance, governance, security, and contribution standards.

Use `START_HERE.md` for the learner path and the README matrix for the complete lecture sequence. The textbook remains optional deep reference.

## Mastery standard

Completing a notebook is not mastery. A learner graduates from each major stage only after producing evidence:

**understand → implement → measure → break → explain → decide → reproduce**.

The final standard is the Model Program Dossier in `projects/04_llm_program_dossier.md`.
