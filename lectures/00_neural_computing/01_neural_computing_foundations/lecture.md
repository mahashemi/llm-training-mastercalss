# Course 1 · Chapter 1 — Neural Computation: What Does It Mean to Learn?

**Course:** Deep Learning & Neural Computing Foundations  
**Lab:** [Executable laboratory](./lab.ipynb)

## 1. Start with a problem, not a neural network

Suppose a hospital has two measurements for each patient and wants to classify whether a simple screening rule is positive.

We have observations

$$
x = [x_1,x_2]
$$

and a binary target

$$
y \in {0,1}.
$$

A useful first question is not “Which neural network should we use?”

It is:

> **Can we learn a function that maps measurements to decisions from examples?**

That is the central idea behind neural computation.

A learning algorithm receives examples

$$
(x^{(1)},y^{(1)}),\ldots,(x^{(n)},y^{(n)})
$$

and searches for parameters that make its predictions agree with the observed targets.

The important word is **parameters**. Instead of manually writing every decision rule, we specify a family of functions and let data determine the useful parameters.

---

## 2. The simplest neuron

A linear neuron computes

$$
z = w_1x_1+w_2x_2+b.
$$

In vector notation:

$$
z = w^	op x+b.
$$

For classification, a perceptron turns this score into a decision:

$$
hat y =
egin{cases}
1 & z ge 0\
0 & z < 0.
end{cases}
$$

Geometrically, the equation

$$
w^	op x+b=0
$$

is a line in two dimensions, a plane in three dimensions, and a hyperplane in higher dimensions.

So the first neural model is really learning a **decision boundary**.

### Worked example

Suppose

$$
w=[2,-1], qquad b=-0.5.
$$

For a patient with

$$
x=[1,0],
$$

we get

$$
z=2(1)-1(0)-0.5=1.5,
$$

so the prediction is 1.

For

$$
x=[0,1],
$$

we get

$$
z=-1.5,
$$

so the prediction is 0.

The neuron has not “understood medicine.” It has learned a geometric separation in the feature space.

That distinction matters throughout deep learning.

---

## 3. Why one neuron is not enough

A single linear boundary cannot represent every useful decision.

Consider XOR:

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No single straight line separates the positive examples from the negative examples.

This gives us a fundamental motivation for multilayer networks:

> **If one simple function cannot express the required mapping, compose several simple functions.**

That idea eventually becomes the deep neural network.

---

## 4. Perceptron learning

The perceptron does not need a closed-form solution. It can update its parameters when it makes a mistake.

For a misclassified example, a simple update is

$$
w leftarrow w+eta(y-hat y)x
$$

and

$$
b leftarrow b+eta(y-hat y),
$$

where $eta$ is the learning rate.

If the prediction is correct, the update is zero.

### Why this matters

The update demonstrates an idea that survives into modern training:

1. make a prediction;
2. compare it with the target;
3. measure an error;
4. change parameters in a direction intended to reduce future error.

Modern neural networks use differentiable losses and gradient-based optimization, but this loop is already visible here.

---

## 5. Adaline: replacing the hard decision with a useful learning signal

The perceptron updates according to whether the final classification is correct.

Adaline instead trains the **continuous score**.

Let

$$
hat y = w^	op x+b.
$$

Using mean squared error,

$$
L=rac{1}{n}sum_i(hat y_i-y_i)^2.
$$

For one example,

$$
L=(w^	op x+b-y)^2.
$$

The gradient with respect to $w$ is

$$

abla_w L=2(w^	op x+b-y)x.
$$

Gradient descent then gives

$$
wleftarrow w-eta
abla_w L.
$$

This is our first important bridge to backpropagation:

> **Training is optimization of a differentiable objective with respect to parameters.**

---

## 6. From one neuron to a network

A layer with several neurons computes

$$
h=phi(Wx+b),
$$

where:

