# Open-Weight Training Ladder

## Purpose

This is the practical spine of the LLM Trainer Masterclass.

The student should not merely be able to explain LoRA, QLoRA, SFT, pretraining, or distributed training. By the end, a student should be able to:

1. identify an open-weight model;
2. download the exact checkpoint and tokenizer;
3. inspect architecture and parameter count;
4. estimate weight and training memory before loading it;
5. run inference;
6. build a reproducible dataset;
7. run a smoke-test training job;
8. fine-tune with full FT, LoRA, or QLoRA when hardware permits;
9. evaluate before/after behavior and regressions;
10. save and reload the resulting artifact;
11. move the same experiment from free Colab to an H100;
12. understand which parts change at larger scale.

The central teaching rule is:

> **Same experiment, different scale.**

The repeated lifecycle is:

**checkpoint → tokenizer → dataset → baseline → training → evaluation → checkpoint → failure analysis → decision**

## 1. Hardware ladder

| Tier | Teaching hardware | Primary model class | Main skills | What students actually do |
|---|---|---|---|---|
| 0 | CPU | tiny GPT | tensors, loss, optimizer | implement training loop |
| 1 | Free Colab GPU | Qwen3-0.6B | open-weight workflow | download, infer, SFT, LoRA |
| 2 | Single GPU | Qwen3-1.7B/4B | resource scaling | compare precision, length, rank |
| 3 | 1× H100 80GB | 7B–8B | serious experiments | BF16 inference, QLoRA/LoRA, profiling |
| 4 | 1× H100 80GB | ~27B | large-model adaptation | quantized inference/adaptation, memory accounting |
| 5 | multi-GPU H100 | 7B–30B+ | distributed training | FSDP/ZeRO/tensor/pipeline parallelism |
| 6 | H100 cluster | foundation-model scale | pretraining systems | data pipeline, scaling, recovery |

Model size alone does not determine whether training fits. Sequence length, batch size, optimizer state, activation checkpointing, quantization, implementation, and distributed strategy all matter.

## 2. Why Qwen3-0.6B is the classroom anchor

The official Qwen3-0.6B checkpoint is about 1.52 GB in its repository and has 0.6B parameters; the Base checkpoint is about 1.2 GB. Both expose architecture and Transformers loading information. The course should use these real checkpoints rather than relying only on toy models.

| Checkpoint | Teaching purpose |
|---|---|
| Qwen/Qwen3-0.6B | inference and instruction/post-training workflow |
| Qwen/Qwen3-0.6B-Base | pretrained-model adaptation and continued-training concepts |

Do not blur **base pretraining** and **instruction tuning**. They are different training stages.

## 3. The first real student workflow

### Step 1 — Identify the artifact

Record:

- model repository;
- exact revision/commit;
- license;
- architecture;
- parameter count;
- context length;
- tokenizer;
- dtype;
- base vs instruct/post-trained vs multimodal vs MoE.

A model name alone is not a reproducibility record.

### Step 2 — Estimate memory

For N parameters:

weight memory ≈ N × bytes per parameter

BF16 is approximately 2 bytes/parameter. Four-bit storage is approximately 0.5 bytes/parameter before metadata and packing overhead.

Then add:

- activations;
- gradients;
- optimizer state;
- temporary buffers;
- KV cache for inference;
- framework/runtime overhead.

### Step 3 — Load before training

Prove:

- GPU is visible;
- CUDA/runtime is recorded;
- model loads;
- tokenizer loads;
- one prompt generates output;
- memory is measured.

### Step 4 — Establish a baseline

Save:

- exact prompts;
- decoding configuration;
- outputs;
- task metrics;
- latency;
- peak memory.

A fine-tune without a baseline is not a useful experiment.

### Step 5 — Overfit a tiny subset

Use 8–32 examples and a few steps. Verify:

- loss decreases;
- output changes;
- checkpoint saves;
- checkpoint reload works.

This is a debugging experiment, not a quality result.

### Step 6 — Run the controlled experiment

Change one major variable at a time:

- learning rate;
- adapter rank;
- target modules;
- sequence length;
- data quantity;
- precision.

Do not change five variables and call the result an ablation.

## 4. The Colab curriculum

### Lab A — Download and inspect

Students should configure a model ID, load AutoConfig and AutoTokenizer, print architecture metadata, and count parameters.

The exercise is to explain every field that affects memory or computation.

### Lab B — Inference

Use Transformers and the model's chat template. Measure:

- load time;
- peak memory;
- prompt tokens;
- generated tokens;
- generation latency;
- tokens/sec.

### Lab C — SFT

Use a tiny inspectable dataset.

Students must understand:

**SFT objective ≠ LoRA.**

