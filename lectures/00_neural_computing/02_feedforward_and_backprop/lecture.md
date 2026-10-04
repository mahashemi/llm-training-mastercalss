
# Course 1 · Chapter — Feedforward Networks and Backpropagation

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the executable laboratory](./lab.ipynb)

## Why this chapter exists

A single neuron can learn a simple boundary. But real problems often require several stages of computation.

The central question is:

> **If the final prediction is wrong, how do we know which weight should change, in which direction, and by how much?**

That is the problem of **backpropagation**.

We will build the idea from a tiny network, with actual numbers, before relying on automatic differentiation.

## 1. A problem that needs more than one neuron

Consider XOR:

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No single straight line can separate the two classes.

A multilayer network can create intermediate features:

$$
h=\phi(W_1x+b_1)
$$

and then use them:

$$
\hat y=g(W_2h+b_2).
$$

Before reading the equations, understand the story:

**inputs → first computation → hidden representation → second computation → prediction.**

The hidden representation $h$ is simply a new set of numbers computed from the original input. It gives later layers a more useful representation of the problem.

## 2. Forward propagation

Consider one tiny network:

$$
x\r\rightarrow z_1\r\rightarrow h\r\rightarrow z_2\r\rightarrow\hat y.
$$

The arrow means “the output of one computation becomes the input to the next.”

Let

$$
z_1=W_1x+b_1.
$$

Then apply an activation:

$$
h=\sigma(z_1).
$$

Then another linear computation:

$$
z_2=W_2h+b_2.
$$

For binary classification, use a sigmoid at the output:

$$
\hat y=\sigma(z_2).
$$

The sigmoid is

$$
\sigma(a)=\\frac{1}{1+e^{-a}}.
$$

It turns any real number into a value between 0 and 1, which we can interpret as a probability-like score.

### Work through the numbers

Suppose

$$
x=2,\quad W_1=1.5,\quad b_1=-1.
$$

Then

$$
z_1=(1.5)(2)-1=2.
$$

Therefore

$$
h=\\frac{1}{1+e^{-2}}\approx0.881.
$$

Now let

$$
W_2=2,\quad b_2=-1.
$$

Then

$$
z_2=(2)(0.881)-1=0.762.
$$

Finally,

$$
\hat y=\\frac{1}{1+e^{-0.762}}\approx0.682.
$$

We have just performed a complete forward pass with ordinary arithmetic.

## 3. Why nonlinear activation matters

Suppose there were no activation:

$$
h=W_1x+b_1
$$

and

$$
\hat y=W_2h+b_2.
$$

Substitute the first equation into the second:

$$
\hat y
=
W_2(W_1x+b_1)+b_2.
$$

Rearranging gives

$$
\hat y=(W_2W_1)x+(W_2b_1+b_2).
$$

That is still a linear function of $x$.

So stacking linear layers without nonlinearities does not give us the expressive power we want.

A common activation is ReLU:

$$
\\operatorname{ReLU}(a)=\max(0,a).
$$

It keeps positive values and changes negative values to zero.

## 4. Loss: turning a prediction into a number we can optimize

Suppose the correct target is

$$
y=1
$$

and the model predicted

$$
\hat y=0.682.
$$

Binary cross-entropy is

$$
L=
-\left[
y\log(\hat y)
+
(1-y)\log(1-\hat y)
\right].
$$

For $y=1$, this becomes

$$
L=-\log(0.682)\approx0.383.
$$

The important conceptual step is:

> **The loss converts “the model made this prediction” into “here is how undesirable that prediction was.”**

Training can now ask how to change the parameters so that the loss becomes smaller.

## 5. What is a parameter?

A parameter is simply a number the model is allowed to learn.

For this network, examples are:

$$
W_1,\quad b_1,\quad W_2,\quad b_2.
$$

The model starts with some values, usually chosen by an initialization procedure.

Training repeatedly changes these values.

So when we say:

> “The model learned a useful representation,”

we ultimately mean:

