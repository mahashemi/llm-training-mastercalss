# Chapter 12 — GQA and MQA

**Part:** Part I

## 1. The serving bottleneck

Multi-head attention (MHA) uses one K and V head for each query head.

Grouped-query attention (GQA) uses fewer K/V heads than query heads.

Multi-query attention (MQA) uses a single K/V head.

The main engineering motivation is **KV-cache and memory-bandwidth reduction during decode**.

## 2. Shape comparison

Let:

- H_q = query heads;
- H_kv = KV heads.

| Design | H_q | H_kv | Cache size |
|---|---:|---:|---|
| MHA | 32 | 32 | 1× reference |
| GQA | 32 | 8 | 0.25× |
| GQA | 32 | 4 | 0.125× |
| MQA | 32 | 1 | 0.03125× |

For fixed sequence length and head dimension, KV memory scales linearly with H_kv.

## 3. Why this matters at serving scale

If one request uses 1 GB of KV cache under MHA, an idealized 32→8 GQA configuration requires about 0.25 GB for the same cached tokens.

For 100 simultaneous sequences:

| Design | Illustrative KV memory |
|---|---:|
| MHA | 100 GB |
| GQA-8 | 25 GB |
| MQA | 3.125 GB |

Actual runtime memory includes other allocations.

## 4. What changes mathematically?

Queries remain separate:

Q ∈ R^(B×T×H_q×d_head)

Keys/values use:

K,V ∈ R^(B×T×H_kv×d_head)

Query groups attend to shared K/V heads.

This reduces storage and memory traffic but also reduces independent K/V representations.

## 5. Quality/resource trade-off

| Configuration | KV memory | Potential representational flexibility | Serving benefit |
|---|---:|---|---|
| MHA | highest | highest | baseline |
| GQA-8 | low | lower | high |
| GQA-4 | very low | lower | very high |
| MQA | lowest | lowest | highest cache reduction |

Do not assume a cache reduction is free. Evaluate task quality and latency.

## 6. Worked workload

Suppose production has:

- average context = 8k;
- 128 concurrent sequences;
- decode is memory-bandwidth limited.

A GQA architecture may allow substantially more active sequences before memory saturation.

Measure:

- peak KV memory;
- output tokens/sec;
- p95 latency;
- quality.

The correct comparison is **system throughput under the same quality target**.

## 7. Conversion caveat

Some training recipes convert MHA checkpoints to GQA-like forms.

This can reduce serving cost but may alter quality because multiple original K/V heads are merged or otherwise transformed.

Evaluate the converted model separately; do not assume architectural conversion preserves performance exactly.

## Research exercise

Implement/cache-calculate MHA, GQA-8, and MQA.

For fixed:

B=8, T=4096, L=32, d_head=128, BF16,

calculate KV memory.

Then discuss how much additional concurrency each design might permit under a fixed KV budget.

## Laboratory

[attention_and_moe_lab.ipynb](../../notebooks/attention_and_moe_lab.ipynb)

## References

- Multi-query attention: https://arxiv.org/abs/1911.02150
- GQA: https://arxiv.org/abs/2305.13245

## Deepening: GQA is a cache-design decision

During decoding, each generated token needs access to past keys and values.

Let H_q be query heads and H_kv be KV heads.

Approximate cache size scales with:

**2 × layers × H_kv × head_dim × sequence_length × bytes**

### Worked comparison

Hold layers, head dimension, context, and dtype fixed.

Compare:

- MHA: H_kv = H_q;
- GQA: H_kv = H_q/4;
- MQA: H_kv = 1.

Compute relative KV storage.

### Experiment

Measure generation memory as context grows.

### Failure mode

A benchmark that explicitly repeats K/V tensors can hide the expected cache advantage.

The implementation must match the architectural hypothesis.
