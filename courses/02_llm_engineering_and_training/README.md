# Course 2 — LLM Engineering & Training Masterclass

**Purpose:** take a learner from understanding neural networks to being able to build, train, evaluate, optimize, serve, and plan modern language-model systems.

**Recommended prerequisite:** Course 1 — Deep Learning & Neural Computing Foundations.

This course is **not** a collection of Transformer topics. It is a guided engineering progression:

> **text → tokens → objective → Transformer → compute → data → pretraining → adaptation → alignment → evaluation → serving → research → program design**

## What this course teaches

A graduate should be able to:

- build a tiny GPT and explain every major tensor operation;
- train and debug an open-weight model;
- construct and audit language-model datasets;
- understand the compute/memory economics of training;
- choose between prompting, RAG, tools, SFT, PEFT, continued pretraining, preference optimization, distillation, and pretraining;
- design evaluations before changing a model;
- diagnose failures and regressions;
- benchmark inference systems;
- reproduce research and turn observations into experiments;
- create a defensible model/data/compute proposal.

## Chapter standard

A chapter must **teach**, not merely enumerate.

Every chapter should answer:

**What problem are we solving? → How does the mechanism work? → Can I see it on a concrete example? → Can I derive it? → Can I implement it? → What happens on real data? → How does it fail? → What engineering decision follows? → What research question remains?**

The notebook is part of the chapter rather than a detached assignment.

## Course sequence

| # | Chapter | Primary lecture | Learner question |
|---|---|---|---|
| 1 | What is a language model? | [L01](../../lectures/01_what_is_an_llm/lecture.md) | What exactly is being learned? |
| 2 | Tokenization | [L02](../../lectures/02_tokenization/lecture.md) | How does text become computational units? |
| 3 | PyTorch + resource accounting | [L03](../../lectures/03_pytorch_and_resource_accounting/lecture.md) | How do tensors, autograd, memory, FLOPs, and hardware meet? |
| 4 | Transformer architecture + tiny GPT | [L04](../../lectures/04_transformer_architectures/lecture.md) | How does a decoder-only model turn context into next-token probabilities? |
| 5 | Attention alternatives + MoE | [L05](../../lectures/05_attention_alternatives_and_moe/lecture.md) | What changes when we redesign or sparsify computation? |
| 6 | Data sources + construction | [L13](../../lectures/13_data_sources_and_dataset_construction/lecture.md) | Where does training data come from and how do we make it usable? |
| 7 | Filtering + deduplication + mixing | [L14](../../lectures/14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) | What makes a training mixture useful? |
| 8 | Pretraining systems | [L11](../../lectures/11_training_system_design/lecture.md) | How do we turn a training loop into a reliable experiment? |
| 9 | Scaling laws | [L09](../../lectures/09_scaling_laws/lecture.md) | How do model size, data, and compute interact? |
| 10 | GPUs + kernels | [L06](../../lectures/06_gpus_and_kernels/lecture.md) | Why does the same model run at very different speeds? |
| 11 | Efficient attention + Triton | [L07](../../lectures/07_efficient_attention_and_triton/lecture.md) | How do implementation details change memory and latency? |
| 12 | Distributed training | [L08](../../lectures/08_distributed_training/lecture.md) | How do we train beyond one GPU? |
| 13 | Evaluation | [L12](../../lectures/12_evaluation/lecture.md) | How do we know a model improved? |
| 14 | Inference systems | [L10](../../lectures/10_inference_systems/lecture.md) | What determines serving cost and latency? |
| 15 | SFT + post-training | [L15](../../lectures/15_mid_and_post_training_sft_and_rlhf/lecture.md) | How do we turn a base model into a useful assistant? |
| 16 | LoRA + QLoRA + PEFT | [L18](../../lectures/18_lora_qlora_and_peft/lecture.md) | How can we adapt models cheaply? |
| 17 | Continued pretraining + full fine-tuning | [L19](../../lectures/19_full_fine_tuning_and_continued_pretraining/lecture.md) | When should we change knowledge or update all weights? |
| 18 | Preference optimization + distillation | [L20](../../lectures/20_preference_optimization_and_distillation/lecture.md) | How do we shape behavior and transfer capability? |
| 19 | RL with verifiable rewards | [L16](../../lectures/16_reinforcement_learning_with_verifiable_rewards/lecture.md) | When can correctness become a training signal? |
| 20 | Multimodality | [L17](../../lectures/17_multimodality/lecture.md) | How do language models connect to other modalities? |
| 21 | Safety + robustness + failure analysis | [L21](../../lectures/21_safety_robustness_and_failure_analysis/lecture.md) | Where does the model fail and how do we release responsibly? |
| 22 | API vs RAG vs tools vs training | [L22](../../lectures/22_api_vs_rag_vs_tools_vs_training/lecture.md) | What is the right intervention for a real product problem? |
| 23 | Building an LLM program | [L23](../../lectures/23_build_an_llm_program/lecture.md) | How do experiments become an engineering program? |
| 24 | From experiment to fundable model | [L24](../../lectures/24_from_experiment_to_fundable_model/lecture.md) | How do evidence, resources, people, risk, and milestones become a plan? |

## Production-grade learning loop

Every major chapter follows:

**Understand → Implement → Run → Measure → Break → Diagnose → Decide → Reproduce**

The research track then adds:

**Intervene → Ablate → Generalize → Communicate → Release**

## Two levels of examples

Each concept should be taught through both:

- a **small transparent example** where every tensor/calculation can be inspected;
- a **real open-weight or real-data example** where engineering constraints become visible.

That is how the learner moves from “I know the definition” to “I can use this in a production system.”

← Course 1 — Deep Learning & Neural Computing Foundations


## What “deep” means here

A chapter is incomplete if it only says what a technique is.

For example, “attention lets tokens attend to other tokens” is an introduction, not a lesson. The chapter must continue until the learner can take a concrete sequence, construct $Q$, $K$, and $V$, calculate attention scores, apply the causal mask, explain the resulting weighted sum, implement it, and observe what changes when a component is removed.

Likewise, “deduplication improves data” is not sufficient. The learner must measure duplicates, construct controlled mixtures, keep the token budget comparable, train/evaluate the variants, and determine whether the observed difference is attributable to deduplication.

The course therefore treats **examples, derivations, implementation, experiments, and engineering consequences as part of the lecture itself**.
