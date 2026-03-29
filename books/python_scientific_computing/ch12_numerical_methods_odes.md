# Chapter 12: Numerical Methods for ODEs

## Summary

This chapter covers numerical methods for solving ordinary differential equations, progressing from simple Euler methods to higher-order Runge-Kutta methods and multi-step Adams-Bashforth methods. It emphasizes both scalar and vectorized implementations, compares accuracy and efficiency, and applies these methods to physical problems including the wave equation.

## Key Concepts

### Euler Methods
- **Forward (explicit) Euler**: y_{n+1} = y_n + h*f(t_n, y_n)
  - First-order accuracy, simple to implement
  - Can be unstable for stiff systems
- **Backward (implicit) Euler**: y_{n+1} = y_n + h*f(t_{n+1}, y_{n+1})
  - Requires solving a nonlinear equation at each step (e.g., Newton-Raphson)
  - More stable for stiff systems
- **Error analysis**: local truncation error is O(h^2), global error is O(h)

### Runge-Kutta Methods
- **RK4 (classical 4th-order Runge-Kutta)**: the most widely used single-step method
  - k1 = h*f(t_n, y_n)
  - k2 = h*f(t_n + h/2, y_n + k1/2)
  - k3 = h*f(t_n + h/2, y_n + k2/2)
  - k4 = h*f(t_n + h, y_n + k3)
  - y_{n+1} = y_n + (k1 + 2k2 + 2k3 + k4)/6
- Fourth-order accuracy: global error is O(h^4)
- Excellent balance between accuracy and computational cost

### Adams-Bashforth Methods (Multi-Step)
- Use information from multiple previous steps to achieve higher accuracy
- **2-step Adams-Bashforth**: y_{n+1} = y_n + h*(3f_n - f_{n-1})/2
- Requires initialization with another method (e.g., Euler or RK4)
- More efficient than single-step methods for smooth problems

### Vectorized Code
- Replacing Python loops with NumPy array operations for massive speedup
- Vectorized Euler and RK4 implementations
- Time comparison: vectorized code can be 100x faster than loop-based code
- Essential for large-scale simulations

### Wave Equation
- **1D wave equation**: u_tt = c^2 * u_xx
- **Finite difference discretization** in both space and time
- **Boundary conditions**: fixed ends, periodic, or absorbing
- Visualization using animation of traveling waves
- **CFL condition**: stability requirement relating time step to spatial step

### Taylor Series and Error Analysis
- Taylor series expansion as the theoretical basis for numerical methods
- Local truncation error vs. global error
- Order of accuracy: how error scales with step size h
- Richardson extrapolation for improved accuracy

## Code Examples Described
- Forward Euler method implementation (loop and vectorized versions)
- RK4 implementation for systems of ODEs
- Adams-Bashforth 2-step method
- Vectorized wave equation solver with animation
- Comparison plots of Euler vs. RK4 accuracy
- Timing comparison of loop vs. vectorized implementations

## Key Definitions
- **Step size (h)**: the time increment between successive approximations
- **Local truncation error**: error introduced in a single step
- **Global error**: accumulated error after many steps
- **Order of accuracy**: the power of h in the leading error term
- **Stiff system**: a system where some components change much faster than others, requiring small step sizes or implicit methods
- **CFL condition**: Courant-Friedrichs-Lewy condition for numerical stability

## Practical Takeaways
- RK4 is the default choice for most ODE problems -- it is accurate, stable, and easy to implement
- Always use vectorized code for production computations; loop-based code is only for learning
- SciPy's `odeint` uses adaptive step-size methods that are generally superior to fixed-step methods
- For stiff systems, use implicit methods or SciPy's `solve_ivp` with method='Radau' or 'BDF'
- The wave equation finite difference scheme demonstrates how PDEs can be solved by reducing them to systems of ODEs

## Notable References
- Burden, R.L. and Faires, J.D. (2010). *Numerical Analysis*, 9th Ed. Brooks/Cole
- Trefethen, L.N. (1996). *Finite Difference and Spectral Methods for Ordinary and Partial Differential Equations*, Cornell University
