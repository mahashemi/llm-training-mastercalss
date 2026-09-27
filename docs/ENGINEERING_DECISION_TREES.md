# Engineering Decision Trees

## Tree 1 — Should we train anything?

1. Define the target capability and measurable metric.
2. Build the strongest practical API/model baseline.
3. Add retrieval if the problem involves changing external knowledge.
4. Add tools if the problem involves external actions.
5. Try structured prompting/output constraints.
6. Try SFT/PEFT for stable behavior gaps.
7. Try continued pretraining for substantial domain/language distribution shift.
8. Consider pretraining from scratch only when control, data, language coverage, strategic capability, or economics justify a foundation-model program.

## Tree 2 — Which training method?

| Evidence / problem | Candidate |
|---|---|
| high-quality demonstrations | SFT |
| limited GPU memory | LoRA / QLoRA |
| broad parameter change required | Full FT |
| strong domain distribution shift | Continued pretraining |
| ranked responses | Preference optimization |
| verifiable objective | RLVR |
| smaller deployment model needed | Distillation |
| fundamentally new base capability | Pretraining |

These are not mutually exclusive. For example: continued pretraining → SFT → LoRA-based adaptation may be one lifecycle.

## Tree 3 — What should we do when a run is poor?

### Loss is not decreasing
Check:
1. data/labels;
2. target shifting;
3. optimizer/LR;
4. gradient flow;
5. numerical stability;
6. architecture implementation.

### Training loss decreases but validation does not
Check:
1. overfitting;
2. train/validation leakage;
3. data distribution mismatch;
4. evaluation pipeline.

### Quality improves but cost explodes
Check:
1. model size;
2. sequence length;
3. precision;
4. batching;
5. kernels;
6. inference architecture;
7. distillation.

### Model improves in the target domain but worsens elsewhere
Check:
1. catastrophic forgetting;
2. training mixture;
3. retained-capability evaluation;
4. adaptation strength.

## Tree 4 — How should a funding proposal escalate?

**Stage 0:** existing model baseline  
↓  
**Stage 1:** cheap data/behavior pilot  
↓  
**Stage 2:** reproducible training experiment  
↓  
**Stage 3:** controlled scaling experiment  
↓  
**Stage 4:** pilot system  
↓  
**Stage 5:** production/national program

At each stage define:
- evidence required;
- resources released;
- success metric;
- failure/kill criteria;
- next decision.
