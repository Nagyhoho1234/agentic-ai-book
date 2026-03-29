# Chapter 7: Assessing Classification Models

## Summary

This chapter is devoted entirely to the critical topic of how to properly evaluate classification models. It goes well beyond simple accuracy to cover a comprehensive set of assessment metrics, visualization tools, and practical considerations including asymmetric misclassification costs. This is one of the most practically important chapters in the book.

### The Confusion Matrix

The foundation of classification assessment is the confusion matrix (for binary classification):

|  | Predicted Positive | Predicted Negative |
|--|--------------------|--------------------|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

### Key Metrics Derived from the Confusion Matrix

- **Accuracy:** (TP + TN) / Total -- overall correctness, but misleading with imbalanced data
- **Sensitivity (Recall, True Positive Rate):** TP / (TP + FN) -- ability to correctly identify positive cases
- **Specificity (True Negative Rate):** TN / (TN + FP) -- ability to correctly identify negative cases
- **Precision (Positive Predictive Value):** TP / (TP + FP) -- proportion of positive predictions that are correct
- **F1 Score:** Harmonic mean of precision and recall: 2 * (Precision * Recall) / (Precision + Recall)
- **Cohen's Kappa:** Measures agreement beyond chance; accounts for class distribution

### ROC and AUC

- **ROC Curve (Receiver Operating Characteristic):** Plots sensitivity vs. (1 - specificity) across all possible thresholds
- **AUC (Area Under the Curve):** Single number summary of the ROC curve; 0.5 = random guessing, 1.0 = perfect classification
- AUC is threshold-independent and insensitive to class imbalance, making it one of the most robust metrics

### Lift and Gain Charts

- **Lift chart:** Shows how much better the model performs compared to random selection at various percentages of the population
- **Gain chart (cumulative response curve):** Shows the cumulative percentage of positives captured as you move down the ranked predictions
- Particularly useful in marketing applications (e.g., targeting the top 20% of customers captures what percentage of buyers?)

### Cost-Sensitive Analysis

The chapter emphasizes that different types of errors have different costs:
- In medical diagnosis, a false negative (missing a disease) is typically much more costly than a false positive
- In credit decisions, approving a bad loan (false positive) has different costs than rejecting a good customer (false negative)
- The optimal threshold should minimize expected total cost, not maximize accuracy

### A Thought Problem

The chapter presents an interesting thought experiment about the asymmetric benefits of correct classifications. Sometimes correctly identifying the negative class has no actionable value (e.g., correctly predicting a customer will not churn provides no new information for action), while correctly identifying the positive class enables intervention.

## Key Visual Programming Techniques

- **Scorer node:** Generates confusion matrix, accuracy, Cohen's Kappa, sensitivity, specificity
- **ROC Curve node:** Generates ROC curve and computes AUC
- **Lift Chart node:** Creates gain and lift charts
- **Column Expressions node:** Custom cost calculations using if-then logic
- **Math Formula node:** Computing expected costs
- **Parameter Optimization Loop:** Finding the threshold that minimizes expected cost
- **Line Plot node:** Visualizing cost vs. threshold

## Practical Takeaways for Scientists

- Accuracy alone is almost never sufficient -- always examine sensitivity, specificity, and the full confusion matrix
- For imbalanced datasets, accuracy is especially misleading; use AUC, F1, or Cohen's Kappa instead
- Set the classification threshold based on the business costs of different error types, not at 0.5 by default
- ROC curves allow you to visualize the sensitivity/specificity trade-off and choose an operating point
- Lift charts are invaluable when the question is "which subset of cases should I target?" rather than "classify every case"
- Always evaluate on held-out test data; training-set metrics are optimistically biased
- Cohen's Kappa above 0.4 is considered moderate agreement; above 0.6 is substantial

## Notable References

- Cohen's Kappa statistic (Cohen, 1960)
- ROC analysis theory and applications
- Cost-sensitive classification literature
- Employee churn prediction as running example
