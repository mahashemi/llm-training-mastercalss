# Chapter 71 — National Model Architecture Choices

**Part:** Part VIII

## 1. Architecture is a systems decision

A national or regional model should not choose architecture from benchmark fashion.

Choose jointly across:

**data → language mix → tokenizer → architecture → training system → serving target → budget → governance**

## 2. Dense vs mixture-of-experts

| Dimension | Dense | Mixture of Experts |
|---|---|---|
| Parameters active per token | most of model | subset of experts |
| Total parameter storage | lower for same active capacity | potentially much larger |
| Serving simplicity | simpler | higher routing complexity |
| Compute per token | predictable | routing-dependent |
| Distributed complexity | conventional | expert parallelism and routing |
| Load-balance problem | modest | important |
| Capacity scaling | straightforward | can expand expert capacity |
| Best experiment | baseline | compare at matched compute/quality |

Neither is universally better. The relevant frontier is **quality vs active compute vs total memory vs engineering complexity**.

## 3. Context length is not free

Long context affects:

- prefill compute;
- attention memory;
- KV-cache memory;
- latency;
- retrieval packing;
- throughput.

Therefore “supports 128k” is not a complete requirement.

Measure:

| Test | Metric |
|---|---|
| Quality vs context | task accuracy |
| Latency vs context | p50/p95 |
| Memory vs context | peak memory |
| Long-range use | retrieval/needle-style accuracy |
| Serving cost | cost per successful task |

A model that accepts long context but ignores information in the middle is not equivalent to a model that reliably uses it.

## 4. Tokenizer ownership

For multilingual programs, measure:

- tokens/word;
- tokens/character;
- sequence expansion;
- script coverage;
- normalization behavior;
- code-switching.

A language with high fertility can require substantially more sequence tokens for the same content, increasing training and serving costs.

Tokenizer choice should therefore be treated as part of architecture and economics.

## 5. Open weights vs full openness

Separate:

| Level | What is actually available? |
|---|---|
| API | service access |
| Open weights | checkpoint |
| Partially open | weights + some data/code |
| Fully open research artifact | weights + data details/access + training code + evaluations + recipes |

Ai2's OLMo work is a useful reference for transparent model development artifacts:
https://allenai.org/olmo2

## 6. Architecture selection table

| Requirement | Architecture implication |
|---|---|
| Small local deployment | smaller dense model or distilled student |
| Very large capacity under active-compute limits | evaluate MoE |
| Many low-resource languages | tokenizer + sampling become central |
| Long documents | context + retrieval + memory budget |
| Tight latency | smaller model + efficient kernels + batching |
| Many customer adapters | PEFT/adapters + serving design |
| Local/offline deployment | weight ownership + hardware constraints |
| Frequent model updates | lifecycle/update cost becomes important |

## 7. Worked example

Requirements:

- 10 languages;
- 32k practical context;
- local deployment;
- modest serving hardware;
- high throughput.

Do not begin by selecting dense or MoE.

First estimate:

1. data per language;
2. tokenizer fertility;
3. model capacity;
4. context distribution;
5. expected requests/sec;
6. serving hardware;
7. latency target;
8. governance constraints.

Then run small dense and MoE prototypes if both remain plausible.

## 8. Experimental matrix

| Run | Architecture | Parameters | Context | Data | Main question |
|---|---|---:|---:|---|---|
| A | Dense | small | 8k | same | baseline |
| B | Dense | medium | 8k | same | scaling |
| C | MoE | matched active compute | 8k | same | architecture |
| D | Dense | medium | 32k | same | context |
| E | chosen | medium | 32k | multilingual | target workload |

Hold as many variables constant as possible.

## 9. Architecture economics

Compare:

C_total =
training
+ serving
+ memory hardware
+ networking
+ engineering
+ maintenance

An architecture with lower training cost can still lose if it requires expensive serving hardware or causes difficult reliability problems.

## Research exercise

Write an architecture decision record:

**requirements → candidates → resource model → experiment → quality → latency → serving cost → risks → gate**

Do not select an architecture using parameter count alone.

## Laboratory

[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- OLMo 2: https://allenai.org/olmo2
