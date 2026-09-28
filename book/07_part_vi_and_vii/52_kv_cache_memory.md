# Chapter 52 — KV Cache Memory

**Part:** Part VI

## 1. Why KV cache exists

During autoregressive generation, the model repeatedly needs keys and values from previous tokens.

Caching them avoids recomputing the previous sequence at every decode step.

For a simplified decoder-only model:

KV bytes ≈ 2 × B × T × L × H_kv × d_head × bytes_per_element

where:

- B = batch size;
- T = cached sequence length;
- L = number of layers;
- H_kv = number of key/value heads;
- d_head = head dimension.

The factor 2 is for K and V.

## 2. Worked example

Suppose:

- B = 1;
- T = 8,192;
- L = 32;
- H_kv = 8;
- d_head = 128;
- BF16 = 2 bytes.

Then:

KV bytes ≈ 2 × 1 × 8192 × 32 × 8 × 128 × 2
≈ 1.07 GB

The exact implementation has additional details, but the scaling relationship is the important insight.

## 3. Why GQA/MQA matter

| Attention design | KV heads | Cache implication |
|---|---:|---|
| MHA | equal to query heads | largest cache |
| GQA | fewer KV heads | reduced cache |
| MQA | one KV head | much smaller cache |

This is one reason modern architectures use grouped or multi-query attention.

## 4. Cache scaling

Cache grows approximately linearly with:

- batch;
- context length;
- number of layers;
- KV heads;
- head dimension;
- bytes/element.

This creates a direct trade-off between context length and serving capacity.

## 5. Capacity calculation

Suppose a GPU has 80 GB usable for a serving workload.

After reserving 20 GB for weights and 10 GB for runtime/activations:

KV budget ≈ 50 GB

If each active request needs 1 GB of KV cache at its current context:

maximum concurrent cached sequences ≈ 50

This is a simplified planning estimate. Actual schedulers and fragmentation reduce available capacity.

## 6. Quantization and KV cache

Weight quantization does not automatically imply equally aggressive KV-cache quantization.

Evaluate separately:

- weight precision;
- KV precision;
- activation precision.

Measure quality, memory, and latency together.

## 7. Context-length impact

If context doubles, KV memory approximately doubles.

Example:

| Context | Relative KV memory |
|---:|---:|
| 4k | 1× |
| 8k | 2× |
| 16k | 4× |
| 32k | 8× |

This is why long-context serving can exhaust memory even when model weights fit comfortably.

## 8. Prefix and cache reuse

If many requests share the same prefix, reusing cached computation can reduce repeated work.

Examples:

- system prompt;
- long policy header;
- common retrieved document.

Measure the cache hit rate and its effect on TTFT.

## 9. Failure modes

Common problems:

- KV cache exhausted;
- excessive eviction;
- fragmentation;
- long requests starving short requests;
- batch size reduced by memory pressure.

These are serving-system problems, not simply model-quality problems.

## Research exercise

For a hypothetical 7B decoder with:

- 32 layers;
- 8 KV heads;
- 128-dimensional heads;
- BF16 KV,

calculate KV memory for 4k, 8k, 16k, and 32k context at batch sizes 1, 8, and 32.

Then estimate the largest concurrency that fits within a 40 GB KV budget.

## Laboratory

[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Reference

https://docs.vllm.ai/en/stable/
