# Chapter 19: Recurrent Neural Networks

## Summary

This chapter covers recurrent neural networks (RNNs), progressing from discrete Hopfield networks (content-addressable memories) to continuous Hopfield networks (with Lyapunov stability analysis), and culminating in LSTM networks for predicting both chaotic and financial time series. It demonstrates that LSTMs can learn the patterns in chaotic logistic map data and apply this to real-world financial forecasting.

## Key Concepts

### Discrete Hopfield RNN
- **Hopfield (1982)**: content-addressable memory using fixed points as attractors
- **Architecture**: fully connected network where all neurons connect to all others (no self-connections)
- **Hebb's postulate of learning**: weight matrix W = (1/N) * sum(x_r * x_r^T) - (M/N)*I_n
- **Asynchronous updating**: neurons updated one at a time in random order
- **hsgn function**: hard sign activation; 1 if positive, -1 if negative, unchanged if zero
- **Fundamental memories**: stored patterns that are stable fixed points of the network
- **Spurious states**: stable states that are not stored memories (reversed, mixed, or spin-glass states)
- Five-neuron example storing three fundamental memories

### Continuous Hopfield RNN
- **Hopfield (1984)**: analog version with graded response neurons
- **System equation**: dx/dt = -x + W*a(t) + b
- where a(t) = phi(x(t)) is the nonlinear activation function
- **Lyapunov function**: V(a) = -(1/2)*a^T*W*a + sum(integral of phi^{-1}) - b^T*a
- Guarantees convergence to stable states (energy minima) if:
  1. phi^{-1} is monotonically increasing
  2. Weight matrix W is symmetric
- **Two-neuron example**: surface and contour plots of Lyapunov function showing four local minima (four stable states)
- Applications: classification, optimization (travelling salesman problem)

### LSTM Architecture
- **Hochreiter and Schmidhuber (1997)**: Long Short-Term Memory
- Solves the **vanishing gradient problem** of standard RNNs
- **Gates**: forget (sigma_1), input (sigma_2), output (sigma_3) -- all sigmoid functions
- **Cell state (c_t)**: long-term memory channel
- **Hidden state (h_t)**: short-term memory/output
- Tanh functions (phi_1, phi_2) regulate data flow and prevent information fading
- Gates control what information to store, update, or output

### LSTM for Chaotic Time Series
- **Logistic map**: x_{n+1} = 4*x_n*(1-x_n) generates chaotic time series (mu = 4)
- 1000 iterates, 80% training / 20% testing
- Architecture: 128 LSTM units -> 1 Dense output
- 30 epochs, batch size 16, time steps = 10
- Adam optimizer with learning rate 0.001
- **Remarkable results**: LSTM successfully predicts chaotic time series despite sensitivity to initial conditions

### LSTM for Financial Time Series
- **US/EUR exchange rate** data from FRED API (Sept 2017 - Sept 2020)
- Data preprocessing: forward-fill missing values, 80/20 train/test split
- Architecture: 128 LSTM units -> 1 Dense output
- 250 epochs, batch size 16, time steps = 1
- Good prediction performance, though results diverge toward the end of the prediction window
- Demonstrates practical applicability of LSTM to real financial data

## Code Examples Described
- Discrete Hopfield network storing and recalling three 5-element patterns (Program_19a.py)
- Continuous Hopfield Lyapunov function contour and surface plots (Program_19b.py)
- LSTM prediction of chaotic logistic map time series (Program_19c.ipynb)
- LSTM prediction of US/EUR exchange rate with FRED API data access (Program_19d.ipynb)

## Key Definitions
- **Content-addressable memory**: memory accessed by content (pattern) rather than by address
- **Fundamental memory**: a stored pattern that is a stable fixed point of the Hopfield network
- **Lyapunov function**: energy-like function that decreases along trajectories, guaranteeing convergence to stable states
- **LSTM**: RNN architecture with gated memory cells that can learn long-range dependencies
- **Vanishing gradient problem**: gradients become exponentially small during backpropagation through many time steps, preventing learning of long-range dependencies

## Practical Takeaways
- Hopfield networks demonstrate that ANNs can function as associative memories -- given a partial or noisy pattern, they converge to the nearest stored memory
- The Lyapunov function provides a rigorous proof of convergence for continuous Hopfield networks
- LSTM networks are remarkably effective at learning temporal patterns, even in chaotic systems
- For financial time series, LSTM predictions are reasonable in the short term but deteriorate over longer horizons
- Time steps, LSTM units, batch size, and learning rate are the key hyperparameters to tune for LSTM networks
- Always use `shuffle=False` for time series data to preserve temporal ordering

## Notable References
- Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 99, 1735-1780
- Hopfield, J.J. (1982). Neural networks with emergent collective computational abilities. *PNAS*, 79, 2554-2558
- Korstanje, J. (2021). *Advanced Forecasting with Python*, Apress
- Salem, F.M. (2022). *Recurrent Neural Networks: From Simple to Gated Architectures*, Springer
