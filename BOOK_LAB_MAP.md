# Book ↔ Lecture ↔ Laboratory Map

**Curriculum control plane:** [Learning Graph](docs/LEARNING_GRAPH.md) · [Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)

The textbook and lecture layers are intentionally many-to-one with laboratories. A chapter may reuse a laboratory when one executable experiment can teach several related concepts.

## Primary laboratory families

| Laboratory | Primary concepts | Used by chapters / lectures |
|---|---|---|
| Open-Weight Model Audit | checkpoint identification, config/tokenizer, memory, baseline inference | Open-Weight chapter; H100 case study; open-weight runbook |
| Notebook 01 — next-token prediction | probability model, logits, loss, autoregressive training | Ch. 1, 3, 9; Lecture 1 |
| Tokenizer measurement | BPE, fertility, multilingual tokenization | Ch. 2, 24; Lecture 2 |
| Resource accounting | parameter memory, FLOPs, hardware sizing | Ch. 11, 40, 68; Lecture 3 |
| Tiny Transformer | embeddings, RoPE, normalization, MLP, Transformer composition | Ch. 4–7, 11; Lecture 4 |
| Attention / MoE | MHA, MQA, GQA, MoE routing | Ch. 8, 12–13; Lecture 5 |
| GPU kernel benchmark | GPU hierarchy, arithmetic intensity, throughput | Lecture 6 |
| Attention memory / tiling | attention memory traffic, FlashAttention, tiling | Lecture 7 |
| DDP / sharding simulation | distributed data flow, sharding, communication | Lecture 8 |
| Scaling-law fit | parameter/token allocation and extrapolation | Ch. 40 + scaling material; Lecture 9 |
| Inference / KV cache | prefill, decode, KV cache, batching, latency | Ch. 51–56; Lecture 10 |
| Training instrumentation | optimizer state, checkpointing, accumulation, observability | Ch. 10, 14–16, 25, 39; Lecture 11 |
| Evaluation harness | benchmark design, statistics, release gates | Ch. 22, 41–47, 50, 73; Lecture 12 |
| Dataset curation | sources, filtering, provenance, quality | Ch. 17–18, 21, 23, 66, 72; Lecture 13; [Real Dataset Bench](notebooks/real_dataset_corpus_bench.ipynb); [Persian Track](data/PERSIAN_DATASET_TRACK.md) |
| Dedup + data mixing | deduplication, mixture weights, sampling | Ch. 19–20; Lecture 14 |\n| Persian longitudinal case | target-language tokenizer, corpus quality, synthetic-vs-real data, continued PT, SFT/PEFT, evaluation | Ch. 2, 17–24, 26–33, 41–50, 62–65; Lectures 2, 12–15, 18–19, 23 | [Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md) using existing labs |
| Qwen3-0.6B SFT | real open-weight model loading, SFT, evaluation | Ch. 27, 33, 62; Lecture 15 |
| RLVR toy | reward verification, reward hacking | Lecture 16 |
| Multimodal alignment | modality encoders, token budgets, alignment | Lecture 17 |
| LoRA / QLoRA | PEFT, rank, quantized adaptation | Ch. 29–31, 38; Lecture 18 |
| Full FT vs LoRA | broad adaptation, forgetting, resource trade-offs | Ch. 28, 32, 63; Lecture 19 |
| DPO + distillation | preferences, DPO mechanics, teacher/student | Ch. 34–37; Lecture 20 |
| Failure analysis | safety, robustness, groundedness, error taxonomy | Ch. 43, 45, 48–49; Lecture 21 |
| Build-vs-buy | API/RAG/tools/training decision making | Ch. 57–61; Lecture 22 |
| Program/resource plan | scaling, teams, procurement, program economics | Ch. 64–75; Lectures 23–24 |
| Tiny GPT pretraining campaign | end-to-end pretraining | project bridge + capstone |

## How to read the map

A chapter can have a primary lab and still ask analytical exercises.

When a chapter says:

> Before opening the notebook…

it must either link a real notebook in that section or state explicitly that the exercise is paper-and-pencil and no notebook is required.

## Lab contract

Every primary lab should contain:

**predict → run → measure → break → explain → save artifact → propose next experiment**

The notebook README contains the executable path. The chapter explains why the experiment matters. The lecture provides instructor framing. The runbook provides operational procedure.

This separation prevents duplicate prose while keeping the learning path connected.
