# Chapter 20: Convolutional Neural Networks, TensorBoard and Further Reading

## Summary

This chapter covers convolutional neural networks (CNNs) for image classification, TensorBoard for model visualization, and provides an overview of emerging AI topics including cyber security, ethics in AI, IoT, NLP, and reinforcement learning. The CNN section demonstrates the complete pipeline from convolution and pooling theory to MNIST digit classification achieving over 98% accuracy.

## Key Concepts

### Convolving and Pooling
- **Convolution**: applying a filter (kernel) to an input array by sliding and computing element-wise products
- **Filter/kernel**: small matrix detecting specific features (e.g., vertical lines, edges)
- Example: 5x5 filter for vertical line detection applied to a 7x7 input (padded with zeros)
- **Padding**: adding zeros around the input to preserve spatial dimensions
- **Stride**: step size when sliding the filter (stride=1 in examples)
- **ReLU activation**: applied after convolution, setting negative values to zero
- **Max pooling**: downsampling by taking the maximum value in each pooling window (e.g., 3x3)
- **Flattening**: converting 2D pooled arrays into 1D vectors for the fully connected ANN

### CNN Architecture
- Five layer types: input, convolutional, pooling, fully connected, output
- **MNIST example architecture**: Input(28x28x1) -> Conv2D(5x5, 64 filters) -> MaxPool(2x2) -> Conv2D(5x5, 64 filters) -> MaxPool(2x2) -> Flatten -> Dense(128, ReLU) -> Dense(128, ReLU) -> Dense(10, softmax)
- Total parameters: 253,130
- **Softmax activation**: S(x_i) = e^{x_i} / sum(e^{x_j}) -- converts output to probability distribution over classes
- **Sparse categorical crossentropy**: loss function for multi-class classification

### MNIST Classification
- **MNIST dataset**: 60,000 training + 10,000 testing images of handwritten digits (28x28 pixels)
- Data normalization using `tf.keras.utils.normalize()`
- 3 epochs achieve over 98% accuracy
- `model.predict()` for classifying new images
- Conv2D with 64 filters, 5x5 kernel, stride 2, ReLU activation

### TensorBoard
- Visualization tool for monitoring TensorFlow training
- **Scalars dashboard**: loss, accuracy, learning rate vs. epoch
- **Graphs**: visual representation of the model architecture
- **Distributions and Histograms**: weight and bias distributions over time
- **Dropout layer** (rate=0.2) introduced to prevent overfitting
- Example: MNIST classification without CNN, using Dense layers with dropout

### Cyber Security
- AI for detecting malware, monitoring misinformation, preventing phishing
- Companies: CyberArk, Darktrace, FireEye, Google, Microsoft, Rapid7
- 10,000 cyber security alerts per day for average business

### Ethics in AI
- Bias, fairness, and transparency concerns
- **Asilomar AI Principles** (2017): 23 principles developed by 100+ world leaders
- Research issues, ethics and values, longer-term concerns
- Codes of ethics being developed by most organizations

### Internet of Things (IoT)
- Physical devices connected over communication networks
- Projected 21 billion IoT devices by 2025
- Raspberry Pi as a practical IoT platform
- Convergence of sensors, ML, embedded systems, and ubiquitous computing

### Natural Language Processing (NLP)
- Applications: chatbots, email classification, sentiment analysis, translation
- **Shakespeare text generation** example using LSTM on Google Colab TPU
- ChatGPT and natural language generation (NLG)
- Text analysis and translation tools

### Reinforcement Learning (RL)
- Agent learns through positive and negative rewards
- Applications: game playing (Atari, chess, Go), robotics, optimization
- Uses Markov Decision Processes (MDPs)
- Future: robots learning through trial-and-error interaction with environment
- Tensor rank of sensory data: video (4-5D tensor), perception (6th dimension)

## Code Examples Described
- Convolution implementation: sliding 5x5 filter over padded input array (Program_20a.py)
- CNN for MNIST digit classification using Keras functional API (Program_20b.ipynb)
- TensorBoard integration for monitoring training with dropout layer (Program_20c.ipynb)

## Key Definitions
- **Convolution**: mathematical operation where a filter slides across an input to produce a feature map
- **Pooling**: downsampling operation that reduces spatial dimensions while retaining important features
- **Softmax**: activation function that converts raw outputs to a probability distribution
- **Dropout**: regularization technique that randomly removes neurons during training to prevent overfitting
- **TensorBoard**: TensorFlow's visualization toolkit for monitoring model training

## Practical Takeaways
- CNNs are the standard architecture for image classification tasks
- The convolution -> ReLU -> pool pipeline is the fundamental building block of CNNs
- Just 3 epochs on MNIST with a simple CNN achieves >98% accuracy, demonstrating the power of convolutional architectures
- TensorBoard is invaluable for diagnosing training problems (overfitting, learning rate issues)
- Dropout is a simple and effective regularization technique
- The AI field extends far beyond what is covered in this book -- cyber security, IoT, NLP, and RL are all active research areas with growing Python tool ecosystems

## Notable References
- Geron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, O'Reilly
- LeCun, Y. (1989). Backpropagation applied to handwritten zip code recognition. *Neural Computation*, 1, 541-551
- Norvig, P. and Russell, S. (2021). *Artificial Intelligence: A Modern Approach*, 4th Ed. Pearson
- Sutton, R. and Barto, A.G. (2018). *Reinforcement Learning*, 2nd Ed. MIT Press
