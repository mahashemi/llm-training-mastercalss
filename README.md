# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to **understand, build, train, evaluate, optimize, deploy, and manage large language models**—from a tiny GPT and real open-weight checkpoints to H100-scale systems, research, economics, and program design.

**Audience:** high-school graduates, engineers, researchers, and organizations.

## Master Course Flow — the one path through the repository

**This README is the canonical learning path.** Do not try to complete folders independently. For each stage, use this order:

**lecture → assigned textbook chapters → primary laboratory → attached runbook/decision aid when needed → evidence artifact**

The **lecture IDs (01–24) remain stable**, but the teaching order below is intentionally reorganized around dependencies. The book is the deep explanation layer; lectures provide the narrative; notebooks are where the mechanism becomes measurable; runbooks are operational references rather than another curriculum to read linearly.

```mermaid
flowchart TD
    A["0 · Orient<br/>Practical spine + real checkpoint"] --> B["1 · Foundations<br/>LM → tokens → Transformer → attention"]
    B --> C["2 · Training systems<br/>math → GPUs → kernels → distributed → scaling"]
    C --> D["3 · Evaluation contract<br/>define what success means"]
    D --> E["4 · Real data<br/>sources → quality → dedup → mixtures"]
    E --> F["5 · Train & adapt<br/>pretraining → SFT → FT → LoRA/QLoRA"]
    F --> G["6 · Align<br/>RLVR → preferences → distillation"]
    G --> H["7 · Extend & release<br/>multimodality + safety + robustness"]
    H --> I["8 · Serve & decide<br/>inference → RAG/tools → build vs buy"]
    I --> J["9 · Program & research<br/>national strategy → resources → funding"]
    F -. evaluate again .-> D


| Stage | Natural teaching order | Textbook coverage | Primary hands-on work |
|---|---|---|---|
| **0. Orient** | Open-weight path before abstraction overload | Ch. 00 | [Open-Weight Model Audit](notebooks/open_weight_model_audit.ipynb), [START HERE](START_HERE.md) |
| **1. Foundations** | L01 → L02 → L04 → L05 | Ch. 01–13 | Tiny LM, tokenizer, tiny Transformer, attention/MoE |
| **2. Training + systems** | L03 → L06 → L07 → L08 → L09 → L11 | Ch. 14–16, 25, 39–40 | resource accounting, GPU/kernel, tiling, distributed, scaling, instrumentation |
| **3. Evaluation contract** | L12 | Ch. 41–47 | evaluation harness + benchmark design before expensive training |
| **4. Real data** | L13 → L14 | Ch. 17–24 | [Real Dataset Corpus Bench](notebooks/real_dataset_corpus_bench.ipynb), curation, filtering, dedup, mixing |
| **5. Train + adapt** | L15 → L18 → L19 | Ch. 26–33, 38 | [Qwen3-0.6B SFT](notebooks/sft_with_a_small_open_model.ipynb), [LoRA/QLoRA](notebooks/lora_qlora_comparison.ipynb), [Full FT vs LoRA](notebooks/full_ft_vs_lora.ipynb), [Tiny-GPT pretraining campaign](notebooks/25_tiny_gpt_pretraining_campaign.ipynb) |
| **6. Align** | L16 → L20 | Ch. 34–37 | RLVR verifier experiment; DPO + distillation concepts |
| **7. Extend + release** | L17 → L21 | Ch. 48–50, 73; L17 is a lecture-led multimodality extension with no dedicated textbook chapter | multimodal alignment map; failure/safety evaluation |
| **8. Serve + decide** | L10 → L22 | Ch. 51–64 | KV-cache/serving lab; API vs RAG vs tools vs training decision lab |
| **9. Program + research** | L23 → L24 | Ch. 65–75 | resource plan, program design, paper/proposal pipeline, capstone dossier |

> **The evaluation loop is deliberate:** students define the evaluation contract early (Stage 3), train/adapt against it, then return to evaluation and safety in Stage 7.

## Lecture Series TOC — 24 lectures

The table is the **canonical lecture ID list**. Follow the **Natural teaching order** above rather than reading 01–24 blindly as the only possible sequence.

| # | Lecture | Primary laboratory |
|---:|---|---|
| 01 | [What Is an LLM](01_what_is_an_llm/lecture.md) | [Tiny LM](../notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb) |
| 02 | [Tokenization](02_tokenization/lecture.md) | [Tokenizer](../notebooks/tokenizer_design_and_measurement.ipynb) |
| 03 | [PyTorch + Resource Accounting](03_pytorch_and_resource_accounting/lecture.md) | [Resources](../notebooks/resource_accounting_flops_memory.ipynb) |
| 04 | [Transformer Architectures](04_transformer_architectures/lecture.md) | [Tiny Transformer](../notebooks/build_a_tiny_transformer.ipynb) |
| 05 | [Attention Alternatives + MoE](05_attention_alternatives_and_moe/lecture.md) | [Attention/MoE](../notebooks/attention_and_moe_lab.ipynb) |
| 06 | [GPUs and Kernels](06_gpus_and_kernels/lecture.md) | [GPU benchmark](../notebooks/gpu_kernel_benchmark.ipynb) |
| 07 | [Efficient Attention + Triton](07_efficient_attention_and_triton/lecture.md) | [Attention tiling](../notebooks/attention_memory_and_tiling.ipynb) |
| 08 | [Distributed Training](08_distributed_training/lecture.md) | [DDP/sharding](../notebooks/ddp_and_sharding_simulation.ipynb) |
| 09 | [Scaling Laws](09_scaling_laws/lecture.md) | [Scaling fit](../notebooks/scaling_law_fit.ipynb) |
| 10 | [Inference Systems](10_inference_systems/lecture.md) | [KV cache](../notebooks/inference_and_kv_cache.ipynb) |
| 11 | [Training System Design](11_training_system_design/lecture.md) | [Instrumentation](../notebooks/training_loop_instrumentation.ipynb) |
| 12 | [Evaluation](12_evaluation/lecture.md) | [Evaluation harness](../notebooks/evaluation_harness.ipynb) |
| 13 | [Data Sources + Construction](13_data_sources_and_dataset_construction/lecture.md) | [Curation](../notebooks/dataset_curation_pipeline.ipynb) |
| 14 | [Filtering + Dedup + Mixing](14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) | [Data interventions](../notebooks/dedup_and_data_mixing.ipynb) |
| 15 | [SFT + RLHF](15_mid_and_post_training_sft_and_rlhf/lecture.md) | [Qwen3-0.6B SFT](../notebooks/sft_with_a_small_open_model.ipynb) |
| 16 | [RLVR](16_reinforcement_learning_with_verifiable_rewards/lecture.md) | [RLVR toy](../notebooks/rlvr_toy_experiment.ipynb) |
| 17 | [Multimodality](17_multimodality/lecture.md) | [Alignment map](../notebooks/multimodal_alignment_map.ipynb) |
| 18 | [LoRA + QLoRA](18_lora_qlora_and_peft/lecture.md) | [PEFT comparison](../notebooks/lora_qlora_comparison.ipynb) |
| 19 | [Full FT + Continued PT](19_full_fine_tuning_and_continued_pretraining/lecture.md) | [FT vs LoRA](../notebooks/full_ft_vs_lora.ipynb) |
| 20 | [Preference + Distillation](20_preference_optimization_and_distillation/lecture.md) | [DPO/distillation](../notebooks/dpo_and_distillation_concepts.ipynb) |
| 21 | [Safety + Failure Analysis](21_safety_robustness_and_failure_analysis/lecture.md) | [Failure analysis](../notebooks/failure_analysis_and_safety_eval.ipynb) |
| 22 | [API/RAG/Tools/Training](22_api_vs_rag_vs_tools_vs_training/lecture.md) | [Build vs buy](../notebooks/build_vs_buy_decision_lab.ipynb) |
| 23 | [Build an LLM Program](23_build_an_llm_program/lecture.md) | [Resource plan](../notebooks/national_llm_resource_plan.ipynb) |
| 24 | [Fundable Model](24_from_experiment_to_fundable_model/lecture.md) | [Capstone](../notebooks/capstone_model_program.ipynb) |

### Textbook TOC — at a glance

| Part | Chapters | Main arc |
|---|---:|---|
| Practical path | 00 | Open-weight model workflow, resource accounting, reproducibility |
| Language models without magic | 01 | Probability model and next-token prediction |
| Part I | 02–10 | Tokenization, logits/loss, embeddings, RoPE, residuals, MLPs, attention, autoregressive training, hyperparameters |
| Parts II–III | 11–20 | Attention shapes, GQA/MQA, MoE, optimization, batching, data, filtering, dedup, mixing |
| Part IV | 21–30 | Synthetic data, contamination, pipelines, target-language tokenizer, pretraining, continued PT, SFT, full FT, LoRA, QLoRA |
| Part V | 31–40 | Adapter variants, forgetting, instruction/preference data, RLHF, DPO, distillation, quantization, checkpointing, scale |
| Part VI | 41–50 | Loss/perplexity, benchmarks, human/judge evaluation, error taxonomies, ablations, statistics, groundedness, robustness, release engineering |
| Parts VII–VIII | 51–70 | Inference, KV cache, serving, RAG, tools/agents, API economics/privacy, training-method decisions, national language/data, teams, compute, scale, risk |
| Parts VIII–IX | 71–75 | Architecture choices, governance, national/multilingual evaluation, technical proposal, funding/publication |

<details>
<summary>Open the full 76-chapter textbook TOC</summary>

## PRACTICAL TRAINING PATH

00. [The Open-Weight Training Path](book/00_open_weight_training_path.md)

This chapter is the bridge from the conceptual textbook to actual checkpoint download, inference, SFT/PEFT, H100 adaptation, distributed training, and pretraining.

## LANGUAGE MODELS WITHOUT MAGIC

01. [A Language Model Is A Probability Model](book/01_language_models_without_magic/01_a_language_model_is_a_probability_model.md)

## PART I

02. [Tokenization As A Modeling Decision](book/02_part_i/02_tokenization_as_a_modeling_decision.md)
02. [Logits Softmax And Cross Entropy](book/02_part_i/03_logits_softmax_and_cross_entropy.md)
02. [Embeddings And Representations](book/02_part_i/04_embeddings_and_representations.md)
02. [Positional Information And Rope](book/02_part_i/05_positional_information_and_rope.md)
02. [Residual Streams And Normalization](book/02_part_i/06_residual_streams_and_normalization.md)
02. [Feed Forward Networks And Swiglu](book/02_part_i/07_feed_forward_networks_and_swiglu.md)
02. [Causal Self Attention](book/02_part_i/08_causal_self_attention.md)
02. [Autoregressive Training And Generation](book/02_part_i/09_autoregressive_training_and_generation.md)
02. [Hyperparameters As A Coupled System](book/02_part_i/10_hyperparameters_as_a_coupled_system.md)

## PART II AND III

03. [Multi Head Attention Shapes](book/03_part_ii_and_iii/11_multi_head_attention_shapes.md)
03. [Gqa And Mqa](book/03_part_ii_and_iii/12_gqa_and_mqa.md)
03. [Mixture Of Experts](book/03_part_ii_and_iii/13_mixture_of_experts.md)
03. [Initialization And Optimization Stability](book/03_part_ii_and_iii/14_initialization_and_optimization_stability.md)
03. [Optimizers Adamw And Schedules](book/03_part_ii_and_iii/15_optimizers_adamw_and_schedules.md)
03. [Gradient Accumulation And Effective Batch Size](book/03_part_ii_and_iii/16_gradient_accumulation_and_effective_batch_size.md)
03. [Pretraining Corpus Design](book/03_part_ii_and_iii/17_pretraining_corpus_design.md)
03. [Document Filtering And Quality Models](book/03_part_ii_and_iii/18_document_filtering_and_quality_models.md)
03. [Exact And Near Deduplication](book/03_part_ii_and_iii/19_exact_and_near_deduplication.md)
03. [Data Mixing And Sampling](book/03_part_ii_and_iii/20_data_mixing_and_sampling.md)

## PART IV

04. [Synthetic Data](book/04_part_iv/21_synthetic_data.md)
04. [Contamination And Leakage](book/04_part_iv/22_contamination_and_leakage.md)
04. [Data Pipelines As Distributed Systems](book/04_part_iv/23_data_pipelines_as_distributed_systems.md)
04. [Tokenizer Training For A Target Language](book/04_part_iv/24_tokenizer_training_for_a_target_language.md)
04. [Pretraining Run Design](book/04_part_iv/25_pretraining_run_design.md)
04. [Continued Pretraining](book/04_part_iv/26_continued_pretraining.md)
04. [Supervised Fine Tuning](book/04_part_iv/27_supervised_fine_tuning.md)
04. [Full Fine Tuning](book/04_part_iv/28_full_fine_tuning.md)
04. [Lora Fundamentals](book/04_part_iv/29_lora_fundamentals.md)
04. [Qlora And Quantized Training](book/04_part_iv/30_qlora_and_quantized_training.md)

## PART V

05. [Adapter Variants And Dora](book/05_part_iv/31_adapter_variants_and_dora.md)
05. [Catastrophic Forgetting](book/05_part_iv/32_catastrophic_forgetting.md)
05. [Instruction Data Design](book/05_part_iv/33_instruction_data_design.md)
05. [Preference Data](book/05_part_iv/34_preference_data.md)
05. [Rlhf Pipeline](book/05_part_iv/35_rlhf_pipeline.md)
05. [Dpo Mechanics](book/05_part_iv/36_dpo_mechanics.md)
05. [Distillation](book/05_part_iv/37_distillation.md)
05. [Quantization](book/05_part_iv/38_quantization.md)
05. [Checkpointing And Recovery](book/05_part_iv/39_checkpointing_and_recovery.md)
05. [Pretraining At Scale](book/05_part_iv/40_pretraining_at_scale.md)

## PART VI

06. [Validation Loss And Perplexity](book/06_part_v/41_validation_loss_and_perplexity.md)
06. [Benchmark Design](book/06_part_v/42_benchmark_design.md)
06. [Human Evaluation](book/06_part_v/43_human_evaluation.md)
06. [Model As Judge Evaluation](book/06_part_v/44_model_as_judge_evaluation.md)
06. [Error Taxonomies](book/06_part_v/45_error_taxonomies.md)
06. [Ablation Studies](book/06_part_v/46_ablation_studies.md)
06. [Statistical Thinking For Llm Evaluation](book/06_part_v/47_statistical_thinking_for_llm_evaluation.md)
06. [Hallucination And Groundedness](book/06_part_v/48_hallucination_and_groundedness.md)
06. [Robustness And Distribution Shift](book/06_part_v/49_robustness_and_distribution_shift.md)
06. [Evaluation Release Engineering](book/06_part_v/50_evaluation_release_engineering.md)

## PART VII

07. [Inference Graphs And Prefill](book/07_part_vi_and_vii/51_inference_graphs_and_prefill.md)
07. [Kv Cache Memory](book/07_part_vi_and_vii/52_kv_cache_memory.md)
07. [Serving With Vllm](book/07_part_vi_and_vii/53_serving_with_vllm.md)
07. [Quantized Inference](book/07_part_vi_and_vii/54_quantized_inference.md)
07. [Speculative Decoding](book/07_part_vi_and_vii/55_speculative_decoding.md)
07. [Inference Economics](book/07_part_vi_and_vii/56_inference_economics.md)
07. [Knowledge Problem Vs Behavior Problem](book/07_part_vi_and_vii/57_knowledge_problem_vs_behavior_problem.md)
07. [Rag Architecture](book/07_part_vi_and_vii/58_rag_architecture.md)
07. [Tool Use And Agents](book/07_part_vi_and_vii/59_tool_use_and_agents.md)
07. [Api Economics And Tco](book/07_part_vi_and_vii/60_api_economics_and_tco.md)

## PART VIII

08. [Api Privacy And Data Governance](book/08_part_vii_and_viii/61_api_privacy_and_data_governance.md)
08. [When Fine Tuning Is Justified](book/08_part_vii_and_viii/62_when_fine_tuning_is_justified.md)
08. [When Continued Pretraining Is Justified](book/08_part_vii_and_viii/63_when_continued_pretraining_is_justified.md)
08. [When Training From Scratch Is Justified](book/08_part_vii_and_viii/64_when_training_from_scratch_is_justified.md)
08. [National Language Strategy](book/08_part_vii_and_viii/65_national_language_strategy.md)
08. [Low Resource Data Acquisition](book/08_part_vii_and_viii/66_low_resource_data_acquisition.md)
08. [Team Design For Llm Programs](book/08_part_vii_and_viii/67_team_design_for_llm_programs.md)
08. [Compute Procurement And Cluster Design](book/08_part_vii_and_viii/68_compute_procurement_and_cluster_design.md)
08. [Scaling A Pilot Into A Program](book/08_part_vii_and_viii/69_scaling_a_pilot_into_a_program.md)
08. [Risk Register And Kill Criteria](book/08_part_vii_and_viii/70_risk_register_and_kill_criteria.md)

## PART IX

09. [National Model Architecture Choices](book/09_part_viii_and_ix/71_national_model_architecture_choices.md)
09. [Training Data Governance](book/09_part_viii_and_ix/72_training_data_governance.md)
09. [Evaluation For National And Multilingual Models](book/09_part_viii_and_ix/73_evaluation_for_national_and_multilingual_models.md)
09. [The Technical Proposal](book/09_part_viii_and_ix/74_the_technical_proposal.md)
09. [The Funding And Publication Package](book/09_part_viii_and_ix/75_the_funding_and_publication_package.md)

</details>

## Supporting materials — use them at the stage, not as separate courses

| Need | Use |
|---|---|
| **Deep explanation** | [Textbook](BOOK_TOC.md) |
| **Instructor narrative** | [Lecture Index](lectures/LECTURE_INDEX.md) |
| **Executable work** | [Notebook map](notebooks/README.md) |
| **Real data** | [Dataset registry](data/REAL_DATASET_REGISTRY.md) · [Real-data bench](notebooks/real_dataset_corpus_bench.ipynb) |
| **Operational procedure** | [Runbook index](INDEX.md#build) |
| **Engineering decisions** | [Training Method Matrix](docs/TRAINING_METHOD_MATRIX.md) · [Decision Trees](docs/ENGINEERING_DECISION_TREES.md) |
| **Research / reproducibility** | [Paper Pipeline](docs/PAPER_PIPELINE.md) · [Reproducibility Standard](REPRODUCIBILITY.md) |
| **Final synthesis** | [Projects](INDEX.md#projects) · [Model Program Dossier](projects/04_llm_program_dossier.md) |

**Rule of thumb:** never ask “Which folder do I finish next?” Ask **“Which stage am I in, and what evidence must I produce?”**

## North-star outcome

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
