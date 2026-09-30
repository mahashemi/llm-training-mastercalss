# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to **understand, build, train, evaluate, optimize, deploy, and manage large language models**—from a tiny GPT and real open-weight checkpoints to H100-scale systems, research, economics, and program design.

**Audience:** high-school graduates, engineers, researchers, and organizations.

## Learning Graph — the one path through the repository

**[Open the complete Learning Graph](docs/LEARNING_GRAPH.md)** · **[Open the Dataset Learning Matrix](data/REAL_DATASET_REGISTRY.md)** · **[Open the Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)**

The repository is organized as one learning graph, not as separate lecture/notebook/runbook courses. Each stage connects concept → lecture → book → real artifact → experiment → evaluation → decision.

## Master Course Flow — the one path through the repository

**This README is the canonical learning path.** Do not complete folders independently. For each stage:

**lecture → textbook → primary laboratory → runbook/decision aid → evidence**

The separate lecture and textbook TOCs live in [LECTURE_INDEX](lectures/LECTURE_INDEX.md) and [BOOK_TOC](BOOK_TOC.md). They are intentionally **not duplicated here**. This one table is the README's compact control plane.

### Master curriculum map

| Stage | Lectures | Book coverage | Primary laboratory / real data | Learner evidence |
|---|---|---|---|---|
| **0 · Orient** | L01 foundation entry | Ch. 00 | [Open-Weight Model Audit](notebooks/open_weight_model_audit.ipynb) · [START HERE](START_HERE.md) | model audit + reproducible environment |
| **1 · Foundations** | L01 → L02 → L04 → L05 | Ch. 01–13 | Tiny LM · [Tokenizer](notebooks/tokenizer_design_and_measurement.ipynb) · Tiny Transformer · Attention/MoE | explain tensors, tokenization, loss, attention |
| **2 · Training systems** | L03 → L06 → L07 → L08 → L09 → L11 | Ch. 14–16, 25, 39–40 | resource accounting · GPU/kernel benchmark · tiling · DDP/sharding · scaling · instrumentation | resource model + bottleneck analysis |
| **3 · Evaluation contract** | L12 | Ch. 41–47 | [Evaluation harness](notebooks/evaluation_harness.ipynb) · benchmark design | evaluation contract + failure taxonomy |
| **4 · Real data** | L13 → L14 | Ch. 17–24 | [Real Dataset Corpus Bench](notebooks/real_dataset_corpus_bench.ipynb) · curation · dedup · mixing · **[Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)** | dataset manifest + quality/dedup/mixing report |
| **5 · Train + adapt** | L15 → L18 → L19 | Ch. 26–33, 38 | [Qwen3-0.6B SFT](notebooks/sft_with_a_small_open_model.ipynb) · [LoRA/QLoRA](notebooks/lora_qlora_comparison.ipynb) · [FT vs LoRA](notebooks/full_ft_vs_lora.ipynb) · Tiny-GPT pretraining | controlled baseline/intervention experiment |
| **6 · Align** | L16 → L20 | Ch. 34–37 | RLVR verifier · DPO/distillation concepts | alignment experiment + reward/signal analysis |
| **7 · Extend + release** | L17 → L21 | Ch. 48–50, 73 | multimodal alignment · failure/safety evaluation | release gate + regression analysis |
| **8 · Serve + decide** | L10 → L22 | Ch. 51–64 | KV-cache/serving · API vs RAG vs tools vs training decision lab | architecture decision record + TCO |
| **9 · Program + research** | L23 → L24 | Ch. 65–75 | resource plan · paper/proposal pipeline · capstone | Model Program Dossier |

> **The evaluation loop is deliberate:** define the evaluation contract early, train/adapt against it, then return to evaluation, safety, and release gates.

### How to read the repository

Think of the artifacts as **layers of one course**, not separate courses:

**Lecture = why → Book = how/why in depth → Notebook = prove it → Runbook = operate it → Dataset = reality → Evaluation = decide whether it worked → Project = synthesize it.**

For the full lecture list, use [Lecture Index](lectures/LECTURE_INDEX.md). For all 76 textbook chapters, use [Book TOC](BOOK_TOC.md).

## Supporting materials — use them at the stage, not as separate courses

