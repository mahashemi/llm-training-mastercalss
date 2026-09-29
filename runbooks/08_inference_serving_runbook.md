# Inference and Serving Runbook

## Objective

Turn a checkpoint into a reliable serving system.

## Benchmark workload

Specify:
- model revision;
- precision;
- prompt-length distribution;
- output-length distribution;
- concurrency;
- hardware;
- batching policy.

## Measure

- time-to-first-token;
- inter-token latency;
- output tokens/sec;
- request throughput;
- peak memory;
- error rate;
- cost per useful output token.

## Optimization order

1. profile;
2. batching/scheduling;
3. KV-cache strategy;
4. quantization;
5. efficient kernels;
6. caching/prefix reuse;
7. speculative decoding where appropriate;
8. model size reduction/distillation.

## Production checklist

- [ ] load/reload tested
- [ ] readiness/liveness checks
- [ ] request limits
- [ ] authentication/authorization
- [ ] safe logging
- [ ] model/version pinning
- [ ] monitoring
- [ ] rollback path


## Serving benchmark protocol

### Workload definition

Record distributions for:

- prompt tokens;
- output tokens;
- concurrency;
- streaming;
- request arrival rate.

### Benchmark matrix

Run at least:

**concurrency 1 / 4 / 16 / 32**

and several prompt/output length combinations.

### Metrics

Measure:

- TTFT p50/p95/p99;
- inter-token latency p50/p95;
- output tokens/sec;
- peak memory;
- GPU utilization;
- queue time;
- errors/timeouts;
- cost per successful request.

### Capacity

A server is capacity-safe only at a configuration that meets the stated SLO. Higher throughput at unacceptable tail latency does not count as usable capacity.

### Failure tests

Run long-context, burst, restart, memory-pressure, and rolling-update tests before release.
