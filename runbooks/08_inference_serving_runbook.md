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
