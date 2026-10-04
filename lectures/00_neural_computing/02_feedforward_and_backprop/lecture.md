# Course 1 · Chapter 2 — Feedforward Networks and Backpropagation

**Course:** Deep Learn\\ing & Neural Comput\\ing Foundations  
**Lab:** [Executable laboratory](./lab.ipynb)

## 1. The problem: one neuron is not enough

Chapter 1 showed that a s\\ingle neuron can learn a l\\inear boundary. Real problems are rarely that simple.

Suppose we want to learn XOR:

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No s\\ingle l\\ine can solve it.

A multilayer network can:

$$
h=\\phi(W_1x+b_1)
$$

followed by

$$
\\hat{y}=g(W_2h+b_2).
$$

The hidden layer creates an \\intermediate representation. The output layer reads that representation.

The key question of this chapter is:

> **If the f\\inal error depends on thousands or millions of parameters, how do we know how to chan\\ge each parameter?**

That is the backpropagation problem.

## 2. Forward propagation

Consider a t\\iny network:

$$
x ightarrow z_1 ightarrow h ightarrow z_2 ightarrow \\hat{y}.
$$

Let

$$
z_1=W_1x+b_1
$$

and

$$
h=\\sigma(z_1).
$$

Then

$$
z_2=W_2h+b_2
$$

and for b\\inary classification,

$$
\\hat{y}=\\sigma(z_2).
$$

The forward pass is simply function composition.

For a concrete scalar example, suppose

$$
x=2,\\quad W_1=1.5,\\quad b_1=-1,
$$

so

$$
z_1=1.5(2)-1=2.
$$

Us\\ing the sigmoid,

$$
h=\\\\frac{1}{1+e^{-2}}approx0.881.
$$

Suppose

$$
W_2=2,\\quad b_2=-1,
$$

then

$$
z_2=2(0.881)-1=0.762.
$$

and

$$
\\hat{y}approx0.682.
$$

A neural network is therefore not mysterious dur\\ing \\inference. It is a sequence of ord\\inary mathematical operations.

## 3. Why nonl\\inear activation matters

If

$$
h=W_1x+b_1
$$

and

$$
\\hat{y}=W_2h+b_2,
$$

then:

$$
\\hat{y}=W_2W_1x+W_2b_1+b_2.
$$

The entire network is still one l\\inear function.

A nonl\\inear activation such as sigmoid, tanh, or ReLU prevents this collapse.

For ReLU:

$$
operatorname{ReLU}(x)=max(0,x).
$$

Its simplicity is one reason it became so useful \\in deep networks.

## 4. Loss turns prediction \\into an optimization problem

Suppose the tar\\get is $y=1$ and the model predicts $\\hat{y}=0.682$.

For b\\inary cross-entropy:

$$
L=-[ylog\\hat{y}+(1-y)log(1-\\hat{y})].
$$

Because $y=1$,

$$
L=-log(0.682)approx0.383.
$$

Now we have a scalar quantity that tells us how undesirable the prediction was.

Tra\\in\\ing asks:

$$
m\\in_\\th\\eta L(\\th\\eta)
$$

where $\\th\\eta$ represents every tra\\inable parameter.

## 5. The cha\\in rule is the eng\\ine of backpropagation

Consider:

$$
L ightarrow \\hat{y} ightarrow z_2 ightarrow h ightarrow z_1 ightarrow W_1.
$$

The effect of $W_1$ on the f\\inal loss is obta\\ined with the cha\\in rule:

$$
\\\\frac{\\partial L}{\\partial W_1}
=
\\\\frac{\\partial L}{\\partial \\hat{y}}
\\\\frac{\\partial \\hat{y}}{\\partial z_2}
\\\\frac{\\partial z_2}{\\partial h}
\\\\frac{\\partial h}{\\partial z_1}
\\\\frac{\\partial z_1}{\\partial W_1}.
$$

This is backpropagation.

It is not a separate k\\ind of mathematics. It is an efficient organization of repeated applications of the cha\\in rule.

## 6. A useful mental model: credit assignment

Imag\\ine the f\\inal prediction is wrong.

Which parameter deserves blame?

Backpropagation sends \\information about the error backward through the computation graph.

Parameters that had a stron\\ger effect on the loss receive lar\\ger gradients.

So:

> **Backpropagation is a credit-assignment mechanism for differentiable computation.**

That perspective rema\\ins useful for Transformers, diffusion models, and multimodal networks.

## 7. Gradient descent

Once we have a gradient,

$$

abla_\\th\\eta L,
$$

we update:

$$
\\th\\eta_{new}=\\th\\eta_{old}-\\eta
abla_\\th\\eta L.
$$

The negative sign moves us approximately downhill.

If $\\eta$ is too small, learn\\ing can be pa\\infully slow.

If it is too lar\\ge, updates can overshoot or become unstable.

This gives us the first major optimization experiment.

## 8. Batch tra\\in\\ing chan\\ges the estimate

A s\\ingle example gives a noisy gradient.

For a m\\ini-batch $B$:

$$

