# Lecture 22 — API vs RAG vs Tools vs Training

**Lab:** [build_vs_buy_decision_lab.ipynb](./lab.ipynb)
**Primary goal:** Diagnose the bottleneck before choosing an architecture.

## Learning outcome

The learner should be able to take a requirement such as:

“Build an assistant that answers from changing documents, follows a strict format, and can perform actions.”

and decompose it into **knowledge, behavior, and action** problems.

## The trap

Show four responses to:

“The assistant gives answers from old policy.”

A. fine-tune it  
B. make the prompt longer  
C. add retrieval  
D. train a new foundation model

Consider which experiment would be most informative.

Then establish the rule:

**If the source of truth changes externally, first test whether the model needs access to that source rather than new memorized weights.**

## The three-bucket model

**KNOWLEDGE:** What information should the model see?  
Typical method: RAG or live data.

**BEHAVIOR:** How should the model respond?  
Typical method: prompting → SFT/PEFT.

**ACTION:** What should the system do outside the model?  
Typical method: tools/APIs.

Then add a fourth bucket:

**REPRESENTATION:** Is the model fundamentally weak on the domain/language?  
Possible method: continued pretraining.

## Decision matrix

| Dimension | API | API + RAG | API + tools | SFT/PEFT | Continued PT | Scratch |
|---|---|---|---|---|---|---|
| Up-front effort | low | low–medium | medium | medium | high | very high |
| Main asset | provider model | model + corpus | model + APIs | adapted weights | adapted base | full training stack |
| Freshness | provider-dependent | strong | live state | retrain | retrain | retrain |
| Stable behavior | prompt | prompt + context | workflow-dependent | strong candidate | indirect | indirect |
| Live action | no | no | yes | no | no | no |
| Data ownership | depends on provider/app | corpus + provider path | app + tool data | training data | training corpus | full corpus |
| Main burden | integration | retrieval | workflow reliability | model lifecycle | training lifecycle | full program |

Stress that the table is a **problem-to-method map**, not a winner table.

## Worked scenario

Hospital assistant requirements:

1. current internal policy;
2. structured triage object;
3. live appointment schedule;
4. fixed latency budget;
5. minimal infrastructure.

Map the architecture:

**base model/API**  
+ **RAG for policy**  
+ **structured output or small PEFT experiment for stable format**  
+ **tool for appointment availability**

Evaluate each requirement separately.

| Requirement | Measurement |
|---|---|
| Current policy | retrieval recall + answer correctness |
| Structured response | schema validity + semantics |
| Appointment | tool selection + execution success |
| Latency | p50/p95 |
| Cost | cost per successful task |

## Cost reasoning

API request:

C_request =
input tokens × price
+ output tokens × price
+ retrieval/tool costs

Training lifecycle:

C_training =
compute + data + evaluation + engineering + retries

Thought experiment:

A fine-tune costs 1,000 currency units and saves 0.01 per successful task.

Break-even is about 100,000 successful tasks.

Then add update cadence. Daily-changing knowledge can make repeated retraining uneconomic even when per-request inference becomes cheaper.

## Failure analysis

**Correct document never retrieved**  
→ retrieval failure.

**Correct document retrieved but contradicted**  
→ evidence-use/generation failure.

**Right action, wrong arguments**  
→ tool-contract/model-selection failure.

**Correct semantics, invalid JSON**  
→ structured-output/behavior failure.

**Persistent weak language performance despite correct evidence**  
→ possible representation problem; test continued pretraining.

Learn to map **failure → system layer**.

## Escalation ladder

**Strong baseline**  
↓  
**Add context**  
↓  
**Add actions**  
↓  
**Adapt stable behavior**  
↓  
**Change domain/language distribution**  
↓  
**Foundation-model program only with evidence**

Every escalation must record quality, latency, cost, regression, and operational complexity.

## Exit challenge

Write one sentence for each:

1. What external knowledge is missing?
2. What stable behavior is missing?
3. What external action is required?
4. What is the cheapest experiment that distinguishes the hypotheses?

## Research bridge

- RAG: https://arxiv.org/abs/2005.11401
- Toolformer: https://arxiv.org/abs/2302.04761
- ReAct: https://arxiv.org/abs/2210.03629
- Stanford CS336: https://cs336.stanford.edu/

## Required deliverable

Create an architecture decision record:

**requirement → failure class → baseline → intervention → experiment → quality → latency → cost → risk → next decision**


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Deepening — solve the smallest layer first

Take this requirement:

**“Answer current policy questions, return valid JSON, and book appointments.”**

Decompose:

| Requirement | Layer | Experiment |
|---|---|---|
| current policy | knowledge | RAG retrieval/oracle-context test |
| valid JSON | behavior/interface | structured output + SFT pilot |
| book appointment | action | tool-selection/execution test |
| poor language representation | representation | continued-pretraining pilot |

### Cost comparison exercise

For each architecture estimate:

**quality → latency → successful tasks → recurring cost → one-time cost → engineering burden**

You must identify the assumption with the greatest sensitivity.

### Training escalation

Only escalate to weight updates when the simpler system layer cannot explain or solve the measured failure.



## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 21 — Safety, Robustness and Failure Analysis](../21_safety_robustness_and_failure_analysis/lecture.md) · [Next: Lecture 23 — Build an LLM Program →](../23_build_an_llm_program/lecture.md)

</div>