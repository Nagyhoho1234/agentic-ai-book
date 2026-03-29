# Chapter 8: Scikit-Learn and Decision Trees

## Summary

This chapter introduces machine learning with scikit-learn, covering unsupervised learning (k-means clustering), supervised learning (decision trees for classification and regression), linear programming, and applications in economics. It provides practical examples using the Iris dataset and Boston housing data, demonstrating the complete ML pipeline from data loading to model evaluation.

## Key Concepts

### Scikit-Learn Fundamentals
- **scikit-learn** (sklearn): comprehensive Python library for machine learning
- Consistent API: `fit()`, `predict()`, `score()` pattern across all models
- Built-in datasets: Iris, Boston housing, wine, digits
- Data preprocessing: scaling, normalization, train-test splitting

### K-Means Clustering (Unsupervised Learning)
- Groups data into k clusters by minimizing within-cluster variance
- **Algorithm**: (1) choose k centroids randomly, (2) assign points to nearest centroid, (3) recalculate centroids, (4) repeat until convergence
- Applied to Iris dataset without labels to discover natural groupings
- Visualization using pair plots and cluster coloring

### Decision Trees
- **Classification trees**: predict categorical labels by recursively splitting data on features
- **Regression trees**: predict continuous values using the same splitting approach
- **Gini index**: measure of impurity used to determine optimal splits
- **Confusion matrix**: table showing true vs. predicted classifications
- Visualization of tree structure using `export_graphviz`
- Iris dataset classification example achieving high accuracy

### Linear Programming
- **Objective function**: linear function to be maximized or minimized
- **Constraints**: linear inequalities defining the feasible region
- **Simplex method**: algorithm for finding optimal solutions
- Using `scipy.optimize.linprog()` for solving LP problems
- **Feasibility region**: graphical representation of constraints

### Economics Applications
- **Isoquant curves**: combinations of inputs producing the same output level
- **Isocost lines**: combinations of inputs with the same total cost
- **Cobb-Douglas production function**: Q = A * L^alpha * K^beta
- **Microeconomics**: supply and demand curves, equilibrium price
- **Macroeconomics**: Solow-Swan growth model, expansion paths

### Data Visualization
- **ggplot-style** grid plots for professional presentation
- **Pair plots** (scatter matrix): visualizing relationships between all variable pairs
- Seaborn integration for statistical visualization

## Code Examples Described
- K-means clustering on Iris data with pair plot visualization
- Decision tree classifier for Iris species with confusion matrix
- Decision tree regressor for Boston housing prices
- Linear programming problem solver with feasible region plot
- Cobb-Douglas production function visualization
- Solow-Swan macroeconomic growth model

## Key Definitions
- **Supervised learning**: ML where the training data includes known labels/targets
- **Unsupervised learning**: ML where the algorithm finds patterns in unlabeled data
- **Gini index**: measure of how often a randomly chosen element would be misclassified; 0 = pure, 0.5 = maximum impurity
- **Confusion matrix**: table summarizing classification performance with true/false positives and negatives
- **Linear programming**: optimization of a linear objective function subject to linear constraints

## Practical Takeaways
- scikit-learn provides a unified API that makes switching between ML algorithms straightforward
- K-means is effective for exploratory data analysis to discover natural groupings
- Decision trees are interpretable models suitable for both classification and regression
- Always evaluate model performance using confusion matrices and train-test splits
- Linear programming is directly applicable to resource allocation problems in science and engineering

## Notable References
- Geron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, O'Reilly
- Muller, A.C. and Guido, S. (2016). *Introduction to Machine Learning with Python*, O'Reilly
