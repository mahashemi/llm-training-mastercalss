# Chapter 58 — RAG Architecture: Retrieval Is a System, Not a Prompt Trick

**Part:** Part VII

## 1. What RAG changes

Retrieval-Augmented Generation keeps model weights fixed and changes the information available at inference time:

p_theta(y | x, R(x))

where R(x) is a retrieval process over an external corpus.

The practical consequence is that documents can change without retraining the model.

That does not make RAG automatically correct. RAG adds a chain of possible failures:

**source → parsing → chunking → indexing → retrieval → reranking → context assembly → generation → attribution**

The original RAG work treats retrieval as non-parametric memory alongside parametric model memory:
https://arxiv.org/abs/2005.11401

## 2. Reference architecture

| Layer | Responsibility | Measurement | Common failure |
|---|---|---|---|
| Source ingestion | Collect approved content | ingestion completeness | missing source |
| Parsing | Preserve text/tables/structure | parse accuracy | broken structure |
| Chunking | Create retrieval units | coverage | context split |
| Indexing | Store searchable representations | index freshness | stale index |
| Retrieval | Select candidates | Recall@k | relevant evidence missed |
| Reranking | Order candidates | MRR/NDCG | good evidence buried |
| Context assembly | Fit useful evidence | evidence-token ratio | context overload |
| Generation | Answer from evidence | correctness/groundedness | evidence ignored |
| Attribution | Connect claims to sources | citation support | unsupported citation |
| Monitoring | Detect drift | SLOs | silent degradation |

A vector database is an implementation detail. Evaluate the end-to-end behavior.

## 3. Retrieval quality is not answer quality

Separate:

- **retrieval failure:** the correct evidence was not in top-k;
- **ranking failure:** relevant evidence exists but is poorly ordered;
- **evidence-use failure:** evidence is present but ignored;
- **generation failure:** unsupported text is added;
- **attribution failure:** the citation does not support the claim.

This decomposition makes debugging possible.

## 4. Chunking is a modeling decision

A fixed-size chunk can accidentally separate a rule from its exception.

A retrieval unit should often preserve:

- document ID;
- title;
- section hierarchy;
- effective date;
- access-control metadata;
- source location;
- surrounding heading context.

The objective is not a fashionable chunk size. The objective is **recoverable evidence**.

### Controlled chunking experiment

| Variant | Size | Overlap | Metadata | Hypothesis |
|---|---:|---:|---|---|
| A | small | low | title | precision |
| B | medium | medium | hierarchy | balance |
| C | large | low | hierarchy + date | continuity |

Keep retriever and generator fixed. Compare recall, answer quality, latency, and cost.

## 5. Retrieval strategies

| Strategy | Strength | Weakness | Useful when |
|---|---|---|---|
| Lexical | exact terms, IDs | semantic mismatch | terminology-heavy |
| Dense | semantic similarity | exact identifiers may be weak | natural-language questions |
| Hybrid | combines both | more complexity | mixed enterprise data |
| Reranking | better ordering | extra latency | high-value queries |
| Metadata filters | access/time constraints | depends on clean metadata | regulated/private corpora |

No single retrieval method should be assumed best without measurement on the actual corpus.

## 6. Latency budget

A useful decomposition is:

L_total =
routing
+ retrieval
+ reranking
+ context assembly
+ model prefill
+ model decode
+ tool/other latency

Retrieved context increases prefill work.

Illustrative budget:

| Stage | Target |
|---|---:|
| Query processing | 20 ms |
| Retrieval | 40 ms |
| Reranking | 50 ms |
| Network/assembly | 20 ms |
| Prefill | 150 ms |
| Decode | 450 ms |
| Total | 730 ms |

These numbers are teaching examples, not universal targets. Measure your own stack.

## 7. RAG economics

A simplified monthly model is:

C_RAG =
embedding/indexing
+ storage
+ request_count × retrieval_cost
+ request_count × model_cost(base_input + retrieved_tokens + output)

RAG shifts part of the cost from periodic retraining to per-request retrieval and extra context processing.

Therefore, query volume matters.

## 8. Worked example — policy assistant

Suppose:

- 1,000,000 requests/month;
- 900 base input tokens;
- 700 retrieved tokens;
- 250 output tokens.

The model now processes 1,600 input tokens instead of 900.

The incremental input burden is:

700 × 1,000,000 = 700 million extra input tokens/month.

That number should appear directly in a cost and latency model.

Now compare two architectures:

| Dimension | Prompt-only | RAG |
|---|---|---|
| Current policy | weak unless manually injected | source-driven |
| Input tokens | lower | higher |
| Retrieval infrastructure | none | required |
| Update path | edit prompts/app | update source/index |
| Evidence trace | manual | can be explicit |
| Main risk | stale/unsupported answers | retrieval misses/wrong context |

## 9. Freshness testing

A mature RAG benchmark contains controlled updates:

1. publish source version A;
2. query;
3. replace with version B;
4. re-index;
5. query again;
6. verify the answer reflects B;
7. verify obsolete A is no longer selected.

Measure **time-to-correct-answer after source change**.

## 10. Access-control testing

Carry authorization metadata through:

identity → query policy → retrievable corpus → retrieved chunks → context → answer

Test two users with different permissions.

The critical assertion is:

**restricted evidence never enters the model context.**

This should be automated, not checked once by a human.

## 11. Failure-analysis matrix

| Symptom | Likely stage | Test |
|---|---|---|
| Correct document never appears | retrieval | Recall@k |
| Correct document rank is poor | ranking | compare reranker |
| Correct evidence present but ignored | generation | oracle-context test |
| Answer right, citation wrong | attribution | claim-to-span test |
| Old content persists after update | indexing | freshness test |
| User sees restricted data | ACL boundary | adversarial identity test |
| Quality falls with more context | assembly/model | context-budget sweep |

## 12. Minimum production evaluation

Report at least:

**Retrieval:** Recall@k, MRR/NDCG, critical-evidence coverage  
**Answer:** correctness, completeness, groundedness  
**Attribution:** citation support  
**Operations:** p50/p95 latency, tokens/request, cost/request  
**Security:** unauthorized retrieval rate  
**Freshness:** update-to-correct-answer latency

A single RAG score hides too much.

## Research exercise

Build three variants:

1. lexical;
2. dense;
3. hybrid plus reranker.

Keep the generator fixed.

Report:

Δ Recall@5  
Δ Answer Quality  
Δ p95 Latency  
Δ Cost per Correct Answer

Then explain cases where better retrieval metrics do not produce better final answers.

## Laboratory

[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## References

- Lewis et al., https://arxiv.org/abs/2005.11401
- Stanford CS336, https://cs336.stanford.edu/
