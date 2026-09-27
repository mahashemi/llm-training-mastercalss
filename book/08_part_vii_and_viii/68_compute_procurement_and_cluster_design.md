# Chapter 68 — Compute Procurement and Cluster Design

**Part:** Part VIII

## Core concepts
1. **Accelerator choice** — Memory, bandwidth, interconnect, software ecosystem, availability.
2. **Node topology** — GPU-GPU and node-node bandwidth can dominate distributed performance.
3. **Storage** — Training requires high-throughput input and checkpoint storage.
4. **Reliability** — Capacity should include failure, maintenance, and recovery.

## Formal view
Cluster throughput is bounded by the weakest critical resource. Peak GPU FLOPs alone do not predict delivered training tokens/sec.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[resource_accounting_flops_memory.ipynb](../../notebooks/resource_accounting_flops_memory.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://docs.nvidia.com/megatron-core/developer-guide/latest/
