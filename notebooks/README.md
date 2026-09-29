# Notebook Laboratory Map

**27 notebooks in the current course build.**

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

| # | Notebook | Resource | Role |
|---|---|---|---|
| 00 | Orientation / Resource Accounting | CPU / optional GPU | hardware and memory mental model |
| 01 | Next-token Prediction and Tiny LM | CPU / free Colab | objective + training loop |
| 02 | Tokenizer Design and Measurement | CPU | tokenization + fertility |
| 03 | Resource Accounting — FLOPs and Memory | CPU | model/training resource math |
| 04 | Build a Tiny Transformer | CPU / free Colab | architecture implementation |
| 05 | Attention Variants and MoE | CPU | MHA/GQA/MQA/MoE |
| 06 | GPU Kernel Benchmark | GPU optional | hardware behavior |
| 07 | Attention Memory and Tiling | CPU / GPU optional | IO/memory-aware attention |
| 08 | DDP and Sharding Simulation | CPU | distributed resource reasoning |
| 09 | Scaling-law Fit | CPU | model/data/compute allocation |
| 10 | Inference and KV Cache | CPU / GPU optional | serving memory/latency |
| 11 | Training Loop Instrumentation | CPU / GPU optional | observability/recovery |
| 12 | Evaluation Harness | CPU | metrics and release gates |
| 13 | Dataset Curation Pipeline | CPU | data transformation |
| 14 | Deduplication and Data Mixing | CPU | corpus intervention |
| 15 | SFT with a Small Open Model | GPU recommended | real open-weight training |
| 16 | RLVR Toy Experiment | CPU | verifier/reward design |
| 17 | Multimodal Alignment Map | CPU | visual-token/resource reasoning |
| 18 | LoRA / QLoRA Comparison | GPU recommended | parameter-efficient training |
| 19 | Full Fine-tuning vs LoRA | CPU accounting / GPU optional | adaptation resource trade-offs |
| 20 | DPO and Distillation Concepts | CPU | preference/teacher-student |
| 21 | Failure Analysis and Safety Evaluation | CPU | failure taxonomy |
| 22 | Build-vs-Buy Decision Lab | CPU | architecture decisions |
| 23 | National LLM Resource Plan | CPU | compute derivation |
| 24 | Capstone Model Program | CPU | evidence-to-program |
| 25 | Tiny GPT Pretraining Campaign | CPU / free Colab | end-to-end pretraining bridge |

## Open-weight training labs

| Lab | Purpose |
|---|---|
| [Open-Weight Model Audit](./open_weight_model_audit.ipynb) | download, inspect, resource-estimate, baseline inference |
| [Qwen3-0.6B SFT](./sft_with_a_small_open_model.ipynb) | real open-weight SFT |
| [LoRA / QLoRA](./lora_qlora_comparison.ipynb) | parameter-efficient training and resource trade-offs |

### Real checkpoint path

[Qwen3-0.6B SFT](./sft_with_a_small_open_model.ipynb) is the first real checkpoint-training lab.

Students must:

**download → inspect → estimate → infer → baseline → smoke test → SFT → evaluate → reload**

### PEFT path

[LoRA / QLoRA](./lora_qlora_comparison.ipynb) turns adapter theory into a measured rank/precision/resource experiment.

### Scale path

Use [Open-Weight Training Ladder](../docs/OPEN_WEIGHT_TRAINING_LADDER.md) to repeat the same methodology on larger checkpoints and H100s.

## Reporting

Use [EXPERIMENT_CARD.md](../templates/EXPERIMENT_CARD.md).

Do not report a model result without its model/data revision, evaluation protocol, and resource measurements.



## Real dataset bench

[Real Dataset Corpus Bench](./real_dataset_corpus_bench.ipynb) is the canonical hands-on dataset lesson. It pulls real slices from multiple Hugging Face datasets and can optionally acquire Kaggle datasets using kagglehub.

Students should run this before calling the curation pipeline “real.” The lab makes the following sources concrete: FineWeb, FineWeb-Edu, Wikipedia, OpenWebMath, Aya, OpenR1-Math-220k, plus Kaggle Tashkeela/RUFND/Gita.
