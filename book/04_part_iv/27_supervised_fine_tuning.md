# Chapter 27 — Supervised Fine-Tuning

**Part:** Part IV

## Core concepts
1. **Instruction-response pairs** — Train the model on desired input/output behavior.
2. **Loss masking** — Often compute loss only on assistant/completion tokens.
3. **Formatting** — Chat templates are part of the data interface.
4. **Data quality** — Few excellent demonstrations can be more useful than many noisy ones.

## Formal view
SFT minimizes negative log-likelihood on the desired response conditional on the prompt/context. Dataset formatting controls which tokens receive gradient pressure.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://huggingface.co/docs/trl/sft_trainer
