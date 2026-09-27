# Training Method Matrix

The methods below are deliberately presented as separate axes: **problem/objective**, **data**, **which parameters move**, **precision**, and **optimization**.

| Method | Changes weights? | Typical data | Best suited to | Main cost | First baseline |
|---|---|---|---|---|---|
| Prompting | No | prompt | simple behavior | inference tokens | model/API |
| RAG | No | external documents | fresh knowledge | retrieval + context | prompt-only |
| Tools | No model weights | live APIs/actions | external actions | orchestration | direct model |
| SFT | Yes | demonstrations | stable instruction/behavior | training | prompting |
| Full fine-tuning | Yes, most/all | task/domain data | broad adaptation | high memory/storage | SFT/PEFT |
| LoRA | Adapter weights | demonstrations/domain | parameter-efficient adaptation | low train memory | SFT baseline |
| QLoRA | Adapter weights + quantized base | demonstrations/domain | limited GPU memory | low train memory | LoRA |
| Continued pretraining | Yes | unlabeled domain text | broad domain/language shift | large token budget | SFT/PEFT |
| Preference optimization | Yes | chosen/rejected responses | preference/style/alignment | data + training | SFT |
| RLHF | Yes | preference + reward | iterative preference optimization | operational complexity | DPO/SFT |
| RLVR | Yes | verifiable rewards | math/code/other checkable outcomes | rollout/training complexity | SFT |
| Distillation | Student weights | teacher outputs | smaller/cheaper model | teacher generation + training | target model |
| Pretraining from scratch | Yes | huge unlabeled corpus | new foundation capability/control | very high | all simpler methods |

## How to choose

Ask these questions in order:

1. Is the missing information external and changing?
2. Is the missing capability a stable behavior?
3. Is the domain/language distribution fundamentally different?
4. Is a smaller model sufficient?
5. Is there a verifier or reliable preference signal?
6. Do we actually need to own the foundation model?

## Important

SFT, LoRA, QLoRA, preference optimization, and continued pretraining are not mutually exclusive. A realistic lifecycle may be:

**continued pretraining → SFT → LoRA-based specialization → preference optimization → evaluation → serving**

Use evidence to justify each stage.
