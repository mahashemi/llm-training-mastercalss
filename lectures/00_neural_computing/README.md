# Course 1 — Deep Learning & Neural Computing Foundations

A standalone 12-chapter deep-learning course. It teaches neural computation as a coherent subject and can be taken independently. It also serves as recommended preparation for Course 2 — LLM Engineering & Training.

## Units

1. Introduction to Neural Computing — perceptron, Adaline, history, applications.
2. Feedforward Networks — multilayer networks, memorization/generalization, backpropagation and training.
3. Competitive Learning and Self-Organizing Feature Maps — SOM and evolving SOM.
4. Convolutional Networks — CNNs, extensions, residual and dense networks.
5. Autoencoders — basic, regularized, sparse, denoising, stacked denoising and contractive.
6. Generative Models — VAE, GAN and diffusion.
7. Recurrent Networks — simple recurrence, LSTM and GRU.
8. Recurrent Architectures — Elman, Jordan, fully recurrent networks and forecasting.
9. Boltzmann Machines — RBM, contrastive divergence and deep belief networks.
10. Attention — attention types, Transformer, BERT and GPT.
11. Deep Reinforcement Learning — RL foundations and DQN.
12. Research Capstone — reproduce, intervene, ablate and write.

Every chapter follows **problem → intuition → worked example → mathematics → from-scratch implementation → framework implementation → real data → baseline → intervention → failure analysis → engineering decision → research question**. See the [Lecture Authoring Standard](../../docs/LECTURE_AUTHORING_STANDARD.md).

## Real-data anchors

Labs use real Hugging Face datasets including ylecun/mnist, farish07/banknote-authentication-dataset, Beothuk/uci-har-federated, tulipa762/electricity_load_diagrams, and stanfordnlp/imdb.

## Course outcome

A motivated learner accumulates methods, baselines, ablations, figures, error analyses, resource measurements and reproducibility records throughout the course. Completing the course does not guarantee publication; it teaches a defensible workflow for producing evidence strong enough to evaluate for publication.

## Labs

- [Labs 01–03](./labs_01_03.ipynb)
- [Labs 04–06](./labs_04_06.ipynb)
- [Labs 07–09](./labs_07_09.ipynb)
- [Labs 10–12 + publication capstone](./labs_10_12.ipynb)