- $W$ contains many learned weights;
- $b$ contains biases;
- $phi$ is a nonlinear activation function.

Why is the nonlinearity essential?

Without it, two consecutive linear layers collapse into one:

$$
W_2(W_1x+b_1)+b_2
=
(W_2W_1)x+(W_2b_1+b_2).
$$

So stacking linear layers without nonlinearities does **not** create a genuinely deeper function class.

With nonlinearities, composition becomes much more expressive:

$$
f(x)=W_2phi(W_1x+b_1)+b_2.
$$

This is the conceptual birth of a multilayer perceptron.

---

## 7. What does “learning a representation” mean?

Imagine the original features cannot be separated by a straight line.

A hidden layer transforms

$$
x 
ightarrow h.
$$

The goal is not merely to create more numbers. It is to create a representation in which the desired relationship becomes easier for later layers to model.

This idea will return in:

- CNN feature maps;
- autoencoder latent spaces;
- recurrent hidden states;
- Transformer residual streams;
- language-model embeddings.

A useful mental model is:

> **Each layer changes the coordinate system in which the next layer sees the problem.**

---

## 8. Real-world connection

The same mathematical mechanism appears in very different systems:

- fraud detection learns boundaries in transaction features;
- vision models learn increasingly structured image representations;
- speech models transform acoustic patterns into linguistic representations;
- language models transform token representations through many contextual layers.

The domain changes. The learning loop remains recognizable:

**data → computation → prediction → loss → gradient → parameter update.**

---

## 9. What the model can and cannot learn

A model can only learn from the information and supervision available to it.

If the data contains a strong shortcut, the model may learn the shortcut.

If a feature is absent, no optimizer can recover information that was never represented.

If the training distribution differs from deployment, a high training score can coexist with poor real-world behavior.

Therefore:

> **A trained model is not automatically a causal model, a truthful model, or a robust model.**

This is why later chapters will study generalization, distribution shift, evaluation, and failure analysis.

---

## 10. Laboratory: predict before you run

Open the notebook and first predict:

1. whether the dataset is linearly separable;
2. how the learned boundary should move when the learning rate increases;
3. what should happen when labels are shuffled;
4. whether adding nonlinear hidden units should solve XOR.

Then run:

- a from-scratch perceptron;
- Adaline;
- a small framework implementation;
- a controlled learning-rate experiment;
- a shuffled-label experiment.

Record the prediction **before** the result.

That turns a notebook from a calculator into an experiment.

---

## 11. Failure analysis

Deliberately create:

- a non-linearly separable dataset;
- noisy labels;
- badly scaled features;
- an excessively large learning rate.

For each failure, answer:

**What failed: representation, optimization, data, or evaluation?**

Do not write “the model performed badly.”

Name the mechanism.

---

## 12. Connection to the next chapter

A single neuron gives us a linear decision surface.

Multiple nonlinear neurons give us compositional representations.

But now we face a harder question:

> **How do we efficiently calculate how every weight contributed to the final error?**

That question leads to **backpropagation**.

## Mastery questions

1. Why is a perceptron limited?
2. Why does a hidden-layer nonlinearity matter?
3. Why can two linear layers collapse into one?
4. What is a parameter?
5. What is the difference between a prediction and a loss?
6. Why does feature scaling affect optimization?
7. What would a shuffled-label experiment tell us?

### Answers

1. A single perceptron produces one linear decision boundary.
2. It allows composition of genuinely nonlinear functions.
3. The composition of linear functions is still linear.
4. A learned quantity, such as a weight or bias, that determines the model's computation.
5. A prediction is the model output; a loss quantifies disagreement with the target.
6. Poorly scaled dimensions can make optimization poorly conditioned.
7. It tests how much performance depends on learnable structure versus memorization/capacity.

---

<div align="center">

[Course 1 home](../README.md) · [Next: Feedforward Networks + Backpropagation →](../02_feedforward_and_backprop/lecture.md)

</div>
