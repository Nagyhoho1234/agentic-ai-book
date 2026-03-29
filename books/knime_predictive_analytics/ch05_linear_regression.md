# Chapter 5: Linear Regression

## Summary

This chapter covers linear regression as the foundational supervised learning technique for predicting continuous target variables. It begins with simple linear regression (one predictor) and extends to multiple regression (many predictors), covering model building, interpretation, diagnostics, and assessment using KNIME workflows.

### Core Concepts

- **Simple linear regression:** Y = b0 + b1*X + error. The model finds the line that minimizes the sum of squared residuals (ordinary least squares, OLS)
- **Multiple regression:** Y = b0 + b1*X1 + b2*X2 + ... + bp*Xp + error. Extends to multiple predictors
- **Coefficients:** Each bi represents the change in Y for a one-unit change in Xi, holding all other predictors constant
- **R-squared:** The proportion of variance in Y explained by the model; ranges from 0 to 1
- **Adjusted R-squared:** Penalizes for the number of predictors to discourage overfitting

### Model Diagnostics

- **Residual analysis:** Residuals should be approximately normally distributed with constant variance
- **Multicollinearity:** High correlations among predictors inflate standard errors and make coefficients unstable; detected via correlation matrices
- **Outliers and influential observations:** Can disproportionately affect the regression line

### Model Assessment

- **RMSE (Root Mean Squared Error):** Standard metric for regression accuracy
- **MAE (Mean Absolute Error):** Less sensitive to outliers than RMSE
- **MAPE (Mean Absolute Percentage Error):** Expressed as a percentage, useful for comparing across different scales
- Training vs. test set performance comparison to detect overfitting

### Example Applications

The chapter uses the Toyota Corolla dataset to predict used car prices based on age, mileage, horsepower, fuel type, and other features. A KNIME workflow demonstrates reading data, partitioning into training/test sets, fitting the model, making predictions, and computing accuracy metrics.

## Key Visual Programming Techniques

- **Linear Regression Learner node:** Fits the regression model on training data; outputs the model and coefficient statistics
- **Regression Predictor node:** Applies the trained model to new data to generate predictions
- **Numeric Scorer node:** Computes RMSE, MAE, MAPE, and R-squared for comparing predicted vs. actual values
- **Partitioning node:** Creates training and test data splits with stratified or random sampling
- **Column Filter node:** Selects relevant predictor variables
- **Scatter Plot / Line Plot nodes:** Visualize relationships and model fit
- The workflow pattern: File Reader -> Data Prep -> Partitioning -> Learner (training) -> Predictor (test) -> Scorer

## Practical Takeaways for Scientists

- Linear regression is interpretable: each coefficient tells you the direction and magnitude of a predictor's effect
- Always check residuals for patterns -- non-random patterns indicate model misspecification
- Use the test set for final accuracy assessment, not the training set
- RMSE is the most common accuracy metric for regression, but consider MAE for datasets with outliers
- Multicollinearity does not affect prediction accuracy, but it makes individual coefficient interpretation unreliable
- Include only meaningful predictors -- adding irrelevant variables can degrade test-set performance
- The KNIME workflow provides a complete audit trail of the analysis

## Notable References

- OLS regression theory and assumptions
- Toyota Corolla dataset from Kaggle
- KNIME regression node documentation
