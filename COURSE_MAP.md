# Course Map — LLM Trainer Masterclass

## The destination

This is deliberately larger than a fine-tuning course. The end state is a person or organization capable of answering:

> **What model should we build? Why? With what data? How much compute? How will we know it works? What could go wrong? What should we fund?**

## Table of Contents

### PART I — LANGUAGE MODELS WITHOUT MAGIC

1. What an LLM actually is
2. Tokens, tokenizers, vocabulary, and context
3. Next-token prediction, cross-entropy, perplexity
4. Embeddings and representation learning
5. Self-attention: the information routing mechanism
6. The Transformer block
7. Sampling, decoding, and why generation is not training
8. The complete training loop

### PART II — DATA IS THE MODEL

9. What counts as training data?
10. Data collection and provenance
11. Cleaning, normalization, language identification
12. Quality filtering and deduplication
13. Data mixtures, weighting, curriculum, and contamination
14. Instruction datasets and conversational data
15. Synthetic data and teacher-model pipelines
16. Building datasets for low-resource and national languages

### PART III — PRETRAINING FROM ZERO

17. Model architecture choices
18. Parameters, memory, FLOPs, tokens, batch size
19. Optimizers, schedules, initialization, regularization
20. Mixed precision and efficient kernels
21. GPU memory and arithmetic intensity
22. Data parallelism, tensor parallelism, pipeline parallelism
23. Checkpointing, fault tolerance, observability
24. Scaling laws and compute allocation
25. Running a real pretraining campaign

### PART IV — POST-TRAINING AND ADAPTATION

26. Why a pretrained model is not a chatbot
27. Supervised fine-tuning / instruction tuning
28. Full fine-tuning
29. Parameter-efficient fine-tuning
30. LoRA and QLoRA
31. Continued pretraining / domain adaptation
32. Preference learning: RLHF, DPO, and related methods
33. Reasoning and reinforcement learning with verifiable rewards
34. Distillation and model compression
35. Model merging, adapters, and specialization

### PART V — EVALUATION IS AN ENGINEERING SYSTEM

36. What does “better” mean?
37. Validation loss and why it is not enough
38. Benchmark design and leakage
39. Human evaluation
40. Task-specific and domain-specific evaluation
41. Multilingual evaluation
42. Safety, robustness, refusal, and jailbreak evaluation
43. Ablations and scientific experiment design
44. Release criteria and model cards

### PART VI — SERVING THE MODEL

45. Inference cost and latency
46. KV cache, batching, quantization
47. Serving stacks and throughput
48. RAG, tools, agents, and model boundaries
49. Monitoring, drift, and post-deployment evaluation

### PART VII — BUILD OR BUY?

50. Prompting vs RAG vs tools vs fine-tuning vs pretraining
51. When training is mandatory
52. When training is wasteful
53. API economics vs self-hosting
54. Data sovereignty and privacy constraints
55. Vendor lock-in and strategic control
56. Total cost of ownership

### PART VIII — NATIONAL / ORGANIZATIONAL LLM ENGINEERING

57. Defining a national language-model mission
58. Data sovereignty, licensing, governance, and provenance
59. Language coverage and multilingual balancing
60. Tokenizer and corpus strategy for local languages
61. Model-size roadmap and compute planning
62. Cluster architecture and procurement
63. Team structure and operating model
64. Research portfolio and experiment queue
65. Funding proposal: from benchmark to budget
66. Risk register and failure budget
67. Partnership model: universities, government, industry, community
68. Sustainability: inference, retraining, data refresh, talent

### PART IX — CAPSTONES

69. Train a tiny GPT from scratch
70. Fine-tune an open model with SFT
71. Compare full fine-tuning, LoRA, and QLoRA
72. Build a domain model using continued pretraining
73. Build a multilingual/national-language pilot
74. Write a model-training proposal and defend its budget
75. Final capstone: design an LLM program from mission to deployment

---

# 25-minute lecture map

