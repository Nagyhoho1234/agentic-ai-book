# Chapter 13: Numerical Methods for PDEs and Signal Processing

## Summary

This chapter extends numerical methods to partial differential equations (heat equation, advection equation) and introduces signal processing with Fourier transforms. It covers finite difference methods for PDEs, vectorized implementations, the discrete Fourier transform (DFT), fast Fourier transform (FFT), and applications in physics and engineering.

## Key Concepts

### Heat Equation (Diffusion)
- **1D heat equation**: u_t = alpha * u_xx (parabolic PDE)
- **Explicit finite difference** scheme: forward in time, central in space
- **Stability condition**: alpha * dt / dx^2 <= 0.5
- **2D heat equation**: u_t = alpha * (u_xx + u_yy) for heat diffusion in a plate
- Vectorized implementation using array slicing for the spatial Laplacian
- Boundary conditions: Dirichlet (fixed temperature) and Neumann (fixed flux)

### Advection Equation
- **1D advection**: u_t + c * u_x = 0 (hyperbolic PDE)
- **Upwind scheme**: uses one-sided difference in the direction of wave propagation
- **CFL condition**: c * dt / dx <= 1 for stability
- Demonstrates wave propagation without distortion (ideal) vs. numerical diffusion

### Finite Difference Methods
- **Forward difference**: (u_{i+1} - u_i) / dx approximates du/dx
- **Backward difference**: (u_i - u_{i-1}) / dx
- **Central difference**: (u_{i+1} - u_{i-1}) / (2*dx) -- more accurate
- **Second derivative**: (u_{i+1} - 2*u_i + u_{i-1}) / dx^2
- Constructing the difference equations on a grid

### Fourier Transforms and Signal Processing
- **Discrete Fourier Transform (DFT)**: decomposes a signal into frequency components
- **Fast Fourier Transform (FFT)**: efficient algorithm for computing DFT in O(n log n)
- `numpy.fft.fft()` and `numpy.fft.ifft()` for forward and inverse transforms
- **Power spectrum**: |FFT(signal)|^2 shows energy distribution across frequencies
- **Frequency resolution**: determined by sampling rate and signal length

### Physics Applications
- **SFR resonator**: signal frequency response analysis
- **Nonlinear optics**: modeling light propagation in nonlinear media
- **Planetary motion**: Newton's equations for orbital mechanics
- **Josephson junction**: superconducting device showing hysteresis

## Code Examples Described
- 1D heat equation solver with animation showing temperature evolution
- 2D heat diffusion in a plate with boundary conditions
- Advection equation solver comparing upwind and central difference schemes
- FFT analysis of composite signals to identify frequency components
- Power spectrum plotter for signal analysis
- Vectorized PDE solver comparison with loop-based version

## Key Definitions
- **Parabolic PDE**: PDE like the heat equation that describes diffusion processes
- **Hyperbolic PDE**: PDE like the wave/advection equation that describes wave propagation
- **Finite difference method**: numerical technique that approximates derivatives using differences at discrete grid points
- **FFT (Fast Fourier Transform)**: algorithm for efficiently computing the DFT in O(n log n) operations
- **Power spectrum**: distribution of signal energy as a function of frequency

## Practical Takeaways
- The explicit finite difference method for the heat equation is simple but has a restrictive stability condition
- Always check the CFL/stability condition before running a PDE simulation
- Vectorized array slicing (e.g., `U[1:-1] += C * (U[2:] - U[:-2])`) is the key to fast PDE solvers in Python
- FFT is essential for analyzing experimental signals and identifying dominant frequencies
- For production PDE solving, consider FEniCS or SciPy's specialized solvers

## Notable References
- Strikwerda, J.C. (2004). *Finite Difference Schemes and Partial Differential Equations*, SIAM
- Smith, G.D. (1985). *Numerical Solution of Partial Differential Equations*, Oxford University Press
