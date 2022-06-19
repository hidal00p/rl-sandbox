# Neural networks
Neural networks serve as corner stone objects for RL framework. Their ability to approximate very sparsly parametrized worlds and fucntions is utilized for A, V, T and Pi description.
These graph-like structures with certain rules of information propagation, are capable of exracting very intricate features from data, if correctly tuned.

Neural nets are also classified into different categories: FF, Conv, GA or Recurrent. 
Yet all of them are relient on tensor algebra and transformations for mapping, and optimizations for tuning.

## FF nn
Feed forward nets, are represented in a form of a layerd, sequential, ?fully connected? graph. And are probably the simplest form of a NN architecture.

## Conv nn
In really really broad terms it seems that conv layers idea is to utilize the kernel arithmetic with descrete convolution and pooling to extract various features of the input.
A kernel gets projected onto an N-M (is assymetry possible?) input and performs some arithmetic operations on the projection area, thereby attempring to squeeze features out.

**Resources:**
- [Intro to convolutions](https://github.com/vdumoulin/conv_arithmetic)
- [A lot of articles on conv nns](https://colah.github.io/)

It also appears that it is a common practice to combine layers, eg conv layers in the beggining of the data transformation pipeline and some linear(dense according to Keras) in the end, to translate visual interpretation to more arithmetic oriented.

## Optimization aka learning