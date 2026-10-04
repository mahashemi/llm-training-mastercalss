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



## Work through one request

Inference has two different phases.

**Prefill:** process the prompt and build the initial KV cache.

**Decode:** generate one new token at a time while reusing cached keys and values.

This distinction explains why long prompts and long generated answers stress different resources.

If a request has prompt length P and generates G tokens, the system experiences one relatively large prompt-processing phase followed by G sequential decoding steps.

## A simple KV-cache calculation

For a decoder model, a simplified cache size scales with:

$$
M_{\text{KV}}\propto
L_{\text{layers}}
\times L_{\text{context}}
\times N_{\text{KV heads}}
\times d_{\text{head}}
\times \text{bytes per value}.
$$

The important engineering insight is the linear dependence on context length.

If context length doubles while everything else remains fixed, the KV cache approximately doubles.

This is why MHA, GQA, and MQA matter for serving economics.

## Latency versus throughput

A user asking for one answer cares about latency. A serving fleet cares about aggregate throughput and utilization.

Useful measurements include:

- time to first token;
- inter-token latency;
- end-to-end latency;
- tokens/sec;
- requests/sec;
- batch size;
- peak memory.

Optimizing one can hurt another. Continuous batching, for example, can improve utilization while changing individual-request latency.

## Real-world decision

Suppose two serving configurations produce the same quality:

| Configuration | TTFT | decode speed | memory | operational question |
|---|---:|---:|---:|---|
| A | lower | lower | lower | interactive workload |
| B | higher | higher | higher | batch workload |

There is no universal winner. The correct choice follows the service-level objective.

## Failure analysis

A slow inference system may be limited by:

- prompt processing;
- decode compute;
- KV-cache memory;
- memory bandwidth;
- batching policy;
- queueing;
- network transfer;
- model loading.

Measure each phase before changing the model.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 13 — Evaluation](../12_evaluation/lecture.md) · [Next: Lecture 15 — SFT and Post-Training →](../15_mid_and_post_training_sft_and_rlhf/lecture.md)

</div>
## Video companions

[Video companions: LLM inference, KV cache and serving](https://www.youtube.com/results?search_query=LLM+inference+KV+cache+serving+lecture)

## Navigation

[← Previous](../09_scaling_laws/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../11_training_system_design/lecture.md)
