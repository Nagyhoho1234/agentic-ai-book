# Chapter 6: Feedback Flow from Virtual to Physical -- Foundational Research Needs and Opportunities

## Comprehensive Summary

This chapter addresses the virtual-to-physical direction of the digital twin feedback loop: how the virtual representation drives changes in the physical counterpart through automated control, optimization, decision support, and sensor steering. It also covers human-digital twin interactions and the ethical/social implications of digital twin decision-making.

### Prediction, Control, Steering, and Decision Under Uncertainty

Digital twins support a broad range of decision tasks including:
- Automated control of engineering systems
- Optimized treatment regimens in medicine
- Sensor placement and steering for optimal data collection
- Diagnostic/therapeutic recommendations to human decision-makers

Practical examples (Box 6-1): drug discovery screening, contaminant assessment and control in subsurface water, asset performance management for industrial equipment, thermal management of large motors, and locomotive trip optimization.

Unique challenges for digital twin control and optimization:
- The **scale and complexity** of multiphysics, multiscale systems make optimization computationally challenging even with few decision variables
- **VVUQ** burden is even greater for decision-making tasks because end-to-end uncertainty must be quantified
- Need for **tight, iterative coupling** between data assimilation and optimal control -- possibly in real time on deployed platforms

### Rare Events and Risk Assessment

Many digital twin applications involve characterizing low-probability, high-consequence events (e.g., engineering failures, adverse medical outcomes). Challenges:
- Gap between state-of-the-art risk quantification and tools used in practical decision-making
- Risk metrics like superquantiles are widely used in finance but have limited adoption in engineering
- Many risk measures are non-differentiable, complicating gradient-based optimization
- Monte Carlo sampling is extremely inefficient for low-probability events

### Sensor Steering, Optimal Experimental Design, and Active Learning

A critical class of problems involves optimizing the sensing and observing systems of the physical counterpart:
- Sensor placement, steering, and dynamic scheduling
- Mathematically characterized as **optimal experimental design (OED)** or **active learning**
- Current OED formulations do not scale to the high-dimensional problems anticipated for digital twins
- The OED problem cannot be considered in isolation -- it must be integrated with data assimilation and decision-support tasks (the full **sense-assimilate-predict-control-steer cycle**)

### Real-Time Decision-Making

Many digital twin applications require real-time or near-real-time control. Time scales range from fractions of seconds (engineering control) to hours (clinical decisions). Challenges:
- Surrogate models must be predictive over parameter space and decision variable space, not just state space
- Edge computing may be needed under constraints on precision, power, and communication
- ML models execute rapidly but their black-box nature creates VVUQ challenges

### Dynamic Adaptation in Decision-Making

Digital twins must adapt to new conditions on the fly (new available states, changed transition probabilities, environmental changes). Key gaps:
- Reinforcement learning approaches address this but currently lack theoretical performance guarantees in practical (non-stylized) settings
- Safety-constrained reinforcement learning is beginning to address keeping systems within safe zones
- Dynamically adaptive optimization and control algorithms that exploit sensitivity information from previous solutions are promising

### Model-Centric and Data-Centric Views of Decision-Making

The relative richness or scarcity of data determines the approach:
- **Data-rich**: new opportunities to develop decision-making without explicit system models; however, the digital twin must still assess uncertainty and predict responses to new actions
- **Data-poor**: models must play a greater role; methods for deterministic optimization are mature but solving optimization under uncertainty at digital twin scale remains challenging
- **Adjoint methods** for sensitivity information are powerful but time-intensive, require specialized expertise, and are practically impossible for legacy codebases
- **Automatic differentiation** capabilities need to be advanced, particularly for multiphysics, multiscale, multi-code coupled models

### Human-Digital Twin Interactions

Human-computer interaction in the digital twin context introduces unique challenges:

**Use- and User-Centered Design**: The intended use defines necessary data flows, acceptable uncertainty ranges, and HCI requirements. When digital twins interact continuously with operators, mechanisms must account for human attention fatigue, biases, and the most effective forms of human feedback.

**Communicating Uncertainty**: Effective visualization and communication of uncertainty is critical. Context matters enormously -- weather temperature uncertainty is perceived differently than cancer treatment uncertainty. There is limited research on how the mode of human-digital twin interaction impacts decision quality.

**Building Trust**: Trust in digital twins should not be absolute. Users need to understand parameter ranges where the DT is reliable and which aspects carry what level of trust. Interpretable methods are essential. Digital twins add complexity because they evolve over time in response to new data.

**Data Generation and Collection**: Human interactions with digital twins (button clicks, mouse movements, biometrics) are themselves data sources. Augmented and virtual reality interactions generate additional data. The challenge of standardizing terminologies and ontologies across domains remains.

### Ethics and Social Implications

- Privacy concerns are acute: a digital twin of a human is inherently identifiable
- Models may yield discriminatory results from training data biases or developer biases
- "Victim-blaming" bias: health recommendations may ignore socioeconomic factors that limit a patient's ability to comply
- Multiple humans-in-the-loop (patient, caregivers, providers) create governance complexity

## Key Research Gaps Identified

**Priority 1:**
- Scalable methods for goal-oriented sensor steering and OED encompassing the full sense-assimilate-predict-control-steer cycle
- Trusted ML and surrogate models meeting computational and temporal requirements for real-time decision-making
- Theory and methods for trusted decisions and quantified uncertainty for data-centric digital twins
- Methods and tools to make sensitivity information more readily available (including automatic differentiation for multiphysics, multi-code DTs)
- Implementation science research around digital twins, user-centered design, and human behavior adaptations
- Recognition that content/context/uncertainty presentation impacts decision-making, with limited research on this impact

**Priority 2:**
- Scalable methods to achieve dynamic adaptation in digital twin decision-making
- Uncertainty visualization approaches for human-DT interactions
- Scalable and efficient optimization and UQ methods for non-differentiable functions
- Methods to incorporate state-of-the-art risk metrics in practical DT decision-making contexts

## Practical Takeaways for Scientists

- Design the full sense-assimilate-predict-control-steer cycle as an integrated system, not as separate components -- the interactions matter enormously
- If you need real-time decision support, plan for surrogate models from the start, but ensure they are validated over the decision variable space, not just the state space
- Invest in automatic differentiation capabilities for your codebase -- this is an enabler for scalable model-centric decision-making
- When presenting uncertainty to end users, consider the context carefully -- the same uncertainty range will be interpreted very differently depending on the stakes and time pressure
- If your digital twin involves human interaction, budget for HCI research and user testing -- do not treat the interface as an afterthought
- Be vigilant about bias: audit your training data, your model assumptions, and the socioeconomic context of your recommendations

## Notable References

- Brunke, L., et al. 2022. "Safe Learning in Robotics" (safety-constrained reinforcement learning)
- Ferrari, A. 2023. "Building Robust Digital Twins" (presentation on robust DT foundations)
- Ghattas, O. 2022/2023. (multiple presentations on predictive digital twins, OED, and sensor steering)
- Obermeyer, Z., et al. 2019. "Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations" (algorithmic bias in healthcare)
- Sinha, G., R. Shahi, and M. Shankar. 2010. "Human Computer Interaction" (HCI foundations)
- Trauer, J., et al. 2023. "A Digital Twin Business Modelling Approach" (trust stakeholder analysis)