| Need | Use |
|---|---|
| **Deep explanation** | [Textbook](BOOK_TOC.md) |
| **Instructor narrative** | [Lecture Index](lectures/LECTURE_INDEX.md) |
| **Executable work** | [Notebook map](notebooks/README.md) |
| **Real data** | [Dataset registry](data/REAL_DATASET_REGISTRY.md) · [Real-data bench](notebooks/real_dataset_corpus_bench.ipynb) · **[Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)** |
| **Operational procedure** | [Runbook index](INDEX.md#build) |
| **Engineering decisions** | [Training Method Matrix](docs/TRAINING_METHOD_MATRIX.md) · [Decision Trees](docs/ENGINEERING_DECISION_TREES.md) · **[Learning Graph](docs/LEARNING_GRAPH.md)** |
| **Research / reproducibility** | [Paper Pipeline](docs/PAPER_PIPELINE.md) · [Reproducibility Standard](REPRODUCIBILITY.md) |
| **Final synthesis** | [Projects](INDEX.md#projects) · [Model Program Dossier](projects/04_llm_program_dossier.md) |

**Rule of thumb:** never ask “Which folder do I finish next?” Ask **“Which stage am I in, and what evidence must I produce?”**

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

The course now has an explicit hardware-to-training ladder. Start with a real open-weight model on free Colab, then move the same experiment to larger single-GPU and H100 environments.

**Practical progression:**

CPU tiny GPT → Qwen3-0.6B on free Colab → Qwen3-1.7B/4B experiments → 7B/8B on H100 → Qwen3.8-27B adaptation → multi-GPU training → foundation-model planning.

See **[Open-Weight Training Ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md)** and **[Open-Weight Training Path](book/00_open_weight_training_path.md)**.

The current classroom anchor is Qwen3-0.6B because the official checkpoint is small enough to make a real open-weight workflow practical in a free-first course. The larger-model path is deliberately the same workflow with different resource constraints.

The course distinguishes four different activities that are often incorrectly called “training”: **inference, supervised fine-tuning, continued pretraining, and pretraining from scratch**. It also treats **full FT, LoRA, and QLoRA as parameter-update strategies**, not as alternatives to the training objective itself.

### Open-weight model ladder

| Stage | Model class | Student outcome | Hardware target |
|---|---|---|---|
| Foundation mechanics | tiny GPT | understand every tensor and gradient | CPU / Colab |
| First real checkpoint | Qwen3-0.6B | download, inspect, infer, SFT | free Colab |
| Resource scaling | Qwen3-1.7B/4B | precision, sequence, adapter experiments | Colab / single GPU |
| Professional adaptation | 7B–8B | LoRA, QLoRA, profiling, evaluation | 1× H100 |
| Large-model adaptation | Qwen3.8-27B | memory accounting and parameter-efficient training | 1× H100 for selected workflows; multi-GPU for broader training |
| Distributed training | 7B–30B+ | sharding, communication, checkpointing | multi-GPU H100 |
| Foundation model | project-specific | data + architecture + pretraining program | H100 cluster |

This is intentionally **not** a claim that every model at a given size fits every operation on that hardware. Each notebook must calculate the resource requirement before launching a run.

## Learning engine

Every lesson follows:

**Intuition → visual → mathematics → code → systems → experiment → failure analysis → decision → research question**

Every important concept is taught twice: once for understanding and once for engineering judgment.

## Free-first rule

Practical labs target free Google Colab or CPU fallbacks whenever possible. Colab's free tier provides access to compute resources, including GPUs/TPUs, but availability and limits are dynamic and not guaranteed. Therefore no lab assumes a particular accelerator will always be available.

For large-scale training, the course uses small reproducible runs to teach the method and then converts the same experiment into a scaling proposal with explicit assumptions.

## Repository architecture

- `book/` — textbook chapters and long-form explanations
- `lectures/` — 25-minute lecture scripts and slide plans
- `notebooks/` — executable Colab-first laboratories
- `runbooks/` — operational procedures
- `visuals/` — diagrams and visual teaching assets
- `videos/` — curated public lectures with timestamps, purpose, and critical questions
- `papers/` — paper-reading guides and reproduction plans
- `cheat_sheets/` — compact references
- `projects/` — graded and capstone projects
- `templates/` — experiment cards, paper reports, technical proposals, funding proposals
- `references/` — canonical sources and citations

## Research philosophy

The course treats model training as an experimental science and an engineering discipline. Claims are tied to evidence, configurations are recorded, and every major result is accompanied by a failure analysis and a reproducibility checklist.

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

- 24 lecture packages;
- 76 textbook chapters plus chapter template;
- 28 notebooks including orientation, lecture laboratories, the standalone open-weight model audit, real-data corpus bench, open-weight SFT/PEFT labs, and the end-to-end tiny-GPT pretraining campaign;
- 14 operational runbooks;
- 4 capstone/project briefs;
- research, proposal, model-card, dataset-card, and experiment templates;
- curated lecture/video and paper-reading paths;
- citation, reproducibility, maintenance, governance, security, and contribution standards.

Use `START_HERE.md` for the learner path, `COURSE_MAP.md` for the curriculum map, `BOOK_TOC.md` for the textbook, `BOOK_LAB_MAP.md` for chapter/lab connections, and `notebooks/README.md` for the Colab laboratory map.

## Mastery standard

Completing a notebook is not mastery. A learner graduates from each major stage only after producing evidence:

**understand → implement → measure → break → explain → decide → reproduce**.

The final standard is the Model Program Dossier in `projects/04_llm_program_dossier.md`.
