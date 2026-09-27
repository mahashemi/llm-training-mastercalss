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
