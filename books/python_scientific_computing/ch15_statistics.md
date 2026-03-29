# Chapter 15: Statistics

## Summary

This chapter covers essential statistical methods implemented in Python, including linear regression, Markov chains, statistical tests (t-test, Levene's test), probability distributions, and Monte Carlo simulation. It uses SciPy's statistics module and demonstrates practical data analysis workflows applicable to scientific research.

## Key Concepts

### Linear Regression
- **Simple linear regression**: fitting y = mx + b to data using `scipy.stats.linregress()`
- **Coefficient of determination (R^2)**: measure of how well the regression explains variance
- **Residual analysis**: examining the difference between observed and predicted values
- **Durbin-Watson test**: detecting autocorrelation in residuals
- Application to carbon dioxide emissions data

### Probability Distributions
- **Normal (Gaussian) distribution**: bell curve characterized by mean and standard deviation
- **t-distribution**: used when sample size is small and population variance unknown
- **Probability plots (Q-Q plots)**: comparing data distribution to theoretical distribution
- **Probability distribution curves**: plotting PDFs using SciPy's `stats.norm.pdf()`
- **Box-and-whisker plots**: visualizing data distribution, quartiles, and outliers
- **Quantile-quantile plots**: assessing normality of data

### Statistical Tests
- **Student's t-test**: comparing means of two groups
  - `scipy.stats.ttest_ind()` for independent samples
- **Levene's test**: testing equality of variances between groups
  - `scipy.stats.levene()` -- prerequisite for valid t-test
- **ANOVA (Analysis of Variance)**: comparing means of three or more groups (referenced in exercises)
- **p-values**: probability of obtaining test results under the null hypothesis
- **Significance level**: typically alpha = 0.05

### Markov Chains
- **Transition matrix**: T[i,j] = probability of moving from state i to state j
- **Directed graphs**: visual representation of state transitions
- **Steady-state vector**: long-run probability distribution satisfying v*T = v
- **Convergence**: iterated multiplication of transition matrix converges to steady state
- Example: bull-bear-stagnant market system

### Monte Carlo Simulation
- Formal foundations by von Neumann and Ulam in the 1940s
- **European roulette simulation**: demonstrating that the house always wins
  - 37 pockets (0-36), probability of winning on red = 18/37
  - 100 simulations of 3,700 spins showing bankroll trajectories
  - Average bankroll converges to 5,000 euros after 1,850 spins (losing half the initial 10,000)
- Applications: estimating pi, solving integrals, financial risk assessment

### Descriptive Statistics
- **Skewness**: measure of asymmetry in data distribution
- **Kurtosis**: measure of tail heaviness relative to normal distribution
- **Omnibus test**: combined test for skewness and kurtosis
- **Jarque-Bera test**: testing normality based on skewness and kurtosis

## Code Examples Described
- Linear regression with prediction interval and residual plots
- Normal distribution PDF plotting and probability calculations
- Student's t-test comparing two datasets with Levene's test
- Markov chain steady-state computation and convergence visualization
- Monte Carlo roulette simulation showing bankroll evolution across 100 gamblers
- Box-and-whisker plots and Q-Q plots for data exploration

## Key Definitions
- **p-value**: probability of obtaining results at least as extreme as observed, assuming the null hypothesis is true
- **Markov chain**: stochastic process where future state depends only on current state (memoryless property)
- **Monte Carlo simulation**: computational technique using repeated random sampling to obtain numerical results
- **Steady-state distribution**: the probability vector that remains unchanged under the transition matrix
- **Coefficient of determination (R^2)**: proportion of variance in the dependent variable explained by the model

## Practical Takeaways
- Always check assumptions (normality, equal variances) before applying parametric statistical tests
- Levene's test should precede the t-test to verify the equal variance assumption
- Markov chains are useful for modeling systems that transition between discrete states (market conditions, weather, queues)
- Monte Carlo simulation is a versatile tool for problems that are analytically intractable
- The roulette example vividly demonstrates the law of large numbers: short-term luck averages out to the house edge

## Notable References
- Barbu, A. (2020). *Monte Carlo Methods*, Springer
- Haslwanter, T. (2018). *An Introduction to Statistics with Python*, Springer
- Frost, J. (2020). *Regression Analysis*, Statistics by Jim Publishing
- Privault, N. (2018). *Understanding Markov Chains*, Springer
