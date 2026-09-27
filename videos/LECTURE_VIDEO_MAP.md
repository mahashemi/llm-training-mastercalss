# Lecture-to-Video Map

External videos are enrichment. The repository's notebooks and explanations remain the canonical teaching path.

| Lecture | Primary companion | Use |
|---|---|---|
| 01 | Karpathy — Let's build GPT | implementation intuition |
| 02 | Stanford CS336 — tokenization lecture(s) | tokenization at systems scale |
| 03 | Stanford CS336 — resource accounting | FLOPs/memory |
| 04 | Karpathy + 3Blue1Brown | architecture + intuition |
| 05 | Stanford CS336 — MoE/attention material | attention variants |
| 06 | Stanford CS336 — GPUs/kernels | hardware |
| 07 | Stanford CS336 — FlashAttention/Triton | memory-aware kernels |
| 08 | Stanford CS336 — distributed training | parallelism |
| 09 | Stanford CS336 — scaling laws | scaling |
| 10 | Stanford CS336 — inference | serving |
| 11 | Karpathy — Let's reproduce GPT-2 | training systems |
| 12 | Stanford CS336 — evaluation | evaluation design |
| 13 | Stanford CS336 — data | corpus construction |
| 14 | Stanford CS336 — data filtering/dedup | data quality |
| 15 | Raschka + HF TRL material | SFT |
| 16 | Stanford CS336 — RL/RLVR | verifiable rewards |
| 17 | Stanford CS336 — multimodality | multimodal training |
| 18 | HF PEFT/TRL material | LoRA/QLoRA |
| 19 | Stanford/HF training material | full FT / continued pretraining |
| 20 | HF TRL DPO material | preference optimization |
| 21 | evaluation/safety sessions | failure analysis |
| 22 | project material | build-vs-buy reasoning |
| 23 | OLMo / BLOOM / multilingual talks | program design |
| 24 | OLMo / open-model talks + proposal work | evidence-to-funding |

## High-value anchors

### Karpathy — Let's build GPT
https://www.youtube.com/watch?v=kCc8FmEb1nY

Use for the first implementation journey.

### Karpathy — Let's reproduce GPT-2
https://www.youtube.com/watch?v=l8pRSuU81PU

Use for systems scaling after the tiny model work.

### 3Blue1Brown — Attention in transformers
https://www.youtube.com/watch?v=eMlx5fFNoYc

Use for visual intuition before the formal attention derivation.

### Stanford CS336
https://cs336.stanford.edu/

Use as the academic lecture backbone. The current course spans the full modern lifecycle.

### Sebastian Raschka
https://www.sebastianraschka.com/llms-from-scratch/

Use as a second implementation path and reference text.

## Viewing protocol

For each assigned video:

**watch → stop → predict → run our lab → compare → identify an untested assumption → write a follow-up experiment**
