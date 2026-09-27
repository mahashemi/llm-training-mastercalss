# Notebook Laboratory Map

Every numbered lecture has a corresponding lab. The repository also contains an orientation notebook (`00`) that can be used before Lecture 01.

## Free-first rule

The core learning path is designed to run on CPU or free Colab whenever practical. GPU-recommended labs retain an analytical or reduced-size path so concepts remain accessible without paid compute.

## Canonical notebooks

| # | Notebook | Resource | Role |
|---|---|---|---|
| 00 | [Orientation / Resource Accounting](./00_orientation_resource_accounting.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/00_orientation_resource_accounting.ipynb) | CPU / optional GPU | Orientation |
| 01 | [Next-token Prediction and Tiny Language Model](./01_next_token_prediction_and_a_tiny_language_model.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb) | CPU / free Colab | First required lab |
| 02 | [Tokenizer Design and Measurement](./tokenizer_design_and_measurement.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/tokenizer_design_and_measurement.ipynb) | CPU | Required |
| 03 | [Resource Accounting — FLOPs and Memory](./resource_accounting_flops_memory.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/resource_accounting_flops_memory.ipynb) | CPU | Required |
| 04 | [Build a Tiny Transformer](./build_a_tiny_transformer.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/build_a_tiny_transformer.ipynb) | CPU / free Colab | Required |
| 05 | [Attention Variants and MoE](./attention_and_moe_lab.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/attention_and_moe_lab.ipynb) | CPU | Required |
| 06 | [GPU Kernel Benchmark](./gpu_kernel_benchmark.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/gpu_kernel_benchmark.ipynb) | GPU optional | Required |
| 07 | [Attention Memory and Tiling](./attention_memory_and_tiling.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/attention_memory_and_tiling.ipynb) | CPU / GPU optional | Required |
| 08 | [DDP and Sharding Simulation](./ddp_and_sharding_simulation.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/ddp_and_sharding_simulation.ipynb) | CPU | Required |
| 09 | [Scaling-law Fit](./scaling_law_fit.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/scaling_law_fit.ipynb) | CPU | Required |
| 10 | [Inference and KV Cache](./inference_and_kv_cache.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/inference_and_kv_cache.ipynb) | CPU | Required |
| 11 | [Training Loop Instrumentation](./training_loop_instrumentation.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/training_loop_instrumentation.ipynb) | CPU / GPU optional | Required |
| 12 | [Evaluation Harness](./evaluation_harness.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/evaluation_harness.ipynb) | CPU | Required |
| 13 | [Dataset Curation Pipeline](./dataset_curation_pipeline.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/dataset_curation_pipeline.ipynb) | CPU | Required |
| 14 | [Deduplication and Data Mixing](./dedup_and_data_mixing.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/dedup_and_data_mixing.ipynb) | CPU | Required |
| 15 | [SFT with a Small Open Model](./sft_with_a_small_open_model.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/sft_with_a_small_open_model.ipynb) | GPU recommended | Primary post-training lab |
| 16 | [RLVR Toy Experiment](./rlvr_toy_experiment.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/rlvr_toy_experiment.ipynb) | CPU | Required |
| 17 | [Multimodal Alignment Map](./multimodal_alignment_map.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/multimodal_alignment_map.ipynb) | CPU | Required |
| 18 | [LoRA / QLoRA Comparison](./lora_qlora_comparison.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/lora_qlora_comparison.ipynb) | GPU recommended | Primary PEFT lab |
| 19 | [Full Fine-tuning vs LoRA](./full_ft_vs_lora.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/full_ft_vs_lora.ipynb) | CPU accounting / GPU optional | Required |
| 20 | [DPO and Distillation Concepts](./dpo_and_distillation_concepts.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/dpo_and_distillation_concepts.ipynb) | CPU | Required |
| 21 | [Failure Analysis and Safety Evaluation](./failure_analysis_and_safety_eval.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/failure_analysis_and_safety_eval.ipynb) | CPU | Required |
| 22 | [Build-vs-Buy Decision Lab](./build_vs_buy_decision_lab.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/build_vs_buy_decision_lab.ipynb) | CPU | Required |
| 23 | [National LLM Resource Plan](./national_llm_resource_plan.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/national_llm_resource_plan.ipynb) | CPU | Required |
| 24 | [Capstone Model Program](./capstone_model_program.ipynb) / [Open in Colab](https://colab.research.google.com/github/mahashemi/llm-training-mastercalss/blob/main/notebooks/capstone_model_program.ipynb) | CPU | Required |

## Lab protocol

1. Read the lecture prediction questions.
2. State your prediction before running code.
3. Execute the smallest experiment.
4. Record baseline measurements.
5. Change one major variable.
6. Inspect the result and at least one failure case.
7. Complete an experiment card.
8. State the next experiment that would reduce uncertainty.

## Research use

For experiments used in papers or engineering reports, preserve the notebook Git commit, dataset/model versions, environment, hardware, and results. See REPRODUCIBILITY.md and templates/paper_report.md.
