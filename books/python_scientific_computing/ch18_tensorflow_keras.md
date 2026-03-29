# Chapter 18: TensorFlow and Keras

## Summary

This chapter introduces TensorFlow and Keras as the primary deep learning frameworks, providing a brief history of AI milestones. It covers linear regression, the XOR logic gate, Boston housing data analysis with multiple model architectures, and demonstrates how overfitting occurs with increasingly complex networks. The chapter serves as the gateway to practical deep learning.

## Key Concepts

### Artificial Intelligence Overview
- **AI subcategories**: Computer Vision, Deep Learning, Machine Learning, NLP, ANNs (with RNN and CNN subtypes)
- **Key milestones**:
  - 1986: Backpropagation algorithm
  - 1997: Deep Blue beats Kasparov
  - 2012: AlexNet wins ImageNet
  - 2014: DeepMind plays Atari games
  - 2016: AlphaGo beats Go champion
  - 2018: Google's BERT for NLP
  - 2019: TensorFlow 2 released

### TensorFlow
- Google's open-source library for numerical computation and deep learning
- Written in Python, C++, and CUDA for GPU acceleration
- Uses **tensors** (multi-dimensional arrays) as fundamental data structures
- Access via Google Colab for free GPU/TPU computing
- NumPy preprocesses data before feeding to TensorFlow

### Keras
- High-level API adopted by TensorFlow
- Provides user-friendly interface for defining, compiling, and training ANNs
- Key components: layers, activation functions, loss functions, optimizers, metrics, callbacks
- **Sequential model**: linear stack of layers

### Linear Regression with TensorFlow
- Simplest possible ANN: one input, one neuron, one output
- `tf.keras.layers.Dense(units=1, input_shape=[1])`
- Compiled with mean squared error loss and Adam optimizer
- 100 epochs sufficient for convergence on linear data
- Weight gives slope, bias gives y-intercept of best-fit line

### Activation Functions
- **ReLU**: f(x) = max(0, x) -- piecewise linear, solves vanishing gradient problem
- **Leaky ReLU**: f(x) = max(alpha*x, x) where alpha is small (e.g., 0.01)
- **Sigmoid**: f(x) = 1/(1+e^{-x}) -- maps to (0,1)
- **Tanh**: f(x) = (e^x - e^{-x})/(e^x + e^{-x}) -- maps to (-1,1)

### XOR Gate with TensorFlow
- XOR is not linearly separable -- requires hidden layer
- Architecture: 8 neurons (ReLU) -> 8 neurons (ReLU) -> 1 neuron (sigmoid)
- Training data: [[0,0], [0,1], [1,0], [1,1]] with targets [[0], [1], [1], [0]]
- 500 epochs with Adam optimizer (learning rate 0.1)
- Loss and accuracy curves plotted for monitoring

### Boston Housing with TensorFlow
- Four progressively complex models demonstrating overfitting:
  - **Model 1**: 1 neuron, no overfitting (training and test loss curves agree)
  - **Model 2**: 10 neurons in hidden layer, some overfitting (curves diverge)
  - **Model 3**: 100 neurons in two hidden layers, more overfitting
  - **Model 4**: same as Model 3 but 90% validation split -- worst results
- **Key lesson**: more complex models don't always perform better; overfitting is the main risk
- `validation_split` parameter for automatic train/test splitting

### Keras API Reference
- **Models**: Sequential, Model (functional API)
- **Layers**: Dense, Conv2D, LSTM, Dropout, BatchNormalization, Flatten, Attention
- **Optimizers**: SGD, Adam, RMSprop, Adadelta, Adagrad
- **Losses**: MSE, categorical crossentropy, binary crossentropy, hinge
- **Callbacks**: ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau
- **Datasets**: MNIST, CIFAR-10/100, IMDB, Reuters, Fashion MNIST, Boston housing

## Code Examples Described
- Linear regression ANN with training data generation, model training, and best-fit line (Program_18a)
- XOR gate ANN with loss/accuracy curve plotting (Program_18b)
- Four Boston housing models comparing overfitting levels (Program_18c)

## Key Definitions
- **Overfitting**: when a model learns noise in training data, performing well on training but poorly on test data
- **Epoch**: one complete pass of the entire dataset through the neural network
- **Adam optimizer**: adaptive learning rate optimization algorithm combining benefits of AdaGrad and RMSProp
- **Validation split**: fraction of training data held out for evaluating model performance during training
- **Sequential model**: Keras model where layers are stacked linearly

## Practical Takeaways
- Google Colab is the easiest way to get started with TensorFlow (free GPUs)
- Start with simple models and increase complexity only if needed -- avoid overfitting
- Monitor both training and validation loss curves; divergence indicates overfitting
- ReLU is the default activation function for hidden layers; sigmoid/softmax for output layers
- The Adam optimizer with default parameters works well for most problems
- Keras's Sequential API makes building standard architectures extremely simple

## Notable References
- Geron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, O'Reilly
- Krizhevsky, A. et al. (2012). ImageNet classification with deep convolutional neural networks. *NIPS*
- Rumelhart, D.E. et al. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536
