# Course 1 · Chapter 4 — Convolutional Networks, Residual Learning, and Dense Connections

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the executable laboratory](./lab.ipynb)

## Why this chapter exists

Images contain local structure: edges, corners, textures, and shapes. Convolution builds that prior directly into the model.

A convolution kernel is a small set of shared weights that scans an image. Residual connections then make deeper networks easier to optimize by giving information a shortcut path.

You will connect parameter sharing, receptive fields, residuals, and actual image accuracy.

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Start with the image problem: a detector for an edge should not need a completely different parameter for every pixel location. Convolution introduces a useful inductive bias: the same local detector can be reused across positions.

For a 1-D illustration, the output at position $i$ is a weighted sum of nearby input values:

$$
y_i=\sum_k w_k x_{i+k}.
$$

Here $x_{i+k}$ is an input value in the local window, $w_k$ is the learned weight applied to it, and the sum combines those weighted values into one output. In 2-D the same idea becomes a sliding kernel over height and width. A feature map therefore answers questions such as “where does this learned pattern occur?”

### Work out a convolution's output size

For one spatial dimension, the output size is

$$ N_{\mathrm{out}}=\left\lfloor\frac{N_{\mathrm{in}}+2P-K}{S}\right\rfloor+1, $$

where $N_{\mathrm{in}}$ is the input width (or height), $K$ is kernel size, $P$ is padding on each side, and $S$ is stride. The floor means “round down to the nearest whole number,” because a kernel cannot start at a fractional pixel position.

For a $28\times28$ image with a $3\times3$ kernel, stride $S=1$, and padding $P=1$,

$$ N_{\mathrm{out}}=\left\lfloor\frac{28+2(1)-3}{1}\right\rfloor+1=28. $$

So the feature map remains $28\times28$. If a $2\times2$ max-pooling layer then uses stride 2 with no padding, the spatial size becomes $14\times14$. Track height, width, and channels separately: a convolution with 16 filters produces 16 output channels.

### Count parameters rather than guessing

For a dense layer from 784 inputs to 64 units, there are $784\times64$ weights plus 64 biases, or 50,240 trainable parameters. A convolution with 16 filters, each of size $3\times3$ and one input channel, has $16(3\times3+1)=160$ trainable parameters. The kernel weights are reused at every image location; the number of locations affects computation, not the number of shared parameters.

Then explain depth: early layers can detect edges/textures, later layers can combine them into more complex patterns. Residual networks change the optimization problem by learning a residual:

$$
y=F(x)+x.
$$

Here $x$ is the incoming representation, $F(x)$ is the learned correction, and $y$ is the output. The shortcut carries $x$ directly to the addition, giving information and gradients a direct path. This identity addition requires $F(x)$ and $x$ to have the same shape. If channels or spatial dimensions differ, a projection shortcut (often a $1\times1$ convolution with a suitable stride) can map $x$ to the required shape.

Dense networks instead concatenate earlier representations:

$$
x_\ell=H_\ell([x_0,\ldots,x_{\ell-1}]).
$$

The brackets mean “join these feature tensors along the feature/channel dimension,” not add them.

Real connection: CNNs power visual inspection, medical imaging, OCR, satellite imagery, and many multimodal encoders.

Failure experiment: compare a CNN with and without augmentation under a controlled background shift. Ask whether the model learned the object or a shortcut.

## Build the intuition before the notation

Imagine looking for the same type of edge everywhere in a photograph. A dense layer could learn a separate detector for every location. A convolution says something more sensible:

> “If this pattern matters here, it may matter somewhere else too.”

That is **translation-aware parameter sharing**.

The kernel is therefore not merely a smaller matrix. It is a statement about what kinds of relationships the model expects to find useful.

### A concrete parameter-count exercise

For a $28\times28$ grayscale image, compare:

- dense layer: $784\rightarrow64$;
- convolution: 16 filters of size $3\times3$.

The dense layer has:

$$
784\times64+64=50,240
$$

parameters.

The convolution has:

$$
16(3\times3+1)=160.
$$

The dramatic difference comes from two assumptions:

1. each filter looks locally;
2. the same filter is reused at every location.

Neither assumption is universally correct. That is why controlled experiments matter.

### Receptive field thought experiment

A single $3\times3$ convolution sees a $3\times3$ neighborhood.

