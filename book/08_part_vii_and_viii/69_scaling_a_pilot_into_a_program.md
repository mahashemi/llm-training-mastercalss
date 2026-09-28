# Chapter 69 — Scaling a Pilot Into a Program

**Part:** Part VIII

## 1. Scale uncertainty down before scaling compute up

A pilot should answer the questions that could otherwise make a large run wasteful:

- Does the data improve the target metric?
- Does the tokenizer represent the target language efficiently?
- Does the architecture train stably?
- Does the evaluation measure the actual goal?
- Can the cluster deliver the required throughput?
- Is the projected quality gain large enough to matter?

Only after these are answered should the program scale.

## 2. Stage-gate model

| Stage | Spend | Main question | Exit evidence |
|---|---|---|---|
| 0 — Baseline | tiny | Is the existing model sufficient? | reproducible gap |
| 1 — Cheap intervention | low | Can prompt/RAG/tools/SFT close it? | controlled result |
| 2 — Training pilot | low–medium | Is the training signal real? | loss + target metric |
| 3 — Scale test | medium | Does scaling behave as expected? | throughput + scaling curve |
| 4 — Product pilot | medium | Does the system work for users? | task/SLO evidence |
| 5 — Full program | high | Is larger investment justified? | budget + evidence + risk |

## 3. Gate design

Every gate needs:

**objective → metric → threshold → evidence artifact → resource released → next decision**

Example:

Gate 2 objective: improve target-language benchmark.

Metric: native QA score.

Threshold: at least +5 points with retained capability inside the agreed regression limit.

Evidence: checkpointed experiment + evaluation report.

Resource released: larger token budget only after the gate passes.

The numerical threshold is illustrative. Each project must set its own based on user value and measurement noise.

## 4. Scaling-law thinking

For model size N and tokens D, use multiple smaller experiments rather than assuming the largest run will work.

An empirical fit can look like:

loss(N,D) ≈ A N^-alpha + B D^-beta + E

The exact functional form is an assumption. The important practice is to estimate trends from measured runs and report uncertainty.

Stanford CS336 includes scaling work, systems optimization, and implementation-heavy language-model training:
https://cs336.stanford.edu/

## 5. Evidence chain for scale-up

A credible scale-up case is:

**baseline → controlled intervention → ablation → scaling trend → product metric → TCO → risk**

Each link answers a different question.

## 6. Worked example

Suppose:

| Model | Target benchmark gain | Relative compute |
|---:|---:|---:|
| 1B | +6% | 1× |
| 3B | +9% | 4× |
| 7B | +10% | 12× |

The last step gives a smaller incremental gain.

Questions to ask:

- Is the next scale step expected to deliver enough value?
- Would better data produce a larger gain per unit compute?
- Would post-training close the remaining gap?
- Does serving cost rule out the larger model?

A scale decision should answer those questions with evidence.

## 7. Spend by milestone

Attach resources to evidence.

| Milestone | Example release condition |
|---|---|
| Dataset v1 | rights + quality card |
| Training pilot | stable training curve |
| Scaling test | throughput + scaling efficiency |
| Product pilot | task success + p95 SLO |
| Larger program | integrated technical/economic case |

This is better than approving a large hardware request at project start.

## 8. Kill and pivot conditions

Predeclare conditions that cause a pause or change:

- target metric fails to improve;
- cost per improvement exceeds the program ceiling;
- training instability persists;
- regression exceeds limit;
- data rights remain unresolved;
- production SLO cannot be met.

A failed gate should identify whether the next action is **stop, fix, reduce scope, gather evidence, or pivot architecture**.

## 9. Research exercise

Design a five-stage scale plan for a model program.

For every stage write:

**uncertainty → experiment → metric → threshold → spend → stop/pivot condition**

Then estimate how much budget remains if each stage fails.

## Laboratory

[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## Reference

https://cs336.stanford.edu/
