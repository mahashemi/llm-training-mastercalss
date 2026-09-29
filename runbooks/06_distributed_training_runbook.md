# Distributed Training Runbook

## Objective

Move from one accelerator to multiple devices without losing correctness or wasting the cluster.

## Step 1 — single-device correctness

Prove:
- forward;
- backward;
- loss;
- checkpoint;
- deterministic sanity checks.

## Step 2 — DDP

Confirm:
- each rank sees the correct shard/batch;
- gradients synchronize;
- effective global batch is correct;
- metrics are reduced correctly.

## Step 3 — memory scaling

If the model state no longer fits, evaluate FSDP2/ZeRO or model-parallel approaches.

## Step 4 — profile

Measure:
- compute time;
- communication time;
- input pipeline time;
- synchronization stalls;
- GPU memory;
- interconnect utilization.

## Step 5 — scale efficiency

Record:
- single-GPU tokens/sec;
- multi-GPU tokens/sec;
- scaling efficiency;
- cost per training token.

## Failure triage

If scaling is poor:
1. verify correctness;
2. check input starvation;
3. check communication;
4. inspect synchronization;
5. inspect kernel efficiency;
6. inspect topology;
7. only then add hardware.


## Distributed launch checklist

### Topology

Record:

- GPU count/type;
- nodes;
- network/interconnect;
- rank topology;
- storage path.

### Correctness before scale

Verify single-GPU equivalence first.

Then validate distributed loss/gradient behavior on a tiny fixed batch.

### Scaling benchmark

Run:

1 GPU → 2 → 4 → 8

Measure:

**tokens/sec, scaling efficiency, communication time, peak memory, input wait**

### Sharding decision

Use sharding when memory is the limiting resource. Use data parallelism when the model and state fit and throughput is the primary objective.

### Failure/recovery test

Kill one worker during a short controlled run. Verify the job can recover from the latest valid checkpoint.

### Acceptance

The distributed system is ready only when:

- scaling is measured;
- communication is understood;
- checkpoint recovery is proven;
- evaluation is unchanged;
- the resource gain justifies the complexity.
