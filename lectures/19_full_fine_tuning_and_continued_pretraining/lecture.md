# Lecture 19 — Full Fine-Tuning and Continued Pretraining

**Lab:** [full_ft_vs_lora.ipynb](./lab.ipynb)
**Primary anchor:** https://cs336.stanford.edu/

## Outcome

Learn to distinguish a narrow behavior update from a broad domain/language distribution shift, then choose between PEFT, full fine-tuning, and continued pretraining using evidence.

## Three different requests

1. “Always return this JSON format.”  
2. “Understand our specialist terminology better.”  
3. “Become substantially better at a low-resource language.”

Consider: whether all three require the same training method.

No.

| Requirement | Candidate |
|---|---|
| stable narrow behavior | SFT/PEFT |
| broad adaptation | full FT may be tested |
| language/domain exposure | continued pretraining |

## Full fine-tuning

Full FT updates most/all parameters.

Training memory includes:

**weights + gradients + optimizer state + activations + runtime**

This can be many times larger than inference-only memory.

## Continued pretraining

Continued pretraining feeds additional unlabeled tokens.

The hypothesis is:

**the model needs more exposure to the target distribution**

not:

**the model needs a different output format.**

For a dense model, a first-order compute heuristic is:

FLOPs ≈ 6ND

Use measured throughput to translate this into wall time.

## Decision matrix

| Question | SFT/PEFT | Full FT | Continued PT |
|---|---|---|---|
| Stable format | strong candidate | possible but heavy | indirect |
| Broad domain behavior | candidate | candidate | strong hypothesis |
| Low-resource language exposure | limited | possible | strong hypothesis |
| Fresh changing knowledge | poor fit | poor fit | poor fit |
| Data type | labeled examples | labeled/domain data | large unlabeled corpus |
| Training memory | low–medium | high | high |
| Main risk | under/overfitting | high cost/forgetting | forgetting + compute |

## Worked example

Suppose:

- base target score = 70;
- SFT = 76;
- continued PT = 81;
- continued PT also lowers general score from 88 to 84.

Now the program has an explicit trade-off.

Test:

**mixed target + general replay**

and evaluate whether target quality can be retained without unacceptable regression.

## Why the order matters

Recommended evidence ladder:

**prompt/RAG/tools → SFT/PEFT → continued PT → full FT/scratch when justified**

This avoids spending expensive compute before identifying the actual bottleneck.

## Break it

Give a small 1B-token specialist corpus.

Ask:

“Should we immediately continued-pretrain a 70B model?”

Answer:

No. First test whether the corpus is large/novel enough and whether a small pilot changes the target metric.

## Exit challenge

Complete:

> “The evidence suggests ___ is a behavior problem / representation problem because ___. Therefore the next experiment is ___.”

### References

Stanford CS336: https://cs336.stanford.edu/  
Chinchilla: https://arxiv.org/abs/2203.15556


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Deepening — separate adaptation breadth from parameter-update breadth

You often mix up:

**what the model is learning**

and

**which parameters are allowed to move**.

Build a 2×2:

| Objective | Full FT | PEFT |
|---|---|---|
| SFT | behavior, broad parameter update | behavior, constrained update |
| continued PT | distribution exposure | possible but capacity-constrained |

### Fair comparison

Fix:

- base checkpoint;
- tokenizer;
- dataset;
- training-token budget;
- evaluation.

Measure:

**target quality + retained capability + memory + throughput + checkpoint size + cost**.

### H100 feasibility drill

Given a 7B model and one H100, you must write the memory budget before choosing full FT.

Then ask:

> Which additional measurement would determine whether sharding is required?



## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 16 — LoRA, QLoRA and PEFT](../18_lora_qlora_and_peft/lecture.md) · [Next: Lecture 18 — Preference Optimization and Distillation →](../20_preference_optimization_and_distillation/lecture.md)

</div>