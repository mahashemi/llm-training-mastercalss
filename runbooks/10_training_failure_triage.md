# Training Failure Triage

## First rule

Do not immediately change the learning rate. Classify the failure first.

## 1. Loss is NaN or Inf

Check:
1. invalid or corrupt data;
2. numerical stability;
3. precision/dtype path;
4. exploding gradients;
5. learning rate;
6. optimizer state;
7. custom kernel correctness.

### Minimum diagnostic
Run one batch in full precision and compare forward/backward behavior.

## 2. Loss does not decrease

Check:
- target shifting;
- labels and masking;
- trainable parameters;
- optimizer parameter list;
- non-zero gradients;
- data variation;
- learning rate;
- initialization.

### Sanity test
Overfit a tiny fixed batch. A model that cannot overfit a tiny batch is not ready for a long run.

## 3. Training loss decreases, validation stalls

Check:
- overfitting;
- leakage;
- evaluation bugs;
- domain mismatch;
- repetition;
- data mixture.

## 4. GPU utilization is low

Profile before adding GPUs.

Potential causes:
- small kernels;
- input starvation;
- CPU preprocessing;
- synchronization;
- memory bandwidth;
- communication;
- inefficient attention;
- padding/packing waste.

## 5. Multi-GPU scaling is poor

Measure compute, communication, synchronization, input pipeline, interconnect, and per-rank memory. Separate data-parallel problems from model-parallel communication.

## 6. SFT looks good on training examples but fails in use

Check:
- evaluation leakage;
- template mismatch;
- insufficient diversity;
- overfitting;
- hidden formatting assumptions.

## 7. Fine-tuning improves target behavior but destroys general behavior

Check:
- adaptation strength;
- data mixture;
- learning rate;
- epochs/steps;
- retained-capability evaluation.

## 8. Serving is too expensive

Profile prefill, decode, KV cache, batching, precision, model size, and request distribution. Then test quantization, scheduling, smaller models, distillation, caching, and speculative decoding as appropriate.

## Incident record

For every material failure record:
- timestamp;
- run/checkpoint;
- exact symptom;
- first observed step;
- hypothesis;
- diagnostic;
- intervention;
- result;
- root cause;
- prevention.


## Triage decision tree

### 1. Did the job start?

If no:

**environment → dependency → CUDA/device → checkpoint/tokenizer**

### 2. Is the loss finite?

If no:

**precision → LR → data → optimizer → initialization**

### 3. Does training loss decrease?

If no:

**label/template → data → gradient flow → objective → learning rate**

### 4. Does validation improve?

If training improves but validation does not:

**overfitting → contamination → distribution mismatch → evaluation error**

### 5. Is throughput lower than expected?

Check:

**data loader → kernel utilization → memory bandwidth → communication → checkpoint/evaluation overhead**

### 6. Is memory unexpectedly high?

Check:

**sequence length → batch → activations → optimizer → KV cache → temporary buffers → fragmentation**

### Incident record

Record:

**symptom → first observation → hypothesis → test → result → root cause → fix → regression test**

Never repair an expensive run without preserving the evidence that explains the failure.
