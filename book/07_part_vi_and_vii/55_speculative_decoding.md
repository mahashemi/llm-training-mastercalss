# Chapter 55 — Speculative Decoding

**Part:** Part VI

## 1. The basic idea

A smaller draft model proposes several tokens.

A larger target model verifies them.

Instead of making the large model generate every token from scratch, the system may accept several draft tokens in one verification pass.

The potential benefit is lower decode latency when draft tokens have a high acceptance rate.

## 2. What controls speedup

Speedup depends on:

- draft-model latency;
- target-model latency;
- number of proposed tokens;
- acceptance rate;
- verification overhead;
- memory bandwidth;
- workload.

The common mistake is:

“Drafting five tokens means five times speed.”

It does not.

## 3. Simplified intuition

Suppose:

- draft proposes k = 5 tokens;
- average accepted tokens = 4;
- target verification is one forward pass.

If the target would otherwise require four separate decode steps, batching the verification can reduce the number of expensive sequential target passes.

But the draft model itself has cost.

## 4. Workload dependence

| Workload | Expected behavior to test |
|---|---|
| Predictable text | potentially high acceptance |
| Code | may vary by language/model pairing |
| Creative writing | acceptance may be lower |
| Long-context RAG | prefill may dominate, limiting benefit |
| Very short answers | setup overhead may dominate |

Never generalize a speedup from one workload.

## 5. Acceptance-rate experiment

Measure acceptance at:

| Draft tokens k | Acceptance rate | Output tok/s |
|---:|---:|---:|
| 2 | measure | measure |
| 4 | measure | measure |
| 8 | measure | measure |

There may be a point where larger draft windows stop helping.

## 6. Latency decomposition

Compare:

baseline decode  
vs  
draft generation + target verification

Measure:

- TTFT;
- inter-token latency;
- end-to-end latency;
- target-model compute;
- draft-model compute;
- memory.

## 7. Worked example

Suppose baseline output throughput is 20 tok/s.

Speculative decoding gives:

- draft = 8 tok/s equivalent work;
- target verification;
- achieved output = 28 tok/s.

Speedup:

28/20 = 1.4×

The useful comparison is achieved end-to-end throughput, not theoretical accepted tokens.

## 8. When to consider it

Evaluate speculative decoding when:

- decode is the bottleneck;
- the draft model is much cheaper;
- a compatible draft can be run;
- acceptance is high enough;
- latency matters.

It is less useful when prefill or retrieval dominates total latency.

## Research exercise

Compare baseline decoding with speculative decoding using two draft-window sizes.

Report:

- acceptance rate;
- output tok/s;
- TTFT;
- ITL;
- GPU memory;
- cost per million output tokens.

Then identify the workload characteristics that explain the observed speedup.

## Laboratory

[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Reference

https://docs.vllm.ai/en/stable/

## Deepening: speculative decoding depends on acceptance

Speculative decoding uses a faster draft model to propose tokens and a larger model to verify them.

The useful intuition is:

**draft speed × acceptance rate → potential decode acceleration**

### Experiment

Vary draft-model quality or proposal length.

Measure:

- acceptance rate;
- end-to-end tokens/sec;
- latency;
- verifier work.

### Failure mode

A weak draft model proposes many tokens that are rejected, adding overhead without useful acceleration.

### Decision

Benchmark speculative decoding with the actual target workload; do not infer speedup from draft-model latency alone.
