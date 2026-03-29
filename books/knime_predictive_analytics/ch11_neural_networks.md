# Chapter 11: Neural Networks

## Summary

This chapter covers artificial neural networks (ANNs), powerful predictive models inspired by biological neurons that can learn complex non-linear relationships without explicit model specification. The chapter covers the architecture of neural networks, the learning process, activation functions, the overfitting problem, and practical KNIME workflows for both classification and regression tasks.

### What Are Artificial Neural Networks?

ANNs are inspired by biological neurons but are fundamentally computational models. The chapter traces the history:
- **McCulloch & Pitts (1943):** First mathematical model of a neuron (binary on/off switches)
- **Rosenblatt (1958):** The perceptron -- a single-layer model that could learn from data
- **Minsky & Papert (1969):** Demonstrated limitations (XOR problem), leading to the "AI winter"
- **Rumelhart et al. (1986):** Backpropagation algorithm revived interest by enabling training of multilayer networks

### Architecture

- **Input layer:** Receives the predictor variables
- **Hidden layers:** One or more layers of neurons that transform the inputs; each neuron computes a weighted sum of inputs plus a bias, then applies an activation function
- **Output layer:** Produces the prediction (class probabilities for classification, continuous value for regression)

### Activation Functions

- **Step function:** Original perceptron; binary output
- **Logistic (sigmoid):** Smooth output between 0 and 1; used in early networks
- **Hyperbolic tangent (tanh):** Output between -1 and 1
- **ReLU (Rectified Linear Unit):** max(0, x); enables deep learning by avoiding the vanishing gradient problem; the modern default

### The Learning Process (Backpropagation)

1. Initialize weights randomly
2. Forward pass: compute predictions
3. Calculate the error (cost function) between predictions and actual values
4. Backward pass: propagate the error back through the network
5. Update weights using gradient descent
6. Repeat until convergence or maximum iterations

KNIME uses the **RProp (Resilient Propagation)** algorithm, which is faster than standard backpropagation and does not require the user to set a learning rate.

### The Overfitting Problem

Neural networks are particularly prone to overfitting because they can have many parameters (weights):
- With enough iterations and nodes, a neural network can memorize any training data perfectly
- Demonstrated with the Iris dataset using randomized target: the model achieved perfect training accuracy but near-random test accuracy

Techniques to reduce overfitting:
1. Decrease model complexity (fewer nodes, fewer layers)
2. Reduce the number of training iterations
3. Add a penalty term (regularization)
4. Randomly drop neurons during training (dropout)

Techniques 1 and 2 are available in KNIME's RPropMLP; techniques 3 and 4 are available in KNIME's deep learning models.

### Example Applications

1. **Iris classification (multiclass):** Three species, four features. RProp MLP with 1 hidden layer and 3 neurons. Perfect training accuracy; 2 errors on test data (45 observations). Workflow uses Normalizer (0-1 required), Partitioning, RProp MLP Learner, MultiLayerPerceptron Predictor, and Scorer nodes.

2. **German credit risk prediction (cost minimization):** 1000 observations, 20 predictors. The analysis goes beyond accuracy to minimize expected business cost. Asymmetric costs: misclassifying a "bad" risk as "good" costs 5x more than the reverse. Data rebalanced to 95/5 ratio to reflect real-world prevalence. Parameter Optimization Loop tunes iterations (30-50), hidden layers (1-10), and neurons per layer (1-20). Result: cost dropped from 185 (no model) to 12 with the neural network.

3. **Toyota Corolla price prediction (regression):** Neural network vs. OLS regression. Parameter Optimization Loop finds best architecture. Neural net achieved RMSE of 0.042 vs. OLS 0.053 on normalized test data. Workflow has three sections: optimization loop, best model assessment, and OLS comparison.

## Key Visual Programming Techniques

- **RProp MLP Learner node:** Trains the multilayer perceptron; settings include max iterations, number of hidden layers, neurons per layer, class column, and random seed
- **MultiLayerPerceptron Predictor node:** Applies the trained model; can output class probabilities
- **Normalizer node:** Min-max (0-1) normalization is **required** for neural networks
- **Normalizer (Apply) node:** Applies the same normalization to test data using the model from the training Normalizer
- **One to Many node:** Converts categorical predictors to binary indicators (required for neural nets)
- **Parameter Optimization Loop Start (Table) / Loop End:** Tunes multiple parameters simultaneously from a Table Creator-defined grid
- **Table Creator node:** Manually specifies parameter ranges for optimization
- **Table Row to Variable node:** Converts optimization results to flow variables
- **Metanodes:** Used to encapsulate complex sub-workflows (e.g., the cost rebalancing and estimation metanode with 11 internal nodes)
- **Workflow Annotations:** KNIME's annotation boxes label sections of the workflow for clarity

## Practical Takeaways for Scientists

- Neural networks are powerful but opaque -- they are "black boxes" with no interpretable coefficients or variable importance measures
- **Always normalize** inputs to 0-1 range; the RProp MLP Learner requires it
- Start simple: one hidden layer with a small number of neurons, then increase complexity if needed
- Monitor both training and test performance; a large gap indicates overfitting
- The Parameter Optimization Loop is essential for neural networks because performance is highly sensitive to architecture choices
- For business applications, optimize for the relevant business metric (cost, profit) rather than accuracy
- Neural networks excel when relationships are non-linear and complex, but simpler models may be sufficient and more interpretable for many problems
- Missing data is not handled natively; all missing values must be addressed in preprocessing
- Use a random seed for reproducibility -- different random initializations can produce different results

## Notable References

- McCulloch, W. S., & Pitts, W. H. (1943). A logical calculus of the ideas immanent in nervous activity
- Rosenblatt, F. (1958). The perceptron
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Backpropagation
- Minsky, M., & Papert, S. (1969). Perceptrons
- Nielsen, M. (2019). Neural networks and deep learning (online book)
- Silipo, R., & Melcher, K. (2020). Codeless deep learning with KNIME
- Sagar, V. (2019). 5 techniques to prevent overfitting in neural networks
- Gromping, U. (2019). South German Credit Data correction
