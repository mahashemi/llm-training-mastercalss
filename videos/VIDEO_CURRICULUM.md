# Video Curriculum — LLM Trainer Masterclass

This is a curated companion, not a dump of links. Watch the recommended segment only after attempting the relevant lab when practical.

## Tier 1 — Build the mental model

### 1. Andrej Karpathy — Let's build GPT from scratch
https://www.youtube.com/watch?v=kCc8FmEb1nY

Use for: tokenization, language modeling, bigram baseline, self-attention, Transformer blocks, training, generation.

Teaching use:
- first watch the opening and data sections;
- run our tiny language-model notebook;
- return for attention and the training loop;
- pause when Karpathy makes a system choice and ask why an alternative might be chosen.

### 2. 3Blue1Brown — Attention in transformers, step-by-step
https://www.youtube.com/watch?v=eMlx5fFNoYc

Use for: visual intuition for attention, Q/K/V, masking, multiple heads, cross-attention.

### 3. Stanford CS336 — Language Modeling from Scratch
https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_

Use for: the complete lifecycle. Stanford's current Spring 2026 course covers tokenization, resource accounting, architectures, MoE, GPUs/TPUs, kernels/Triton, parallelism, scaling, inference, evaluation, data, SFT/RLHF, RLVR, and multimodality.

### 4. Sebastian Raschka — Build a Large Language Model From Scratch
https://www.sebastianraschka.com/llms-from-scratch/

Use for: a second implementation path through tokenizer → embeddings → attention → GPT architecture → pretraining → finetuning.

## Tier 2 — Training systems

### 5. Andrej Karpathy — Let's reproduce GPT-2 (124M)
https://www.youtube.com/watch?v=l8pRSuU81PU

Use for: mixed precision, Tensor Cores, torch.compile, FlashAttention, AdamW, schedulers, gradient accumulation, DDP, validation, evaluation, and end-to-end training reproduction.

Suggested checkpoints:
- implementation and forward pass;
- training loop;
- GPU optimization;
- FlashAttention;
- optimizer and schedules;
- DDP;
- evaluation.

### 6. NVIDIA GTC — Megatron-LM
https://developer.nvidia.com/gtc/2020/video/s21496-vid

Use for: why model parallelism exists and how large-model training becomes a distributed-systems problem.

## Tier 3 — Systems reference

### 7. PyTorch distributed/FSDP tutorials
https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html

Use for: practical understanding of parameter/gradient/optimizer sharding.

### 8. NVIDIA Megatron Core documentation and examples
https://docs.nvidia.com/megatron-core/developer-guide/latest/

Use for: production-oriented distributed training, model/data/tensor/pipeline/expert/context parallelism, mixed precision, and data preparation.

### 9. vLLM documentation
https://docs.vllm.ai/en/stable/

Use for: serving, PagedAttention, continuous batching, KV-cache management, quantization, and distributed inference.

## Viewing protocol

For every important video:
1. Watch a segment.
2. Write down one claim.
3. Run our corresponding experiment.
4. Identify one assumption the video did not test.
5. Write one follow-up experiment.

The goal is not video completion. The goal is transfer of engineering judgment.
