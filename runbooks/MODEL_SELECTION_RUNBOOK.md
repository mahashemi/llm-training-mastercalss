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
