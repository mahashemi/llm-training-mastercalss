# Lecture Index

Every lecture has a linked executable laboratory and a required evidence artifact.

| # | Lecture | Primary lab | Evidence |
|---:|---|---|---|
| 01 | [What Is an LLM](01_what_is_an_llm/lecture.md) | [Tiny LM](../notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb) | loss + generation + training/inference explanation |
| 02 | [Tokenization](02_tokenization/lecture.md) | [Tokenizer](../notebooks/tokenizer_design_and_measurement.ipynb) | fertility + sequence expansion |
| 03 | [PyTorch + Resource Accounting](03_pytorch_and_resource_accounting/lecture.md) | [Resources](../notebooks/resource_accounting_flops_memory.ipynb) | memory/FLOPs worksheet |
| 04 | [Transformer Architectures](04_transformer_architectures/lecture.md) | [Tiny Transformer](../notebooks/build_a_tiny_transformer.ipynb) | tensor-shape audit |
| 05 | [Attention Alternatives + MoE](05_attention_alternatives_and_moe/lecture.md) | [Attention/MoE](../notebooks/attention_and_moe_lab.ipynb) | KV/resource comparison |
| 06 | [GPUs and Kernels](06_gpus_and_kernels/lecture.md) | [GPU benchmark](../notebooks/gpu_kernel_benchmark.ipynb) | measured throughput |
| 07 | [Efficient Attention + Triton](07_efficient_attention_and_triton/lecture.md) | [Attention tiling](../notebooks/attention_memory_and_tiling.ipynb) | memory/latency comparison |
| 08 | [Distributed Training](08_distributed_training/lecture.md) | [DDP/sharding](../notebooks/ddp_and_sharding_simulation.ipynb) | scaling-efficiency model |
| 09 | [Scaling Laws](09_scaling_laws/lecture.md) | [Scaling fit](../notebooks/scaling_law_fit.ipynb) | fit + extrapolation error |
| 10 | [Inference Systems](10_inference_systems/lecture.md) | [KV cache](../notebooks/inference_and_kv_cache.ipynb) | TTFT/ITL/memory |
| 11 | [Training System Design](11_training_system_design/lecture.md) | [Instrumentation](../notebooks/training_loop_instrumentation.ipynb) | observable training run |
| 12 | [Evaluation](12_evaluation/lecture.md) | [Evaluation harness](../notebooks/evaluation_harness.ipynb) | scorecard + slices |
| 13 | [Data Sources + Construction](13_data_sources_and_dataset_construction/lecture.md) | [Curation](../notebooks/dataset_curation_pipeline.ipynb) | transformation accounting |
| 14 | [Filtering + Dedup + Mixing](14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) | [Data interventions](../notebooks/dedup_and_data_mixing.ipynb) | controlled data experiment |
| 15 | [SFT + RLHF](15_mid_and_post_training_sft_and_rlhf/lecture.md) | [Qwen3-0.6B SFT](../notebooks/sft_with_a_small_open_model.ipynb) | baseline → smoke → SFT |
| 16 | [RLVR](16_reinforcement_learning_with_verifiable_rewards/lecture.md) | [RLVR toy](../notebooks/rlvr_toy_experiment.ipynb) | verifier/reward failure |
| 17 | [Multimodality](17_multimodality/lecture.md) | [Alignment map](../notebooks/multimodal_alignment_map.ipynb) | visual-token budget |
| 18 | [LoRA + QLoRA](18_lora_qlora_and_peft/lecture.md) | [PEFT comparison](../notebooks/lora_qlora_comparison.ipynb) | rank/precision/resource frontier |
| 19 | [Full FT + Continued PT](19_full_fine_tuning_and_continued_pretraining/lecture.md) | [FT vs LoRA](../notebooks/full_ft_vs_lora.ipynb) | adaptation trade-off |
| 20 | [Preference + Distillation](20_preference_optimization_and_distillation/lecture.md) | [DPO/distillation](../notebooks/dpo_and_distillation_concepts.ipynb) | preference + KL experiment |
| 21 | [Safety + Failure Analysis](21_safety_robustness_and_failure_analysis/lecture.md) | [Failure analysis](../notebooks/failure_analysis_and_safety_eval.ipynb) | severity/type matrix |
| 22 | [API/RAG/Tools/Training](22_api_vs_rag_vs_tools_vs_training/lecture.md) | [Build vs buy](../notebooks/build_vs_buy_decision_lab.ipynb) | architecture decision record |
| 23 | [Build an LLM Program](23_build_an_llm_program/lecture.md) | [Resource plan](../notebooks/national_llm_resource_plan.ipynb) | evidence-to-resource chain |
| 24 | [Fundable Model](24_from_experiment_to_fundable_model/lecture.md) | [Capstone](../notebooks/capstone_model_program.ipynb) | staged model program |

## Teaching invariant

The lecture is not complete until students have:

**predicted → run → measured → broken → diagnosed → decided**

See [Book ↔ Lecture ↔ Laboratory Map](../BOOK_LAB_MAP.md).
