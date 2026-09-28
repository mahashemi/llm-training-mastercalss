# Engineering Decision Trees

These trees convert an LLM requirement into a sequence of falsifiable experiments. They are decision aids, not universal rankings.

## Tree 1 — What kind of problem is this?

### Step 1: Is the information external and changing?

Examples: policies, inventory, schedules, patient records, regulations.

**Yes → evaluate retrieval or a live data source.**

### Step 2: Is the missing capability a stable behavior?

Examples: format, classification, workflow structure, response style.

**Yes → strong prompting/structured output → SFT/PEFT if the gap remains.**

### Step 3: Does the task require external action?

Examples: booking, database writes, calculation, messaging.

**Yes → tool/API integration with validation and authorization.**

### Step 4: Does the model remain weak with correct context?

**Yes → investigate representation/domain exposure.**

Then consider continued pretraining.

### Step 5: Do we need foundation-model ownership?

Only after the preceding paths have been measured and shown insufficient.

## Tree 2 — Method-selection matrix

| Evidence / bottleneck | Candidate first test |
|---|---|
| Instruction ambiguity | prompt sweep |
| Output contract failure | structured output |
| Current/private knowledge | RAG |
| Live state/action | tool |
| Stable behavior gap | SFT/LoRA |
| Limited GPU memory | QLoRA |
| Broad domain/language gap | continued PT |
| Need lower serving cost | distillation |
| Strategic foundation requirement | pretraining feasibility |

## Tree 3 — Required evidence before escalation

| Escalation | Evidence required |
|---|---|
| prompt → RAG | knowledge/freshness failure + retrieval hypothesis |
| RAG → training | correct evidence supplied but behavior/representation remains weak |
| SFT → continued PT | broad domain/language gap rather than narrow behavior |
| continued PT → scratch | persistent structural gap + strong data/control/ownership case |
| small → large model | measured scaling trend + economic justification |
| prototype → production | task success + latency + reliability + safety |

## Tree 4 — Poor training run

### Loss not decreasing

Check:

1. data;
2. target shifting;
3. optimizer/LR;
4. gradient flow;
5. numerical stability;
6. architecture.

### Training loss decreases but validation does not

Check:

1. overfitting;
2. leakage;
3. distribution mismatch;
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

### Target improves but general capability falls

Check:

1. forgetting;
2. training mixture;
3. adaptation strength;
4. retained-capability evaluation.

## Tree 5 — Product decision

When comparing architectures, score each candidate on the same dimensions:

**quality → freshness → latency → cost → privacy → reliability → maintenance → control**

Do not use one aggregate score to hide a critical failure.

## Tree 6 — Scaling gate

Before approving a larger run ask:

- What uncertainty does this run remove?
- What cheaper experiment could answer the same question?
- What is the expected gain?
- What is the incremental TCO?
- What is the stop condition?
- What fallback exists?

If these answers are unclear, scaling is not yet an engineering decision.

## Tree 7 — Funding escalation

**Stage 0:** existing baseline  
↓  
**Stage 1:** low-cost intervention  
↓  
**Stage 2:** reproducible training pilot  
↓  
**Stage 3:** controlled scaling study  
↓  
**Stage 4:** product/system pilot  
↓  
**Stage 5:** full program

Every stage defines:

**evidence → budget released → owner → threshold → stop/pivot condition**

## Required artifact

For every major decision, create:

**decision statement → alternatives → assumptions → baseline → experiment → measurements → TCO → risks → gate → next action**
