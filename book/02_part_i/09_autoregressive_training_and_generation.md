# Chapter 9 — Autoregressive Training and Generation

**Part:** Part I

## 1. Training and generation use the same probability model differently

Training has the full target sequence available.

For each position:

p(x_t | x_<t)

can be computed in parallel for all positions using a causal mask.

Generation cannot know future tokens.

It therefore proceeds:

x_1 → x_2 → x_3 → …

## 2. Teacher forcing

During training, the model receives the ground-truth prefix.

Example:

Input: “The capital of France is”

Target: “Paris”

The model does not need to generate earlier tokens before learning the next one.

This makes training highly parallelizable.

## 3. Why inference is sequential

At generation time:

step 1 produces token 1  
step 2 uses token 1 to produce token 2  
step 3 uses tokens 1–2 to produce token 3

This makes decode latency fundamentally different from training.

## 4. Training vs inference

| Dimension | Training | Generation |
|---|---|---|
| Future targets available | yes | no |
| Parallel sequence positions | yes | no |
| Main bottleneck | compute/memory/communication | sequential decode |
| KV cache | not central in same way | central |
| Objective | minimize token loss | sample/choose tokens |
| Typical metric | loss/tokens/sec | TTFT/ITL/tokens/sec |

## 5. Decoding choices

Common controls:

- greedy;
- temperature;
- top-k;
- top-p;
- constrained decoding.

These affect output behavior without changing model weights.

## 6. Worked example

Suppose a model generates 100 tokens.

If decode speed is 20 tokens/sec:

approximate generation time = 5 sec

If it reaches 50 tokens/sec:

≈2 sec

The same model weights can therefore produce very different user experience depending on serving optimization.

## 7. Failure modes

### Exposure bias
Training conditions differ from generated histories.

### Repetition
Decoding or model behavior creates loops.

### Sampling instability
High temperature can increase variability.

### Context overflow
Conversation exceeds context budget.

## Research exercise

Generate the same prompt under:

- greedy;
- temperature 0.7;
- temperature 1.0;
- top-p 0.9.

Compare:

**diversity → factuality → repetition → length**

Then explain which behavior is caused by decoding rather than training.

## Laboratory

[01_next_token_prediction_and_a_tiny_language_model.ipynb](../../notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

## References

- Transformer: https://arxiv.org/abs/1706.03762
- GPT-3: https://arxiv.org/abs/2005.14165

## Deepening: teacher forcing versus generation cost

During training, the target sequence is known, so many positions can be processed in parallel under a causal mask.

During generation, token t must be produced before token t+1.

### Resource consequence

Training emphasizes:

**throughput + batch tokens + accelerator utilization**

Generation emphasizes:

**TTFT + inter-token latency + KV cache + concurrency**

### Experiment

Compare a fixed prompt under:

- greedy decoding;
- sampling;
- different max_new_tokens.

Measure output tokens/sec and latency.

Then vary prompt length separately from generated length.

### Failure mode

A model can have excellent training throughput and poor interactive latency. These are different optimization problems.
