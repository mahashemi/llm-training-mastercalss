# Course 1 · Chapter 1 — Neural Computation: What Does It Mean to Learn?

**Course:** Deep Learn\\ing & Neural Comput\\ing Foundations  
**Lab:** [Executable laboratory](./lab.ipynb)

## 1. Start with a problem, not a neural network

Suppose a hospital has two measurements for each patient and wants to classify whether a simple screen\\ing rule is positive.

We have observations

$$
x = [x_1,x_2]
$$

and a b\\inary tar\\get

$$
y \\\in {0,1}.
$$

A useful first question is not “Which neural network should we use?”

It is:

> **Can we learn a function that maps measurements to decisions from examples?**

That is the central idea beh\\ind neural computation.

A learn\\ing algorithm receives examples

$$
(x^{(1)},y^{(1)}),\ldots,(x^{(n)},y^{(n)})
$$

and searches for parameters that make its predictions agree with the observed tar\\gets.

The important word is **parameters**. Instead of manually writ\\ing every decision rule, we specify a family of functions and let data determ\\ine the useful parameters.

---

## 2. The simplest neuron

A l\\inear neuron computes

$$
z = w_1x_1+w_2x_2+b.
$$

In vector notation:

$$
z = w^\\top x+b.
$$

For classification, a perceptron turns this score \\into a decision:

$$
\\hat{y} =
\\beg\\in{cases}
1 & z \\ge 0\
0 & z < 0.
end{cases}
$$

Geometrically, the equation

$$
w^\\top x+b=0
$$

is a l\\ine \\in two dimensions, a plane \\in three dimensions, and a hyperplane \\in higher dimensions.

So the first neural model is really learn\\ing a **decision boundary**.

### Worked example

Suppose

$$
w=[2,-1], q\\quad b=-0.5.
$$

For a patient with

$$
x=[1,0],
$$

we \\get

$$
z=2(1)-1(0)-0.5=1.5,
$$

so the prediction is 1.

For

$$
x=[0,1],
$$

we \\get

$$
z=-1.5,
$$

so the prediction is 0.

The neuron has not “understood medic\\ine.” It has learned a \\geometric separation \\in the feature space.

That dist\\inction matters throughout deep learn\\ing.

---

## 3. Why one neuron is not enough

A s\\ingle l\\inear boundary cannot represent every useful decision.

Consider XOR:

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No s\\ingle straight l\\ine separates the positive examples from the negative examples.

This gives us a fundamental motivation for multilayer networks:

> **If one simple function cannot express the required mapp\\ing, compose several simple functions.**

That idea eventually becomes the deep neural network.

---

## 4. Perceptron learn\\ing

The perceptron does not need a closed-form solution. It can update its parameters when it makes a mistake.

For a misclassified example, a simple update is

$$
w \\leftarrow w+\\eta(y-\\hat{y})x
$$

and

$$
b \\leftarrow b+\\eta(y-\\hat{y}),
$$

where $\\eta$ is the learn\\ing rate.

If the prediction is correct, the update is zero.

### Why this matters

The update demonstrates an idea that survives \\into modern tra\\in\\ing:

1. make a prediction;
2. compare it with the tar\\get;
3. measure an error;
4. chan\\ge parameters \\in a direction \\intended to reduce future error.

Modern neural networks use differentiable losses and gradient-based optimization, but this loop is already visible here.

---

## 5. Adal\\ine: replac\\ing the hard decision with a useful learn\\ing signal

The perceptron updates accord\\ing to whether the f\\inal classification is correct.

Adal\\ine \\instead tra\\ins the **cont\\inuous score**.

Let

$$
\\hat{y} = w^\\top x+b.
$$

Us\\ing mean squared error,

$$
L=\\\\frac{1}{n}sum_i(\\hat{y}_i-y_i)^2.
$$

For one example,

$$
L=(w^\\top x+b-y)^2.
$$

The gradient with respect to $w$ is

$$

abla_w L=2(w^\\top x+b-y)x.
$$

Gradient descent then gives

$$
w\\leftarrow w-\\eta
abla_w L.
$$

This is our first important brid\\ge to backpropagation:

> **Tra\\in\\ing is optimization of a differentiable objective with respect to parameters.**

---

## 6. From one neuron to a network

A layer with several neurons computes

$$
h=\\phi(Wx+b),
$$

where:

- $W$ conta\\ins many learned weights;
- $b$ conta\\ins biases;
- $\\phi$ is a nonl\\inear activation function.

Why is the nonl\\inearity essential?

Without it, two consecutive l\\inear layers collapse \\into one:

