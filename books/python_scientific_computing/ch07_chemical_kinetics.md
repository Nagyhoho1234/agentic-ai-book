# Chapter 7: Chemical Kinetics and SIR Models

## Summary

This chapter applies Python to chemical kinetics and reaction modeling. It covers balancing chemical equations, chemical equilibrium, Le Chatelier's principle, the common-ion effect, solubility curves, ozone layer chemistry, and the Chapman cycle. Pandas DataFrames are introduced for data management of chemical and environmental datasets.

## Key Concepts

### Chemical Reaction Equations
- **Balancing equations**: using SymPy's linear algebra to balance chemical equations systematically
- Example: sodium bicarbonate and citric acid reaction
- Matrix method for balancing complex reactions

### Chemical Equilibrium
- **Equilibrium constant (K)**: ratio of product concentrations to reactant concentrations at equilibrium
- **Le Chatelier's principle**: systems shift to counteract disturbances (temperature, pressure, concentration)
- **Common-ion effect**: reduction in solubility of a salt when a common ion is added
- **Silver chloride (AgCl)** solubility as a function of KCl concentration

### Reaction Kinetics
- **Rate equations**: differential equations describing concentration changes over time
- **First-order reactions**: exponential decay of reactant concentration
- **Autocatalysis**: reactions where a product catalyzes the reaction (e.g., Belousov-Zhabotinski reaction)
- **Brusselator model**: theoretical model exhibiting oscillating chemical reactions

### Ozone Chemistry
- **Chapman cycle**: four reactions governing stratospheric ozone production and destruction
- Modeling O, O2, and O3 concentrations as a system of ODEs
- **Stiff systems**: reactions occurring on vastly different timescales requiring specialized numerical methods
- Singlet and triplet oxygen chemistry

### Pandas DataFrames
- Creating and manipulating DataFrames for chemical data
- Reading/writing CSV files
- Data cleaning and filtering
- Plotting from DataFrames using matplotlib

## Code Examples Described
- Automatic chemical equation balancer using matrix null space
- Solubility curve plotter for AgCl vs. KCl concentration
- Chapman cycle ODE system solver showing ozone dynamics
- Autocatalytic reaction simulation
- Belousov-Zhabotinski oscillating reaction model
- Pandas-based analysis of chemical concentration data

## Key Definitions
- **Chemical kinetics**: study of rates of chemical reactions and the factors that affect them
- **Equilibrium constant (K)**: quantitative measure of the position of equilibrium for a reversible reaction
- **Stiff system**: ODE system with widely separated time scales, requiring implicit numerical methods
- **Autocatalysis**: a reaction in which one of the products is also a reactant/catalyst

## Practical Takeaways
- SymPy's linear algebra can systematically balance even complex chemical equations
- Chemical equilibrium problems translate directly to systems of nonlinear equations solvable with Python
- Ozone chemistry demonstrates the importance of handling stiff ODE systems properly
- Pandas provides the data management backbone for chemical and environmental datasets
- The Belousov-Zhabotinski reaction shows that chemical systems can exhibit dynamical behavior analogous to biological oscillators

## Notable References
- Connors, K.A. (1990). *Chemical Kinetics*, VCH Publishers
- Pilling, M.J. and Seakins, P.W. (1996). *Reaction Kinetics*, Oxford University Press
