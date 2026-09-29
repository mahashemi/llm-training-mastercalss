# Book Table of Contents — LLM Trainer Masterclass

**76 chapters + 1 template**

This is the durable textbook layer. Chapters explain the mechanism, connect it to computation/resources, point to the relevant companion laboratory, and finish with failure analysis and an engineering/research decision.

## PRACTICAL TRAINING PATH

00. [The Open-Weight Training Path](../book/00_open_weight_training_path.md)

This chapter is the bridge from the conceptual textbook to actual checkpoint download, inference, SFT/PEFT, H100 adaptation, distributed training, and pretraining.

## LANGUAGE MODELS WITHOUT MAGIC

01. [A Language Model Is A Probability Model](../book/01_language_models_without_magic/01_a_language_model_is_a_probability_model.md)

## PART I

02. [Tokenization As A Modeling Decision](../book/02_part_i/02_tokenization_as_a_modeling_decision.md)
02. [Logits Softmax And Cross Entropy](../book/02_part_i/03_logits_softmax_and_cross_entropy.md)
02. [Embeddings And Representations](../book/02_part_i/04_embeddings_and_representations.md)
02. [Positional Information And Rope](../book/02_part_i/05_positional_information_and_rope.md)
02. [Residual Streams And Normalization](../book/02_part_i/06_residual_streams_and_normalization.md)
02. [Feed Forward Networks And Swiglu](../book/02_part_i/07_feed_forward_networks_and_swiglu.md)
02. [Causal Self Attention](../book/02_part_i/08_causal_self_attention.md)
02. [Autoregressive Training And Generation](../book/02_part_i/09_autoregressive_training_and_generation.md)
02. [Hyperparameters As A Coupled System](../book/02_part_i/10_hyperparameters_as_a_coupled_system.md)

## PART II AND III

03. [Multi Head Attention Shapes](../book/03_part_ii_and_iii/11_multi_head_attention_shapes.md)
03. [Gqa And Mqa](../book/03_part_ii_and_iii/12_gqa_and_mqa.md)
03. [Mixture Of Experts](../book/03_part_ii_and_iii/13_mixture_of_experts.md)
03. [Initialization And Optimization Stability](../book/03_part_ii_and_iii/14_initialization_and_optimization_stability.md)
03. [Optimizers Adamw And Schedules](../book/03_part_ii_and_iii/15_optimizers_adamw_and_schedules.md)
03. [Gradient Accumulation And Effective Batch Size](../book/03_part_ii_and_iii/16_gradient_accumulation_and_effective_batch_size.md)
03. [Pretraining Corpus Design](../book/03_part_ii_and_iii/17_pretraining_corpus_design.md)
03. [Document Filtering And Quality Models](../book/03_part_ii_and_iii/18_document_filtering_and_quality_models.md)
03. [Exact And Near Deduplication](../book/03_part_ii_and_iii/19_exact_and_near_deduplication.md)
03. [Data Mixing And Sampling](../book/03_part_ii_and_iii/20_data_mixing_and_sampling.md)

## PART IV

04. [Synthetic Data](../book/04_part_iv/21_synthetic_data.md)
04. [Contamination And Leakage](../book/04_part_iv/22_contamination_and_leakage.md)
04. [Data Pipelines As Distributed Systems](../book/04_part_iv/23_data_pipelines_as_distributed_systems.md)
04. [Tokenizer Training For A Target Language](../book/04_part_iv/24_tokenizer_training_for_a_target_language.md)
04. [Pretraining Run Design](../book/04_part_iv/25_pretraining_run_design.md)
04. [Continued Pretraining](../book/04_part_iv/26_continued_pretraining.md)
04. [Supervised Fine Tuning](../book/04_part_iv/27_supervised_fine_tuning.md)
04. [Full Fine Tuning](../book/04_part_iv/28_full_fine_tuning.md)
04. [Lora Fundamentals](../book/04_part_iv/29_lora_fundamentals.md)
04. [Qlora And Quantized Training](../book/04_part_iv/30_qlora_and_quantized_training.md)

## PART V

05. [Adapter Variants And Dora](../book/05_part_iv/31_adapter_variants_and_dora.md)
05. [Catastrophic Forgetting](../book/05_part_iv/32_catastrophic_forgetting.md)
05. [Instruction Data Design](../book/05_part_iv/33_instruction_data_design.md)
05. [Preference Data](../book/05_part_iv/34_preference_data.md)
05. [Rlhf Pipeline](../book/05_part_iv/35_rlhf_pipeline.md)
05. [Dpo Mechanics](../book/05_part_iv/36_dpo_mechanics.md)
05. [Distillation](../book/05_part_iv/37_distillation.md)
05. [Quantization](../book/05_part_iv/38_quantization.md)
05. [Checkpointing And Recovery](../book/05_part_iv/39_checkpointing_and_recovery.md)
05. [Pretraining At Scale](../book/05_part_iv/40_pretraining_at_scale.md)

