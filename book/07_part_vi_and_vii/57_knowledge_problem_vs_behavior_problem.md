# Chapter 57 — Knowledge Problem vs Behavior Problem

**Part:** Part VII  
**Purpose:** Diagnose what is actually missing before choosing prompting, retrieval, tools, fine-tuning, continued pretraining, or foundation-model training.

## 1. The central diagnostic

Many LLM projects begin with: **“The model needs to know our information.”** That sentence is ambiguous.

There are at least four different failure classes:

| Failure | What is missing? | Typical symptom | First intervention |
|---|---|---|---|
| Knowledge access | External facts or documents | Outdated or unsupported answer | Retrieval |
| Stable behavior | A repeatable response pattern | Knows what to say but violates format/process | Prompting → SFT/PEFT |
| External action | Access to a live system | Describes an action but cannot perform it | Tool/API integration |
| Model capability/domain exposure | Learned representation or broad domain competence | Retrieval/prompting cannot close a persistent gap | Continued pretraining; scratch only if justified |

These can coexist. A clinical assistant may need retrieval for current policy, tools for appointment lookup, and SFT for consistent conversation structure.

## 2. Parametric memory vs external memory

Let a frozen model be p_theta(y | x).

Retrieval changes the information available at inference:

p_theta(y | x, R(x))

where R(x) is retrieved evidence.

Fine-tuning changes the parameters:

p_theta_prime(y | x)

Continued pretraining changes the learned distribution over a much larger unlabeled corpus.

Tools add an action loop:

request → model decision → tool(action) → observation → model

This distinction explains why fine-tuning is often the wrong first move for changing facts: the facts live in a moving external source, while the weights are a relatively expensive and slow-to-update memory.

## 3. Complete decision matrix

| Dimension | Prompting | RAG | Tools | SFT / PEFT | Continued pretraining | From scratch |
|---|---|---|---|---|---|---|
| Changes weights | No | No | No | Yes | Yes | Yes |
| Main thing changed | Instructions | Context | Actions | Behavior | Domain/language distribution | Foundation model |
| Fresh facts | Weak unless supplied | Strong fit | Strong fit for live state | Weak | Fixed at train time | Fixed at train time |
| Stable style/format | Sometimes | Sometimes | Sometimes | Strong candidate | Indirect | Indirect |
| Live transactions | No | No | Strong fit | No | No | No |
| Provenance | Manual | Can be explicit | Tool trace | Indirect | Indirect | Indirect |
| Update path | Immediate | Re-index/update source | Live | Retrain | Retrain | Retrain |
| Up-front resource | Very low | Low–medium | Medium | Medium | High | Very high |
| Per-request effect | Prompt tokens | Retrieval + context tokens | Tool calls + generation | Usually similar serving class | Usually similar serving class | Depends on model |
| Data needed | Instructions/examples | Searchable sources | Schemas/APIs | Demonstrations | Large unlabeled corpus | Very large corpus |
| First test | Prompt sweep | Retrieval ablation | Tool success test | Small adaptation | Domain LM-loss pilot | Feasibility + baselines |
| Main risk | Brittleness | Bad retrieval/context overload | Invalid or unsafe actions | Overfit/regression | Forgetting/compute inefficiency | Program-scale failure |

This is a mapping from failure type to intervention type, not a ranking.

## 4. Fast diagnosis

Ask these questions in order:

1. **Would the correct information exist in a source available at query time?**  
   Yes → test retrieval or a live source.

2. **Does the model already have the information but fail to follow a stable procedure?**  
   Yes → strengthen prompting/structured output, then test SFT/PEFT.

3. **Does the task require changing external state?**  
   Yes → use a tool or API; training does not replace the system of record.

4. **Does the model remain weak after correct evidence is supplied?**  
   Yes → determine whether the problem is behavior or learned domain/language representation.

5. **Do you actually need to own a foundation model?**  
   Only after the preceding interventions have been measured and shown insufficient.

## 5. Worked example A — changing policy

Requirement:

“Answer according to the policy currently in force and identify the supporting section.”

A fine-tuned model can memorize old policy text, but every substantive policy change creates a refresh problem.

A retrieval design can:

1. index approved policy versions;
2. preserve section metadata and effective dates;
3. retrieve relevant sections;
4. generate from retrieved evidence;
5. attach a citation or evidence pointer.

The key experiment is not just static accuracy. Replace the source document with a controlled updated version and measure whether the answer changes correctly.

## 6. Worked example B — stable response protocol

Requirement:

“For every patient message, output concern, clarifying question, urgency, and next step.”

The knowledge may already be available. The gap is stable behavior.

Run:

- prompt-only baseline;
- structured-output constraints;
- small SFT or LoRA pilot.

Measure schema validity, field omission, semantic quality, latency, and regression on unrelated tasks.

## 7. Worked example C — live action

Requirement:

“Find the next available appointment and book it after confirmation.”

The model cannot invent current appointment state.

A tool-enabled system can:

request → availability tool → show choices → user confirmation → booking tool → booking verification

The tool provides the external state and side effect. Training may improve tool selection or argument formatting but cannot guarantee that the appointment system is available or authorized.

## 8. Worked example D — domain/language representation

Suppose a model remains weak on a target language even when the correct information is supplied in context.

Possible causes include:

- poor tokenization;
- weak language representation;
- limited morphological coverage;
- domain terminology gaps;
- weak instruction tuning for that language.

Now a continued-pretraining experiment has a coherent hypothesis: additional target-language/domain tokens may change the model's learned distribution.

Measure target-language language-model loss, native-language task quality, retained general capability, and compute per improvement.

Only after these experiments should a team consider building a new base model.

## 9. Cost and latency reasoning

For an inference request:

C_request =
retrieval cost
+ input tokens × input price
+ output tokens × output price
+ tool-call cost

For RAG, input tokens become base input + retrieved context.

For training:

C_training_lifecycle =
compute
+ data preparation
+ evaluation
+ engineering
+ retries
+ storage
+ monitoring

The correct comparison is therefore lifecycle cost under the target workload.

## 10. Experiment ladder

Use this escalation path:

**Strong baseline**  
→ **Add missing context**  
→ **Add missing actions**  
→ **Adapt stable behavior**  
→ **Change domain/language distribution**  
→ **Build a foundation model only with program-level evidence**

At each step record:

- target metric;
- quality delta;
- latency delta;
- one-time cost;
- recurring cost;
- data requirements;
- regression risk;
- operational burden;
- evidence that the next step is warranted.

## 11. Anti-patterns

### “The model is wrong, so fine-tune it.”

Wrong when the source of truth is external and changing.

### “RAG solves everything.”

Wrong for stable behavior, external actions, or fundamental representation gaps.

### “Tools are just prompting.”

No. Tools add external state, authorization, validation, retries, failure modes, and potentially irreversible side effects.

### “A bigger model will fix the architecture.”

A larger model can hide a systems problem while increasing latency and cost.

## 12. Research exercise

Create three hypotheses:

- **Knowledge hypothesis:** the failure disappears when correct evidence is retrieved.
- **Behavior hypothesis:** the failure remains with correct evidence but improves with demonstrations/training.
- **Action hypothesis:** the intent is correct but the task cannot complete without an external tool.

Design the cheapest experiment that distinguishes the three.

## Laboratory

[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Research bridge

- Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://arxiv.org/abs/2005.11401
- Stanford CS336: https://cs336.stanford.edu/
