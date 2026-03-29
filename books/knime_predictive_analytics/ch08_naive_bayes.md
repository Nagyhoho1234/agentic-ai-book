# Chapter 8: Naive Bayes

## Summary

This chapter covers the Naive Bayes classifier, a probabilistic algorithm based on Bayes' theorem that is surprisingly effective despite its "naive" assumption of conditional independence among predictors. The chapter explains the mathematical foundations, demonstrates KNIME workflows, and applies the technique to customer churn prediction.

### Bayes' Theorem

The foundation of Naive Bayes is Bayes' theorem:

P(Class | Features) = P(Features | Class) * P(Class) / P(Features)

- **Prior probability P(Class):** The probability of each class before observing any features (estimated from training data frequencies)
- **Likelihood P(Features | Class):** The probability of observing the feature values given the class
- **Posterior probability P(Class | Features):** The updated probability after observing the features -- this is what we want to predict

### The "Naive" Assumption

The key simplification is **conditional independence**: the algorithm assumes that each predictor variable is independent of every other predictor, given the class label. This means the joint probability of all features can be computed as the product of individual feature probabilities:

P(X1, X2, ..., Xp | Class) = P(X1 | Class) * P(X2 | Class) * ... * P(Xp | Class)

This assumption is almost always violated in practice, yet the algorithm often performs remarkably well. The reason is that it only needs to get the relative ranking of posterior probabilities correct, not the absolute values.

### Handling Different Variable Types

- **Categorical predictors:** Use frequency tables to estimate P(Xi | Class)
- **Continuous predictors:** Assume a normal distribution and estimate P(Xi | Class) using the class-specific mean and standard deviation
- **Zero-frequency problem:** If a category-class combination never appears in training data, the probability becomes zero, which zeroes out the entire product. **Laplace smoothing** adds a small count to every combination to prevent this.

### Example Application: Churn Prediction

The chapter applies Naive Bayes to the telecom churn dataset:
- Target variable: whether a customer churned (yes/no)
- Predictors include account features, usage patterns, and customer service interactions
- The model is trained, tested, and assessed using confusion matrices, accuracy, and AUC
- Results are compared with logistic regression on the same data

### Bayes' Theorem Illustrated

A clear numerical example is provided showing step-by-step computation of posterior probabilities using a small dataset, making the abstract formula concrete and accessible.

## Key Visual Programming Techniques

- **Naive Bayes Learner node:** Trains the model on labeled training data; handles both categorical and continuous predictors
- **Naive Bayes Predictor node:** Applies the model to new data; outputs class predictions and posterior probabilities
- **Scorer node:** Generates confusion matrix and accuracy metrics
- **ROC Curve node:** For AUC-based assessment
- **Partitioning node:** With stratified sampling on the target variable
- The standard workflow pattern: Read -> Prep -> Partition -> Learner -> Predictor -> Scorer

## Practical Takeaways for Scientists

- Naive Bayes is fast, simple, and often a good baseline model -- try it first and use it as a benchmark
- Despite the unrealistic independence assumption, it frequently performs competitively with more complex algorithms
- It works particularly well when the number of predictors is large relative to the number of observations
- Naive Bayes naturally outputs class probabilities, not just class labels -- use the probabilities for ranking
- Watch out for the zero-frequency problem with categorical variables; enable Laplace smoothing
- The algorithm handles missing values naturally (by simply omitting the missing feature from the product)
- It is computationally cheap: training is essentially counting frequencies, making it suitable for very large datasets
- Continuous variables must approximately follow a normal distribution within each class for the Gaussian assumption to work; consider discretizing heavily skewed variables

## Notable References

- Bayes, T. (1763). Original essay on probability
- Telecom churn dataset
- Laplace smoothing and its theoretical justification
- Comparison studies of Naive Bayes vs. other classifiers
