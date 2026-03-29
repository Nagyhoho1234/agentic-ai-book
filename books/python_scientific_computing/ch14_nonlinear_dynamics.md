# Chapter 14: Nonlinear Dynamics and Hysteresis

## Summary

This chapter delves deeper into nonlinear dynamics, covering hysteresis phenomena, periodically forced systems, the Ikeda map, Josephson junctions, and Newton's equations for planetary bodies. It emphasizes the practical importance of hysteresis in physics and engineering, and demonstrates how Python can reveal complex dynamical behaviors.

## Key Concepts

### Hysteresis
- **Hysteresis**: system behavior depends on history; different paths for increasing vs. decreasing parameters
- **Duffing oscillator hysteresis**: amplitude jumps when forcing frequency is swept up vs. down
- **Pinched hysteresis**: characteristic of memristors, where the I-V curve passes through the origin
- **Memristors**: fourth fundamental circuit element predicted by Chua (1971), discovered by HP Labs (2008)
- Applications in nonvolatile memory, neuromorphic computing

### Periodically Forced Systems
- **Duffing equation with forcing**: demonstrates transition from periodic to chaotic motion
- **Bifurcation diagrams** as a function of forcing amplitude
- **Poincare sections**: sampling the phase portrait at multiples of the forcing period
- **Power spectrum analysis**: using FFT to distinguish periodic, quasiperiodic, and chaotic motion

### Ikeda Map
- **Ikeda map**: 2D discrete map modeling light in a ring cavity with nonlinear optical medium
- Parameters: A (laser amplitude), B (coupling coefficient)
- Exhibits fixed points, period doubling, and chaos
- Bifurcation diagrams and Lyapunov exponents

### Josephson Junctions (JJ)
- **Josephson effect**: quantum mechanical phenomenon in superconducting circuits
- **JJ equations**: coupled ODEs describing phase difference and voltage across the junction
- **Hysteresis in JJs**: different I-V curves for increasing vs. decreasing current
- **SFR (Single Flux Resonator)**: Josephson junction coupled to a resonant cavity
- Applications in quantum computing, SQUID magnetometers, superconducting electronics

### Newton's Equations and Planetary Motion
- **N-body problem**: simulating gravitational interactions between multiple bodies
- **Planetary orbits**: numerical integration of Keplerian and perturbed orbits
- Demonstrates sensitivity to initial conditions in gravitational dynamics

## Code Examples Described
- Duffing oscillator hysteresis loop with frequency sweep
- Bifurcation diagram for the forced Duffing equation
- Ikeda map bifurcation diagram and attractor visualization
- Josephson junction I-V curve with hysteresis
- Memristor pinched hysteresis loop simulation
- Planetary orbit simulator using RK4

## Key Definitions
- **Hysteresis loop**: closed curve in parameter-response space showing history-dependent behavior
- **Poincare section**: cross-section of a phase space trajectory, reducing continuous dynamics to a discrete map
- **Memristor**: circuit element whose resistance depends on the history of current flow
- **Josephson junction**: superconducting device exhibiting macroscopic quantum effects
- **Quasiperiodic motion**: motion with two or more incommensurate frequencies

## Practical Takeaways
- Hysteresis is ubiquitous in physical systems and must be accounted for in modeling and measurement
- Bifurcation diagrams are the essential tool for mapping out parameter-dependent behavior
- Power spectrum analysis (via FFT) provides a complementary view to bifurcation diagrams
- Josephson junctions are the basis for superconducting quantum computing -- understanding their dynamics is increasingly important
- The transition from periodic to chaotic motion can be smooth (quasiperiodic route) or abrupt (intermittency)

## Notable References
- Lynch, S. (2018). *Dynamical Systems with Applications using Python*, Springer
- Strogatz, S.H. (2015). *Nonlinear Dynamics and Chaos*, Westview Press
- Chua, L.O. (1971). Memristor -- the missing circuit element. *IEEE Trans. Circuit Theory*, 18, 507-519
