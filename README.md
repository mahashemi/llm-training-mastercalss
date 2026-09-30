# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to **understand, build, train, evaluate, optimize, deploy, and manage large language models**—from a tiny GPT and real open-weight checkpoints to H100-scale systems, research, economics, and program design.

**Audience:** high-school graduates, engineers, researchers, and organizations.

## Learning Graph — the one path through the repository

**[Open the complete Learning Graph](docs/LEARNING_GRAPH.md)** · **[Open the Dataset Learning Matrix](data/REAL_DATASET_REGISTRY.md)** · **[Open the Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)**

The repository is organized as one learning graph, not as separate lecture/notebook/runbook courses. Each stage connects concept → lecture → book → real artifact → experiment → evaluation → decision.

## Master Course Matrix — the single curriculum control plane

**This is the one table you need to navigate the course.** Follow each row from left to right:

**lecture → embedded lab → real data/case → decision → evidence**

The repository's other folders are supporting references. They do **not** define another learning order. A learner should be able to stay inside the lecture sequence and complete each stage without hunting through indexes.

| # / Stage | Lecture | Textbook chapters | Primary laboratory | Real data / longitudinal case | Runbook / decision aid | Evidence / deliverable |
|---|---|---|---|---|---|---|
| **01 · Foundations** | [L01 · What Is an LLM](lectures/01_what_is_an_llm/lecture.md) | Ch. 01–03, 09 | [Tiny LM](lectures/01_what_is_an_llm/lab.ipynb) | [Open-weight audit](lectures/23_build_an_llm_program/open_weight_model_audit.ipynb) | [Open-weight runbook](runbooks/12_open_weight_model_runbook.md) | loss, generation, training-vs-inference explanation |
| **02 · Foundations** | [L02 · Tokenization](lectures/02_tokenization/lecture.md) | Ch. 02, 24 | [Tokenizer measurement](lectures/02_tokenization/lab.ipynb) | [Persian track](data/PERSIAN_DATASET_TRACK.md) · PerSpaCor · CulturaX-fa | [Dataset curation runbook](runbooks/01_dataset_curation_runbook.md) | fertility + Unicode/ZWNJ analysis |
| **03 · Training systems** | [L03 · PyTorch + Resource Accounting](lectures/03_pytorch_and_resource_accounting/lecture.md) | Ch. 11, 40 | [FLOPs + memory](lectures/03_pytorch_and_resource_accounting/lab.ipynb) | Qwen3-0.6B resource baseline | [Resource estimation](docs/RESOURCE_ESTIMATION.md) | memory/FLOPs worksheet |
| **04 · Foundations** | [L04 · Transformer Architectures](lectures/04_transformer_architectures/lecture.md) | Ch. 04–07, 11 | [Tiny Transformer](lectures/04_transformer_architectures/lab.ipynb) | tiny GPT / open-weight checkpoint comparison | [Model selection](runbooks/MODEL_SELECTION_RUNBOOK.md) | tensor-shape audit |
| **05 · Foundations** | [L05 · Attention Alternatives + MoE](lectures/05_attention_alternatives_and_moe/lecture.md) | Ch. 08, 12–13 | [Attention + MoE](lectures/05_attention_alternatives_and_moe/lab.ipynb) | open-weight architecture configs | [Systems stack](docs/SYSTEMS_STACK.md) | KV/resource comparison |
| **06 · Training systems** | [L06 · GPUs and Kernels](lectures/06_gpus_and_kernels/lecture.md) | Ch. 14–16 | [GPU benchmark](lectures/06_gpus_and_kernels/lab.ipynb) | Qwen3 workload shapes | [Systems stack](docs/SYSTEMS_STACK.md) | measured throughput |
| **07 · Training systems** | [L07 · Efficient Attention + Triton](lectures/07_efficient_attention_and_triton/lecture.md) | Ch. 15–16 | [Attention tiling](lectures/07_efficient_attention_and_triton/lab.ipynb) | long-context workload slices | [Systems stack](docs/SYSTEMS_STACK.md) | memory/latency comparison |
| **08 · Training systems** | [L08 · Distributed Training](lectures/08_distributed_training/lecture.md) | Ch. 25, 39 | [DDP + sharding](lectures/08_distributed_training/lab.ipynb) | multi-GPU scaling scenario | [Distributed training runbook](runbooks/06_distributed_training_runbook.md) | scaling-efficiency model |
| **09 · Training systems** | [L09 · Scaling Laws](lectures/09_scaling_laws/lecture.md) | Ch. 40 | [Scaling-law fit](lectures/09_scaling_laws/lab.ipynb) | controlled model/data/compute sweeps | [Resource estimation](docs/RESOURCE_ESTIMATION.md) | fit + extrapolation error |
| **10 · Serve + systems** | [L10 · Inference Systems](lectures/10_inference_systems/lecture.md) | Ch. 51–56 | [KV cache](lectures/10_inference_systems/lab.ipynb) | Qwen3 serving workload | [Inference runbook](runbooks/08_inference_serving_runbook.md) | TTFT / ITL / memory report |
| **11 · Training systems** | [L11 · Training System Design](lectures/11_training_system_design/lecture.md) | Ch. 10, 14–16, 25, 39 | [Training instrumentation](lectures/11_training_system_design/lab.ipynb) | end-to-end training campaign | [Pretraining runbook](runbooks/02_pretraining_runbook.md) | observable training run |
| **12 · Evaluation** | [L12 · Evaluation](lectures/12_evaluation/lecture.md) | Ch. 22, 41–47, 50, 73 | [Evaluation harness](lectures/12_evaluation/lab.ipynb) | ParsiNLU · PersianMedQA · held-out slices | [Evaluation runbook](runbooks/07_evaluation_runbook.md) | scorecard + failure taxonomy |
| **13 · Real data** | [L13 · Data Sources + Construction](lectures/13_data_sources_and_dataset_construction/lecture.md) | Ch. 17–18, 21, 23, 66, 72 | [Real Dataset Corpus Bench](lectures/13_data_sources_and_dataset_construction/lab.ipynb) · [Curation](notebooks/dataset_curation_pipeline.ipynb) | FineWeb · Dolma · CulturaX · Naab · FineWeb2-HQ | [Dataset curation](runbooks/01_dataset_curation_runbook.md) | source manifest + transformation accounting |
| **14 · Real data** | [L14 · Filtering + Dedup + Mixing](lectures/14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) | Ch. 19–20 | [Dedup + mixing](lectures/14_filtering_deduplication_mixing_and_synthetic_data/lab.ipynb) | real-vs-synthetic Persian · FineWeb-Edu · OpenWebMath | [Dataset curation](runbooks/01_dataset_curation_runbook.md) | controlled data intervention |
| **15 · Train + adapt** | [L15 · SFT + RLHF](lectures/15_mid_and_post_training_sft_and_rlhf/lecture.md) | Ch. 26–27, 33 | [Qwen3-0.6B SFT](lectures/15_mid_and_post_training_sft_and_rlhf/lab.ipynb) | Aya · Persian instruction data | [SFT runbook](runbooks/03_sft_runbook.md) | baseline → smoke → SFT → evaluation |
| **16 · Align** | [L16 · RLVR](lectures/16_reinforcement_learning_with_verifiable_rewards/lecture.md) | Ch. 34–35 | [RLVR toy](lectures/16_reinforcement_learning_with_verifiable_rewards/lab.ipynb) | OpenR1-Math-220k · verifier data | [Pretraining decision](runbooks/PRETRAINING_DECISION_RUNBOOK.md) | verifier/reward failure analysis |
| **17 · Extend** | [L17 · Multimodality](lectures/17_multimodality/lecture.md) | Ch. 48–50 | [Multimodal alignment](lectures/17_multimodality/lab.ipynb) | text + image/audio/video modality budget | [Systems stack](docs/SYSTEMS_STACK.md) | modality/token-budget analysis |
| **18 · Train + adapt** | [L18 · LoRA + QLoRA](lectures/18_lora_qlora_and_peft/lecture.md) | Ch. 29–31, 38 | [LoRA / QLoRA](lectures/18_lora_qlora_and_peft/lab.ipynb) | Qwen3-0.6B + Persian adaptation | [PEFT runbook](runbooks/04_peft_lora_qlora_runbook.md) | rank/precision/resource frontier |
| **19 · Train + adapt** | [L19 · Full FT + Continued PT](lectures/19_full_fine_tuning_and_continued_pretraining/lecture.md) | Ch. 28, 32, 63 | [FT vs LoRA](lectures/19_full_fine_tuning_and_continued_pretraining/lab.ipynb) | Persian corpus / domain adaptation | [Full FT runbook](runbooks/05_full_finetuning_runbook.md) | adaptation + forgetting trade-off |
| **20 · Align** | [L20 · Preference + Distillation](lectures/20_preference_optimization_and_distillation/lecture.md) | Ch. 36–37 | [DPO + distillation](lectures/20_preference_optimization_and_distillation/lab.ipynb) | preference pairs / teacher traces | [SFT runbook](runbooks/03_sft_runbook.md) | preference + KL experiment |
| **21 · Evaluate + release** | [L21 · Safety + Failure Analysis](lectures/21_safety_robustness_and_failure_analysis/lecture.md) | Ch. 43, 45, 48–49 | [Failure analysis](lectures/21_safety_robustness_and_failure_analysis/lab.ipynb) | multilingual + adversarial slices | [Model release](runbooks/11_model_release_runbook.md) · [Evaluation](runbooks/07_evaluation_runbook.md) | severity/type matrix + release gate |
| **22 · Serve + decide** | [L22 · API / RAG / Tools / Training](lectures/22_api_vs_rag_vs_tools_vs_training/lecture.md) | Ch. 57–61 | [Build-vs-buy decision lab](lectures/22_api_vs_rag_vs_tools_vs_training/lab.ipynb) | representative application workload | [Training Method Matrix](docs/TRAINING_METHOD_MATRIX.md) · [Decision Trees](docs/ENGINEERING_DECISION_TREES.md) | architecture decision record + TCO |
| **23 · Program + research** | [L23 · Build an LLM Program](lectures/23_build_an_llm_program/lecture.md) | Ch. 64–72 | [National LLM resource plan](lectures/23_build_an_llm_program/lab.ipynb) | Persian-first national-language case | [Funding runbook](runbooks/09_funding_and_program_proposal_runbook.md) · [Experiment → Program](docs/EXPERIMENT_TO_PROGRAM.md) | evidence-to-resource chain |
| **24 · Program + research** | [L24 · Fundable Model](lectures/24_from_experiment_to_fundable_model/lecture.md) | Ch. 73–75 | [Capstone model program](lectures/24_from_experiment_to_fundable_model/lab.ipynb) | all prior evidence | [Funding runbook](runbooks/09_funding_and_program_proposal_runbook.md) | **Model Program Dossier** |

