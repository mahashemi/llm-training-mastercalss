# Chapter 39 — Checkpointing and Recovery

**Part:** Part III

## 1. A checkpoint is a recovery mechanism

A usable training checkpoint may need:

- model state;
- optimizer state;
- scheduler state;
- gradient-scaler state when applicable;
- current step/token count;
- random state where reproducibility requires it;
- data position/shard state;
- configuration;
- tokenizer/version metadata.

Saving only model weights can be insufficient to resume a long optimization run faithfully.

## 2. Checkpoint cadence is an optimization

Let:

- C_ckpt = cost/overhead of checkpointing;
- C_recompute = expected cost of lost work after failure;
- λ = failure rate.

Longer intervals:

- reduce checkpoint overhead;
- increase expected lost work.

Shorter intervals do the opposite.

The optimal interval depends on failure probability, checkpoint duration, storage bandwidth, and restart requirements.

## 3. Simple expected-loss model

If failures are approximately random and checkpoint interval is Δ:

expected_lost_work is on the order of Δ/2 per failure.

This is a rough model. Real infrastructure failures are not perfectly random.

## 4. Worked example

Suppose:

- training cost = 10k currency units/day;
- checkpoint interval = 6 hours;
- major failure occurs once every 3 days on average.

Expected recompute from one failure is roughly 3 hours:

0.125 day × 10k = 1.25k

If checkpointing every hour adds 2% runtime overhead:

24 hours/day × 2% × 10k = 200/day

The economics may favor more frequent checkpointing.

The actual decision must use measured checkpoint overhead and observed failure behavior.

## 5. Checkpoint integrity test

Never trust a checkpoint until it passes:

1. save;
2. stop process;
3. load checkpoint;
4. resume;
5. compare loss trajectory;
6. verify optimizer/scheduler state;
7. verify data position;
8. compare expected step count.

Automate this test.

## 6. Storage planning

If a checkpoint consumes S GB and K are retained:

storage = S × K

But full optimizer checkpoints can be much larger than model-only checkpoints.

Also account for:

- replicas;
- failed checkpoints;
- upload/download traffic;
- object-store lifecycle policies.

## 7. Recovery-time objective

Define:

RTO = maximum acceptable restore time

and:

RPO = maximum acceptable lost training work

Checkpoint design should satisfy both.

## 8. Large-run example

A 30-day run with RPO of 30 minutes requires much stronger checkpointing than a 4-hour classroom experiment.

This is why production training operations cannot simply “save every few epochs.”

## Research exercise

Build a checkpoint strategy for a 14-day training job.

Specify:

- cadence;
- checkpoint size;
- retention count;
- storage;
- expected lost work;
- RTO;
- recovery test.

Then compare a cheap and a reliable policy.

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Reference

Stanford CS336: https://cs336.stanford.edu/
