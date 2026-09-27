# Course Map — LLM Trainer Masterclass

## North-star outcome

This is a curriculum for progressing from Deep Learning fundamentals to independent LLM training and program leadership.

The learner should eventually be able to answer:

> What should we build? Why? With what data? Which training method? How much compute? How much will it cost? How will we know it worked? What can fail? What should be funded?

## 24 lecture sequence

| # | Lecture | Main lab |
|---|---|---|
| 01 | What Is an LLM? | [Tiny language model](notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb) |
| 02 | Tokenization | [Tokenizer measurement](notebooks/tokenizer_design_and_measurement.ipynb) |
| 03 | PyTorch and Resource Accounting | [FLOPs + memory](notebooks/resource_accounting_flops_memory.ipynb) |
| 04 | Transformer Architectures | [Tiny Transformer](notebooks/build_a_tiny_transformer.ipynb) |
| 05 | Attention Alternatives and MoE | [Attention/MoE](notebooks/attention_and_moe_lab.ipynb) |
| 06 | GPUs and Kernels | [GPU benchmark](notebooks/gpu_kernel_benchmark.ipynb) |
| 07 | Efficient Attention and Triton | [Attention tiling](notebooks/attention_memory_and_tiling.ipynb) |
| 08 | Distributed Training | [DDP/FSDP simulation](notebooks/ddp_and_sharding_simulation.ipynb) |
| 09 | Scaling Laws | [Scaling-law fit](notebooks/scaling_law_fit.ipynb) |
| 10 | Inference Systems | [KV cache](notebooks/inference_and_kv_cache.ipynb) |
| 11 | Training System Design | [Instrumentation](notebooks/training_loop_instrumentation.ipynb) |
| 12 | Evaluation | [Evaluation harness](notebooks/evaluation_harness.ipynb) |
| 13 | Data Sources and Dataset Construction | [Curation pipeline](notebooks/dataset_curation_pipeline.ipynb) |
| 14 | Filtering, Deduplication, Mixing, Synthetic Data | [Dedup + mixing](notebooks/dedup_and_data_mixing.ipynb) |
| 15 | Mid/Post Training: SFT and RLHF | [SFT](notebooks/sft_with_a_small_open_model.ipynb) |
| 16 | Reinforcement Learning with Verifiable Rewards | [RLVR toy](notebooks/rlvr_toy_experiment.ipynb) |
| 17 | Multimodality | [Multimodal map](notebooks/multimodal_alignment_map.ipynb) |
| 18 | LoRA, QLoRA, and PEFT | [LoRA/QLoRA](notebooks/lora_qlora_comparison.ipynb) |
| 19 | Full Fine-Tuning and Continued Pretraining | [Full FT vs LoRA](notebooks/full_ft_vs_lora.ipynb) |
| 20 | Preference Optimization and Distillation | [DPO + distillation](notebooks/dpo_and_distillation_concepts.ipynb) |
| 21 | Safety, Robustness, Failure Analysis | [Failure analysis](notebooks/failure_analysis_and_safety_eval.ipynb) |
| 22 | API vs RAG vs Tools vs Training | [Build-vs-buy](notebooks/build_vs_buy_decision_lab.ipynb) |
| 23 | Build an LLM Program | [Resource planning](notebooks/national_llm_resource_plan.ipynb) |
| 24 | From Experiment to Fundable Model | [Capstone](notebooks/capstone_model_program.ipynb) |

## Textbook

Chapters 1–75 are the durable reference layer. See BOOK_TOC.md for the full linked table of contents.

## Mastery gates

1. Understand — explain the method.
2. Implement — build the smallest useful version.
3. Measure — establish a baseline and quantitative result.
4. Break — violate one assumption and diagnose the failure.
5. Decide — choose an approach under constraints.
6. Reproduce — another person can rerun it.
7. Research — formulate a falsifiable research question.
8. Program — convert evidence into a budgeted implementation plan.

## Free-first progression

CPU → free Colab → small GPU experiments → analytical scaling → real cluster proposal.

Paid compute enters only after the learner demonstrates that the experiment is worth scaling.

## Operating rule

Never scale an experiment merely because more hardware is available. Scale when the expected information or capability gain justifies the additional resource.