> **Learning loop:** define the evaluation contract early → build/train → measure → break → diagnose → decide → reproduce. The same real-data and Persian cases recur across the matrix so the learner sees how data decisions propagate into tokenization, training, evaluation, serving, and program economics.

### How to use the matrix

Do **not** read every folder independently. Pick the next row, follow its links left-to-right, produce the evidence in the final column, then move to the next row.

****Lecture = the complete learning unit.** The lecture contains the explanation, deep technical material, primary experiment, real-data connection, decision exercise, and mastery evidence. Books and runbooks are optional reference material for instructors or deeper study.**

[Full textbook TOC](BOOK_TOC.md) · [Dataset registry](data/REAL_DATASET_REGISTRY.md) · [Persian longitudinal track](data/PERSIAN_DATASET_TRACK.md) · [Open-weight training ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md)

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

- `lectures/` — the primary 24 self-contained learning packages; each owns its primary lab
- `book/` — optional deep-reference chapters; not required for the learner path
- `runbooks/` — reusable operational procedures for instructors/advanced practitioners
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
- an optional 76-chapter deep-reference textbook;
- executable labs now stored inside their owning lecture packages;
- 14 operational runbooks;
- 4 capstone/project briefs;
- research, proposal, model-card, dataset-card, and experiment templates;
- curated lecture/video and paper-reading paths;
- citation, reproducibility, maintenance, governance, security, and contribution standards.

Use `START_HERE.md` for the learner path and the README matrix for the complete lecture sequence. The textbook remains optional deep reference.

## Mastery standard

Completing a notebook is not mastery. A learner graduates from each major stage only after producing evidence:

**understand → implement → measure → break → explain → decide → reproduce**.

The final standard is the Model Program Dossier in `projects/04_llm_program_dossier.md`.
