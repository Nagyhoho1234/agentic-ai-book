# Chapter 16: Brain Inspired Computing

## Summary

This chapter presents the author's own patented invention of brain-inspired computing using threshold oscillators. It covers the Hodgkin-Huxley neuron model, the simplified FitzHugh-Nagumo (FN) model, and how networks of coupled oscillators can perform binary logic (half-adder) and memory (SR flip-flop) operations. The chapter bridges biological neuroscience with computational hardware design and discusses five potential research avenues for building next-generation computers.

## Key Concepts

### Hodgkin-Huxley Model
- **1952 Nobel Prize-winning model** of neuron action potentials (Hodgkin and Huxley)
- System of four coupled ODEs describing membrane voltage and ion channel gating variables
- Variables: V (membrane potential), m (sodium activation), h (sodium inactivation), n (potassium activation)
- Parameters from experimental data: C = 1 uF/cm^2, g_Na = 120, g_K = 36, g_L = 0.3 mmho/cm^2
- **Threshold behavior**: neuron fires (oscillates) only when input current exceeds threshold I_C = 6.23 mA
- Rate constants alpha and beta for each gating variable are voltage-dependent

### FitzHugh-Nagumo (FN) Model
- **Simplified 2-ODE model** capturing essential neuron dynamics
- du/dt = i + u(u - theta)(1 - u) - v (fast variable, action potential)
- dv/dt = epsilon(u - gamma*v) (slow variable, recovery)
- Parameters theta, gamma, epsilon control threshold, oscillation frequency, and critical points
- **Threshold oscillator**: oscillates only when input current i exceeds a critical value i_T

### Binary Oscillator Half-Adder (Invention)
- **Patented in 2012 and 2015** by Lynch and Borresen
- Uses two threshold oscillators (O1 and O2) with excitatory and inhibitory synaptic connections
- **Excitation**: a pre-synaptic oscillator can switch on a post-synaptic oscillator (via sigmoidal transfer function)
- **Inhibition**: a pre-synaptic oscillator can switch off a post-synaptic oscillator
- Implements XOR (sum) and AND (carry) operations using only oscillator dynamics
- **Key advantage**: oscillation = binary 1, no oscillation = binary 0
- Synaptic weights w1 = 0.8, w2 = 0.45, x1 = -1.5 for excitation and inhibition

### SR Flip-Flop (Memory Device)
- **Set-Reset flip-flop** constructed from two coupled FN oscillators
- Bistable device: can store one bit of information
- Equivalent to conventional NOR-gate SR flip-flop but using threshold oscillators
- **Ballistic propagation**: a single pulse can cause a switch, saving power
- Current I_C keeps oscillators near threshold

### Real-World Applications and Future Work
- **Human brain**: ~10^11 neurons, ~10^15 synapses, only 25W power consumption
- **CMOS limitations**: scaling below 100nm causes manufacturing problems; needs ~megawatts to mimic a brain
- Five research avenues for binary oscillator computing:
  1. **Josephson Junction (JJ) oscillators**: 100M times faster, 1000x smaller than biological neurons
  2. **Biological neuron oscillators**: for modeling neuronal degradation (Alzheimer's, Parkinson's)
  3. **CMOS oscillators**: 65nm artificial neurons demonstrated (Sourikopoulos et al., 2017)
  4. **Memristors**: neuristor-like behavior, structural plasticity
  5. **Optical oscillators**: photonic synapses for brain-like computing
- **Neuronal degradation assay**: using simple neural circuits to test drug effects on diseased neurons

## Code Examples Described
- Hodgkin-Huxley neuron action potential solver (Program_16a.py) showing voltage, gating variables, and input current
- FitzHugh-Nagumo half-adder simulation (Program_16b.py) with four coupled FN equations
- FitzHugh-Nagumo SR flip-flop simulation (Program_16c.py) demonstrating memory storage
- All programs use `scipy.integrate.odeint` for ODE integration

## Key Definitions
- **Threshold oscillator**: a device that oscillates only when input exceeds a critical threshold
- **Excitation**: increasing the input to a neuron/oscillator above its firing threshold
- **Inhibition**: suppressing oscillation by providing negative input
- **Action potential**: the electrical pulse generated when a neuron fires
- **Synaptic weight**: the strength of connection between two neurons/oscillators
- **Half-adder**: logic circuit that adds two single binary digits, producing sum and carry

## Practical Takeaways
- Brain-inspired computing is the opposite of AI: it uses brain dynamics to build computers, while AI uses computers to simulate brains
- Understanding biological neurons is fundamental to both neuroscience and AI
- Simple coupled oscillator networks can perform all basic logic operations
- The Hodgkin-Huxley model, despite being 70 years old, remains the gold standard for neuron modeling
- The FN model is sufficient for computational neuroscience applications where detailed ion channel dynamics are not needed
- Threshold oscillator computing could potentially double processing power with linear (not exponential) increase in components

## Notable References
- Borresen, J. and Lynch, S. (2012). Oscillatory threshold logic. *PLoS ONE*, 7(11): e48498
- Hodgkin, A.L. and Huxley, A.F. (1952). A qualitative description of membrane current. *J. Physiol.*, 117, 500-544
- FitzHugh, R. (1961). Impulses and physiological states in theoretical models of nerve membranes. *Biophys.*, 1182, 445-466
- Lynch, S. et al. (2020). Mathematical modeling of neuronal logic, memory and clocking circuits. *Int. J. of Bifurcation and Chaos*, 30, 2050003
