# Lecture 10 — Inference Systems: Prefill, Decode, KV Cache, and Serving

**Lab:** [Inference and KV Cache](`./lab.ipynb`)  
**Primary anchor:** vLLM — https://docs.vllm.ai/en/stable/

## Outcome

You can separate prefill from decode, calculate why KV cache grows, and benchmark latency versus throughput.

## Why inference is not training

Training sees the target sequence and can parallelize positions.

Generation creates one new token at a time.

Ask:

> What repeated computation can be avoided between generated tokens?

KV cache.

## Prefill versus decode

**Prefill:** process the prompt and construct cache.

**Decode:** generate one or a few new tokens repeatedly using cached K/V.

Students identify:

- compute-heavy prefill;
- memory/latency-sensitive decode.

## KV memory

A simplified per-token cache estimate is proportional to:

**2 × layers × KV heads × head dimension × bytes**

Then multiply by:

**sequence length × batch/concurrency**

The exact implementation adds runtime effects, but the scaling relationship is the key.

## Laboratory

Vary:

- prompt length;
- batch/concurrency;
- output length.

Measure:

| Condition | TTFT | ITL | peak memory | output tok/s |
|---|---:|---:|---:|---:|
| short | measure | measure | measure | measure |
| medium | measure | measure | measure | measure |
| long | measure | measure | measure | measure |

## Break it

Increase concurrency until memory or latency becomes unacceptable.

Identify whether the failure is:

**capacity → queueing → KV memory → scheduler**

## Engineering decision

An inference profile must state:

**model + precision + context distribution + output distribution + concurrency + SLO**

A single tokens/sec number is not a capacity plan.

## Exit challenge

Why can throughput rise while user-perceived latency gets worse?

## Research bridge

Compare a small-model local benchmark with a serving runtime such as vLLM and explain which system optimizations target memory, scheduling, or batching.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
