# Open LLM Engineering Stack

This is the current practical stack studied by the masterclass. Tool versions and APIs change; use the linked official docs for current syntax.

| Layer | Representative tools | What students learn |
|---|---|---|
| Core tensor framework | PyTorch | tensors, autograd, distributed primitives |
| Data | Hugging Face Datasets + custom streaming | dataset transformation, sharding, provenance |
| Tokenizers | Hugging Face Tokenizers / custom tokenizer code | vocabulary construction, BPE, multilingual measurement |
| Model implementations | Transformers / custom PyTorch | model configs, loading, generation |
| PEFT | Hugging Face PEFT | LoRA, QLoRA, adapters |
| Post-training | Hugging Face TRL | SFT, DPO, RL-style training workflows |
| Distributed training | PyTorch FSDP2 / TorchTitan | sharding, multi-dimensional parallelism |
| Large-scale training | Megatron Core | tensor/pipeline/data/expert/context parallelism |
| Kernel optimization | PyTorch compile, Triton, FlashAttention | profiling and memory-aware kernels |
| Inference | vLLM | PagedAttention, batching, KV cache, speculative decoding |
| Experiment tracking | simple versioned artifacts first; optional external tracker later | reproducibility before dashboards |
| Packaging | Git + GitHub + release/DOI | research traceability |

## Teaching order

Do not begin with a high-level framework.

The learner should first understand:
**PyTorch → tiny model → training loop → profiling → distributed concepts → framework abstraction**.

Only then introduce framework-specific convenience layers.

## Official references

PyTorch:
https://pytorch.org/

TorchTitan:
https://github.com/pytorch/torchtitan

Megatron Core:
https://docs.nvidia.com/megatron-core/developer-guide/latest/

Transformers:
https://huggingface.co/docs/transformers/

PEFT:
https://huggingface.co/docs/peft/

TRL:
https://huggingface.co/docs/trl/

vLLM:
https://docs.vllm.ai/en/stable/