> **The training process changed its parameters so that the computation behaves differently on future inputs.**

## 6. The chain rule: the idea behind backpropagation

Suppose the loss depends on the prediction, the prediction depends on $z_2$, $z_2$ depends on $h$, and $h$ depends on $z_1$.

The dependency chain is:

$$
W_1
\r\rightarrow z_1
\r\rightarrow h
\r\rightarrow z_2
\r\rightarrow \hat y
\r\rightarrow L.
$$

The chain rule says that the total effect of changing $W_1$ can be found by multiplying the local effects along the path:

$$
\\frac{\partial L}{\partial W_1}
=
\\frac{\partial L}{\partial\hat y}
\\frac{\partial\hat y}{\partial z_2}
\\frac{\partial z_2}{\partial h}
\\frac{\partial h}{\partial z_1}
\\frac{\partial z_1}{\partial W_1}.
$$

### Read the equation in English

Do not memorize the symbols first.

Read it as:

> **How much does $W_1$ affect $L$?**

Start at $W_1$ and ask:

1. If I change $W_1$, how much does $z_1$ change?
2. If $z_1$ changes, how much does $h$ change?
3. If $h$ changes, how much does $z_2$ change?
4. If $z_2$ changes, how much does $\hat y$ change?
5. If $\hat y$ changes, how much does the loss change?

Multiplying those local sensitivities gives the overall sensitivity.

That is the heart of backpropagation.

## 7. A tiny derivative calculation

For

$$
z_1=W_1x+b_1,
$$

the derivative with respect to $W_1$ is

$$
\\frac{\partial z_1}{\partial W_1}=x.
$$

Why?

Because if

$$
z_1=W_1x+b_1,
$$

then changing $W_1$ by a small amount $\Delta W_1$ changes $z_1$ by approximately

$$
\Delta z_1\approx x\,\Delta W_1.
$$

So $x$ tells us how sensitive this computation is to the weight.

This is what a derivative means: **local sensitivity**.

## 8. From gradients to parameter updates

Once backpropagation has calculated a gradient, an optimizer can use it.

For one parameter $\theta$:

$$
\theta_{\text{new}}
=
\theta_{\text{old}}
-
\eta
\\frac{\partial L}{\partial\theta}.
$$

Here:

- $\theta$ means “the particular parameter we are updating”;
- $\frac{\partial L}{\partial\theta}$ says how the loss changes if that parameter changes;
- $\eta$ is the learning rate, the size of our step;
- the minus sign says “move against the slope.”

For many parameters, we write the same idea compactly as

$$
\theta_{\text{new}}
=
\theta_{\text{old}}
-
\eta\n\nabla_\theta L.
$$

Here $\nabla_\theta L$ is just a vector containing all those individual partial derivatives.

### Tiny numerical example

Suppose

$$
\theta_{\text{old}}=2,
\qquad
\\frac{\partial L}{\partial\theta}=3,
\qquad
\eta=0.1.
$$

Then

$$
\theta_{\text{new}}
=
2-(0.1)(3)
=
1.7.
$$

If the gradient were $-3$ instead:

$$
\theta_{\text{new}}
=
2-(0.1)(-3)
=
2.3.
$$

The gradient tells us the direction; the learning rate tells us how far to move.

## 9. Backpropagation is not gradient descent

These two ideas are often incorrectly treated as one thing.

**Backpropagation** calculates gradients efficiently by applying the chain rule backward through the computation graph.

**Gradient descent** uses those gradients to change the parameters.

So the training loop is:

**forward pass → loss → backpropagation → gradients → optimizer update → repeat.**

This distinction becomes essential when we later replace basic gradient descent with Adam, AdamW, momentum methods, or other optimizers.

## 10. Mini-batches

A single example can give a noisy estimate of the direction that reduces loss.

For a mini-batch $B$, the average loss can be written as

$$
L_B=
\\frac{1}{|B|}
\sum_{i\in B}L_i.
$$

The corresponding gradient is the average of the example gradients:

