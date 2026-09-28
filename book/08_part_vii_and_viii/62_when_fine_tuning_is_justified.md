# Chapter 62 — When Fine-Tuning Is Justified

**Part:** Part VII  
**Focus:** Decide whether a behavior gap warrants changing model weights, and if so, choose the least expensive adaptation that can test the hypothesis.

## 1. Fine-tuning solves a particular class of problem

Fine-tuning is justified when the desired improvement is a **stable, learnable behavior** and the baseline model is consistently failing despite a strong inference-time baseline.

Typical examples:

- reliable output structure;
- narrow classification;
- domain-specific response style;
- consistent tool-use patterns;
- stable instruction-following behavior.

Fine-tuning is usually a poor mechanism for frequently changing facts. Those belong in retrieval or live tools.

The decision is not “Can we fine-tune?” It is:

**Does changing parameters address the measured bottleneck enough to justify training, evaluation, maintenance, and regression cost?**

## 2. Establish the baseline first

Before training, freeze:

- model version;
- tokenizer;
- prompt;
- decoding settings;
- system instructions;
- retrieval/tools if present;
- evaluation set;
- quality metric;
- latency and cost measurements.

A useful baseline table is:

| Baseline | Quality | p95 latency | Cost/task | Schema validity | Main failure |
|---|---:|---:|---:|---:|---|
| Prompt only | measure | measure | measure | measure | inconsistency |
| Structured output | measure | measure | measure | measure | residual errors |
| SFT/LoRA | measure | measure | measure | measure | overfit/regression |

Do not compare a fine-tuned model against a weak prompt baseline and call the improvement causal.

## 3. Full fine-tuning vs PEFT

| Method | Trainable parameters | Training memory | Operational complexity | Best experiment |
|---|---|---|---|---|
| Full fine-tuning | most/all | highest | highest | broad adaptation |
| LoRA | small adapters | lower | low–medium | default efficient pilot |
| QLoRA | adapters + quantized base | lower still | medium | constrained GPU |
| Prompting | none | none | very low | required baseline |

LoRA freezes the base weights and learns low-rank updates. The original paper reported large reductions in trainable parameters and memory compared with full fine-tuning in its studied settings: https://arxiv.org/abs/2106.09685

QLoRA combines low-rank adaptation with a quantized frozen base to reduce training memory. The QLoRA paper demonstrated training a 65B model on a single 48GB GPU under its experimental setup: https://arxiv.org/abs/2305.14314

These paper results are evidence for the method, not a guarantee for a particular model, GPU, sequence length, or software stack.

## 4. Data quantity is not the decision by itself

There is no universal number of examples that makes fine-tuning “work.”

A practical experimental progression is:

| Dataset size | Use |
|---:|---|
| 100–1k high-quality examples | feasibility / format behavior |
| 1k–10k | first serious SFT baseline |
| 10k–100k+ | broader variation / failure coverage |
| 100k+ | only when the marginal examples add useful diversity |

These are planning ranges, not laws.

Quality, coverage, correctness, and diversity matter more than raw count.

## 5. Data design

Each training example should answer:

- what input distribution is expected?
- what is the desired output?
- what should the model refuse?
- which edge cases matter?
- which cases are ambiguous?
- what behavior should remain unchanged?

A dataset containing 20,000 nearly identical examples can be less useful than 3,000 diverse examples covering real failure modes.

## 6. Fine-tuning decision test

Fine-tune only when all are approximately true:

1. the failure is stable across many representative examples;
2. the desired behavior can be expressed as training examples;
3. the strongest prompt/structured-output baseline has been measured;
4. relevant knowledge is already available or separately grounded;
5. regression tests exist;
6. the improvement has economic or product value.

If one of these is false, training may be premature.

## 7. Worked example — strict JSON

Requirement:

95% schema-valid output is needed; baseline is 82%.

Run:

**Stage A:** stronger prompt  
**Stage B:** structured-output enforcement  
**Stage C:** 2k high-quality SFT examples  
**Stage D:** LoRA rank/data sweep

Metrics:

- schema validity;
- semantic correctness;
- omission rate;
- unsupported field rate;
- latency;
- cost;
- regression on unrelated prompts.

A successful fine-tuning campaign should improve the target metric **without creating a larger regression elsewhere**.

## 8. Cost model

For a training campaign:

C_FT =
GPU compute
+ data engineering
+ evaluation
+ engineering time
+ retries
+ checkpoint/storage
+ model release/monitoring

Expected annual cost:

C_annual =
updates_per_year × C_FT
+ inference
+ ongoing evaluation
+ operations

This is why update cadence matters.

Stable behavior that changes twice a year has a very different economics from behavior that changes weekly.

## 9. Latency considerations

Fine-tuning can affect latency indirectly:

- a smaller adapted model may be sufficient;
- a merged adapter may avoid a separate adapter request path;
- sequence length may change because prompts can become shorter;
- however, model size still dominates much of serving cost.

Therefore measure:

**quality at target workload + p95 latency + cost per successful task**

not just benchmark score.

## 10. Regression and forgetting

Evaluate both:

**target capability:** did the new behavior improve?

**retained capability:** what unrelated behavior changed?

At minimum maintain:

- target set;
- general set;
- safety set;
- adversarial set;
- production-like slice.

A fine-tuned model that gains 8 points on one metric and loses critical capability elsewhere is not a complete success.

## 11. When full fine-tuning may be warranted

Full fine-tuning deserves a separate experiment when:

- a broad fraction of the model behavior must change;
- many layers appear relevant to the target capability;
- PEFT capacity is demonstrably insufficient;
- the team can afford the memory and operational cost;
- the resulting model must be self-contained.

The evidence should be comparative:

**full FT vs LoRA/QLoRA under the same data and evaluation protocol.**

## 12. When not to fine-tune

Do not use fine-tuning as the first fix for:

- changing policies;
- current inventory;
- live user records;
- real-time schedules;
- database state;
- one-off factual additions.

Use retrieval or tools for those problems.

## Research exercise

Take a real task and run:

prompt-only → structured output → LoRA → full FT

Hold the evaluation set fixed.

Report:

- quality;
- trainable parameters;
- GPU-hours;
- peak memory;
- p50/p95 latency;
- cost per successful task;
- retained capability.

Then write the smallest evidence-based statement that justifies the next step.

## Laboratory

[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## References

- LoRA: https://arxiv.org/abs/2106.09685
- QLoRA: https://arxiv.org/abs/2305.14314
