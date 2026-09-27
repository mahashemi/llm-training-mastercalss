# Paper Reading Path

Read papers in this order. Do not attempt to memorize every detail. Extract: problem, method, evidence, assumptions, limitations, and what you would reproduce.

## Foundations

1. Vaswani et al. (2017) — Attention Is All You Need
https://arxiv.org/abs/1706.03762

2. Brown et al. (2020) — Language Models are Few-Shot Learners
https://arxiv.org/abs/2005.14165

3. Kaplan et al. (2020) — Scaling Laws for Neural Language Models
https://arxiv.org/abs/2001.08361

4. Hoffmann et al. (2022) — Training Compute-Optimal Large Language Models
https://arxiv.org/abs/2203.15556

## Training efficiency

5. Dao et al. (2022) — FlashAttention
https://arxiv.org/abs/2205.14135

6. Shazeer (2017) — Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
https://arxiv.org/abs/1701.06538

7. Fedus et al. (2022) — Switch Transformers
https://arxiv.org/abs/2101.03961

## Open model lifecycle

8. Touvron et al. (2023) — LLaMA
https://arxiv.org/abs/2302.13971

9. Touvron et al. (2023) — Llama 2
https://arxiv.org/abs/2307.09288

10. Grattafiori et al. (2024) — The Llama 3 Herd of Models
https://arxiv.org/abs/2407.21783

11. Groeneveld et al. (2024) — OLMo
https://arxiv.org/abs/2402.00838

12. Soldaini et al. (2024) — Dolma
https://arxiv.org/abs/2402.00159

13. Penedo et al. (2024) — FineWeb
https://arxiv.org/abs/2406.17557

## Post-training

14. Ouyang et al. (2022) — Training language models to follow instructions with human feedback
https://arxiv.org/abs/2203.02155

15. Hu et al. (2021) — LoRA
https://arxiv.org/abs/2106.09685

16. Dettmers et al. (2023) — QLoRA
https://arxiv.org/abs/2305.14314

17. Rafailov et al. (2023) — Direct Preference Optimization
https://arxiv.org/abs/2305.18290

## Research method

For every paper answer:
- What problem was unsolved?
- What is the smallest implementation that captures the core idea?
- What experiment actually supports the claim?
- What baseline is appropriate?
- What does the paper not establish?
- Which assumption is most fragile?
- What would a reproduction cost?
- What new experiment would be publishable?

## Reproduction priority

The best early reproduction targets are:
1. tokenizer behavior;
2. attention and masking;
3. scaling-law fit;
4. data filtering/dedup;
5. SFT;
6. LoRA/QLoRA;
7. DPO;
8. distributed training measurements.