Two stride-1 $3\times3$ layers can combine information from a larger region. Stacking local operations therefore gradually builds a wider effective context.

This gives a useful mental progression:

**local pixels → local patterns → combinations of patterns → larger structures.**

### Why residual connections matter mathematically

If a block learns $F(x)$, ordinary learning asks it to produce the entire transformed representation.

A residual block asks it to produce a correction:

$$
F(x)=y-x.
$$

If the best transformation is close to identity, the desired correction is small.

The shortcut therefore changes what the block must learn, not merely how many parameters it contains.

### Research habit

Whenever comparing CNN architectures, report parameter count and training budget. Otherwise “Model B is better” may simply mean Model B was given more capacity or more optimization.


## Work a small example by hand

Consider this $3\times3$ input and a $2\times2$ filter. For clarity, we use **cross-correlation** (the operation most deep-learning libraries call convolution): slide the filter without flipping it.

$$
X=\begin{bmatrix}1&2&0\\0&1&3\\2&1&0\end{bmatrix},
\qquad
K=\begin{bmatrix}1&0\\0&-1\end{bmatrix}.
$$

At the upper-left position, multiply matching entries and add:

$$
1(1)+2(0)+0(0)+1(-1)=0.
$$

Move the filter one column right:

$$
2(1)+0(0)+1(0)+3(-1)=-1.
$$

Repeat for the bottom row. The output feature map is

$$
Y=\begin{bmatrix}0&-1\\-1&1\end{bmatrix}.
$$

Every output cell is a local weighted measurement. The same four filter weights are reused at all four positions. This is the heart of parameter sharing.

### Predict the output shape before running code

For input height $H$, kernel size $K$, padding $P$, and stride $S$, the output height is

$$
H_{\text{out}}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1.
$$

For a $28\times28$ image, a $3\times3$ kernel, stride 1, and padding 1, the output stays $28\times28$. Sixteen filters produce 16 output channels.

A residual block makes a different numerical move: if $x=2.0$ and the learned correction $F(x)=0.2$, then $y=x+F(x)=2.2$. The block can preserve the original representation while learning a correction. A dense block instead concatenates features, so feature dimensions grow as earlier maps are reused.

**Check yourself:** what would happen to the output size if the stride changed from 1 to 2? Before coding, calculate it using the formula and explain why rounding down is needed.


### Tensor shapes and parameter counts: make the comparison explicit

For a convolution with kernel height $K_h$, kernel width $K_w$, input channels $C_{\mathrm{in}}$, and output channels $C_{\mathrm{out}}$, the number of trainable parameters (including one bias per output channel) is

$$
P_{\mathrm{conv}}=K_hK_wC_{\mathrm{in}}C_{\mathrm{out}}+C_{\mathrm{out}}.
$$

The earlier $3\times3$ example assumes one input channel and 16 output filters, so $3\cdot3\cdot1\cdot16+16=160$. With RGB input, the same 16 filters would instead require $3\cdot3\cdot3\cdot16+16=448$ parameters. Each filter spans **all input channels**; it is not a separate 2-D filter per channel that is independently summed afterward.

For height and width separately, the output-size formula is

$$
H_{\mathrm{out}}=\left\lfloor\frac{H+2P_h-K_h}{S_h}\right\rfloor+1,
\qquad
W_{\mathrm{out}}=\left\lfloor\frac{W+2P_w-K_w}{S_w}\right\rfloor+1.
$$

For example, a $28\times28$ input with a $3\times3$ kernel, stride 2, and padding 1 gives $\lfloor(28+2-3)/2\rfloor+1=14$ positions in each dimension. With 16 filters, the output shape is $14\times14\times16$ (ignoring the batch dimension). The floor is necessary because only complete kernel placements count.

### A residual addition has a shape requirement

The expression $y=x+F(x)$ requires $x$ and $F(x)$ to have compatible shapes. If a block changes the number of channels or spatial resolution, a plain identity shortcut cannot be added directly. A common solution is a learned projection on the shortcut, such as a $1\times1$ convolution (possibly with stride), that maps $x$ to the required shape. This projection has parameters and should be included when reporting the model's parameter count.

## Core concepts

This unit covers **convolution, pooling, receptive fields, CNN extensions, residual and dense networks**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advantage from a larger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible baseline.
3. Implement the central mechanism once from first principles.
4. Run the framework implementation.
5. Keep the primary budget fixed while changing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncertainty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short interpretation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Failure analysis: what did the network actually learn?

