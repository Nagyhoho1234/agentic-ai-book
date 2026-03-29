# Chapter 5: Applied Mathematics

## Summary

This chapter applies Python to solve practical problems in applied mathematics, covering sequences and series, calculus applications, physics problems (kinematics, forces, projectile motion), probability, and hypothesis testing. It demonstrates how Python can replace tedious hand calculations in real-world scientific and engineering problems.

## Key Concepts

### Sequences and Series
- **Arithmetic sequences**: constant difference between terms; `range()` and list comprehensions for generation
- **Geometric series**: constant ratio between terms; formula for sum of infinite geometric series
- **Convergence tests**: determining whether infinite series converge
- **Function composition**: g(f(x)) computed symbolically with SymPy

### Applied Calculus
- **Chain rule, product rule, quotient rule**: implemented symbolically
- **Integration by substitution and by parts**: automated with SymPy
- **Partial fractions**: decomposition for integration of rational functions
- **Parametric equations**: curves defined by x(t), y(t) with derivatives dy/dx = (dy/dt)/(dx/dt)

### Physics Applications
- **Kinematics**: SUVAT equations for constant acceleration motion
- **Projectile motion**: trajectory computation including air resistance
- **Forces**: resolving forces in 2D, friction coefficients, equilibrium conditions
- **Moments**: calculating torques and rotational equilibrium

### Probability and Statistics
- **Probability density functions**: continuous probability distributions
- **Normal distribution**: z-scores, standard normal tables, probability calculations
- **Hypothesis testing**: formal procedure with null/alternative hypotheses, significance levels, and conclusions
- **Applications**: drug efficacy testing, quality control, population studies

### Numerical Integration
- Using `scipy.integrate.quad()` for numerical integration
- Comparison between symbolic and numerical integration methods

## Code Examples Described
- Computing partial sums of series and checking convergence
- Solving projectile motion problems with visualization of trajectories
- Force resolution diagrams with vector plots
- Statistical hypothesis testing for drug trial data
- Numerical integration of functions without closed-form antiderivatives

## Key Definitions
- **Convergence**: a series converges if the sequence of partial sums approaches a finite limit
- **SUVAT equations**: five equations relating displacement (s), initial velocity (u), final velocity (v), acceleration (a), and time (t)
- **z-score**: the number of standard deviations a data point is from the mean
- **Significance level (alpha)**: the probability threshold below which the null hypothesis is rejected

## Practical Takeaways
- SymPy can verify hand calculations in calculus, providing a safety net for complex derivations
- Python eliminates the tedium of physics calculations while maintaining exact results
- Statistical hypothesis testing is straightforward to implement and can be applied to experimental data immediately
- For integrals without closed-form solutions, SciPy's numerical integration provides reliable results
- Combining symbolic and numerical approaches gives both insight and practical answers

## Notable References
- Nearing, J. (2003). *Mathematical Tools for Physics*, Dover
- Riley, K.F. et al. (2006). *Mathematical Methods for Physics and Engineering*, Cambridge University Press
