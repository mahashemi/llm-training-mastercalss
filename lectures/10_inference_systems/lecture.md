# Lecture 10 — Inference Systems: Prefill, Decode, KV Cache, and Serving

**Lab:** [Inference and KV Cache](./lab.ipynb)  
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

Identify: 

- compute-heavy prefill;
- memory/latency-sensitive decode.

## KV memory

A simplified per-token cache estimate is proportional to:

**2 × layers × KV heads × head dimension × bytes**

Then multiply by:

**sequence length × batch/concurrency**

The exact implementation adds runtime effects, but the scaling relationship is the key.

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

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 13 — Evaluation](../12_evaluation/lecture.md) · [Next: Lecture 15 — SFT and Post-Training →](../15_mid_and_post_training_sft_and_rlhf/lecture.md)

</div>