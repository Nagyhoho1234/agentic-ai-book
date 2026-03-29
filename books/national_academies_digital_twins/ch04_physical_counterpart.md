# Chapter 4: The Physical Counterpart -- Foundational Research Needs and Opportunities

## Comprehensive Summary

This chapter addresses data acquisition and data integration for digital twins -- how data flows from the physical world into the virtual representation. The central argument is that only when high-quality, integrated data are combined with advanced modeling approaches can the full potential of digital twins be realized.

### Data Acquisition Challenges

**Undersampling** in complex systems with large spatiotemporal variability is a fundamental challenge. Complex physical and biological systems exhibit intricate patterns, nonlinear behaviors, feedback, and emergent phenomena requiring comprehensive sampling. However, resources, time, and accessibility constraints often prevent adequate data collection. Undersampling can lead to:
- Incomplete characterization of the system
- Overlooking critical events or significant features
- Propagated uncertainty through predictive models
- Inaccurate or misleading outcomes, especially in safety-critical applications

Data acquisition is inherently multidisciplinary, combining expertise in data acquisition, modeling, and system analysis.

### Data Accuracy and Reliability

Key concerns include:
- **Data quality assurance**: How to handle outlier and anomalous data -- sometimes outliers are sensor malfunctions (ignore them), sometimes they are rare events (essential to capture them)
- **Anomaly detection**: Traditional methods focus on maximizing average-case performance and may yield large errors on rare events. Rethinking loss functions and performance metrics is needed
- **Sensor reliability**: Sensors degrade over time; a new sensor producing different output than the digital twin may indicate sensor error or genuine change in the physical system
- **Data provenance**: Documenting data quality and metadata that reflect provenance is critical (Finding 4-1)
- **Quality assurance frameworks**: The absence of standardized QA frameworks makes cross-organization comparison difficult (Finding 4-2)

### Considerations for Sensors

Sensors provide timely data on the physical counterpart. Research needs include:
- Sensor calibration, performance, maintenance, and fusion methods
- Detecting and mitigating adversarial attacks (tampering, false data injection)
- Multimodal sensors combining multiple sensing technologies

### Data Integration

Integrating data from diverse sources is challenging due to differences in format, quality, and structure. Key issues:
- **Data interoperability**: ability for systems to exchange and use information from other systems; current efforts toward semantic integration are not scalable
- **Metadata standardization**: inadequate metadata hinders harmonization and integration; efforts to standardize are insufficient for digital twin needs
- **Lack of adopted standards** in data generation hinders interoperability (Conclusion 4-1)

### Handling Large Amounts of Data

Data may stream at full four-dimensional resolution in real time. Challenges include:
- ML models need to be trained and applied on the fly
- Data assimilation and data handling architecture must be scalable
- Subsampling and low-power ML methods may be needed under resource constraints
- Online and incremental learning methods with adaptive learning rates are important
- Adaptive model training in the presence of anomalies and outliers is particularly challenging

### Data Fusion and Synchronization

Digital twins must integrate data from different streams, addressing:
- Missing data and data sparsity
- Data synchronization across scales
- Heterogeneity of data sources (e.g., diverse sensor systems)
- Disparate sampling rates, duplication, and seemingly contradictory data
- Data imputation to mitigate missing data effects

### Data Access and Collaboration

Data collaboration must address ownership, responsibility, and intellectual property issues. Earth science provides an exemplary model: since the late 1970s, satellites have provided near-simultaneous global observations, combined via data assimilation to create weather forecasts. This infrastructure (Global Telecommunication System, National Centers for Environmental Information with 700+ TB/month) represents a mature data collaboration framework that other domains can learn from.

## Key Research Gaps Identified

**Priority 1:**
- Standards to facilitate interoperability of data and models for digital twins (e.g., by regulatory bodies) are lacking
- Tools for data and metadata handling and management to ensure data are gathered, stored, and processed efficiently

**Priority 2:**
- Undersampling in complex systems with large spatiotemporal variability
- Data imputation approaches for high-volume and multimodal data
- Mathematical tools for assessing data quality, determining appropriate utilization of available information, and guiding algorithm choice

## Practical Takeaways for Scientists

- Document your data provenance meticulously -- metadata and quality records are as important as the data itself
- When designing a digital twin data pipeline, plan for how you will distinguish genuine rare events from sensor malfunctions in your anomaly detection
- Do not assume data integration is a solved problem -- format, quality, and semantic differences across sources require active research and engineering
- Consider the Earth system science data collaboration model (global data sharing, standardized formats, real-time exchange) as an aspirational target for your domain
- For streaming data applications, invest in online/incremental learning methods rather than batch retraining
- Budget for sensor calibration, maintenance, and reliability monitoring as part of your digital twin lifecycle -- sensor degradation is a real and ongoing concern

## Notable References

- Chung, C., and D. Jaffray. 2021. "Cancer Needs a Robust 'Metadata Supply Chain' to Realize the Promise of Artificial Intelligence" (metadata importance for biomedical DTs)
- VanDerHorn, E., and S. Mahadevan. 2021. "Digital Twin: Generalization, Characterization and Implementation" (general DT framework)
- Ackerman, S.A., et al. 2019. "Satellites See the World's Atmosphere" (satellite observing systems)
- Balsamo, G., et al. 2018. "Satellite and In Situ Observations for Advancing Global Earth Surface Modelling" (Earth observation for modeling)
