# Lecture 22 — API vs RAG vs Tools vs Training

**Duration:** 25 minutes  
**Primary goal:** Diagnose the bottleneck before choosing an architecture.

## Learning outcome

The learner should be able to take a requirement such as:

“Build an assistant that answers from changing documents, follows a strict format, and can perform actions.”

and decompose it into **knowledge, behavior, and action** problems.

## 0–3 minutes — The trap

Show four responses to:

“The assistant gives answers from old policy.”

A. fine-tune it  
B. make the prompt longer  
C. add retrieval  
D. train a new foundation model

Ask students which experiment would be most informative.

Then establish the rule:

**If the source of truth changes externally, first test whether the model needs access to that source rather than new memorized weights.**

## 3–7 minutes — The three-bucket model

**KNOWLEDGE:** What information should the model see?  
Typical method: RAG or live data.

**BEHAVIOR:** How should the model respond?  
Typical method: prompting → SFT/PEFT.

**ACTION:** What should the system do outside the model?  
Typical method: tools/APIs.

Then add a fourth bucket:

**REPRESENTATION:** Is the model fundamentally weak on the domain/language?  
Possible method: continued pretraining.

## 7–12 minutes — Decision matrix

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

## 12–16 minutes — Worked scenario

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

## 16–19 minutes — Cost reasoning

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

## 19–22 minutes — Failure analysis

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

Teach students to map **failure → system layer**.

## 22–24 minutes — Escalation ladder

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

## 24–25 minutes — Exit challenge

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
