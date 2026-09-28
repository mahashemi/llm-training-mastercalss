# Training and Architecture Method Matrix

This is the curriculum's decision reference. It is not a ranking. It maps common interventions to the type of problem they modify.

## 1. Master matrix

| Method | What changes? | Typical data | Freshness | Up-front resource | Per-request effect | Best-fit problem | Major risk | First experiment |
|---|---|---|---|---|---|---|---|---|
| Prompting | input instructions | prompts/examples | immediate | very low | prompt-token cost | instruction/format gap | brittleness | prompt sweep |
| Structured output | output contract | schema | immediate | low | small overhead | format validity | unsupported constraints | schema-validity test |
| RAG | external context | documents/records | high | low–medium | retrieval + extra tokens | changing knowledge | retrieval failure | oracle-context + retrieval |
| Tools | external state/actions | APIs + schemas | live | medium | tool calls + latency | transactions/actions | unsafe/invalid calls | tool-selection test |
| SFT | model weights | demonstrations | retrain | medium | similar serving class | stable behavior | overfit/regression | small SFT pilot |
| LoRA/PEFT | adapter weights | demonstrations/domain data | retrain | low–medium | serving-dependent | behavior under GPU constraints | overspecialization | rank/data sweep |
| QLoRA | adapter + quantized base | demonstrations/domain data | retrain | low | lower training memory | limited GPU training memory | quantization trade-off | QLoRA vs LoRA |
| Full fine-tuning | most/all weights | task/domain data | retrain | high | same model class | broad adaptation | memory + forgetting | compare to PEFT |
| Continued pretraining | learned distribution | large unlabeled corpus | retrain | high | often same serving shape | language/domain shift | forgetting + compute | domain LM pilot |
| Preference optimization | weights | chosen/rejected pairs | retrain | medium–high | same model class | preference/style | preference bias | small DPO-style pilot |
| RLHF | policy + preference process | preferences/rollouts | retrain | high | training complexity | iterative preference | instability/ops | controlled pilot |
| RLVR | policy | verifiable rewards | retrain | high | training complexity | math/code/verifiable tasks | reward hacking | verifier ablation |
| Distillation | student weights | teacher outputs + targets | retrain | medium–high | can reduce serving cost | smaller deployment | teacher bias transfer | student cost frontier |
| Pretraining from scratch | entire foundation model | very large corpus | retrain | very high | full serving footprint | new foundation capability/control | program-scale failure | feasibility + pilot |

## 2. Diagnose before choosing

### A. External, changing knowledge

Start with retrieval or a live source.

Examples: policies, schedules, inventory, patient records, regulations.

### B. Stable behavior

Start with prompting/structured output. If the gap remains and representative demonstrations exist, test SFT/PEFT.

Examples: JSON format, stable classification policy, output protocol, narrow style.

### C. External state or action

Use tools.

Examples: appointment booking, database lookup, calculation, messaging, workflow execution.

### D. Learned domain/language exposure

Consider continued pretraining after measuring that context/prompting/adaptation cannot close the gap.

Examples: low-resource language representation, domain terminology, specialist corpus.

### E. Foundation-model ownership

Require a program-level justification.

Examples:

- data/control requirements;
- long-term deployment independence;
- target-language representation;
- research questions that require training access.

## 3. Smallest sufficient intervention

| Bottleneck | Cheapest plausible intervention |
|---|---|
| wording/format | prompt/structured output |
| changing facts | RAG |
| live state/action | tool |
| narrow stable behavior | SFT/LoRA |
| limited training VRAM | QLoRA |
| broad domain distribution shift | continued pretraining |
| lower-cost deployment | distillation |
| no viable base solution plus strategic need | from-scratch feasibility |

This is an escalation rule, not a performance ranking.

## 4. Combined lifecycles

Methods compose.

Example:

continued pretraining → SFT → PEFT specialization → preference optimization → RAG → tools → serving

The ordering depends on product and research objectives.

## 5. Evidence required before escalation

| Evidence | Why it matters |
|---|---|
| Baseline quality | defines the gap |
| Error taxonomy | identifies the bottleneck |
| Resource usage | enables cost estimates |
| Latency | prevents quality-only optimization |
| Regression tests | protects existing capability |
| Data quality | prevents noisy adaptation |
| Update frequency | drives retraining economics |
| Security/privacy constraints | can rule out architectures |
| Operational ownership | determines feasibility |

## 6. Decision examples

**Old policy answers:** prompt-only vs RAG with controlled source update.

**JSON failures:** prompt/structured output vs small SFT/LoRA.

**Live appointment:** tool-enabled workflow.

**Weak low-resource language despite correct context:** continued-pretraining pilot.

## 7. Anti-patterns

Do not decide from:

- parameter count alone;
- one benchmark score;
- token price alone;
- GPU price alone;
- training loss alone;
- tiny user samples;
- a successful demo.

The unit of analysis is measured capability under the actual workload and constraints.
