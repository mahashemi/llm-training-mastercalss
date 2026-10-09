# Lecture 15 — Mid and Post Training: SFT, RLHF, and the Post-Training Stack

**Lab:** [sft_with_a_small_open_model.ipynb](./lab.ipynb)
**Primary anchor:** https://arxiv.org/abs/2203.02155

## Learning outcome

By the end, the learner can distinguish:

**continued pretraining → SFT → preference optimization/RLHF**

and decide which stage addresses a measured failure.

## Why “train the model more” is ambiguous

Start with three failures:

1. The model does not know a specialist domain.
2. The model knows the domain but ignores the required response format.
3. The model follows the format but prefers unsafe or unhelpful responses.

Consider: whether one training method should solve all three.

Reveal:

| Failure | Likely intervention |
|---|---|
| Broad domain/language exposure | continued pretraining |
| Stable behavior | SFT / PEFT |
| Preference trade-offs | DPO / RLHF-style methods |

## The post-training stack

Draw:

**base model**  
↓  
**continued pretraining (optional)**  
↓  
**SFT**  
↓  
**preference optimization**  
↓  
**evaluation + safety**  
↓  
**serving**

Explain that stages are composable, not mandatory.

## SFT in concrete terms

SFT learns from:

**input → desired response**

### What receives the loss?

The stored example and the supervised tokens are not the same thing. A conversational record contains user/system context and one or more assistant messages, but a common assistant-tuning setup computes next-token loss on the assistant target while masking context tokens from the loss.

For example, the user question is needed as context so the model can answer it; it usually is not the answer we want the assistant to imitate. If the loss is accidentally applied to the entire serialized conversation, the model is also trained to reproduce user text and system instructions. That can be intentional for some language-modeling objectives, but it is not the default goal of assistant-response SFT.

The lab therefore uses a structured `messages` record and `assistant_only_loss=True` with Qwen3's supported chat-template handling. Always inspect the trainer/template behavior for your model family: a JSON field called `messages` does not by itself guarantee the right loss mask.

For prompt-completion data, the equivalent distinction is whether loss is computed on the completion only or on the full sequence. See the [TRL SFTTrainer documentation](https://huggingface.co/docs/trl/main/sft_trainer).


Show a bad dataset:

- repetitive prompts;
- low-quality answers;
- only easy cases;
- no refusal/uncertainty examples.

Then a good coverage matrix:

| Dimension | Examples |
|---|---|
| intent | factual / advisory / procedural |
| difficulty | easy / medium / hard |
| language | L1 / L2 / L3 |
| output | prose / JSON / table |
| safety | ordinary / edge / refusal |

Explain:

**dataset composition = gradient pressure on behavior.**

## Preference optimization vs RLHF

| Property | SFT | DPO-style preference optimization | Classic RLHF |
|---|---|---|---|
| Data | targets | chosen/rejected | preferences + rollouts |
| Reward model | no | no | yes |
| Online loop | no | usually no | yes |
| Complexity | low | medium | high |
| Main risk | imitation errors | preference bias | reward hacking/stability |

Key lesson:

A more complex training loop is justified only when it solves a problem the simpler loop cannot.

## Worked example

Target: “safe, concise, grounded medical responses.”

Baseline:

- correctness = 84%;
- schema validity = 96%;
- unnecessary refusal = 12%.

SFT improves:

- correctness = 88%;
- schema validity = 98%;
- refusal = 12%.

Preference optimization then tests whether the preference data can reduce verbosity/refusal without harming correctness.

Measure:

| Metric | Before | After |
|---|---:|---:|
| Correctness | 84 | measure |
| Groundedness | 82 | measure |
| Refusal rate | 12 | measure |
| Mean output tokens | 240 | measure |
| Safety failures | measure | measure |

## Break it

Give a preference dataset where chosen responses are always longer.

Predict:

- verbosity increases;
- serving cost increases;
- human helpfulness may not improve.

Then inspect the preference data.

## Engineering judgment

The learner must answer:

**When is another training stage justified?**

Require:

- stable failure;
- measurable target metric;
- representative data;
- protected evaluation;
- known resource cost;
- acceptable regression.

## Exit challenge

Complete:

> “We should use ___ rather than ___ because the dominant failure is ___, and the cheapest experiment is ___.”

### Research bridge

- InstructGPT: https://arxiv.org/abs/2203.02155
- DPO: https://arxiv.org/abs/2305.18290


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 14 — Inference Systems](../10_inference_systems/lecture.md) · [Next: Lecture 16 — LoRA, QLoRA and PEFT →](../18_lora_qlora_and_peft/lecture.md)

</div>
## Video companions

[Video companions: SFT and RLHF](https://www.youtube.com/results?search_query=supervised+fine+tuning+RLHF+lecture)

## Navigation

[← Previous](../14_filtering_deduplication_mixing_and_synthetic_data/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../16_reinforcement_learning_with_verifiable_rewards/lecture.md)
