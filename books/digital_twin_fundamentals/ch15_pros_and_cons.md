# Chapter 15: Digital Twin: Pros and Cons

**Author:** Prakash J.
**Affiliation:** Department of Computer Science & Engineering, PSG College of Technology, Tamil Nadu, India
**Pages:** 233--246

## Summary

This final chapter provides a balanced assessment of digital twin technology, systematically listing and discussing the pros and cons. It also covers application-wise pros for specific sectors (oil and gas, industrial, automotive, construction). The chapter includes a detailed historical overview and positions digital twin as an evolving strategic technology with growing adoption and impact.

The chapter reviews digital twin fundamentals (types: DTP, DTI, DTE; predictive and interrogative purposes), traces its history from NASA's 1960s work through David Gelernter's 1991 "Mirror Worlds" book, Michael Grieves' 2002 presentation, John Vickers' 2010 naming, to its current status as a Gartner top-ten strategic technology trend (2017). The author emphasizes that digital twin is still evolving and its pros and cons will continue to update as the technology matures.

The discussion of cons is particularly valuable as most other chapters focus primarily on benefits. The three main cons identified -- need for deep domain knowledge, sensor reliability issues, and security challenges -- represent genuine barriers to adoption that practitioners must address.

## Key Concepts

- **Pros of digital twin:**

  1. **Problem forecasting before arrival:** Digital twins can predict what possible problems could occur in a product or object by monitoring its virtual replica in real-time, allowing preventive action before problems manifest physically

  2. **Monitoring capability:** Real-time data from sensors keeps the digital twin synchronized with the physical object; any change in the real object is immediately mimicked in the twin, enabling remote monitoring from anywhere

  3. **Waste reduction:** Manufacturing with digital twins reduces waste by catching defects and process issues in the virtual environment before they produce physical waste (defective products, wasted materials, resource consumption)

  4. **Hazardous situation avoidance:** In sectors like oil and gas, digital twins forecast future problems, avoiding dangerous situations at work before they occur

  5. **Increased speed of work completion:** Digital twins help complete manufacturing and development work faster, reducing time-to-market

- **Cons of digital twin:**

  1. **Deep knowledge requirement:** Creating and handling digital twins requires deep domain expertise in both the physical system being twinned and the digital twin technology itself; not a simple plug-and-play technology

  2. **Sensor issues affect the twin:** If sensors transmitting data from the physical object have issues (failure, drift, noise), the digital twin's accuracy is directly compromised; the twin is only as good as its sensor data

  3. **Security challenges:** The bidirectional connection between physical and digital creates potential attack surfaces; data breaches in the digital twin could affect the connected physical object; complete security assurance is challenging

- **Application-wise pros by sector:**

  1. **Oil and gas sector:** Preventive maintenance, process monitoring, cost savings in a capital-intensive industry

  2. **Industrial sector:** Manufacturing process monitoring, reduced wastage, faster time to market for products

  3. **Automotive sector:** Vehicle performance monitoring via sensor data, real-time environment performance tracking, data-driven software updates (Tesla example)

  4. **Construction sector:** Support at all stages (design, building, operations), smart city construction support, scenario testing with city parameters

- **Key historical milestones:**
  - 1960s: NASA begins working on digital twin concepts
  - 1970: First use during Apollo 13 mission
  - 1991: David Gelernter publishes "Mirror Worlds"
  - 2002: Michael Grieves presents at Society of Manufacturing Engineers conference, Michigan
  - 2010: John Vickers coins the term "digital twin" in a NASA report
  - 2017: Gartner lists digital twin as top-ten strategic technology trend

## Practical Takeaways for Scientists

1. **Acknowledge the expertise barrier.** Building a useful digital twin requires deep understanding of both the physical domain and the digital twin technology. Cross-disciplinary teams (domain experts + software engineers + data scientists) are typically needed.

2. **Sensor reliability is the Achilles' heel.** Invest in high-quality, redundant sensor systems with self-diagnostics. A digital twin fed by unreliable sensor data can be worse than no twin at all -- it may provide false confidence.

3. **Security must be designed in, not bolted on.** The bidirectional nature of digital twins means a security breach can potentially affect the physical system. Implement comprehensive security from the architecture level.

4. **The pros clearly outweigh the cons** at present, but the cons represent real barriers that must be actively managed rather than ignored. Budget for sensor maintenance, security infrastructure, and personnel training.

5. **Digital twin is still evolving.** The technology is not yet mature. Early adopters will face teething issues but will also gain competitive advantage. Scientists should evaluate readiness based on their specific domain and data infrastructure maturity.

6. **Sector-specific value assessment.** Not all sectors benefit equally. High-value, high-risk sectors (oil and gas, aviation, healthcare) see faster ROI than lower-stakes applications. Assess the value proposition for your specific domain.

## Notable References

- Kritzinger, W., Karner, M., Traar, G., et al., Digital twin in manufacturing: A categorical literature review and classification. *IFAC-Papers online*, vol. 51, pp. 1016--1022, 2018
- Rasheed, A., San, O., Kvamsdal, T., Digital twin: Values, challenges and enablers. *IEEE Access*, 8, 21980--22012, 2020
- Grieves, M. and Vickers, J., Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems. *Transdisciplinary perspectives on complex systems*, pp. 85--113, Springer, 2017
- Barricelli, B.R., Casiraghi, E., Fogli, D., A survey on digital twin. *IEEE Access*, 7, 167653--167671, 2019
- Schroeder, G.N., Steinmetz, C., Pereira, C.E., Digital twin data modeling with automation ML and a communication methodology for data exchange. *IFACPapers Online*, 49, 30, 12--17, 2016
