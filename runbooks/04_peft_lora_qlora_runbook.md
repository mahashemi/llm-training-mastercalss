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


## Reproducible PEFT protocol

### 1. Architecture audit

List all candidate linear modules. Record which are selected and why.

### 2. Parameter accounting

For each selected matrix:

**full = d_in × d_out**

**LoRA = r(d_in + d_out)**

Sum across all targeted layers.

### 3. Rank sweep

Use a controlled ladder such as:

**r = 4, 8, 16, 32**

Keep:

- data;
- steps;
- sequence length;
- evaluation

fixed.

### 4. Quantization experiment

Compare BF16 LoRA and 4-bit QLoRA under the same task/evaluation protocol.

Measure:

**quality + peak memory + throughput + wall time + adapter size**

### 5. Merge/reload test

Verify that:

- adapter-only load works;
- adapter + base works;
- merged model reproduces expected outputs within the chosen tolerance.

### 6. Release

Publish the exact base model revision and PEFT configuration. Never publish an adapter without identifying the base checkpoint required to use it.