A high test score can still hide a shortcut. For example, if every training image of a wolf has snow in the background, a CNN may learn “snow means wolf” rather than robust animal features. Test the hypothesis by evaluating on a background-shifted set or by constructing a controlled background intervention while keeping the object label fixed.

Compare a baseline and an augmentation condition with the same split, architecture, optimizer, epochs, and random seeds where possible. Report overall accuracy **and** performance on the shifted subset. If augmentation helps only on the shifted subset, that supports a robustness interpretation; if it improves all scores, the cause may be broader regularization. If the shifted subset is tiny or differs in multiple ways, say so—the experiment cannot isolate background reliance cleanly.

## Research exercise

The lab must end with a research question. A good question has a measurable independent variable, a defined outcome, a baseline, and a reason the result would matter. Examples include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same training budget?
- Does it improve robustness under distribution shift?
- Does it reduce inference memory or latency?
- Which failure mode becomes more or less common?

## Paper-ready deliverable

Every learner produces a **mini research package**: hypothesis, related-work note, dataset card, method description, experiment matrix, baseline, results table, one figure, error analysis, limitations, reproducibility block, and next-work proposal. These artifacts accumulate toward the final publication capstone.

## Exit questions

1. What problem does the method solve?
2. What inductive bias does it introduce?
3. Which tensor operations implement it?
4. What is the simplest credible baseline?
5. Which metric and split answer the research question?
6. What failure would falsify your hypothesis?

### Answers

1. Convolution reuses a local kernel across locations, encoding the assumption that the same pattern may matter in different positions.
2. A $3\times3$ kernel over one input channel with 16 output channels has $3\cdot3\cdot1\cdot16+16=160$ parameters when each filter has a bias.
3. Receptive field is the region of the original input that can influence a unit; stacked layers generally enlarge it.
4. A residual block adds a learned correction to its input; addition requires compatible tensor shapes, or a projection shortcut is needed.
5. A larger model or longer training budget can explain apparent gains, so match parameter count and training protocol when possible.
6. A background-shift test or controlled intervention can reveal whether performance depends on a spurious visual cue.

## Visual intuition

![CNNs build features across space](../../../visuals/course1/04-convolutional-networks.svg)

*Figure: Local filters detect patterns; deeper layers combine them into larger structures.*

— local filters, shared weights, and skip paths

A convolutional filter looks at a small patch and reuses the same weights at many image locations. This encodes the assumption that a useful local pattern—such as an edge—may matter wherever it appears.

```mermaid
flowchart LR
    I["Image tensor"] --> C["3×3 convolution: local weighted patch"]
    K["One shared kernel"] --> C
    C --> F["Feature maps"]
    F --> P["Activation / pooling"]
    P --> D["Deeper features"]
    D --> O["Classifier"]
```

Residual and dense connections address a different question: how should information move through a deep stack?

```mermaid
flowchart TB
    subgraph RES["Residual block"]
      X1["x"] --> FX["Transform F(x)"]
      X1 --> ADD["Add"]
      FX --> ADD
      ADD --> Y1["y = x + F(x)"]
    end
    subgraph DEN["Dense-style connectivity"]
      A["Feature 1"] --> B["Layer 2"]
      A --> C["Layer 3 receives earlier features"]
      B --> C
      A --> D["Later layer receives all earlier features"]
      B --> D
      C --> D
    end
```

## Laboratory — run the experiment end to end

**[Open the executable laboratory](./lab.ipynb)**

This notebook is part of the chapter, not optional homework. Follow the same scientific loop used in real ML work:

**predict → establish a baseline → run → change one factor → measure → inspect failures → produce the results table → conclude → propose the next experiment.**

The notebook uses a real dataset or environment, records quantitative results, and ends with an answer key and a research extension.

## Video companions

**Recommended starting point:** [Image classification with CNNs — filters and pooling](https://www.youtube.com/watch?v=HGwBXDKFk9I)

For a broader selection, [browse more CNNs, ResNet, and DenseNet videos](https://www.youtube.com/results?search_query=CNNs%2C+ResNet%2C+and+DenseNet).

## Navigation

[← Previous](../03_competitive_learning_and_som/lecture.md) · [Course 1 home](../README.md) · [Next →](../05_autoencoders/lecture.md)