## PART VI

06. [Validation Loss And Perplexity](../book/06_part_v/41_validation_loss_and_perplexity.md)
06. [Benchmark Design](../book/06_part_v/42_benchmark_design.md)
06. [Human Evaluation](../book/06_part_v/43_human_evaluation.md)
06. [Model As Judge Evaluation](../book/06_part_v/44_model_as_judge_evaluation.md)
06. [Error Taxonomies](../book/06_part_v/45_error_taxonomies.md)
06. [Ablation Studies](../book/06_part_v/46_ablation_studies.md)
06. [Statistical Thinking For Llm Evaluation](../book/06_part_v/47_statistical_thinking_for_llm_evaluation.md)
06. [Hallucination And Groundedness](../book/06_part_v/48_hallucination_and_groundedness.md)
06. [Robustness And Distribution Shift](../book/06_part_v/49_robustness_and_distribution_shift.md)
06. [Evaluation Release Engineering](../book/06_part_v/50_evaluation_release_engineering.md)

## PART VII

07. [Inference Graphs And Prefill](../book/07_part_vi_and_vii/51_inference_graphs_and_prefill.md)
07. [Kv Cache Memory](../book/07_part_vi_and_vii/52_kv_cache_memory.md)
07. [Serving With Vllm](../book/07_part_vi_and_vii/53_serving_with_vllm.md)
07. [Quantized Inference](../book/07_part_vi_and_vii/54_quantized_inference.md)
07. [Speculative Decoding](../book/07_part_vi_and_vii/55_speculative_decoding.md)
07. [Inference Economics](../book/07_part_vi_and_vii/56_inference_economics.md)
07. [Knowledge Problem Vs Behavior Problem](../book/07_part_vi_and_vii/57_knowledge_problem_vs_behavior_problem.md)
07. [Rag Architecture](../book/07_part_vi_and_vii/58_rag_architecture.md)
07. [Tool Use And Agents](../book/07_part_vi_and_vii/59_tool_use_and_agents.md)
07. [Api Economics And Tco](../book/07_part_vi_and_vii/60_api_economics_and_tco.md)

## PART VIII

08. [Api Privacy And Data Governance](../book/08_part_vii_and_viii/61_api_privacy_and_data_governance.md)
08. [When Fine Tuning Is Justified](../book/08_part_vii_and_viii/62_when_fine_tuning_is_justified.md)
08. [When Continued Pretraining Is Justified](../book/08_part_vii_and_viii/63_when_continued_pretraining_is_justified.md)
08. [When Training From Scratch Is Justified](../book/08_part_vii_and_viii/64_when_training_from_scratch_is_justified.md)
08. [National Language Strategy](../book/08_part_vii_and_viii/65_national_language_strategy.md)
08. [Low Resource Data Acquisition](../book/08_part_vii_and_viii/66_low_resource_data_acquisition.md)
08. [Team Design For Llm Programs](../book/08_part_vii_and_viii/67_team_design_for_llm_programs.md)
08. [Compute Procurement And Cluster Design](../book/08_part_vii_and_viii/68_compute_procurement_and_cluster_design.md)
08. [Scaling A Pilot Into A Program](../book/08_part_vii_and_viii/69_scaling_a_pilot_into_a_program.md)
08. [Risk Register And Kill Criteria](../book/08_part_vii_and_viii/70_risk_register_and_kill_criteria.md)

## PART IX

09. [National Model Architecture Choices](../book/09_part_viii_and_ix/71_national_model_architecture_choices.md)
09. [Training Data Governance](../book/09_part_viii_and_ix/72_training_data_governance.md)
09. [Evaluation For National And Multilingual Models](../book/09_part_viii_and_ix/73_evaluation_for_national_and_multilingual_models.md)
09. [The Technical Proposal](../book/09_part_viii_and_ix/74_the_technical_proposal.md)
09. [The Funding And Publication Package](../book/09_part_viii_and_ix/75_the_funding_and_publication_package.md)

## How to use the textbook

Read the chapter, make the prediction, run the linked primary laboratory where applicable, inspect a failure, and record the engineering decision and next experiment.

Some chapters deliberately share laboratories. See [BOOK_LAB_MAP.md](BOOK_LAB_MAP.md).

A sentence that says “before opening the notebook” must have a real notebook link immediately nearby. Chapters with analytical exercises and no executable lab say so explicitly.