| # | Lecture | Core question | Practical lab |
|---|---|---|---|
| 01 | LLMs without magic | What is actually learned? | tokenize + inspect text |
| 02 | Tokenization | What does a model really see? | BPE tokenizer |
| 03 | Next-token prediction | Why does minimizing loss create language ability? | bigram → tiny LM |
| 04 | Attention | How does a token find relevant context? | attention by hand |
| 05 | Transformer | How do the pieces become a deep network? | GPT block |
| 06 | Training | What does one update actually do? | gradient/debug lab |
| 07 | From tiny GPT to GPT-2 | What changes when we scale? | nanoGPT-style run |
| 08 | Data | Why can better data beat more data? | quality/filtering |
| 09 | Data at scale | How do billions/trillions of tokens become a dataset? | dataset pipeline |
| 10 | Architecture | How do we choose layers, width, heads, context? | parameter calculator |
| 11 | GPU economics | What does training really cost? | FLOP/memory calculator |
| 12 | Distributed training | How do multiple GPUs act as one trainer? | DDP/FSDP simulation |
| 13 | Scaling laws | How should we split compute between parameters and data? | fit scaling curve |
| 14 | Pretraining campaign | How do we manage a real run? | experiment tracker |
| 15 | SFT | How does a base LM become instruction-following? | SFT lab |
| 16 | Full FT vs PEFT | What should we update? | controlled comparison |
| 17 | LoRA / QLoRA | How can a small machine adapt a large model? | adapter lab |
| 18 | Preference optimization | How do we teach preferences? | DPO toy experiment |
| 19 | Synthetic data + distillation | How can one model teach another? | teacher→student |
| 20 | Evaluation | How do we know the model improved? | eval harness |
| 21 | Inference | What happens after training? | quantization + serving |
| 22 | Build vs buy | When should we train at all? | decision matrix |
| 23 | National LLM | How would we build for a language/country? | multilingual planning |
| 24 | Funding the program | How do we turn technical plans into a fundable proposal? | proposal generator |

## Repeated critical-thinking pattern

Each lecture includes at least four questions:

1. **Prediction:** Before seeing the result, what do you expect?
2. **Mechanism:** What physical/computational mechanism would create that result?
3. **Failure:** Under what condition would your reasoning break?
4. **Decision:** Given a budget constraint, what would you do?

Every question is followed by a worked answer and then a counterexample.

## Video spine

The course does not outsource teaching to videos. Videos are pre-class or post-class enrichment, and each one is attached to a specific learning objective.

### Andrej Karpathy — Let's build GPT

7.8M+ views at research time. Use for the first implementation transition from tensors to a working decoder-only Transformer. Important sections include tokenization, the data loader, self-attention, Transformer blocks, pretraining vs fine-tuning, and RLHF.

https://www.youtube.com/watch?v=kCc8FmEb1nY

### Andrej Karpathy — Let's reproduce GPT-2 (124M)

1.1M+ views at research time. Use after the tiny GPT labs to introduce mixed precision, Tensor Cores, FlashAttention, AdamW, scheduling, gradient accumulation, DDP, validation, and benchmark evaluation.

https://www.youtube.com/watch?v=l8pRSuU81PU

### 3Blue1Brown — Attention in transformers, step-by-step

4.5M+ views at research time. Use as the visual intuition pass before doing the equations and implementation.

https://www.youtube.com/watch?v=eMlx5fFNoYc

### Sebastian Raschka — Building LLMs from the Ground Up

3-hour coding workshop covering data, tokenizer, architecture, pretraining, loading pretrained weights, instruction fine-tuning, and evaluation.

https://www.youtube.com/watch?v=quh7z1q7-uc

### Stanford CS336 — Language Modeling from Scratch

Use as the academic backbone. The course explicitly spans data, architecture, systems, distributed training, scaling laws, inference, evaluation, SFT/RLHF, RL, and multimodality. The current course provides recordings and assignments.

https://cs336.stanford.edu/

## Research backbone

The course uses the following case studies as anchors rather than treating them as trivia:

- Chinchilla: compute-optimal allocation of parameters and training tokens.
- Llama 3: modern large-scale dense training and post-training.
- OLMo / OLMo 2: open model lifecycle and reproducibility.
- Dolma and FineWeb: data curation at trillion-token scale.
- BLOOM: multilingual collaborative training.
- NLLB-200: low-resource multilingual transfer.
- LoRA / QLoRA: parameter-efficient adaptation.
- InstructGPT: supervised fine-tuning + preference optimization.
- DPO: preference optimization without the original RLHF pipeline.

## Free-first practical ladder

| Level | Practical target | Default environment |
|---|---|---|
| L0 | Tokenizers, tensors, tiny models | CPU / Colab CPU |
| L1 | 1M–50M parameter toy LMs | Free Colab GPU when available |
| L2 | Tiny GPT pretraining | Free Colab GPU |
| L3 | 0.5B–3B adaptation experiments | Free Colab where memory permits; otherwise CPU/mock mode |
| L4 | 7B/8B adapter demonstrations | Quantized inference + small adapter experiments where hardware permits |
| L5 | Multi-GPU simulation/design | single-GPU emulation + systems notebooks |
| L6 | 7B–70B pretraining proposal | calculator + published case studies + cluster simulator |
| L7 | National-scale program design | full technical/economic/proposal capstone |

## The final artifact

The final student output is not just a model. It is a **Model Program Dossier**:

1. mission and target users;
2. baseline model and benchmark;
3. data inventory and provenance;
4. training-method decision;
5. architecture specification;
6. compute and storage plan;
7. training schedule;
8. evaluation plan;
9. safety and governance plan;
10. deployment architecture;
11. staffing plan;
12. budget and total-cost model;
13. milestone plan;
14. risks and mitigations;
15. expected measurable outcomes;
16. funding pitch.

The student must defend every major assumption.
