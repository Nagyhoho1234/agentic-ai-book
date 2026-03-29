# Chapter 12: Ensemble Models

## Summary

This chapter covers ensemble methods -- techniques that combine multiple models to produce better predictions than any single model. The central insight is that combining diverse, independent models tends to cancel out individual errors and improve both accuracy and stability. The chapter covers bagging, random forests, boosting (AdaBoost, Gradient Boosting Machines, XGBoost), and practical KNIME applications.

### Why Ensemble Models Work

The "Wisdom of Crowds" principle: combining independent estimates tends to produce a better result than any individual estimate. The classic example is Francis Galton's 1907 observation that the median of 800 guesses of an ox's weight was only 9 pounds off from the true weight of 1198 pounds.

For ensembles to work, the component models must be:
- **Diverse:** Different models that make different errors
- **At least somewhat accurate:** Better than random guessing

### Creating Ensemble Models

Approaches to creating diverse component models:
- Using different algorithms (e.g., decision tree + logistic regression + neural network)
- Varying parameters of the same algorithm (e.g., different tree depths)
- Sampling different subsets of predictor variables
- Sampling different subsets of observations

### Ensemble Models Based on Decision Trees

Decision trees are ideal candidates for ensemble methods because they are (a) not globally optimal and (b) unstable (small data changes can produce very different trees).

#### Bagging (Bootstrap Aggregating)
- Create k bootstrap samples (random sampling with replacement) of size n from the training data
- Train a decision tree on each sample
- Aggregate predictions: majority vote for classification, average for regression
- Reduces variance while maintaining (or slightly reducing) bias

#### Random Forests
- Like bagging, but with an additional randomization: at each split, only a random subset of predictors is considered
- This further decorrelates the individual trees, improving ensemble diversity
- Two forms of randomization: sampling observations (bootstrap) and sampling features

#### Boosting
Sequential ensemble where each new model focuses on the errors of the previous ones:

- **AdaBoost:** Weights observations; misclassified cases get higher weight in the next iteration; final prediction is a weighted vote
- **Gradient Boosting Machines (GBM):** Uses gradient descent to optimize a loss function; each new tree fits the residuals of the previous ensemble
- **XGBoost (eXtreme Gradient Boosting):** Highly optimized GBM implementation; includes regularization to reduce overfitting; widely considered "state of the art" for structured data; dominant in Kaggle competitions

### Example Applications

1. **Continuous target -- Toyota Corolla prices:** Comparing OLS regression vs. Gradient Boosted Trees for predicting car prices. Results on test data:
   - MAE: OLS = 851.65, GBT = 775.02
   - RMSE: OLS = 1243.73, GBT = 1075.43
   - MAPE: OLS = 0.08, GBT = 0.07
   Gradient Boosted Trees outperformed OLS on all three metrics.

2. **Binary target -- Churn prediction with XGBoost:** Using the telecom churn dataset with asymmetric costs (misclassifying a churner costs 100x a false churn prediction). A Metanode iterates over threshold values (0.1 to 0.6 in steps of 0.01) to find the threshold that minimizes expected cost. Optimal threshold: 0.25. The cost vs. threshold curve shows a clear minimum.

## Key Visual Programming Techniques

- **Gradient Boosted Trees Learner (Regression) node:** Trains a GBT model for continuous targets; configurable tree depth, number of models
- **Gradient Boosted Trees Predictor (Regression) node:** Applies the GBT regression model
- **XGBoost Tree Ensemble Learner node:** Trains an XGBoost model for classification; outputs model and feature importance
- **XGBoost Predictor node:** Applies the XGBoost model; outputs predictions and class probabilities
- **Numeric Scorer node:** For regression metrics (MAE, RMSE, MAPE)
- **Metanode for threshold optimization:** Complex sub-workflow that iterates over thresholds, computes cost at each, and selects the minimum
- **Line Plot node:** Visualizes expected cost vs. threshold value
- **Column Filter node:** Removes irrelevant columns before modeling

## Practical Takeaways for Scientists

- Ensemble models almost always outperform single models, especially for complex problems
- XGBoost is currently the go-to algorithm for structured (tabular) data prediction tasks
- Ensemble models sacrifice interpretability for accuracy -- you cannot easily visualize or explain hundreds of trees
- The trade-off between accuracy and interpretability is real: use ensembles when accuracy matters most, simpler models when explanation matters most
- k-fold cross-validation is important for assessing ensemble stability across different data samples
- For binary classification with asymmetric costs, always optimize the threshold -- the default 0.5 is rarely optimal
- Gradient Boosted Trees can overfit if too many trees are built or trees are too deep; use validation data to monitor
- XGBoost includes built-in regularization options that help prevent overfitting
- Random forests are simpler to tune than boosted models and provide a good baseline

## Notable References

- Breiman, L. (1966). Bagging predictors
- Ho, T. K. (1998). The random subspace method for constructing decision forests
- Freund, Y., & Schapire, R. E. (1996). AdaBoost
- Friedman, J. (2001, 2002). Gradient boosting and stochastic gradient boosting
- Chen, T., & Guestrin, C. (1996). XGBoost
- Seni, G., & Elder, J. F. (2010). Ensemble methods in data mining
- Surowiecki, J. (2005). The Wisdom of Crowds
- Wallis, K. F. (2014). Revisiting Francis Galton's forecasting competition
