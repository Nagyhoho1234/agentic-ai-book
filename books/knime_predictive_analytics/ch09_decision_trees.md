# Chapter 9: Decision Trees

## Summary

This chapter covers decision tree models, one of the most popular and interpretable machine learning techniques. Decision trees recursively partition the data into increasingly homogeneous subgroups based on predictor variables, creating a tree-like structure that is easy to visualize and interpret. The chapter covers the algorithms, splitting criteria, pruning, and practical applications.

### How Decision Trees Work

A decision tree starts with all observations in a single root node and recursively splits them:
1. Evaluate all possible splits across all predictor variables
2. Select the split that best separates the classes (or reduces variance for regression)
3. Create two (or more) child nodes
4. Repeat until a stopping criterion is met (max depth, min node size, or purity threshold)

### Splitting Criteria

For classification trees:
- **Gini impurity:** Measures the probability of incorrectly classifying a randomly chosen element; ranges from 0 (pure) to 0.5 (maximum impurity for binary)
- **Information gain (entropy):** Based on Shannon's information theory; measures the reduction in uncertainty after a split
- **Chi-squared (CHAID):** Uses statistical significance of the relationship between predictor and target

For regression trees:
- **Variance reduction:** Splits that minimize within-node variance of the target

### Tree Algorithms Available in KNIME

- **C4.5 / C5.0:** Uses information gain ratio; handles categorical and continuous predictors; supports pruning
- **CHAID:** Uses chi-squared tests for splits; can create multi-way splits (not just binary)
- **CART-like:** Binary splits using Gini impurity

### Pruning

Fully grown trees tend to overfit. Two approaches to control complexity:
- **Pre-pruning (early stopping):** Set limits on tree depth, minimum samples per node, or minimum information gain
- **Post-pruning (cost-complexity pruning):** Grow a full tree, then remove branches that do not improve generalization; uses a complexity parameter to trade off accuracy vs. simplicity

### Example Applications

1. **Churn prediction:** Using the telecom dataset to predict customer churn; the tree structure reveals which factors (e.g., number of customer service calls) are most important
2. **Heart disease classification:** Using the Cleveland Clinic dataset with clinical predictors

The chapter provides detailed node-by-node workflow descriptions with all settings specified.

## Key Visual Programming Techniques

- **Decision Tree Learner node:** Trains the tree model; configurable splitting criterion (Gini or information gain), pruning settings (MDL or no pruning), and depth limits
- **Decision Tree Predictor node:** Applies the model to new data; outputs class predictions and class probabilities
- **Decision Tree View:** Interactive visualization of the tree structure -- one of the major advantages of this technique
- **Scorer node:** Confusion matrix and accuracy metrics
- **Partitioning node:** Training/test split with stratified sampling
- **Parameter Optimization Loop:** For tuning tree parameters (depth, min node size)
- The tree visualization shows split criteria, class distributions at each node, and the path from root to any leaf

## Practical Takeaways for Scientists

- Decision trees are the most interpretable model type -- the tree diagram itself explains the decision logic
- They handle both categorical and continuous predictors without requiring dummy coding or normalization
- Trees are prone to overfitting; always use pruning or set depth limits
- Feature importance is built in: variables that appear in higher (earlier) splits are more important
- Trees are unstable: small changes in data can lead to different trees (this limitation motivates ensemble methods in Chapter 12)
- The tree visualization is excellent for communicating results to non-technical stakeholders
- For binary classification, consider adjusting the class weights or threshold rather than using the default majority-vote rule
- Decision trees can capture non-linear relationships and interactions between variables without explicit specification
- Missing values can be handled by the algorithm (surrogate splits) in some implementations

## Notable References

- Quinlan, J. R. -- C4.5 and C5.0 algorithms
- Breiman, L. et al. -- CART (Classification and Regression Trees)
- CHAID algorithm (Kass, 1980)
- Cleveland heart disease dataset (Detrano et al., 1989)
- Telecom churn dataset
