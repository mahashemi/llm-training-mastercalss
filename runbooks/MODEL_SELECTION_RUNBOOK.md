# Model Selection Runbook

| Requirement | First experiment | Escalation |
|---|---|---|
| Fresh factual knowledge | RAG | better retrieval/tooling |
| Structured output | prompting + schema | SFT/LoRA |
| Repeated domain behavior | SFT/LoRA | continued pretraining |
| Target language capability is weak | continued pretraining / multilingual adaptation | train a language-focused model |
| Need complete control of weights/data/training | open-weight model or own pretraining | scratch training |
| Need a fundamentally new foundation capability | pretraining | larger/longer/more diverse training |

The runbook requires evidence from a baseline and an ablation before escalating the intervention.


## Model selection protocol

### Step 1 — Define workload

Record:

**task + quality target + context + latency + cost + data/privacy constraints**

### Step 2 — Establish capability baseline

Test at least one strong existing model or API and, where relevant, a small open-weight model.

### Step 3 — Audit the model

Record:

- architecture;
- parameter count;
- active parameters for MoE;
- context;
- modalities;
- tokenizer;
- license;
- precision/checkpoint variants.

### Step 4 — Resource feasibility

Estimate:

**weights + KV cache + training state if adaptation is planned**

### Step 5 — Decide the next test

Choose the smallest experiment that answers whether the model can satisfy the workload.

Do not choose by parameter count alone.
