# Chapter 1 -- Introduction to Digital Twins

**Authors:** Dhaval Thakker, Zeeshan Pervez, et al.

## Summary

This introductory chapter lays the groundwork for the entire handbook by defining what digital twins (DTs) are, tracing their historical evolution, and surveying the breadth of application domains. A digital twin is defined as a virtual replica of a physical entity that is continuously synchronised through real-time data exchange, enabling monitoring, simulation, and predictive analytics. The chapter positions DTs as a convergence technology that integrates IoT sensing, data analytics, AI/ML, simulation, and visualisation into a unified cyber-physical framework.

The chapter traces the concept from NASA's early use of physical replicas for space missions (Apollo 13 mirror systems) through Michael Grieves' formal articulation of the DT concept in 2003 in the context of product lifecycle management (PLM), to the modern era where cloud computing, 5G, and edge AI have made large-scale DT deployments feasible. The evolution is presented in phases: conceptual origin, enabling technology maturation, and current proliferation across industries.

## Key Concepts and Architectures

- **Three-component model (Grieves):** Physical entity, virtual entity, and the data/information connection between them.
- **DT vs. digital model vs. digital shadow:** A digital model has no automated data flow; a digital shadow has one-way automated data flow (physical to virtual); a true DT has bidirectional automated data flow.
- **Five-dimensional DT architecture:** Physical entity, virtual model, services, data, and connections.
- **DT lifecycle alignment:** DTs can serve across the full product/asset lifecycle -- design, manufacturing, operation, maintenance, and decommissioning.

## Application Domains Surveyed

- **Manufacturing:** Predictive maintenance, process optimisation, quality control.
- **Healthcare:** Patient-specific organ models, hospital operational twins, drug development simulations.
- **Smart cities:** Traffic management, energy grid optimisation, urban planning.
- **Construction and built environment:** BIM-integrated twins for building performance monitoring.
- **Aerospace and defence:** Component-level twins for fatigue monitoring and mission planning.

## Practical Takeaways for Scientists

1. Before building a DT, clarify whether you need a digital model, digital shadow, or a full bidirectional twin -- each has different data infrastructure requirements and costs.
2. The five-dimensional architecture (physical entity, virtual model, services, data, connections) is a useful checklist when scoping a DT project.
3. DTs are not just 3D visualisations -- the real value comes from the closed-loop feedback between the physical and virtual systems.
4. Start with a clearly bounded physical system and a well-defined set of questions the DT should answer; scope creep is the most common failure mode.

## Notable References

- Grieves, M. (2014). *Digital Twin: Manufacturing Excellence through Virtual Factory Replication.* Florida Institute of Technology.
- Tao, F. and Zhang, M. (2017). Digital twin shop-floor: A new shop-floor paradigm towards smart manufacturing. *IEEE Access*, 5, 20418--20427.
- Fuller, A., Fan, Z., Day, C. and Barlow, C. (2020). Digital twin: Enabling technologies, challenges, and open research. *IEEE Access*, 8, 108952--108971.
- Glaessgen, E. and Stargel, D. (2012). The digital twin paradigm for future NASA and US Air Force vehicles. *Structural Dynamics and Materials Conference*.
