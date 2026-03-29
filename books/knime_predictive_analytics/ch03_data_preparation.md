# Chapter 3: Data Preparation

## Summary

This chapter covers the most time-consuming phase of any analytics project -- data preparation. Studies consistently show that 60-80% of a data scientist's time is spent on data preparation. The chapter addresses data quality issues, missing values, variable transformations, and feature engineering, all implemented through KNIME's visual nodes.

### Data Quality and Cleaning

Common data quality problems include:
- **Missing values:** Can be handled by deletion (row or column), imputation (mean, median, mode, regression-based), or indicator variables
- **Outliers:** Extreme values that may be errors or genuine rare observations; can be identified with box plots, z-scores, or domain knowledge
- **Inconsistent formatting:** Mixed date formats, inconsistent category labels, encoding issues
- **Duplicate records:** Identified and handled with GroupBy or duplicate detection nodes

### Variable Transformations

The chapter covers several types of transformations:
- **Normalization:** Min-max scaling (to 0-1 range) and z-score standardization (zero mean, unit variance)
- **Logarithmic transformations:** For skewed distributions
- **Binning:** Converting continuous variables to categorical (equal-width or equal-frequency)
- **One-to-Many (dummy coding):** Converting categorical variables to binary indicators for algorithms that require numeric input
- **Recoding:** Combining categories, renaming levels

### Feature Engineering

- **Deriving new variables:** Using Math Formula nodes to create computed columns
- **Column filtering:** Removing irrelevant or redundant variables
- **Sampling and partitioning:** Creating training and test sets with stratified sampling to preserve class distributions

## Key Visual Programming Techniques

- **File Reader node:** Reads CSV/Excel with automatic type detection
- **Missing Value node:** Configurable strategies per column (mean, median, mode, fixed value, remove row)
- **Column Filter node:** Select/deselect columns by name, type, or pattern
- **Row Filter node:** Filter rows by condition or row number
- **Math Formula node:** Create calculated columns using an expression language
- **Normalizer node:** Min-max or z-score normalization with model output for applying same transformation to new data
- **One to Many node:** Automatic dummy variable creation from categorical columns
- **Partitioning node:** Split data into training/test sets with stratified sampling options
- **Column Rename node:** Rename columns for clarity
- **Column Aggregator / GroupBy node:** Aggregate data by groups
- **Column List Loop Start:** Loop over columns to apply the same operation to multiple variables

## Practical Takeaways for Scientists

- Always inspect your data before modeling -- the Data Explorer and Statistics nodes are your first stop
- Missing values must be addressed before most algorithms can run; the strategy depends on the mechanism of missingness and the percentage missing
- Normalization is critical for distance-based algorithms (kNN, neural networks, clustering) but not needed for tree-based methods
- Dummy coding is required for algorithms that cannot handle categorical inputs directly (neural networks, kNN)
- Stratified sampling preserves the class distribution of the target variable in both training and test sets -- always use it for imbalanced datasets
- Keep the Normalizer's model output port -- you will need it to apply the same normalization to test/new data
- Document your data preparation steps; the KNIME workflow itself serves as documentation

## Notable References

- Best practices for handling missing data in analytics
- Data quality assessment frameworks
- KNIME documentation for data manipulation nodes
