# interTwin: Advancing Scientific Digital Twins through AI, Federated Computing and Data

**Journal:** Future Generation Computer Systems, Volume 179 (2026), Article 108312, Elsevier
**DOI:** [10.1016/j.future.2025.108312](https://doi.org/10.1016/j.future.2025.108312)
**License:** CC BY-NC-ND 4.0
**Received:** 13 May 2025 | **Accepted:** 28 November 2025 | **Published online:** 15 December 2025
**Lead author:** Andrea Manzi (EGI Foundation, Amsterdam)
**Funding:** European Union Horizon Europe Programme, Grant 101058386

---

## Full Summary

The interTwin project is an EU-funded effort that co-designed and implemented a prototype **Digital Twin Engine (DTE)** -- an open-source, interdisciplinary platform providing both generic and domain-specific software components for modelling and simulation. The DTE integrates application-specific Digital Twins (DTs) across scientific disciplines by following a co-designed conceptual model called the **DTE blueprint architecture**, guided by open standards and interoperability principles.

The paper argues that current digital twin platforms fall short for science because they (1) focus on single domains or centralized computing, (2) lack federated interoperability, and (3) cannot deliver the scalable, distributed computing power needed for complex simulations. The DTE addresses these gaps by unifying heterogeneous distributed digital infrastructures -- HPC centres, cloud services, and data storage spread across multiple institutions and countries -- under a single, modular framework.

The platform was co-designed with ten real use cases from high-energy physics, radio astronomy, gravitational-wave astrophysics, climate research, and environmental monitoring. These use cases drove requirements for dynamic workflow composition, real-time data management, quality and uncertainty tracing, and multi-source data fusion.

Key contributions are: (1) a federated architecture for seamless integration of distributed computing and storage; (2) standardized interfaces and protocols for cross-domain interoperability; (3) a co-design approach incorporating requirements from diverse scientific fields; and (4) strong methods for model quality, traceability, and uncertainty measurement.

---

## Digital Twin Engine (DTE) Architecture

### High-Level Structure

The DTE is organized in **three layers** from bottom to top:

1. **DTE Infrastructure** -- Orchestration, Federated Computing, Federated Data Management
2. **DTE Core Capabilities** -- AAI (Authentication and Authorization), Big Data Analytics, AI/ML, Data Fusion, Workflow Composition, Quality Verification, Real-time Data Acquisition and Preprocessing
3. **DTE Thematic Capabilities** -- Domain-specific thematic modules (e.g., climate, physics)
4. **DTE Repositories** -- Container Repository, Code Repository, Model Repository, Workflow Registry

On top of these sit the **DT Applications** themselves, which scientists and developers interact with through well-defined APIs.

### Three Infrastructure Pillars

- **Federated Computation:** Provides seamless access to computing power from commercial cloud services, HPC clusters, or HTC systems. A federated compute framework abstracts provider-specific details, allowing applications to scale up or down based on actual demand.
- **Federated Data Management:** Integrates historical data, real-time streams, and external datasets into a shared **Data Lake**. Addresses differences in data formats and protocols so applications can securely locate, retrieve, and manipulate data regardless of physical location.
- **Intelligent Resource Orchestration:** An AI-based orchestration layer that uses ML and predictive analytics to monitor cloud resource usage and dynamically adjust resource allocation.

### Two User Roles

- **Scientists (End Users):** Launch or schedule simulations, monitor and interpret outputs with minimal configuration. No need to modify low-level infrastructure.
- **Developers:** Create and maintain DT applications and modules -- integrating data sources, designing workflows, extending analytic libraries, managing containers and platform configuration.

### Core Capabilities (Detail)

| Capability | Description |
|---|---|
| **Workflow Composition & Management** | Design, schedule, and track workflows across HPC, HTC, and cloud using Common Workflow Language (CWL). Extended via Ophidia framework for HPC paradigms and Big Data analytics. openEO API selected for Earth Observation use cases. |
| **Real-Time Processing** | Event-triggered execution of workflow engines. Data staging, pre-processing, and quality assessment. Delegates complex processing to dynamically provisioned cloud resources. |
| **Machine Learning and Predictive Analytics (AI/ML)** | Training and deploying ML models via **itwinai**, an open-source Python library. Supports distributed training (PyTorch DDP, TensorFlow, Horovod), hyperparameter optimization (Ray Tune), MLflow/Weights&Biases/TensorBoard integration, and a model registry. |
| **Quality Verification** | Checks data integrity, assesses model performance, ensures alignment with real-world conditions. Relies on SQAaaS (Software Quality Assurance as a Service) platform with CI/CD pipelines for automated quality checks, FAIR data compliance, and digital badges. |
| **Data Fusion** | Unifies information from varied sources into a consistent environment. |
| **Provenance Tracking** | Full W3C PROV-based provenance management via yProv service, yProvExplorer, yProv4WFs (workflow provenance), and yProv4ML (ML training provenance). |

### Key Technical Components

- **interLink:** Extends Kubernetes clusters to remote HPC/cloud resources transparently. Based on Virtual Kubelet technology. Plugin model supports SLURM, UNICORE, Kueue, HTCondor, and Docker backends. Provides a plug-and-play approach to federated compute.
- **Data Lake:** Inspired by the ESCAPE project (HEP community). Uses **Rucio** for large-volume data management, **File Transfer Service (FTS)** for file transfers, and POSIX-mounted filesystems for HPC access. Deployed across five storage technologies (Ceph S3, dCache, Teapot, Onedata S3, StoRM WebDAV) at ten data centres in eight countries.
- **AI Orchestrator:** Based on INDIGO PaaS Orchestrator. Translates high-level deployment requests into actions on OpenStack, OpenNebula, AWS, Azure, Google Cloud, etc. Uses TOSCA templates and an Infrastructure Manager. Includes an MLflow registry for model storage and inference.
- **OSCAR:** Serverless event-driven processing platform on Kubernetes for data-processing requests (triggered by events). Supports Knative, interLink offloading to HPC, and JupyterHub integration.
- **Event-Ingestion System:** Apache NiFi for versatile data routing; Apache Kafka for high-throughput event streaming. Integrated with MinIO, Amazon S3, OneData, dCache, WebDAV. **DCNiOS** tool for deploying dataflows via simple YAML configuration.
- **AAI (Authentication and Authorization):** Based on EGI Check-in service using Keycloak, OIDC, and OAuth 2.0. The ALISE service manages identities, enrolment, and authorization policies across distributed resources.
- **itwinai:** Open-source Python library for scalable ML on HPC. Configuration-based workflow definition; supports data preprocessing, distributed training, HPO, and inference. Extensible plugin architecture. Model registry integration.
- **Big Data Analytics Layer:** TOSCA-based cloud topology templates for deploying data analytic environments on demand.

### DTE Testbed

The practical deployment integrates multiple European computing centres:

- **HPC sites:** EuroHPC VEGA (Slovenia), JULICH (Germany), PSNC (Poland) -- supercomputing with advanced GPU architectures, integrated via interLink
- **Cloud sites:** GRNET, UKRI, EODC (OpenStack) -- Kubernetes clusters for containerized workloads
- **Additional sites:** INFN, CESGA, DESY
- **Unified under:** Common AAI authentication, MLflow for model management, JupyterHub for interactive development, Rucio-based federated Data Lake

---

## Use Cases

### Environmental and Climate Science Applications (6 use cases)

1. **Climate Extremes and Weather Events:**
   - Generic detection of climate extremes using CVAE-based anomaly detection
   - Tropical cyclone detection combining ML with deterministic tracking
   - Climate projection analysis integrating satellite imagery with ML for global-scale burned area estimation
   - Wildfire prediction using U-Net++ CNNs trained on the SeasFire Cube dataset

2. **Flood Adaptation and Early Warning:**
   - Two flood-related applications for coastal and inland regions
   - Early warning systems combining climate impact assessment with real-time alert mechanisms and interactive scenario modelling

3. **Drought Monitoring:**
   - Alpine drought early warning system using surrogate models trained on hydrological simulations across seven river basins
   - Integrates ECMWF seasonal forecasts for predictive analysis

4. **Post-Flood Analysis:**
   - Non-ML-based DT application using physics-based models in coastal regions

### Physics Domain Applications (4 use cases)

5. **High Energy Physics:**
   - Lattice QCD simulations developing normalizing flows for quantum field theory studies
   - Fast particle detector simulations using generative AI for synthetic datasets, reducing computational overhead vs. Monte Carlo

6. **Radio Astronomy:**
   - Noise simulation developing digital twins of telescope systems for training ML classification tools

7. **Gravitational Wave Astrophysics:**
   - **Virgo DT** for realistic simulation of transient noise artifacts (glitches) in gravitational wave detectors
   - GNN-based pipeline for near-real-time glitch identification in detector strain channels
   - Architecture: ANNALISA (channel selection via Q-transform) -> PreprocessAPI (data prep) -> GlitchFlow (GNN-based U-Net with attention gates and residual blocks)
   - De-noising pipeline achieves >90% accuracy at SNR of 6
   - Training subsystem and inference subsystem share PreprocessAPI; inference adds GenerativeAPI for glitch generation
   - All modules implemented as **itwinai** plugins

8. **Tropical Cyclones and Wildfires (detailed implementation):**
   - TC detection: "hybrid" ML approach linking data-driven models (VGG-like CNNs, Graph CNNs) with a deterministic tracker, trained on ERA5 reanalysis + IBTrACS observed TC records
   - Wildfires: U-Net++ CNNs for predicting burned areas, trained on SeasFire Cube dataset
   - Both applications share similar DTE integration workflows: developers train via thematic modules (ML TC detection, ML4Fires), track metrics with itwinai and yProv, store models in ML Model Registry, offload to HPC via interLink
   - End users select pre-trained models, run inference via Jupyter Notebooks, visualize results through Ophidia-based pipelines

---

## Interoperability with Destination Earth (DestinE)

A major interoperability demonstration connects the DTE with the European Commission's **Destination Earth (DestinE)** initiative -- a high-precision digital twin of the Earth for climate and environmental phenomena.

Key integration features:

- **Standardized Data Formats:** DTE adheres to DestinE standards (NetCDF, Zarr, geospatial formats)
- **Federated Data Management:** Aligned data lake approaches for seamless access across domains
- **Data Ingestion and Sharing:** DTE can ingest data from the DestinE Data Lake
- **Data Contribution:** interTwin simulations and models can be accessed via the DestinE Data Lake
- **APIs for Data Access:** Compatible data access protocols based on STAC APIs
- **DestinE Core Service Platform (DESP):** Possibility to onboard interTwin services onto the DESP cloud platform for sustainability

---

## Derived Architectural Requirements (Cross-Cutting)

The paper identifies **five core capabilities** that any scientific DT platform must provide:

1. **Federated Data Integration** -- Standardized interfaces supporting diverse formats, real-time streams, external services; FAIR compliance
2. **Adaptive Workflow Orchestration** -- Batch and streaming workflows with automated resource provisioning; CWL-based standards
3. **Multi-Modal Processing Infrastructure** -- Ultra-low latency for physics; near real-time for environmental monitoring; seamless HPC-cloud integration
4. **Elastic Resource Management** -- Container-based deployment with dynamic scaling across simulations and streaming applications
5. **Comprehensive Quality Assurance** -- Integrated validation, provenance tracking, uncertainty quantification for reproducible research

---

## Practical Takeaways for Scientists Building Digital Twins

1. **Start with a federated mindset.** Do not build around a single HPC centre or cloud provider. Design your DT so that compute, data, and workflows can move transparently between resources. interLink and Kubernetes provide the abstraction layer for this.

2. **Adopt open standards early.** Use CWL for workflow definition, OIDC/OAuth 2.0 for authentication, TOSCA for deployment templates, W3C PROV for provenance, and STAC/OGC APIs for data access. Standards are what make cross-project interoperability (like interTwin-DestinE) possible.

3. **Separate thematic modules from core infrastructure.** The DTE architecture cleanly separates domain-specific science (thematic modules) from generic platform capabilities (workflow composition, data management, AAI). This separation lets you reuse infrastructure across disciplines.

4. **Use itwinai for ML on HPC.** The itwinai library abstracts distributed ML training, hyperparameter optimization, and model management. It lets domain scientists deploy scalable AI without becoming ML infrastructure engineers.

5. **Build provenance tracking in from the start.** The yProv ecosystem (yProv service, yProv4WFs, yProv4ML) provides end-to-end traceability. Retrofitting provenance is much harder than designing it in.

6. **Automate quality assurance.** Use CI/CD pipelines (SQAaaS) to automatically validate data quality, FAIR compliance, and software quality. Embed quality checks in the development process, not as an afterthought.

7. **Leverage event-driven architectures for real-time data.** OSCAR (serverless, event-driven processing on Kubernetes) combined with Apache NiFi and Kafka enables responsive DTs that react to incoming data streams without maintaining always-on compute.

8. **Containerize everything.** The DTE uses Docker/Singularity containers throughout. Container images including DTE core frameworks and domain libraries are deployed on HPC via interLink. This ensures reproducibility and portability.

9. **Plan for two user roles.** Design your DT with separate pathways for developers (who build and train models) and scientists (who run analyses and interpret results via Jupyter Notebooks and pre-trained models).

10. **Use a shared Data Lake with Rucio.** For multi-institutional collaboration, a federated data lake using Rucio (originally from CERN/HEP) with multiple storage backends provides location-transparent data access with proper identity management.

---

## Notable References

| # | Reference | Relevance |
|---|---|---|
| [1] | Kierans et al., "Realising distributed digital twins within federated digital infrastructures," DiDiT 2024 Workshop, Groningen | Foundational work on distributed DT infrastructure |
| [2] | Wu et al., "A comprehensive review of digital twin," Sensors 23(19), 2023 | Comprehensive DT review covering process, data, models, and applications |
| [3] | S.N. others, "Digital ecosystems for developing digital twins of the earth," Remote Sens. 13(11), 2021 | DestinE digital twin of the Earth context |
| [16] | Grieves, "Digital twin: manufacturing excellence through virtual factory replication," 2015 White Paper | Original DT concept by Grieves and Vickers |
| [18] | Bardaji et al., "interTwin D3.5 DTE Blueprint Architecture," Technical Report, Zenodo, 2024 | The DTE blueprint architecture specification (third version) |
| [19] | Caballer et al., "Infrastructure manager: a TOSCA-based orchestrator for the computing continuum," J. Grid Comput. 21(3), 2023 | Infrastructure Manager for TOSCA-based cloud orchestration |
| [20] | Elia et al., "PyOphidia: a python library for high performance data analytics at scale," SoftwareX 24, 2023 | Ophidia/PyOphidia framework for HPC data analytics |
| [24] | Fiore et al., "A graph data model-based micro-provenance approach for multi-level provenance exploration," IEEE BigData 2023 | yProv provenance model |
| [26] | Bernardo et al., "Software quality assurance as a service," Future Gener. Comput. Syst. 156, 2024 | SQAaaS platform for automated quality assurance |
| [27] | yProv4ML, "effortless provenance tracking for machine learning systems," SoftwareX 31, 2025 | ML provenance tracking library |
| [30] | Risco et al., "Rescheduling serverless workloads across the cloud-to-edge continuum," Future Gener. Comput. Syst. 153, 2024 | OSCAR serverless event-driven platform |
| [34] | Ronneberger et al., "U-Net: convolutional networks for biomedical image segmentation," MICCAI 2015 | U-Net architecture used in GlitchFlow GNN model |
| [38] | Accarino et al., "An ensemble machine learning approach for tropical cyclone localization and tracking from ERA5," Earth Space Sci. 10(11), 2023 | Tropical cyclone tracking with deterministic ML approach |
| [40] | Hersbach et al., "The ERA5 global reanalysis," Q. J. R. Meteorol. Soc. 146, 2020 | ERA5 reanalysis dataset used across climate use cases |
| [43] | Karasante et al., "SeasFire cube -- a multivariate dataset for global wildfire modeling," Sci. Data 12(1), 2025 | SeasFire dataset for wildfire prediction training |
| [46] | Cinquini et al., "The earth system grid federation: an open infrastructure for access to distributed geospatial data," Future Gener. Comput. Syst. 36, 2014 | Earth System Grid Federation for climate model data access |

### Key Project Links

- interTwin project: [https://intertwin.eu](https://intertwin.eu)
- GitHub organization: [https://github.com/interTwin-eu](https://github.com/interTwin-eu)
- interLink (federated compute): [https://interlink-project.dev](https://interlink-project.dev)
- itwinai (ML library): [https://itwinai.readthedocs.io](https://itwinai.readthedocs.io)
- DCNiOS (dataflow deployment): [https://github.com/intertwin-eu/dcnios](https://github.com/intertwin-eu/dcnios)
- DestinE: [https://destination-earth.eu](https://destination-earth.eu)
- SQAaaS: integrated in DTE CI/CD
- EGI Check-in (AAI): [https://www.egi.eu/service/check-in/](https://www.egi.eu/service/check-in/)
