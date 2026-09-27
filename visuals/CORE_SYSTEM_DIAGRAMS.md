# Core Visuals

These diagrams are meant to be displayed directly on GitHub and reused in lectures, notebooks, proposals, and papers.

## 1. Language-model learning loop

```mermaid
flowchart LR
    A[Raw text] --> B[Tokenizer]
    B --> C[Token IDs]
    C --> D[Transformer]
    D --> E[Logits]
    E --> F[Cross-entropy]
    F --> G[Backpropagation]
    G --> H[Optimizer update]
    H --> D
    C --> I[Validation]
    D --> I
```

**Notice this:** the model is trained by repeatedly changing parameters so the observed next token becomes more probable.

## 2. Complete model-development lifecycle

```mermaid
flowchart TD
    A[Problem] --> B[Baseline]
    B --> C[Evaluation]
    C --> D{Bottleneck?}
    D -->|Knowledge| E[RAG / tools]
    D -->|Behavior| F[SFT / PEFT]
    D -->|Domain distribution| G[Continued pretraining]
    D -->|Foundation capability| H[Pretraining]
    E --> C
    F --> C
    G --> C
    H --> C
```

**Notice this:** training is one branch of the solution space, not the default answer.

## 3. Pretraining data pipeline

```mermaid
flowchart LR
    A[Sources] --> B[Acquire]
    B --> C[Normalize]
    C --> D[Language ID]
    D --> E[Quality filter]
    E --> F[Deduplicate]
    F --> G[Contamination checks]
    G --> H[Mix / sample]
    H --> I[Tokenize]
    I --> J[Shard]
    J --> K[Train]
```

## 4. GPU memory model

```mermaid
pie title Training memory
    "Weights" : 20
    "Gradients" : 20
    "Optimizer state" : 40
    "Activations / temporary" : 20
```

The exact proportions depend on precision, optimizer, batch, sequence length, checkpointing, and implementation. The diagram is conceptual.

## 5. Distributed training

```mermaid
flowchart LR
    D[Dataset] --> DP1[GPU 1]
    D --> DP2[GPU 2]
    D --> DP3[GPU 3]
    D --> DP4[GPU 4]
    DP1 <-->|collectives| DP2
    DP2 <-->|collectives| DP3
    DP3 <-->|collectives| DP4
```

Data parallelism is only one dimension. Real large-model systems may combine data, tensor, pipeline, context, and expert parallelism.

## 6. Post-training stack

```mermaid
flowchart TD
    A[Base pretrained LM] --> B[Continued pretraining]
    B --> C[SFT]
    C --> D[Preference optimization]
    D --> E[Safety / robustness]
    E --> F[Evaluation]
    F --> G[Serving]
```

Not every model needs every stage.

## 7. Build-vs-buy decision

```mermaid
flowchart TD
    A[Requirement] --> B{Changing knowledge?}
    B -->|Yes| C[RAG / tools]
    B -->|No| D{Stable behavior gap?}
    D -->|Yes| E[SFT / PEFT]
    D -->|No| F{Domain distribution shift?}
    F -->|Yes| G[Continued pretraining]
    F -->|No| H{Need new foundation capability or control?}
    H -->|Yes| I[Pretraining program]
    H -->|No| J[Prompt / API / existing model]
```

## 8. Evidence-to-funding pipeline

```mermaid
flowchart LR
    A[Hypothesis] --> B[Cheap experiment]
    B --> C[Baseline + evidence]
    C --> D[Ablation]
    D --> E[Resource model]
    E --> F[Pilot]
    F --> G[Milestones]
    G --> H[Budget]
    H --> I[Funding proposal]
    I --> J[Scale]
```