abla_\\th\\eta L_B=
\\\\frac{1}{|B|}
sum_{i\\in B}
abla_\\th\\eta L_i.
$$

Increas\\ing batch size often makes the gradient estimate less noisy, but it chan\\ges memory requirements and optimization behavior.

There is no universally best batch size.

The right question is:

> What batch size gives the desired optimization behavior under the available memory and throughput bud\\get?

## 9. Memorization versus \\generalization

A model can drive tra\\in\\ing error almost to zero and still fail on unseen data.

Consider three experiments:

1. tra\\in on the orig\\inal labels;
2. tra\\in on shuffled labels;
3. evaluate on held-out examples.

If a sufficiently lar\\ge network can memorize shuffled labels, that demonstrates someth\\ing important:

> **Low tra\\in\\ing loss does not prove that the model discovered the structure we care about.**

Generalization is therefore an empirical property, not a guarantee from optimization.

## 10. Worked debugg\\ing example

Suppose:

| Run | Tra\\in accuracy | Validation accuracy |
|---|---:|---:|
| small model | 91% | 89% |
| lar\\ge model | 100% | 88% |

The lar\\ge model optimized the tra\\in\\ing set better but \\generalized worse.

Possible explanations \\include:

- overfitt\\ing;
- \\insufficient data;
- optimization differences;
- distribution mismatch;
- leaka\\ge \\in the evaluation design.

Do not automatically label it “overfitt\\ing.” Run an experiment that dist\\inguishes the hypotheses.

## 11. Real-world connection

Feedforward networks are used when the \\input can be represented as a fixed or structured feature vector:

- tabular prediction;
- risk scor\\ing;
- anomaly detection;
- sensor classification;
- learned embedd\\ings and projection heads.

They also provide the conceptual build\\ing blocks of deeper architectures.

CNNs add spatial structure. RNNs add recurrent state. Transformers add learned \\interactions across positions.

## 12. Laboratory

Before runn\\ing the notebook, predict:

- how the loss should chan\\ge when the learn\\ing rate \\increases;
- what happens when the labels are shuffled;
- how depth affects parameter count;
- whether normalization chan\\ges optimization stability.

Then:

1. implement a two-layer network from scratch;
2. verify your gradients numerically;
3. tra\\in the same task with autograd;
4. compare optimizers;
5. perform a width/depth \\intervention;
6. run a shuffled-label control;
7. \\inspect \\individual errors.

### Numerical gradient check

For parameter $\\th\\eta$:

$$
\\\\frac{\\partial L}{\\partial\\th\\eta}
approx
\\\\frac{L(\\th\\eta+epsilon)-L(\\th\\eta-epsilon)}{2epsilon}.
$$

Compare this f\\inite-difference estimate with the analytic gradient.

This is one of the most useful debugg\\ing techniques \\in deep-learn\\ing implementation.

## 13. Common misconceptions

**“Backpropagation updates the weights.”**  
Not exactly. Backpropagation computes gradients. The optimizer uses those gradients to update parameters.

**“A big\\ger model is always better.”**  
A big\\ger model \\increases capacity but can also \\increase cost, \\instability, or memorization.

**“Tra\\in\\ing accuracy proves learn\\ing.”**  
It proves the model can fit the tra\\in\\ing examples. Generalization requires held-out evidence.

**“The learn\\ing rate is just a tun\\ing d\\etail.”**  
It determ\\ines the scale of parameter updates and can completely chan\\ge whether optimization succeeds.

## 14. Research extension

Choose one:

- width at fixed parameter bud\\get;
- depth at fixed parameter bud\\get;
- optimizer at fixed compute;
- batch size at fixed token/example bud\\get;
- \\initialization under controlled seeds;
- regularization under fixed architecture.

State a hypothesis **before** runn\\ing the experiment.

## Mastery questions

1. Why do we need nonl\\inear activations?
2. What does the cha\\in rule have to do with backpropagation?
3. What does a gradient tell an optimizer?
4. Why can a model memorize shuffled labels?
5. Why must tra\\in\\ing and validation data be separated?
6. What does a numerical gradient check test?

### Answers

1. Without them, stacked l\\inear layers collapse \\into one l\\inear transformation.
2. Backpropagation efficiently applies the cha\\in rule through the computation graph.
3. The local direction and magnitude \\in which the loss chan\\ges with respect to parameters.
4. A sufficiently expressive model can memorize arbitrary tra\\in\\ing associations.
5. Otherwise we cannot reliably estimate performance on unseen data.
6. Whether the implemented analytic gradient agrees with an \\independent numerical approximation.

---




## Laboratory — run this experiment end to end

**[Open the executable lab notebook](./lab.ipynb)**

The notebook is part of this chapter, not optional homework. Work through it in order: **predict → establish baseline → run → change one factor → measure → inspect failures → produce the results table → write the conclusion**. The final cells include an answer key and a research extension.

<div align="center">

[← Previous](../01_neural_computing_foundations/lecture.md) · [Course 1 home](../README.md) · [Next →](../03_competitive_learning_and_som/lecture.md)

</div>
