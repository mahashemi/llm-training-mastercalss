# Notebook Index

All notebooks are intended to be exploratory rather than “click run and move on.”

## Core path

| # | Notebook | Resource expectation |
|---|---|---|
| 01 | next_token_prediction_and_a_tiny_language_model | CPU / free Colab |
| 02 | tokenizer_design_and_measurement | CPU |
| 03 | resource_accounting_flops_memory | CPU |
| 04 | build_a_tiny_transformer | CPU / free Colab |
| 05 | attention_and_moe_lab | CPU |
| 06 | gpu_kernel_benchmark | optional GPU |
| 07 | attention_memory_and_tiling | CPU / GPU optional |
| 08 | ddp_and_sharding_simulation | CPU |
| 09 | scaling_law_fit | CPU |
| 10 | inference_and_kv_cache | CPU |
| 11 | training_loop_instrumentation | CPU / GPU optional |
| 12 | evaluation_harness | CPU |
| 13 | dataset_curation_pipeline | CPU |
| 14 | dedup_and_data_mixing | CPU |
| 15 | sft_with_a_small_open_model | GPU recommended |
| 16 | rlvr_toy_experiment | CPU |
| 17 | multimodal_alignment_map | CPU |
| 18 | lora_qlora_comparison | GPU recommended |
| 19 | full_ft_vs_lora | CPU accounting + GPU optional |
| 20 | dpo_and_distillation_concepts | CPU |
| 21 | failure_analysis_and_safety_eval | CPU |
| 22 | build_vs_buy_decision_lab | CPU |
| 23 | national_llm_resource_plan | CPU |
| 24 | capstone_model_program | CPU |

## Important rule

The first six laboratories build the mental model required for the later training labs. Do not skip directly to LoRA because the course is about **knowing why to train**, not only knowing how to invoke a trainer.