$$
\n\nabla_\theta L_B
=
\\frac{1}{|B|}
\sum_{i\in B}
\n\nabla_\theta L_i.
$$

Larger batches often make this estimate less noisy, but they also require more memory and can change optimization behavior.

The engineering question is not “What is the biggest batch?”

It is:

> **What batch size gives useful optimization behavior within our memory and throughput budget?**

## 11. Memorization versus generalization

A network can make training loss extremely small and still perform poorly on unseen examples.

For example:

| Run | Training accuracy | Validation accuracy |
|---|---:|---:|
| smaller model | 91% | 89% |
| larger model | 100% | 88% |

The larger model fit the training data better but did not generalize better.

Possible explanations include overfitting, insufficient data, distribution mismatch, or optimization differences.

Do not choose the explanation first. Design an experiment that distinguishes them.

## 12. Numerical gradient checking

One of the best debugging tools in deep learning is to compare two independent calculations.

For a parameter $\theta$, approximate the derivative using a tiny perturbation $\epsilon$:

$$
\\frac{\partial L}{\partial\theta}
\approx
\\frac{
L(\theta+\epsilon)-L(\theta-\epsilon)
}{
2\epsilon
}.
$$

Conceptually:

1. move the parameter slightly upward;
2. measure the loss;
3. move it slightly downward;
4. measure the loss again;
5. compare the change with the gradient produced by backpropagation.

If the two agree closely, your derivative implementation is probably correct.

If they disagree substantially, investigate the implementation before training a larger model.

## 13. Real-world connection

Feedforward networks are useful for tabular prediction, risk scoring, anomaly detection, sensor classification, and projection heads.

More importantly, the same ideas appear inside modern systems:

**parameters → forward computation → loss → gradients → update.**

CNNs change the computation to exploit spatial structure. RNNs introduce recurrent state. Transformers introduce attention.

The training logic remains recognizable.

## 14. Laboratory

Before running the notebook, predict:

- what happens when the learning rate changes;
- whether the analytic and numerical gradients agree;
- how width changes parameter count;
- what shuffled labels do to validation performance.

Then:

1. implement a two-layer network from scratch;
2. verify gradients numerically;
3. train the same task with autograd;
4. compare optimization settings;
5. change width or depth;
6. run a shuffled-label control;
7. inspect individual errors.

## 15. Failure analysis

Deliberately try:

- an excessively large learning rate;
- a broken gradient;
- shuffled labels;
- a train/validation split with leakage.

For every failure, identify whether the problem is in:

**data → model → gradient → optimizer → evaluation.**

## 16. Research extension

Choose one controlled comparison:

- width at fixed parameter budget;
- depth at fixed parameter budget;
- optimizer at fixed compute;
- batch size at fixed example budget;
- initialization under controlled seeds;
- regularization under fixed architecture.

State the hypothesis before running the experiment.

## Mastery questions

1. What does a derivative mean conceptually?
2. Why does the chain rule matter?
3. What does backpropagation calculate?
4. What does gradient descent do with those gradients?
5. What does the learning rate control?
6. Why can a large model have higher training accuracy but lower validation accuracy?
7. What does a numerical gradient check test?

### Answers

1. A local sensitivity: how much one quantity changes when another changes.
2. It lets us combine local sensitivities along a computation chain.
3. Gradients of the loss with respect to model parameters.
4. It changes parameters in the direction intended to reduce the loss.
5. The size of the parameter update.
6. Greater capacity can fit training-specific patterns without improving generalization.
7. It compares an independent finite-difference estimate with the analytic/backpropagated gradient.

## Laboratory — run the experiment end to end

**[Open the executable laboratory](./lab.ipynb)**

Follow:

**predict → baseline → controlled change → measure → inspect failure → explain → propose next experiment.**

## Navigation

[← Previous](../01_neural_computing_foundations/lecture.md) · [Course 1 home](../README.md) · [Next →](../03_competitive_learning_and_som/lecture.md)