SFT defines the learning signal. Full FT, LoRA, and QLoRA define how parameters are updated.

### Lab D — LoRA

Students calculate:

P_LoRA = r × (d_in + d_out)

and compare it with:

P_full = d_in × d_out.

Then run a rank experiment.

### Lab E — QLoRA

Compare:

- BF16 + LoRA;
- 4-bit + LoRA.

Measure:

- peak memory;
- tokens/sec;
- wall time;
- quality;
- regression.

### Lab F — Dataset scaling

Run the same setup on 100, 500, and 2k examples. Plot quality against data and examine marginal gain.

## 5. Moving from Colab to H100

The code should remain conceptually stable.

| Layer | Colab | H100 |
|---|---|---|
| GPU | opportunistic free accelerator | dedicated high-memory accelerator |
| Model | 0.6B | 7B–30B+ |
| Precision | BF16/4-bit depending on memory | BF16/FP8/quantized experiments |
| Batch | small | larger |
| Context | short first | controlled long-context studies |
| Profiling | basic | PyTorch/Nsight/system metrics |
| Training | adapter-focused | adapter + full FT + distributed studies |
| Failure budget | minutes | expensive GPU-hours |

The methodology should stay stable even when the hardware changes.

## 6. Qwen3.8-27B as the large-model case study

The current Qwen3.8-27B repository contains about 55.6 GB of model artifacts and describes a 27B-parameter post-trained model compatible with Transformers, vLLM, SGLang and other runtimes.

A 27B model in BF16 needs approximately:

27B × 2 bytes ≈ 54 GB

for raw weights alone.

Therefore an 80 GB H100 can make weight loading/inference plausible, subject to runtime, context length, and KV-cache requirements.

It does **not** mean full fine-tuning fits on one 80 GB H100.

Full training additionally needs:

- gradients;
- optimizer state;
- activations;
- temporary buffers;
- runtime/framework memory.

The curriculum therefore separates:

**27B inference on one H100**

from

**27B parameter-efficient adaptation**

from

**27B full fine-tuning**

from

**27B pretraining**.

These are four different resource problems.

## 7. H100 progression

### H100 Lab 1 — Load a large open model

Measure:

- model load time;
- weight memory;
- context-length impact;
- generation throughput;
- peak memory.

### H100 Lab 2 — QLoRA

Keep the base frozen, quantize it, train adapters, and measure memory and rank effects.

### H100 Lab 3 — BF16 LoRA

Repeat without base quantization.

Question:

> How much quality or throughput is gained for the extra memory?

### H100 Lab 4 — Full FT feasibility

Do not launch blindly.

Calculate:

- weights;
- gradients;
- optimizer;
- activations;
- expected peak memory.

Then decide whether one H100, multiple H100s, sharding, checkpointing, or a smaller model is required.

### H100 Lab 5 — Distributed scaling

Measure:

scaling efficiency = throughput(k) / [k × throughput(1)]

Identify where communication becomes the bottleneck.

## 8. Pretraining is the final escalation

The course must not teach:

> “We have an H100, therefore we should train a foundation model.”

Instead:

1. reproduce tiny GPT;
2. train a small open-weight model;
3. adapt an existing model;
4. measure data quality;
5. establish scaling behavior;
6. estimate compute;
7. test distributed training;
8. design a from-scratch run only after evidence.

For dense-model planning, a common first-order estimate is:

FLOPs ≈ 6ND

where N is parameter count and D is training tokens.

This is a planning approximation, not a substitute for profiling.

## 9. Required experiment card

| Field | Required |
|---|---|
| Model ID | yes |
| Model revision | yes |
| License | yes |
| Dataset revision | yes |
| Tokenizer | yes |
| Training objective | yes |
| Update method | yes |
| Precision | yes |
| Sequence length | yes |
| Batch size | yes |
| Gradient accumulation | yes |
| Learning rate | yes |
| Scheduler | yes |
| Trainable parameters | yes |
| Peak GPU memory | yes |
| Tokens/sec | yes |
| Wall time | yes |
| Checkpoint size | yes |
| Evaluation | yes |
| Regression evaluation | yes |
| Failure analysis | yes |
| Next experiment | yes |

This is the bridge from classroom notebooks to research-grade training.

## 10. Final student capability

A graduate should be able to receive:

> “Here is an open-weight 27B model and one H100. Adapt it to this domain.”

and produce:

1. model audit;
2. memory estimate;
3. data specification;
4. baseline evaluation;
5. smallest feasible training method;
6. smoke test;
7. controlled experiment;
8. resource measurement;
9. quality/regression report;
10. next-scale plan.

That is the practical meaning of LLM training.
