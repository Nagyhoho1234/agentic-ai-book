# Chapter 17: Neural Networks and Neurodynamics

## Summary

This chapter introduces artificial neural networks (ANNs) from first principles, covering the mathematical model of a neuron, transfer functions, logic gates implemented as ANNs, the backpropagation algorithm, machine learning on the Boston housing dataset, and neurodynamics (stability analysis of neuromodules). It bridges the biological neuron concepts from Chapter 16 to the deep learning frameworks in Chapters 18-20.

## Key Concepts

### History of Neural Networks
- **1937**: Turing's paper on computable numbers
- **1943**: McCulloch-Pitts neuron model (all-or-none law)
- **1949**: Hebb's learning rule
- **1958**: Rosenblatt's perceptron
- **1969**: Minsky and Papert highlight limitations of single-layer perceptrons
- **1986**: Rumelhart, Hinton, and Williams introduce backpropagation

### Mathematical Neuron Model
- **Activation potential**: v = sum(x_i * w_i) + b (weighted sum of inputs plus bias)
- **Output**: y = sigma(v) where sigma is a transfer function
- **Sigmoid (logistic) function**: sigma(v) = 1/(1 + e^{-v}), maps to (0,1), derivative = sigma(1-sigma)
- **Tanh function**: phi(v) = (e^v - e^{-v})/(e^v + e^{-v}), maps to (-1,1), derivative = 1 - phi^2

### Logic Gates as ANNs
- **AND gate**: single neuron with w1=20, w2=20, b=-30 and sigmoid activation
- **OR gate**: single neuron with w1=20, w2=20, b=-10 and sigmoid activation
- **XOR gate**: requires hidden layer (not linearly separable)
  - Two hidden neurons, one output neuron
  - Demonstrates the necessity of multi-layer networks for non-linear problems

### Backpropagation Algorithm
- **Goal**: minimize the error function (mean squared error) by adjusting weights
- **Chain rule**: compute partial derivatives of error with respect to each weight
- **Weight update**: w_new = w_old - eta * (dErr/dw) where eta is the learning rate
- For output layer: dErr/dw2 = (y_t - y) * sigma(o1) * (1 - sigma(o1)) * sigma(h1)
- For hidden layer: propagate gradients backward through the network
- **Learning rate (eta)**: controls step size; too large causes oscillation, too small causes slow convergence

### Machine Learning on Boston Housing Data
- **Boston housing dataset**: 506 houses with 14 attributes
- Single-layer perceptron with tanh activation function
- **Five-step training process**:
  1. Scale data to zero mean, unit variance; add bias
  2. Set small random weights
  3. Set epochs and learning rate
  4. Compute outputs, errors, gradients; update weights via gradient descent
  5. Plot weight convergence
- Asynchronous (per-sample) weight updating demonstrated
- 100 epochs, 50,600 iterations, eta = 0.0005 for convergence
- Supervised learning with known target values

### Neurodynamics
- **Two-neuron module**: discrete dynamical system modeling interacting neurons
- x_{n+1} = b1 + w11*phi1(x_n) + w12*phi2(y_n)
- y_{n+1} = b2 + w21*phi1(x_n) + w22*phi2(y_n)
- **Stability analysis** using the Jacobian matrix and eigenvalues
- **Bifurcation boundaries**:
  - B^{+1}: fold bifurcation (bistable boundary) when eigenvalue lambda = +1
  - B^{-1}: flip bifurcation (unstable boundary) when lambda = -1
  - B^{NS}: Neimark-Sacker bifurcation (quasiperiodic boundary) when |lambda| = 1
- **Stability diagram**: mapping regions of stable, bistable, unstable, and quasiperiodic behavior in parameter space

## Code Examples Described
- Single-neuron AND and OR gate implementations (Program_17a.py, 17b.py)
- Backpropagation for XOR network with forward pass and weight update (Program_17c.py)
- Boston housing ANN with weight convergence plot (Program_17d.py)
- Stability diagram of a two-neuron module showing fold, flip, and Neimark-Sacker boundaries (Program_17e.py)

## Key Definitions
- **Perceptron**: single-layer neural network; the simplest ANN architecture
- **Backpropagation**: algorithm for computing gradients of the error with respect to weights by propagating errors backward through the network
- **Learning rate (eta)**: hyperparameter controlling the step size of weight updates
- **Epoch**: one complete pass through the entire training dataset
- **Neimark-Sacker bifurcation**: the discrete-time analog of the Hopf bifurcation, producing quasiperiodic behavior

## Practical Takeaways
- Understanding backpropagation from scratch is essential for debugging and designing neural networks
- The XOR problem illustrates why deep networks (multiple layers) are necessary for non-linear classification
- Weight convergence plots are essential diagnostic tools for training neural networks
- Neurodynamics provides a rigorous mathematical framework for understanding neural network stability
- The Boston housing example shows that even simple perceptrons can predict real estate values reasonably well

## Notable References
- Aggarwal, C.C. (2018). *Neural Networks and Deep Learning: A Textbook*, Springer
- Rumelhart, D.E. et al. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536
- Rashid, T. (2016). *Make Your Own Neural Network*, CreateSpace
