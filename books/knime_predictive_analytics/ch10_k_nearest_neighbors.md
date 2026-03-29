# Chapter 10: k Nearest Neighbors

## Summary

This chapter covers k Nearest Neighbors (kNN), a "lazy" learning algorithm that classifies new observations based on their similarity to existing labeled data points. Unlike "eager" learners (logistic regression, decision trees, neural networks) that build an explicit model during training, kNN stores all training data and makes decisions at prediction time by finding the k closest observations in the feature space.

### How kNN Works

1. Compute the distance from the new observation to every observation in the training data
2. Rank distances from smallest to largest
3. Select the k nearest neighbors
4. For classification: assign the majority class among the k neighbors
5. For regression: assign the average target value of the k neighbors

### Distance Metrics

- **Euclidean distance:** The most common metric (straight-line distance in feature space)
- **Manhattan distance:** Sum of absolute differences; more robust to outliers
- **Squared Euclidean distance**
- **Jaccard distance:** For binary features
- **Cosine distance:** For text and high-dimensional sparse data

### Critical Preprocessing

- **Normalization is essential:** Variables with larger scales will dominate the distance calculation; min-max normalization (0-1) is recommended
- **Dummy coding:** kNN requires all numeric inputs; categorical variables must be converted to binary indicators via One-to-Many node
- **Missing value handling:** kNN cannot compute distances with missing values; all missing data must be addressed beforehand

### Choosing k

- Small k (e.g., 1) captures fine detail but is sensitive to noise
- Large k provides smoother decision boundaries but may miss local patterns
- k is typically odd to avoid ties in binary classification
- The optimal k is found using a **Parameter Optimization Loop** that tests multiple values and selects the one with the best accuracy

### Example Applications

1. **Heart disease classification:** Using the Cleveland Clinic dataset; the Parameter Optimization Loop determined k=5 was optimal, achieving 81.7% accuracy
2. **kNN for continuous targets (regression):** Compared kNN regression with OLS on a non-linear simulated dataset. kNN (k=1) achieved RMSE of 0.016 vs. OLS's 0.0754, demonstrating kNN's ability to capture non-linear relationships without specifying functional form. An R Snippet (FNN package) was used since KNIME does not have a native kNN regression node.
3. **Multiclass glass identification:** Predicting type of glass (6 categories) from chemical composition (9 continuous predictors); achieved 71.9% accuracy with k=1 vs. 25% for random assignment

## Key Visual Programming Techniques

- **K Nearest Neighbor node:** Classifies data using the kNN algorithm; configurable for number of neighbors, distance weighting, and output of class probabilities
- **Normalizer node:** Min-max normalization (0,1) -- mandatory preprocessing for kNN
- **One to Many node:** Converts categorical variables to binary indicators
- **Missing Value node:** Handles missing data before distance computation
- **Parameter Optimization Loop Start/End:** Iterates over values of k to find the optimum
- **Scorer node:** Accuracy, confusion matrix
- **Line Plot node:** Visualizes accuracy vs. k to identify the optimal value
- **R Snippet node:** Used for kNN regression via the FNN package (since KNIME lacks a native kNN regression node)
- **Numeric Scorer node:** For regression metrics (RMSE)

## Practical Takeaways for Scientists

- kNN is conceptually simple and requires no assumptions about data distributions -- a good choice when you know little about the underlying relationships
- **Always normalize** before using kNN; failing to do so will produce meaningless results dominated by large-scale variables
- kNN handles non-linear relationships naturally without requiring transformations or model specification
- The algorithm is computationally expensive at prediction time (it must compute distances to all training points), making it slow for large datasets
- Storage requirements are high because the entire training set must be retained for deployment
- kNN can handle multiclass problems directly, unlike some algorithms that require one-vs-all strategies
- Highly correlated variables give extra weight to the underlying factor; consider PCA to decorrelate predictors before applying kNN
- kNN suffers from the curse of dimensionality: as the number of features grows, distances between points become increasingly similar, reducing the algorithm's effectiveness
- Use the Parameter Optimization Loop to find k systematically rather than guessing

## Notable References

- Clements, J. (2021). K-Nearest Neighbors (k-NN) explained
- Deotte, C. (2021). Accelerating k-nearest neighbors 600X using RAPIDS cuML
- Detrano, R., et al. (1989). Cleveland heart disease dataset
- Ougiaroglou & Evangelidis (2015). Dealing with noisy data in the context of k-NN classification
- Wang & Wang (2007). A fast KNN algorithm for text categorization
