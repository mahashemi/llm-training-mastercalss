# Open LLM Engineering Stack

This is a learning stack, not a claim that one framework is mandatory. APIs and versions change; pin the versions used by each experiment and consult the current official documentation.

| Layer | Representative tools | What students learn |
|---|---|---|
| Tensor/autograd | PyTorch | tensors, autograd, memory, distributed primitives |
| Data | Hugging Face Datasets + custom pipelines | streaming, transforms, provenance |
| Tokenizers | Hugging Face Tokenizers / custom code | vocabulary, BPE, fertility |
| Models | Transformers / custom PyTorch | configs, checkpoint loading, generation |
| PEFT | Hugging Face PEFT | LoRA, QLoRA, adapters |
| Post-training | Hugging Face TRL | SFT, DPO, GRPO/RL workflows |
| Distributed | PyTorch FSDP2 / TorchTitan | sharding and parallel training |
| Large-scale | Megatron Core | tensor/pipeline/data/expert/context parallelism |
| Kernels | PyTorch compile, Triton, FlashAttention | profiling and IO-aware kernels |
| Inference | vLLM | batching, KV cache, serving |
| Tracking | Git + structured experiment cards | reproducibility before dashboards |
| Packaging | Git/GitHub + releases/DOI | traceable research artifacts |

## Teaching order

Do not begin with the highest-level framework.

**PyTorch → tiny model → real open-weight checkpoint → training loop → profiling → PEFT → distributed abstractions → large-scale frameworks**

This order prevents students from learning APIs without understanding the computation underneath.

## Open-weight workflow

The practical stack should support:

**Hugging Face model repo → exact revision → tokenizer → Transformers load → baseline inference → TRL/PEFT training → evaluation → model/adapter card → release**

## Hardware ladder

CPU and free Colab are the default teaching environments. H100 is introduced after resource accounting, not before.

## Version policy

Every runnable experiment should record:

- Python;
- PyTorch;
- Transformers;
- PEFT;
- TRL;
- CUDA/runtime;
- GPU;
- model revision;
- dataset revision.

Never rely on an unpinned “latest” environment for a reproducibility claim.

## Official references

PyTorch: https://pytorch.org/  
Transformers: https://huggingface.co/docs/transformers/  
PEFT: https://huggingface.co/docs/peft/  
TRL: https://huggingface.co/docs/trl/  
TorchTitan: https://github.com/pytorch/torchtitan  
Megatron Core: https://docs.nvidia.com/megatron-core/developer-guide/latest/  
vLLM: https://docs.vllm.ai/en/stable/
