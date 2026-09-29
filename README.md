# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to design, train, evaluate, optimize, deploy, and manage large language models.

**Audience:** high-school graduates, engineers, researchers, and organizations. The course begins from intuition and builds toward systems engineering, research, economics, and national-scale model planning.

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

## Course Materials — Start Here

| Stage | What you learn | Core materials |
|---|---|---|
| 0. Orientation | How to use the course, resource thinking, reproducibility | [START HERE](START_HERE.md) · [Course Operating Manual](docs/COURSE_OPERATING_MANUAL.md) |
| 1. Foundations | Tokens, probabilities, embeddings, attention, Transformers, training | [Lectures 01–08](lectures/LECTURE_INDEX.md) · [Book](BOOK_TOC.md) · [Labs](notebooks/README.md) |
| 2. Data | Corpus construction, filtering, deduplication, mixing, synthetic data | [Lectures 13–14](lectures/LECTURE_INDEX.md) · [Data Runbook](runbooks/01_dataset_curation_runbook.md) |
| 3. Pretraining | Scaling laws, resource accounting, checkpoints, distributed training | [Pretraining Runbook](runbooks/02_pretraining_runbook.md) · [Resource Estimation](docs/RESOURCE_ESTIMATION.md) · [Tiny GPT campaign](notebooks/25_tiny_gpt_pretraining_campaign.ipynb) |
| 4. Post-training | SFT, full fine-tuning, LoRA, QLoRA, DPO, RLHF, RLVR, distillation | [Training Method Matrix](docs/TRAINING_METHOD_MATRIX.md) · [Lectures 15–20](lectures/LECTURE_INDEX.md) |
| 5. Evaluation | Benchmarks, human/model judges, ablations, safety, robustness | [Evaluation Runbook](runbooks/07_evaluation_runbook.md) · [Assessment](docs/ASSESSMENT_AND_MASTERY.md) |
| 6. Serving | KV cache, batching, quantization, vLLM, inference economics | [Serving Runbook](runbooks/08_inference_serving_runbook.md) · [Systems Stack](docs/SYSTEMS_STACK.md) |
| 7. Build vs Buy | API vs RAG vs tools vs fine-tuning vs pretraining | [Decision Trees](docs/ENGINEERING_DECISION_TREES.md) · [Build-vs-Buy Lab](notebooks/build_vs_buy_decision_lab.ipynb) |
| 8. LLM Programs | Multilingual/national models, compute, teams, governance | [Program chapters](BOOK_TOC.md) · [Program Runbooks](runbooks/09_funding_and_program_proposal_runbook.md) |
| 9. Research + Funding | Reproduction, paper writing, proposal, budget, milestones | [Paper Pipeline](docs/PAPER_PIPELINE.md) · [Funding Pitch](templates/funding_pitch.md) · [Capstone](projects/04_llm_program_dossier.md) |

### 24-Lecture Table of Contents

