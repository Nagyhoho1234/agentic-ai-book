# Chapter 6: Dynamical Systems

## Summary

This chapter introduces dynamical systems theory, covering both discrete-time (maps) and continuous-time (ODEs) systems. It presents population models, fixed points, stability analysis, bifurcation diagrams, limit cycles, and chaos. The chapter uses SciPy's `odeint` for numerical integration of ODEs and provides the mathematical foundation for nonlinear dynamics explored in later chapters.

## Key Concepts

### Discrete Dynamical Systems
- **Logistic map**: f(x) = mu*x*(1-x), the canonical example of chaos from a simple equation
- **Fixed points** (steady states): found by solving f(x*) = x*
- **Stability**: determined by the magnitude of the derivative |f'(x*)| -- stable if < 1, unstable if > 1
- **Cobweb diagrams**: graphical iteration showing convergence/divergence from fixed points
- **Period doubling**: route to chaos through successive doublings of the period
- **Bifurcation diagrams**: plotting long-term behavior vs. parameter values, revealing the period-doubling cascade

### Continuous Dynamical Systems
- **Phase portraits**: vector fields showing flow in state space
- **Critical points**: where all derivatives are zero simultaneously
- **Jacobian matrix**: matrix of partial derivatives used to determine local stability
- **Classification**: nodes (stable/unstable), saddle points, spirals (stable/unstable), centers
- **Holling-Tanner predator-prey model**: ecological dynamics with functional response

### Population Models
- **Logistic growth**: S-shaped curve with carrying capacity
- **Predator-prey systems**: coupled ODEs modeling interacting species (e.g., lynx-snowshoe hare data)
- **SIR model preview**: epidemiological models introduced (expanded in Chapter 7)
- **Blood cell population model**: physiological application of delay differential equations

### Bifurcation Theory
- **Fold bifurcation**: two fixed points collide and annihilate
- **Period-doubling bifurcation**: stable fixed point loses stability, period-2 orbit emerges
- **Feigenbaum constant** (delta = 4.669...): universal ratio of successive bifurcation intervals
- **Chaos**: deterministic yet unpredictable behavior; sensitive dependence on initial conditions

### Hysteresis
- Systems where the state depends on history, not just current parameters
- **Muscle model**: physiological example of hysteresis (eccentric vs. concentric contraction)

## Code Examples Described
- Cobweb diagram generator for the logistic map
- Bifurcation diagram plotter for discrete maps
- Phase portrait plotter using `odeint` for 2D ODE systems
- Predator-prey simulation with time series and phase plane plots
- COVID-19 SIR model fitting to real data
- Flu model with seasonal forcing

## Key Definitions
- **Dynamical system**: mathematical model describing the time evolution of a system's state
- **Bifurcation**: qualitative change in system behavior as a parameter varies
- **Chaos**: bounded, deterministic behavior that is sensitive to initial conditions and appears random
- **Limit cycle**: isolated periodic orbit in a continuous dynamical system
- **Phase portrait**: plot of trajectories in state space showing the qualitative behavior of a system

## Practical Takeaways
- Simple equations like the logistic map can produce extremely complex behavior
- Bifurcation diagrams are essential for understanding how system behavior changes with parameters
- SciPy's `odeint` is the workhorse for numerically solving systems of ODEs in Python
- Population models are directly applicable to ecology, epidemiology, and physiology
- The Jacobian matrix is the key tool for local stability analysis of nonlinear systems

## Notable References
- Lynch, S. (2018). *Dynamical Systems with Applications using Python*, Springer
- Strogatz, S.H. (2015). *Nonlinear Dynamics and Chaos*, Westview Press
- May, R.M. (1976). Simple mathematical models with very complicated dynamics. *Nature*, 261, 459-467
