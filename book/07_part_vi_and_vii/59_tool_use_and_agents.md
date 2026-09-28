# Chapter 59 — Tool Use and Agents: The Model Becomes Part of a Control Loop

**Part:** Part VII

## 1. Tool use is a systems problem

A tool-enabled model can emit an action:

a_t = (tool_name, arguments)

The system then validates the action, checks identity and permissions, executes the tool, returns an observation, and decides whether another step is needed.

This changes the reliability problem. The model is not judged only on language quality; it is now one component of an **action policy**.

Research on Toolformer and ReAct illustrates this pattern of combining language-model decisions with external actions:
https://arxiv.org/abs/2302.04761
https://arxiv.org/abs/2210.03629

## 2. Levels of tool integration

| Level | Example | Model role | System role |
|---|---|---|---|
| Read-only lookup | search policy | choose query | execute + return evidence |
| Deterministic function | calculator | arguments | validate + compute |
| Reversible action | draft email | choose action | auth + execute |
| Sensitive action | record update | request action | strict policy + audit |
| Irreversible action | financial transfer | propose action | confirmation + policy + execution |

As side effects become more consequential, deterministic controls should dominate.

## 3. Tool schema quality

A weak tool:

book_appointment(patient, doctor, time)

A production contract should specify:

- required/optional fields;
- enums and formats;
- timezone;
- identifier semantics;
- allowed ranges;
- authorization rules;
- side effects;
- idempotency behavior;
- expected errors.

Conceptual schema:

    name: book_appointment
    arguments:
      patient_id: string
      slot_id: string
      confirmation_token: string
    side_effect: creates appointment
    idempotency_key: request_id

The exact format depends on the platform. The engineering principle is stable: **tool contracts are part of the effective environment in which the model operates.**

## 4. Separate the reliability metrics

| Metric | Question |
|---|---|
| Tool selection accuracy | Right tool? |
| Argument validity | Schema-valid arguments? |
| Argument correctness | Semantically correct values? |
| Execution success | Accepted by external system? |
| Recovery success | Recovers from failure? |
| Side-effect safety | Avoids unauthorized actions? |
| End-to-end task success | User goal completed? |

A system can have 98% valid tool syntax and still have poor task success.

## 5. Multi-step reliability

For n independent steps with success probability p:

P(all succeed) ≈ p^n

At p = 0.98:

| Steps | Approx. all-success probability |
|---:|---:|
| 1 | 98.0% |
| 3 | 94.1% |
| 5 | 90.4% |
| 10 | 81.7% |

This is only an approximation because real failures are correlated, but it teaches why agents need verification and recovery.

## 6. Latency

For sequential tool calls:

L_task ≈ sum(model + tool + network latency)

Parallelizable read-only operations can overlap. Writes often have ordering constraints.

| Design | Execution pattern |
|---|---|
| One model answer | one generation |
| Search then answer | retrieval → generation |
| Three parallel searches then answer | parallel lookup → generation |
| Plan → tool → verify → act | multiple serial dependencies |

Agent depth should therefore be treated as a latency and reliability budget.

## 7. State and idempotency

Agents retry.

For write operations, use:

- idempotency keys;
- transaction status;
- precondition checks;
- dry-run or preview;
- explicit confirmation;
- bounded retries;
- compensating actions when appropriate.

A booking action should not create two appointments because a network timeout triggered a retry.

## 8. Worked example — appointment booking

Goal:

“Find the earliest appointment next week and book it after I confirm.”

Safe control flow:

**request → read-only availability → candidate slots → user confirmation → booking → verify booking ID → response**

Unsafe control flow:

**request → model directly books**

The difference is system control flow, not merely model intelligence.

## 9. Agent vs deterministic workflow

| Requirement | Architecture to evaluate first |
|---|---|
| Fixed steps, known branches | deterministic workflow |
| Variable lookup | tool-assisted workflow |
| Open-ended planning | bounded agent |
| High-risk side effects | deterministic policy + model as proposer |
| Human checkpoints needed | human-in-the-loop |

Do not use an agent merely because a process has several steps.

## 10. Security boundary

Treat model-generated arguments as untrusted input.

The tool executor must enforce:

- authentication;
- authorization;
- validation;
- rate limits;
- resource scope;
- secret isolation;
- audit logging;
- confirmation rules.

Natural-language instructions to the model are not a security control.

## 11. When training helps

Training can improve:

- tool selection;
- argument formatting;
- stable workflows;
- domain terminology;
- recovery patterns.

Training does not guarantee:

- API availability;
- permission correctness;
- current external state;
- transaction safety;
- observability.

## Research exercise

Create a five-step synthetic workflow.

Measure:

1. tool selection;
2. argument validity;
3. argument correctness;
4. execution success;
5. recovery success;
6. end-to-end task success;
7. p95 latency;
8. tool calls per successful task.

Compare a free-form agent with a deterministic workflow and explain where the additional complexity is justified.

## Laboratory

[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## References

- Toolformer: https://arxiv.org/abs/2302.04761
- ReAct: https://arxiv.org/abs/2210.03629