| # | Lecture | Lecture | Lab / Primary artifact |
|---:|---|---|---|
| 01 | What Is an LLM? | [Lecture](lectures/01_what_is_an_llm/lecture.md) | [Tiny language model](notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb) |
| 02 | Tokenization | [Lecture](lectures/02_tokenization/lecture.md) | [BPE tokenizer](notebooks/tokenizer_design_and_measurement.ipynb) |
| 03 | PyTorch and Resource Accounting | [Lecture](lectures/03_pytorch_and_resource_accounting/lecture.md) | [FLOPs + memory](notebooks/resource_accounting_flops_memory.ipynb) |
| 04 | Transformer Architectures | [Lecture](lectures/04_transformer_architectures/lecture.md) | [Tiny Transformer](notebooks/build_a_tiny_transformer.ipynb) |
| 05 | Attention Alternatives and MoE | [Lecture](lectures/05_attention_alternatives_and_moe/lecture.md) | [Attention / MoE](notebooks/attention_and_moe_lab.ipynb) |
| 06 | GPUs and Kernels | [Lecture](lectures/06_gpus_and_kernels/lecture.md) | [GPU benchmark](notebooks/gpu_kernel_benchmark.ipynb) |
| 07 | Efficient Attention and Triton | [Lecture](lectures/07_efficient_attention_and_triton/lecture.md) | [Attention tiling](notebooks/attention_memory_and_tiling.ipynb) |
| 08 | Distributed Training | [Lecture](lectures/08_distributed_training/lecture.md) | [DDP / sharding](notebooks/ddp_and_sharding_simulation.ipynb) |
| 09 | Scaling Laws | [Lecture](lectures/09_scaling_laws/lecture.md) | [Scaling-law fit](notebooks/scaling_law_fit.ipynb) |
| 10 | Inference Systems | [Lecture](lectures/10_inference_systems/lecture.md) | [KV cache](notebooks/inference_and_kv_cache.ipynb) |
| 11 | Training System Design | [Lecture](lectures/11_training_system_design/lecture.md) | [Instrumentation](notebooks/training_loop_instrumentation.ipynb) |
| 12 | Evaluation | [Lecture](lectures/12_evaluation/lecture.md) | [Evaluation harness](notebooks/evaluation_harness.ipynb) |
| 13 | Data Sources and Dataset Construction | [Lecture](lectures/13_data_sources_and_dataset_construction/lecture.md) | [Curation pipeline](notebooks/dataset_curation_pipeline.ipynb) |
| 14 | Filtering, Deduplication, Mixing, Synthetic Data | [Lecture](lectures/14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) | [Dedup + mixing](notebooks/dedup_and_data_mixing.ipynb) |
| 15 | Mid/Post Training: SFT and RLHF | [Lecture](lectures/15_mid_and_post_training_sft_and_rlhf/lecture.md) | [SFT](notebooks/sft_with_a_small_open_model.ipynb) |
| 16 | Reinforcement Learning with Verifiable Rewards | [Lecture](lectures/16_reinforcement_learning_with_verifiable_rewards/lecture.md) | [RLVR](notebooks/rlvr_toy_experiment.ipynb) |
| 17 | Multimodality | [Lecture](lectures/17_multimodality/lecture.md) | [Multimodal map](notebooks/multimodal_alignment_map.ipynb) |
| 18 | LoRA, QLoRA, and PEFT | [Lecture](lectures/18_lora_qlora_and_peft/lecture.md) | [LoRA / QLoRA](notebooks/lora_qlora_comparison.ipynb) |
| 19 | Full Fine-Tuning and Continued Pretraining | [Lecture](lectures/19_full_fine_tuning_and_continued_pretraining/lecture.md) | [FT vs LoRA](notebooks/full_ft_vs_lora.ipynb) |
| 20 | Preference Optimization and Distillation | [Lecture](lectures/20_preference_optimization_and_distillation/lecture.md) | [DPO + distillation](notebooks/dpo_and_distillation_concepts.ipynb) |
| 21 | Safety, Robustness, Failure Analysis | [Lecture](lectures/21_safety_robustness_and_failure_analysis/lecture.md) | [Failure analysis](notebooks/failure_analysis_and_safety_eval.ipynb) |
| 22 | API vs RAG vs Tools vs Training | [Lecture](lectures/22_api_vs_rag_vs_tools_vs_training/lecture.md) | [Build-vs-buy](notebooks/build_vs_buy_decision_lab.ipynb) |
| 23 | Build an LLM Program | [Lecture](lectures/23_build_an_llm_program/lecture.md) | [Resource plan](notebooks/national_llm_resource_plan.ipynb) |
| 24 | From Experiment to Fundable Model | [Lecture](lectures/24_from_experiment_to_fundable_model/lecture.md) | [Capstone](notebooks/capstone_model_program.ipynb) |

### Research / Reproducibility Navigation

[Book TOC](BOOK_TOC.md) · [Paper Reading Path](papers/PAPER_READING_PATH.md) · [Experiment → Paper](docs/PAPER_PIPELINE.md) · [Reproducibility Standard](REPRODUCIBILITY.md) · [Contribution Guide](CONTRIBUTING.md)

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
- 75 textbook chapters plus chapter template;
- 27 notebooks including orientation, one lab per numbered lecture, and the end-to-end tiny-GPT pretraining campaign;\n- a dedicated open-weight model-loading and hardware-progression track;
- 13 operational runbooks;
- 4 capstone/project briefs;
- research, proposal, model-card, dataset-card, and experiment templates;
- curated lecture/video and paper-reading paths;
- citation, reproducibility, maintenance, governance, security, and contribution standards.

Use `START_HERE.md` for the learner path, `COURSE_MAP.md` for the curriculum map, `BOOK_TOC.md` for the textbook, and `notebooks/README.md` for the Colab laboratory map.

## Mastery standard

Completing a notebook is not mastery. A learner graduates from each major stage only after producing evidence:

**understand → implement → measure → break → explain → decide → reproduce**.

The final standard is the Model Program Dossier in `projects/04_llm_program_dossier.md`.
