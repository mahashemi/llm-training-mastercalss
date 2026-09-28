# Chapter 68 — Compute Procurement and Cluster Design

**Part:** Part VIII

## 1. Buy delivered training, not theoretical FLOPs

The useful quantity is **measured tokens/sec or effective FLOPs/sec for the actual model, sequence length, precision, kernels, and topology**.

Two accelerators with similar peak specifications can deliver very different training throughput because memory capacity, memory bandwidth, communication, software, and utilization differ.

## 2. Procurement matrix

| Dimension | Question | Why it matters |
|---|---|---|
| Accelerator memory | Does the model fit with desired batch/sequence length? | avoids forced micro-batching |
| Memory bandwidth | Can layers consume data fast enough? | affects utilization |
| GPU-GPU interconnect | How fast are collectives? | distributed scaling |
| Node-node network | Can gradients/data move efficiently? | network bottleneck |
| Storage throughput | Can the loader feed GPUs? | prevents idle accelerators |
| Checkpoint bandwidth | Can saves finish within recovery budget? | reliability |
| Availability | Can capacity be obtained when needed? | schedule |
| Software | Are framework/kernels supported? | engineering cost |
| Price | What is blended delivered accelerator-hour? | TCO |

## 3. Cluster sizing

For a dense-language-model first-order planning estimate:

F_total ≈ 6ND

Suppose:

- target compute = 4.2e21 FLOPs;
- one GPU delivers 50 TFLOP/s effective.

One GPU time:

4.2e21 / 5e13 = 8.4e7 seconds ≈ 972 days

Suppose a 64-GPU system delivers 70% scaling efficiency:

effective throughput =
64 × 50e12 × 0.70
= 2.24e15 FLOP/s

Time:

4.2e21 / 2.24e15 ≈ 1.88e6 seconds ≈ 21.8 days

The scaling penalty is visible.

## 4. Strong-scaling experiment

Benchmark:

1 → 2 → 4 → 8 → 16 → 32 → 64 GPUs

Record:

- tokens/sec;
- effective FLOPs/sec;
- scaling efficiency;
- communication time;
- memory utilization;
- failure/restart behavior.

A larger cluster is useful only when the additional throughput justifies the additional cost.

## 5. Storage planning

Budget for:

- raw data;
- processed shards;
- tokenizer;
- checkpoints;
- optimizer state where applicable;
- evaluations;
- logs;
- multiple model versions.

If one checkpoint is S GB and K checkpoints are retained:

checkpoint_storage ≈ S × K

Then add failed experiments and replicas.

## 6. Data-pipeline capacity

Profile:

- read throughput;
- CPU preprocessing;
- decompression;
- tokenization;
- host-to-device transfer;
- cache hit rate.

A run with poor GPU utilization may have a data-system bottleneck rather than an accelerator bottleneck.

## 7. Reliability economics

Suppose a 20-day run has a significant probability of interruption before checkpoint.

Checkpoint cadence should be tied to acceptable restart loss:

checkpoint_interval ≤ acceptable_restart_loss

Measure the actual checkpoint overhead and recovery time.

## 8. Procurement options

| Option | Strength | Risk |
|---|---|---|
| On-demand cloud | flexible | higher unit price |
| Reserved capacity | predictable | unused capacity |
| Preemptible | lower unit price | interruption |
| Dedicated cluster | control | capital + operations |
| Hybrid | flexibility | complexity |

## 9. Worked procurement example

Suppose a 32-GPU cluster is measured at 1.2e15 effective FLOP/s.

For 4.2e21 FLOPs:

time ≈ 4.2e21 / 1.2e15 ≈ 40.5 days

If the blended cost for the entire cluster is 160 currency units/hour:

compute ≈ 40.5 × 24 × 160 ≈ 155.5k currency units

This is an illustrative planning example, not a market quote. Add:

- data processing;
- storage;
- evaluation;
- retries;
- staffing;
- networking;
- monitoring.

## 10. The procurement gate

Before committing to large capacity:

**model fit → measured throughput → scale efficiency → storage → checkpoint/recovery → availability → software → security → TCO**

Run the exact training workload on a small slice of the intended infrastructure first.

## Research exercise

Benchmark one configuration at 1, 2, 4, and 8 GPUs.

Create:

**tokens/sec → scaling efficiency → wall time → accelerator cost → cost per billion tokens**

Then explain why the chosen cluster size follows from measured evidence.

## Laboratory

[resource_accounting_flops_memory.ipynb](../../notebooks/resource_accounting_flops_memory.ipynb)

## Reference

https://docs.nvidia.com/megatron-core/developer-guide/latest/
