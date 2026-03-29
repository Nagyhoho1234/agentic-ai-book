# Chapter 9: Finance

## Summary

This chapter applies Python to financial mathematics, covering Modern Portfolio Theory (MPT), mean-variance analysis, the efficient frontier, the Black-Scholes option pricing model, and the Greeks. It demonstrates how Python can be used for portfolio optimization, derivatives pricing, and financial data analysis.

## Key Concepts

### Modern Portfolio Theory (MPT)
- **Harry Markowitz** (1952): foundational framework for portfolio selection
- **Expected return**: weighted average of individual asset returns
- **Portfolio variance**: accounts for correlations between assets (covariance matrix)
- **Sharpe ratio**: risk-adjusted return metric = (E[R] - Rf) / sigma
- **Efficient frontier**: set of portfolios offering maximum return for given risk level

### Mean-Variance Analysis
- **Two-asset portfolio**: combining two assets to minimize risk at desired return
- **Covariance** and **correlation** between asset returns determine diversification benefits
- **Risk-free rate**: return from a safe asset (e.g., government bonds)
- Plotting the efficient frontier curve in risk-return space

### Black-Scholes Model
- **Option pricing formula** for European call and put options
- **Assumptions**: continuous trading, no dividends, log-normal price distribution, constant volatility and interest rate
- **Call option**: C = S*N(d1) - K*exp(-rT)*N(d2)
- **Put option**: P = K*exp(-rT)*N(-d2) - S*N(-d1)
- Where d1 and d2 involve stock price S, strike price K, risk-free rate r, time T, and volatility sigma

### The Greeks
- **Delta**: rate of change of option price with respect to underlying asset price
- **Gamma**: rate of change of delta with respect to underlying price (second derivative)
- **Vega**: sensitivity of option price to volatility changes
- **Theta**: rate of change of option price with respect to time (time decay)
- **Rho**: sensitivity of option price to interest rate changes
- Using the `py_vollib` library for computing Black-Scholes and Greeks

### Financial Data Analysis
- Using Pandas for time series financial data
- Plotting stock price data and returns
- Durbin-Watson test for autocorrelation in financial returns
- Omnibus test for normality of returns
- Skewness and kurtosis of return distributions
- Jarque-Bera test for normality

## Code Examples Described
- Portfolio optimization with two assets showing the efficient frontier
- Mean-variance optimization with Sharpe ratio maximization
- Black-Scholes option pricing calculator
- Greeks computation and visualization
- Statistical analysis of financial return distributions
- Financial data import and visualization with Pandas

## Key Definitions
- **Efficient frontier**: the set of portfolios that maximize expected return for each level of risk
- **Sharpe ratio**: (expected return - risk-free rate) / standard deviation; measures risk-adjusted performance
- **Volatility**: standard deviation of returns; measure of price variability
- **European option**: an option that can only be exercised at expiration
- **The Greeks**: partial derivatives of the option price with respect to various parameters

## Practical Takeaways
- MPT provides a systematic framework for portfolio construction that can be implemented in a few lines of Python
- The efficient frontier visualization helps investors understand the risk-return tradeoff
- The `py_vollib` library simplifies Black-Scholes calculations and Greeks computation
- Financial returns are rarely perfectly normally distributed; always test assumptions
- Python enables rapid prototyping of financial models that would be tedious to compute by hand

## Notable References
- Hull, J.C. (2022). *Options, Futures, and Other Derivatives*, 11th Ed. Pearson
- Markowitz, H. (1952). Portfolio selection. *J. Finance*, 7, 77-91
- Black, F. and Scholes, M. (1973). The pricing of options and corporate liabilities. *J. Political Economy*, 81, 637-654