$$
W_2(W_1x+b_1)+b_2
=
(W_2W_1)x+(W_2b_1+b_2).
$$

So stack\\ing l\\inear layers without nonl\\inearities does **not** create a \\genu\\inely deeper function class.

With nonl\\inearities, composition becomes much more expressive:

$$
f(x)=W_2\\phi(W_1x+b_1)+b_2.
$$

This is the conceptual birth of a multilayer perceptron.

---

## 7. What does “learn\\ing a representation” mean?

Imag\\ine the orig\\inal features cannot be separated by a straight l\\ine.

A hidden layer transforms

$$
x 
ightarrow h.
$$

The goal is not merely to create more numbers. It is to create a representation \\in which the desired relationship becomes easier for later layers to model.

This idea will return \\in:

- CNN feature maps;
- autoencoder latent spaces;
- recurrent hidden states;
- Transformer residual streams;
- langua\\ge-model embedd\\ings.

A useful mental model is:

> **Each layer chan\\ges the coord\\inate system \\in which the next layer sees the problem.**

---

## 8. Real-world connection

The same mathematical mechanism appears \\in very different systems:

- fraud detection learns boundaries \\in transaction features;
- vision models learn \\increas\\ingly structured ima\\ge representations;
- speech models transform acoustic patterns \\into l\\inguistic representations;
- langua\\ge models transform token representations through many contextual layers.

The doma\\in chan\\ges. The learn\\ing loop rema\\ins recognizable:

**data → computation → prediction → loss → gradient → parameter update.**

---

## 9. What the model can and cannot learn

A model can only learn from the \\information and supervision available to it.

If the data conta\\ins a strong shortcut, the model may learn the shortcut.

If a feature is absent, no optimizer can recover \\information that was never represented.

If the tra\\in\\ing distribution differs from deployment, a high tra\\in\\ing score can coexist with poor real-world behavior.

Therefore:

> **A tra\\ined model is not automatically a causal model, a truthful model, or a robust model.**

This is why later chapters will study \\generalization, distribution shift, evaluation, and failure analysis.

---

## 10. Laboratory: predict before you run

Open the notebook and first predict:

1. whether the dataset is l\\inearly separable;
2. how the learned boundary should move when the learn\\ing rate \\increases;
3. what should happen when labels are shuffled;
4. whether add\\ing nonl\\inear hidden units should solve XOR.

Then run:

- a from-scratch perceptron;
- Adal\\ine;
- a small framework implementation;
- a controlled learn\\ing-rate experiment;
- a shuffled-label experiment.

Record the prediction **before** the result.

That turns a notebook from a calculator \\into an experiment.

---

## 11. Failure analysis

Deliberately create:

- a non-l\\inearly separable dataset;
- noisy labels;
- badly scaled features;
- an excessively lar\\ge learn\\ing rate.

For each failure, answer:

**What failed: representation, optimization, data, or evaluation?**

Do not write “the model performed badly.”

Name the mechanism.

---

## 12. Connection to the next chapter

A s\\ingle neuron gives us a l\\inear decision surface.

Multiple nonl\\inear neurons give us compositional representations.

But now we face a harder question:

> **How do we efficiently calculate how every weight contributed to the f\\inal error?**

That question leads to **backpropagation**.

## Mastery questions

1. Why is a perceptron limited?
2. Why does a hidden-layer nonl\\inearity matter?
3. Why can two l\\inear layers collapse \\into one?
4. What is a parameter?
5. What is the difference between a prediction and a loss?
6. Why does feature scal\\ing affect optimization?
7. What would a shuffled-label experiment tell us?

### Answers

1. A s\\ingle perceptron produces one l\\inear decision boundary.
2. It allows composition of \\genu\\inely nonl\\inear functions.
3. The composition of l\\inear functions is still l\\inear.
4. A learned quantity, such as a weight or bias, that determ\\ines the model's computation.
5. A prediction is the model output; a loss quantifies disagreement with the tar\\get.
6. Poorly scaled dimensions can make optimization poorly conditioned.
7. It tests how much performance depends on learnable structure versus memorization/capacity.

---




## Laboratory — run this experiment end to end

**[Open the executable lab notebook](./lab.ipynb)**

The notebook is part of this chapter, not optional homework. Work through it in order: **predict → establish baseline → run → change one factor → measure → inspect failures → produce the results table → write the conclusion**. The final cells include an answer key and a research extension.

<div align="center">

[← Course 1 home](../README.md) · [Course 1 home](../README.md) · [Next →](../02_feedforward_and_backprop/lecture.md)

</div>
