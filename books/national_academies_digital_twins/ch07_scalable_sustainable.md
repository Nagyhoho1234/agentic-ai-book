# Chapter 7: Toward Scalable and Sustainable Digital Twins

## Comprehensive Summary

This chapter addresses the crosscutting challenges of making digital twins scalable, sustainable, and translatable across domains. It covers digital twin evolution and lifecycle management, infrastructure scalability, cross-domain translation of methods, model and data collaborations, and workforce development.

### Evolution and Sustainability of a Digital Twin

Digital twins build on decades of computational, mathematical, statistical, and data science research across disciplines. They operate at the convergence of data acquisition (sensors), data generation (models and simulations), large-scale computations (algorithms), visualization, networks, and validation in a secured framework.

Key sustainability challenges:
- Component attributes (model, data, workflows) must be formally described and changeable while preserving integrity across evolution
- Model management requires standards, APIs, and processes for maintaining bidirectional workflows
- Self-monitoring, reporting, tuning, and revision management are essential
- Predictions must be reproducible, improvable, and reusable across scenarios
- The design approach must be holistic, robust, enduring, yet flexible, composable, and adaptable

**The committee introduces a critical insight**: the notion of a digital twin gives inherent value to the virtual representation itself. The mathematical, statistical, and computational models and data are an **asset** that should receive investment and sustainment paralleling the physical counterpart (Conclusion 7-1).

Communities lack a clear definition of digital twin sustainability and lifecycle management. Existing literature focuses on creation and deployment, with little attention to maintenance or end-of-life management.

### Scalability of Digital Twin Infrastructure

Successful adoption requires holistic hardware and software infrastructure spanning:
- Hand-held mobile devices to large-scale HPC installations
- In situ, nearby, and remote access models
- Heterogeneous and distributed infrastructure

Technical requirements:
- Massive CPU/GPU systems, vast memory, low-latency high-bandwidth networks
- Not all workloads suit GPU architectures (e.g., discrete event simulations)
- Cloud computing for dynamically changing computational power vs. persistent infrastructure for other components
- Federation of individual, best-of-breed simulations rather than monolithic software systems
- Application programming interfaces (APIs) for coupling simulations
- Simulations must run faster than real time to support what-if scenarios

A significant practical barrier: many high-value applications (emergency response, disaster management) depend on mobile infrastructure with lower bandwidth and higher latencies than fixed infrastructure. Solutions include:
- Deploying compact surrogate models on end-user devices
- Edge computing (intermediate solutions between mobile and HPC)
- ML models trained on HPC centers but deployed on mobile devices

### Crosscutting Digital Twin Challenges and Translation Across Domains

Many challenges are shared across domains but manifest differently:
- Bidirectional virtual-physical interaction and on-demand continual access present common foundational research gaps
- Domain-specific and cross-domain opportunities exist in each element of the DT ecosystem

Different domains have different levels of maturity:
- Earth system science is a leader in data assimilation
- Engineering leads in integrating VVUQ into simulation-based decision-making
- Biomedical community has a strong culture of prioritizing the human decision-maker

Cross-domain translation is an opportunity: techniques from weather forecasting data assimilation could benefit biomedical digital twins and vice versa. However, there has not been a concerted effort to examine formally which aspects of associated software and workflows cross disciplines.

### Model and Data Collaborations

The weather and climate community provides an exemplary model of global data collaboration:
- Global Telecommunication System for real-time data sharing
- National Centers for Environmental Information (700+ TB per month)
- Global Climate Observing System for long-term records
- U.S. Global Change Research Program for coordinating federal modeling activities
- Multiple federal agencies support independent Earth system modeling (Unified Forecast System, Earth System Prediction Capability, Goddard Earth Observing System)

Other disciplines (e.g., Nanoscale Molecular Dynamics, Gromacs) have open-source shared models but few support the breadth in scale and robust UQ integration found in Earth system models.

The creation of the human genome demonstrates that successful worldwide cooperative efforts can advance ambitious research goals while establishing norms and standards.

Key conclusions:
- Open global data and model exchange has led to more rapid advancement of predictive capability in Earth system sciences (Conclusion 7-3)
- Fostering a culture of collaborative exchange incorporating context through metadata and provenance could accelerate progress across all DT-relevant disciplines (Conclusion 7-4)

### Preparing an Interdisciplinary Workforce

Successful adoption hinges on appropriate education and training. Critical skill sets include:
- Systems engineering and thinking
- Data analytics, ML/AI
- Statistics, probabilistic modeling and simulation
- Uncertainty quantification
- Computational mathematics and decision science

Three areas for foundational improvement:

**Interdisciplinary Degrees**: CSE and DSE programs are growing but remain less common at undergraduate level. Traditional academic structures reward vertical excellence over interdisciplinary achievement. Good models include the Computational Modeling and Data Analytics program at Virginia Tech and the Interdisciplinary Research Institutes at Georgia Tech.

**Research Training Programs**: DOE's Computational Science Graduate Fellowship (CSGF) is an exemplary model requiring interdisciplinary coursework and summer research at a national lab in an area different from the thesis. NSF programs for industry/national lab internships are also valuable.

**Faculty Engagement**: Faculty must perform interdisciplinary research for curricula to reflect it. Challenges include promotion criteria that undervalue interdisciplinary contributions. The Declaration on Research Assessment is beginning to address this. Tutorials, summer schools, and hack-a-thons are recommended over expecting individual faculty to cover the full breadth.

## Key Research Gaps Identified

**Priority 1:**
- Incentives and frameworks for comprehensive data collaborations, standardization of data and metadata (including across public data sets), and model collaborations that go beyond existing open science frameworks
- Clear definition of digital twin sustainability and lifecycle management with corresponding needs for maintaining data, software, sensors, and virtual models (needs may vary across domains)

## Practical Takeaways for Scientists

- Treat your virtual representation as an **asset** with its own lifecycle -- budget for maintenance, updates, and eventually retirement, just as you would for physical equipment
- If you are building infrastructure, plan for a federation of simulations with well-defined APIs rather than a single monolithic system
- For field-deployable digital twins, design for **asymmetric compute**: train on HPC, deploy compact surrogates on mobile/edge devices
- Actively seek cross-domain collaboration -- your data assimilation, surrogate modeling, or UQ techniques may transfer to entirely different fields
- Use the weather/climate data exchange model as inspiration for your own domain's data sharing practices
- If you are in academia, advocate for interdisciplinary degree programs and promotion criteria that recognize interdisciplinary contributions
- Consider the DOE CSGF model for training the next generation: require interdisciplinary coursework plus research experience outside one's core domain

## Notable References

- Zsarnooczay, A., et al. 2023. "Community Perspectives on Simulation and Data Needs for the Study of Natural Hazard Impacts and Recovery" (NSF NHERI framework)
- Grubel, J., et al. 2022. "The Hitchhiker's Guide to Fused Twins: A Review of Access to Digital Twins In Situ in Smart Cities" (access models for DTs)
- NIST. 2009. "The System Development Life Cycle (SDLC)" (lifecycle definition)
- Riishojgaard, L.P., et al. 2021. "WMO Data Exchange -- Background, History and Impact" (global data exchange model)
- Pohl, C., et al. 2015. "How to Successfully Publish Interdisciplinary Research" (publishing challenges)
