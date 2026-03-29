# Chapter 3: SymPy

## Summary

This chapter covers SymPy, Python's library for symbolic mathematics. It demonstrates how to perform calculus (differentiation, integration, limits, series), solve equations (algebraic and differential), work with linear algebra (matrices, eigenvalues), and create interactive plots. SymPy provides an alternative to commercial software like Mathematica and Maple for symbolic computation.

## Key Concepts

### SymPy Basics
- **Symbolic variables** declared with `symbols('x y z')` or `Symbol('x')`
- Exact computation: SymPy works with exact fractions, radicals, and symbolic expressions rather than floating-point approximations
- `simplify()`, `expand()`, `factor()`, `collect()` for expression manipulation
- `Rational(p, q)` for exact fractions

### Calculus Operations
- **Differentiation**: `diff(expr, x)` for first derivatives, `diff(expr, x, n)` for nth derivatives
- **Integration**: `integrate(expr, x)` for indefinite, `integrate(expr, (x, a, b))` for definite integrals
- **Limits**: `limit(expr, x, a)` including one-sided limits
- **Taylor series**: `series(expr, x, x0, n)` for series expansion around a point
- **Partial fractions**: `apart(expr, x)` for decomposition

### Differential Equations
- `dsolve(eq, y(x))` for solving ODEs symbolically
- Supports first and second order ODEs
- Handles initial value problems with `ics=` parameter

### Linear Algebra
- `Matrix()` for creating matrices
- Operations: `det()`, `inv()`, `eigenvals()`, `eigenvects()`, `rref()`
- Matrix arithmetic: addition, multiplication, transpose
- Solving linear systems: `solve()` and matrix methods

### Interactive Plotting
- SymPy's built-in `plot()` function for quick symbolic plots
- Interactive plots using matplotlib widgets (sliders, buttons)
- Parameter exploration through interactive visualization

### Complex Numbers
- Operations with complex numbers using `I` for the imaginary unit
- `Abs()`, `arg()`, `re()`, `im()` for complex number properties
- Euler's formula and polar form

## Code Examples Described
- Symbolic differentiation and integration of complex expressions
- Solving systems of algebraic equations
- Solving first and second order ODEs with initial conditions
- Computing eigenvalues and eigenvectors of matrices
- Interactive phase portrait plotter for ODEs
- Plotting parametric curves and 3D surfaces symbolically

## Key Definitions
- **Symbolic computation**: mathematical computation using exact symbolic expressions rather than numerical approximations
- **ODE (Ordinary Differential Equation)**: equation involving derivatives of a function with respect to one variable
- **Eigenvalue/eigenvector**: scalar/vector pair satisfying Av = lambda*v for matrix A
- **Taylor series**: polynomial approximation of a function near a point

## Practical Takeaways
- SymPy eliminates the need for expensive commercial symbolic math software
- Always define symbolic variables before use with `symbols()`
- Use `N(expr)` or `expr.evalf()` to convert symbolic results to numerical values
- SymPy and NumPy serve different purposes: SymPy for exact symbolic math, NumPy for fast numerical computation
- Interactive plots are excellent for exploring parameter spaces in models

## Notable References
- SymPy documentation: https://www.sympy.org
- Meurer, A. et al. (2017). SymPy: symbolic computing in Python. *PeerJ Computer Science*, 3, e103
