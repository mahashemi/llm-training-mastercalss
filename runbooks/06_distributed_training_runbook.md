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
