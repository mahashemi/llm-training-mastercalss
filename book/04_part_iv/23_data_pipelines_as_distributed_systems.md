# Chapter 23 — Data Pipelines as Distributed Systems

**Part:** Part III

## 1. Training data is a production pipeline

A large corpus is not a folder of files.

A serious pipeline is:

**discover → acquire → parse → normalize → filter → deduplicate → classify → tokenize → shard → publish**

Each stage can fail or change the distribution.

## 2. Pipeline design matrix

| Stage | Main resource | Failure | Measurement |
|---|---|---|---|
| Ingestion | network/storage | missing data | completeness |
| Parsing | CPU/RAM | broken structure | parse success |
| Filtering | CPU/GPU | false removal | retention by source |
| Dedup | CPU/RAM | excessive deletion | duplicate rate |
| Tokenization | CPU/GPU | throughput bottleneck | tokens/sec |
| Sharding | storage/network | skew | shard balance |
| Loading | storage/CPU | GPU starvation | loader wait time |

## 3. Backpressure

If stage A produces 10 GB/s but stage B consumes 4 GB/s, buffering grows until a resource limit is reached.

A pipeline should therefore enforce bounded queues and backpressure.

Measure:

**queue depth → stage latency → throughput**

## 4. Deterministic sharding

A document should map to a stable shard using a reproducible rule.

Benefits:

- repeatable experiments;
- easier debugging;
- balanced workers;
- controlled resume.

Record the sharding version.

## 5. Data lineage

For every training shard preserve:

source IDs → transformations → filtering version → dedup version → shard ID

This makes it possible to trace a surprising model behavior back to its inputs.

## 6. Throughput calculation

Suppose:

- parsing = 200 documents/s;
- filtering = 500 documents/s;
- dedup = 150 documents/s;
- tokenization = 1,000 documents/s.

The pipeline throughput is approximately bounded by the slowest stage:

≈150 documents/s

Optimizing tokenization does little until deduplication is improved.

## 7. Failure recovery

A robust pipeline should support:

- retryable stages;
- idempotent transformations;
- checkpoints;
- checksums;
- partial reruns;
- quarantined failed inputs.

Do not force the entire corpus to restart because 0.1% of documents failed.

## 8. Research exercise

Build a five-stage synthetic data pipeline.

Instrument:

- throughput;
- latency;
- queue depth;
- failure rate;
- CPU/memory usage.

Introduce one slow stage and observe backpressure.

Then improve the bottleneck and quantify end-to-end throughput gain.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Reference

https://cs336.stanford.edu/
