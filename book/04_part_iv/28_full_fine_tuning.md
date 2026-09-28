# Chapter 28 — Full Fine-Tuning

**Part:** Part IV

## 1. What full fine-tuning buys you

Full fine-tuning updates most or all model parameters:

theta' = theta + delta_theta

Unlike LoRA, there is no low-rank constraint on the update.

This gives maximum parameter freedom, but also maximum training-state memory and larger checkpoints.

## 2. Memory accounting

A simplified training footprint is:

weights + gradients + optimizer states + activations + temporary buffers

For N parameters, even the weight-only BF16 footprint is:

2N bytes

But training requires substantially more.

This is why a model that fits for inference may not fit for full fine-tuning.

## 3. Full FT vs LoRA/QLoRA

| Dimension | Full FT | LoRA | QLoRA |
|---|---|---|---|
| Base weights | updated | frozen | frozen |
| Trainable params | most/all | small | small |
| Training memory | highest | lower | lowest among these in many setups |
| Checkpoint | large | small adapter | small adapter |
| Multiple specializations | heavier | convenient | convenient |
| Capacity | unrestricted parameter update | rank-limited | rank-limited |
| First experiment | only when broad adaptation is needed | strong default pilot | when memory constrained |

LoRA reference: https://arxiv.org/abs/2106.09685  
QLoRA reference: https://arxiv.org/abs/2305.14314

## 4. When full FT is a coherent hypothesis

Consider full FT when:

- many layers need coordinated adaptation;
- PEFT consistently saturates;
- the desired change is broad rather than a narrow format/style;
- enough training data exists;
- the extra training memory is available;
- the deployment model should be self-contained.

Do not infer this from model size alone.

## 5. Fair comparison protocol

Compare:

**same base checkpoint → same data → same train/validation split → same evaluation → same target metric**

Then measure:

- trainable parameters;
- peak GPU memory;
- GPU-hours;
- checkpoint size;
- target quality;
- retained capability;
- serving latency;
- regression.

If full FT gets more epochs or a better dataset, the comparison is no longer only about parameterization.

## 6. Worked example

Suppose:

| Method | Target score | General score | Peak memory | GPU-hours |
|---|---:|---:|---:|---:|
| LoRA | 84 | 88 | 20 GB | 3 |
| QLoRA | 83 | 88 | 14 GB | 3.5 |
| Full FT | 86 | 85 | 70 GB | 12 |

The full model gains two target points but loses three general points and costs four times the training compute.

Whether that trade is acceptable depends on the mission.

## 7. Checkpoint economics

If:

- full model checkpoint = S GB;
- adapter checkpoint = A GB;
- K versions retained;

storage difference is roughly:

K(S − A)

For repeated experiments, the difference becomes substantial.

## 8. Fine-tuning objective mismatch

Full FT can still fail when the real issue is:

- changing external knowledge;
- missing tools;
- bad retrieval;
- poor evaluation;
- incorrect product requirements.

More trainable parameters do not fix an architecture diagnosis error.

## Research exercise

Run or simulate:

LoRA vs full FT

under a fixed data/evaluation protocol.

Produce a table of:

**quality → regression → memory → GPU-hours → checkpoint size → cost**

Then state what additional evidence would justify spending more compute.

## Laboratory

[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Reference

https://huggingface.co/docs/transformers/main/trainer
