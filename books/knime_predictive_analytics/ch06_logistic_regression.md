# Chapter 6: Logistic Regression

## Summary

This chapter covers logistic regression, the standard technique for predicting binary (yes/no) outcomes. Unlike linear regression which predicts a continuous value, logistic regression predicts the probability that an observation belongs to a particular class. The chapter covers the mathematical foundation, model building, interpretation, and practical applications using KNIME.

### Core Concepts

- **Binary classification:** Predicting one of two outcomes (e.g., churn/no churn, default/no default, disease/no disease)
- **Logistic function (sigmoid):** Maps any real number to a probability between 0 and 1: P(Y=1) = 1 / (1 + exp(-(b0 + b1*X1 + ... + bp*Xp)))
- **Odds and odds ratio:** The odds are P/(1-P); the log-odds (logit) is a linear function of the predictors
- **Coefficient interpretation:** Each coefficient represents the change in log-odds for a one-unit change in the predictor
- **Threshold (cutoff):** The probability above which an observation is classified as the positive class; default is 0.5 but should be adjusted based on business costs

### Handling Imbalanced Data

A major practical issue addressed in this chapter is class imbalance -- when one class is much more frequent than the other:
- **SMOTE (Synthetic Minority Over-sampling Technique):** Creates synthetic examples of the minority class
- **Oversampling:** Duplicating minority class observations
- **Undersampling:** Removing majority class observations
- **Cost-sensitive thresholds:** Adjusting the classification threshold rather than resampling

### Example Applications

The chapter uses an employee turnover dataset to predict which employees are likely to leave. The workflow includes:
- Data preparation (log transformation of years at company, dummy coding of department and salary)
- SMOTE for balancing the classes
- Logistic regression model training
- Prediction and assessment using confusion matrices

## Key Visual Programming Techniques

- **Logistic Regression Learner node:** Fits the logistic model; outputs model, coefficients with statistics, and learning properties
- **Logistic Regression Predictor node:** Applies the model to generate class predictions and probabilities
- **SMOTE node:** Oversamples minority class using synthetic interpolation
- **Scorer node:** Generates confusion matrix and accuracy statistics
- **Math Formula node:** For variable transformations (e.g., log transformation)
- **ROC Curve node:** Visualizes the trade-off between true positive rate and false positive rate
- **Threshold adjustment:** Using predicted probabilities and a custom threshold instead of the default 0.5

## Practical Takeaways for Scientists

- Logistic regression is highly interpretable -- you can understand which factors drive the prediction and by how much
- Always check for class imbalance; a model that predicts "no event" for everything can still have high accuracy if events are rare
- SMOTE is generally preferred over simple oversampling because it creates diverse synthetic examples rather than duplicates
- The classification threshold should be set based on the relative costs of false positives vs. false negatives, not blindly at 0.5
- Logistic regression coefficients are in log-odds units; exponentiate them to get odds ratios for easier interpretation
- The model outputs class probabilities, which are often more useful than hard class assignments
- Use test data (not training data) to assess model performance

## Notable References

- Employee turnover dataset for churn prediction
- SMOTE technique (Chawla et al., 2002)
- Logistic regression theory and application guidelines
