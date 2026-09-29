# Course Map — LLM Trainer Masterclass

## North-star outcome

Progress from Deep Learning fundamentals to independent open-weight model training and, eventually, professional/H100-scale training-system design.

The learner should be able to:

> download and audit a real checkpoint, estimate resources, train/adapt it reproducibly, evaluate it, diagnose failures, and decide whether to scale.

## 24 lecture sequence

| # | Lecture | Main lab |
|---|---|---|
| 01 | What Is an LLM? | Tiny language model |
| 02 | Tokenization | Tokenizer measurement |
| 03 | PyTorch and Resource Accounting | FLOPs + memory |
| 04 | Transformer Architectures | Tiny Transformer |
| 05 | Attention Alternatives and MoE | Attention/MoE |
| 06 | GPUs and Kernels | GPU benchmark |
| 07 | Efficient Attention and Triton | Attention tiling |
| 08 | Distributed Training | DDP/FSDP simulation |
| 09 | Scaling Laws | Scaling-law fit |
| 10 | Inference Systems | KV cache |
| 11 | Training System Design | Instrumentation |
| 12 | Evaluation | Evaluation harness |
| 13 | Data Sources and Dataset Construction | Curation |
| 14 | Filtering, Deduplication, Mixing, Synthetic Data | Data interventions |
| 15 | SFT + RLHF | Qwen3-0.6B SFT |
| 16 | RLVR | Verifier experiment |
| 17 | Multimodality | Alignment/resource map |
| 18 | LoRA + QLoRA | PEFT comparison |
| 19 | Full FT + Continued PT | FT vs LoRA |
| 20 | Preference + Distillation | DPO/distillation |
| 21 | Safety + Failure Analysis | Failure analysis |
| 22 | API/RAG/Tools/Training | Build-vs-buy |
| 23 | Build an LLM Program | Resource plan |
| 24 | From Experiment to Fundable Model | Capstone |

## Open-weight hardware spine

**tiny GPT → Qwen3-0.6B/free Colab → 1.7B/4B single GPU → 7B/8B H100 → Qwen3.8-27B case study → multi-GPU H100 → foundation-model planning**

The workflow remains:

**inspect → estimate → load → baseline → smoke test → train → evaluate → break → report → scale**

See:

- [Open-Weight Training Ladder](docs/OPEN_WEIGHT_TRAINING_LADDER.md)
- [Qwen3.8-27B + H100 Case Study](docs/OPEN_WEIGHT_QWEN_H100_CASE_STUDY.md)
- [Book ↔ Lecture ↔ Laboratory Map](BOOK_LAB_MAP.md)

## Mastery gates

1. Understand — explain the method.
2. Implement — build the smallest useful version.
3. Measure — establish baseline and quantitative result.
4. Break — violate an assumption and diagnose the failure.
5. Decide — choose under constraints.
6. Reproduce — another person can rerun it.
7. Research — formulate a falsifiable question.
8. Program — convert evidence into a staged resource plan.

## Anti-shallow standard

A lesson is not complete because it defines a technique.

The minimum depth standard is:

**definition → mechanism → numerical example → implementation → resource consequence → controlled experiment → failure mode → evaluation → decision → scale bridge**

## Free-first progression

CPU → free Colab → single-GPU experiments → H100 → multi-GPU → cluster proposal.

Paid compute enters only after a learner demonstrates why the next experiment is worth scaling.
