# Notebook Laboratory Map

**28 notebooks in the current course build.**

Every numbered lecture has a companion laboratory. Some textbook chapters reuse a lab because one executable experiment can teach several tightly related concepts.

## The practical spine

**inspect checkpoint → estimate resources → load → baseline → smoke test → train → evaluate → break → report → scale**

The classroom anchor for real open-weight training is **Qwen3-0.6B**, while later labs move the same workflow to larger models and H100 environments.

## Free-first rule

Core labs are designed for CPU or free Colab when practical. A free runtime may vary in GPU type, memory, session lifetime, or availability, so notebooks should detect the environment instead of assuming one accelerator.

## Lab quality standard

Every substantive lab should contain:

1. a prediction before execution;
2. a baseline;
3. one controlled intervention;
4. a quantitative result;
5. a deliberate failure or edge case;
6. a resource measurement;
7. an interpretation;
8. a next experiment.

Completing all cells is not the learning objective.

## Canonical notebooks

The executable labs align with the 24-lecture sequence, plus orientation, real-data, and end-to-end bridges.

1. [Next-token Prediction and Tiny LM](./01_next_token_prediction_and_a_tiny_language_model.ipynb)
2. [Tokenizer Design and Measurement](./tokenizer_design_and_measurement.ipynb)
3. [Resource Accounting — FLOPs and Memory](./resource_accounting_flops_memory.ipynb)
4. [Build a Tiny Transformer](./build_a_tiny_transformer.ipynb)
5. [Attention Variants and MoE](./attention_and_moe_lab.ipynb)
6. [GPU Kernel Benchmark](./gpu_kernel_benchmark.ipynb)
7. [Attention Memory and Tiling](./attention_memory_and_tiling.ipynb)
8. [DDP and Sharding Simulation](./ddp_and_sharding_simulation.ipynb)
9. [Scaling-law Fit](./scaling_law_fit.ipynb)
10. [Inference and KV Cache](./inference_and_kv_cache.ipynb)
11. [Training Loop Instrumentation](./training_loop_instrumentation.ipynb)
12. [Evaluation Harness](./evaluation_harness.ipynb)
13. [Dataset Curation Pipeline](./dataset_curation_pipeline.ipynb)
14. [Deduplication and Data Mixing](./dedup_and_data_mixing.ipynb)
15. [SFT with a Small Open Model](./sft_with_a_small_open_model.ipynb)
16. [RLVR Toy Experiment](./rlvr_toy_experiment.ipynb)
17. [Multimodal Alignment Map](./multimodal_alignment_map.ipynb)
18. [LoRA / QLoRA Comparison](./lora_qlora_comparison.ipynb)
19. [Full Fine-tuning vs LoRA](./full_ft_vs_lora.ipynb)
20. [DPO and Distillation Concepts](./dpo_and_distillation_concepts.ipynb)
21. [Failure Analysis and Safety Evaluation](./failure_analysis_and_safety_eval.ipynb)
22. [Build-vs-Buy Decision Lab](./build_vs_buy_decision_lab.ipynb)
23. [National LLM Resource Plan](./national_llm_resource_plan.ipynb)
24. [Capstone Model Program](./capstone_model_program.ipynb)
25. [Tiny GPT Pretraining Campaign](./tiny_gpt_pretraining_campaign.ipynb)

Additional bridges:
- [Open-Weight Model Audit](./open_weight_model_audit.ipynb)
- [Real Dataset Corpus Bench](./real_dataset_corpus_bench.ipynb)

## Open-weight training labs

- [Open-Weight Model Audit](./open_weight_model_audit.ipynb) — inspect, estimate resources, and establish a baseline.
- [Qwen3-0.6B SFT](./sft_with_a_small_open_model.ipynb) — first real open-weight training workflow.
- [LoRA / QLoRA](./lora_qlora_comparison.ipynb) — parameter-efficient training and resource trade-offs.

The progression is **download → inspect → estimate → infer → baseline → smoke test → train → evaluate → reload**.

For larger checkpoints, use the [Open-Weight Training Ladder](../docs/OPEN_WEIGHT_TRAINING_LADDER.md).

## Reporting

Use [EXPERIMENT_CARD.md](../templates/EXPERIMENT_CARD.md).

Do not report a model result without its model/data revision, evaluation protocol, and resource measurements.



## Real dataset bench

[Real Dataset Corpus Bench](./real_dataset_corpus_bench.ipynb) is the canonical hands-on dataset lesson. It pulls real slices from multiple Hugging Face datasets and can optionally acquire Kaggle datasets using kagglehub.

Students should run this before calling the curation pipeline “real.” The lab makes the following sources concrete: FineWeb, FineWeb-Edu, Wikipedia, OpenWebMath, Aya, OpenR1-Math-220k, plus Kaggle Tashkeela/RUFND/Gita.
