# Chapter 26 — Continued Pretraining

**Part:** Part III

## 1. Continued pretraining changes the training distribution

Start from an existing pretrained model and train it further on additional unlabeled tokens.

The hypothesis is:

**the base model is underexposed to the target language/domain distribution.**

This differs from SFT, where examples directly specify desired responses.

## 2. Decision table

| Symptom | Better first hypothesis |
|---|---|
| outdated fact | retrieval/live source |
| wrong output format | SFT/PEFT |
| poor tool usage | tool/system design + possibly SFT |
| weak specialist terminology | continued PT candidate |
| poor low-resource language | continued PT candidate |
| broad task behavior gap | SFT/PEFT or broader adaptation |

## 3. Evidence threshold

Before spending heavily, establish:

- strong baseline;
- target benchmark;
- tokenizer efficiency;
- corpus size/quality;
- retrieval baseline;
- SFT/PEFT baseline where relevant.

A continued-pretraining run should answer a specific representation/domain hypothesis.

## 4. Data mixture

Avoid training only on a narrow target corpus by default.

Compare:

| Run | Target | General replay |
|---|---:|---:|
| A | 100% | 0% |
| B | 75% | 25% |
| C | 50% | 50% |

Measure target improvement and retained capabilities.

## 5. Compute planning

Dense-model first-order:

FLOPs ≈ 6ND

Then use measured throughput.

Example:

N = 7B  
D = 100B

FLOPs ≈ 4.2e21

If delivered throughput is 5e15 FLOP/s:

time ≈ 9.7 days

Add data processing, evaluation, storage, retries, and staffing for project TCO.

## 6. Learning-rate risk

The model already contains useful representations.

An overly aggressive learning rate can cause damaging parameter drift.

Therefore sweep:

- learning rate;
- warmup;
- target/general mixture;
- token budget.

Inspect checkpoint trajectories.

## 7. Worked low-resource example

Suppose:

- target-language benchmark = 55;
- RAG increases factuality but not language quality;
- SFT increases format but not grammar;
- tokenizer fertility is high;
- corpus = 5B high-quality tokens.

A coherent next hypothesis is continued pretraining.

Pilot:

100M–500M target-language tokens

Measure:

- target-language loss;
- native benchmark;
- general retention;
- safety;
- compute.

If no meaningful gain appears, do not scale merely because the run is technically possible.

## 8. Stop conditions

Possible predeclared gates:

- target gain below threshold;
- general regression above threshold;
- compute per point gain too high;
- data quality below requirement;
- throughput below plan.

## Research exercise

Run three mixture variants at equal approximate compute.

Report:

**target score → general score → loss → GPU-hours → cost → regression**

Then decide whether another token tranche is justified.

## Laboratory

[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Reference

https://cs336.stanford.edu/
