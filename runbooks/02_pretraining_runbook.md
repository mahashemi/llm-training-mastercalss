# Pretraining Runbook

## Objective

Run a foundation-model pretraining experiment reproducibly and recoverably.

## Preflight

- [ ] tokenizer frozen and evaluated
- [ ] model config frozen
- [ ] data manifest/version frozen
- [ ] train/validation split verified
- [ ] synthetic smoke test passes
- [ ] one-batch forward/backward test passes
- [ ] loss decreases on a tiny overfit test
- [ ] checkpoint save/restore tested
- [ ] monitoring enabled

## Resource accounting

Estimate before allocating a cluster:

C ≈ 6ND

where N = parameters and D = training tokens for a first-order dense-model planning heuristic.

Then convert FLOPs to accelerator-hours using measured effective throughput, not peak specification.

## Run phases

### Phase A — correctness
1–100 steps on tiny data.

### Phase B — short quality run
Enough tokens to detect obvious data/model problems.

### Phase C — scaling experiment
Change one major variable at a time.

### Phase D — production run
Only after the earlier phases are stable.

## Monitor

At minimum:
- training loss;
- validation loss;
- learning rate;
- gradient norm;
- tokens/sec;
- accelerator utilization;
- peak memory;
- dataloader throughput;
- checkpoint duration;
- communication overhead;
- error/restart events.

## Stop conditions

Stop or investigate when:
- loss diverges;
- validation behavior becomes implausible;
- throughput collapses;
- memory grows unexpectedly;
- data pipeline reports corruption;
- checkpoint cannot be restored;
- the run no longer answers the planned research question.

## Post-run

Archive configuration, logs, metrics, checkpoints, data version, code commit, environment, and failure analysis.


## Detailed launch protocol

### Phase 0 — Environment

Capture:

- repository commit;
- model/config revision;
- tokenizer revision;
- framework versions;
- CUDA/runtime version;
- GPU type/count;
- interconnect if distributed.

### Phase 1 — Correctness

Run:

1. one tokenizer batch;
2. one forward pass;
3. one backward pass;
4. one optimizer update;
5. one checkpoint save;
6. one checkpoint restore.

Then overfit a tiny dataset.

### Phase 2 — Throughput

Run a short representative benchmark. Measure:

**tokens/sec, step time, peak memory, input-pipeline time, checkpoint time**

Record both warm and steady-state performance.

### Phase 3 — Stability

Run long enough to inspect:

- loss curve;
- gradient norm;
- LR;
- validation loss;
- NaN/Inf events;
- restart behavior.

### Phase 4 — Scale

Only after Phase 3:

- increase batch;
- increase GPUs;
- increase sequence length;
- increase model size.

Change one major variable at a time.

### Checkpoint rule

Define a recovery objective before launch:

**RPO = maximum acceptable lost training work**

Checkpoint interval must be derived from RPO, checkpoint duration, and failure frequency.

### Post-run

Archive the exact configuration and a machine-readable experiment summary. A checkpoint without its training metadata is an incomplete research artifact.
