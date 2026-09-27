# PEFT / LoRA / QLoRA Runbook

## Objective

Adapt a pretrained model while limiting trainable parameters and memory.

## Decision

Use PEFT when:
- the base model is already broadly capable;
- the desired change is localized/stable;
- hardware or storage is constrained;
- multiple adapters are operationally useful.

Question first whether SFT or a different training objective is needed; PEFT is the parameter-update strategy.

## Preflight

- record base revision;
- inspect target modules;
- count trainable parameters;
- test adapter save/load;
- check quantization support;
- verify dtype/device behavior.

## LoRA

For a linear layer W:
ΔW = BA

with rank r. Trainable parameters = r(d_in + d_out).

## QLoRA

Use a quantized base model with trainable LoRA adapters. Verify the quantization method and compute dtype on the target hardware.

## Evaluation

Compare:
- base;
- LoRA;
- optional full fine-tuning;
- task-specific failures;
- memory;
- runtime;
- adapter size.

## Release

Ship:
- adapter config;
- base model ID/revision;
- tokenizer;
- training data description;
- training configuration;
- evaluation report;
- license/usage notes.
