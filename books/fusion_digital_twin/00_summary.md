# Visualizing Digital Twins of Fusion Power Plants Using NVIDIA Omniverse

**Citation:** Bhatia, N., Costa, R., Pamela, S.J.P., Davis, A., Gonzalez Beltran, A.N., Gopakumar, V., Zanisi, L., de Witt, S., & Akers, R. (2025). *AIP Advances*, 15, 045018. https://doi.org/10.1063/5.0261883

**Affiliation:** United Kingdom Atomic Energy Authority (UKAEA), Culham Campus, Abingdon, UK

**Published:** 8 April 2025 (Submitted 31 January 2025, Accepted 10 March 2025)

**License:** CC BY 4.0

---

## Summary

This paper presents a workflow for creating and visualizing digital twins of fusion power plants using NVIDIA Omniverse, with the MAST-U (Mega Amp Spherical Tokamak Upgrade) device at UKAEA as the primary demonstration case. The authors argue that as global fusion projects (ITER, STEP, CFETR) move toward practical energy production, the engineering complexity demands a unified "single source of truth" that integrates CAD models, physics simulations, real-time sensor data, and material properties into one interactive 3D environment.

The core contribution is a complete pipeline -- from CAD ingestion through photorealistic material assignment and simulation data overlay to real-time collaborative visualization -- all built on NVIDIA Omniverse and its Universal Scene Description (USD) file format. The paper also discusses how Python scripting and generative AI can extend the platform for robotics simulation, Building Information Modeling (BIM) integration, and AI-driven surrogate models, making the digital twin dynamic rather than a static 3D model.

The authors are candid about the platform's current limitations: Windows-centric tooling clashes with the Linux-based HPC environments where fusion simulations run, limited cloud provider support creates data-residency issues, and the AR/VR stack (CloudXR) is Windows-only, restricting adoption in Linux-dominated research facilities.

---

## Key Methods and Platforms

### Core Platform
- **NVIDIA Omniverse** -- the central integration environment, providing real-time 3D rendering, collaboration, and extensibility via Python APIs (Omniverse Kit API)
- **Universal Scene Description (USD)** -- Pixar's open file format used as the interchange standard for all geometry, materials, and simulation data

### CAD Integration Pipeline
1. **STL export** from UKAEA's central design repository (MAST-U CAD parts)
2. **Trimble SketchUp** for preprocessing and refinement of STL geometry
3. **SketchUp-Omniverse Connector** to convert processed CAD data into USD format
4. **Omniverse Nucleus** file server for centralized, multi-user asset hosting
5. **Omniverse USD Composer** for final scene assembly and visualization

### PBR Material Assignment
- **Omniverse USD Composer** with materials from NVIDIA's Omniverse Material Library and Adobe Substance
- **Physically Based Rendering (PBR)** materials simulate realistic light interaction (reflections, roughness, metallicity)
- Ongoing UKAEA-University of Manchester collaboration to define accurate **Bidirectional Reflectance Distribution Function (BRDF)** properties for fusion-specific component textures

### Simulation Data Integration
- **JOREK** magnetohydrodynamics (MHD) code for plasma simulation (Edge Localized Modes / ELMs, D-alpha light emission)
- Simulation data exported in **VTK format**, post-processed in **Kitware ParaView**
- **ParaView-Omniverse Connector** streams processed simulation data as USD into Omniverse Nucleus for real-time overlay on the CAD model

### Rendering Technology
- **NVIDIA RTX GPU** path-traced and ray-traced rendering for photorealistic output
- Transparency/refraction effects for diagnostic windows and coolant channels
- Volume rendering of simulated plasma behavior (ELM time-step visualization)

### Real-Time Data and AI Extensions
- **MQTT** message queues for streaming live sensor data from the tokamak into the digital twin
- **NVIDIA Isaac** platform for virtual sensor simulation and validation
- Python-driven **AI surrogate models** (e.g., Fourier neural operators for plasma surrogate modeling) integrated via Omniverse Kit API for predictive maintenance and design optimization
- **BIM integration** via Python/C++/web connectors to synchronize architectural, construction, and maintenance plans

---

## Visualization Approach

The paper describes a layered visualization strategy:

1. **Geometric fidelity** -- CAD models imported and refined so that every physical component of the tokamak is accurately represented in 3D space
2. **Material realism** -- PBR materials applied to make metallic, dielectric, and emissive surfaces look true-to-life; ray tracing produces realistic shadows, global illumination, and soft lighting
3. **Simulation overlay** -- JOREK MHD plasma simulation data (glowing plasma filaments, ELM structures) rendered as volumetric effects inside the tokamak geometry with transparent walls
4. **Interactive exploration** -- stakeholders can perform virtual walk-throughs, cross-sectional views, and collaborative design reviews in real time using Omniverse USD Composer
5. **Ambient context** -- lighting, camera angles, and animation are tuned to simulate real-world conditions, enhancing the visual fidelity for decision-making

The resulting digital twin (illustrated in Figures 1-4 of the paper) shows the MAST-U tokamak with transparent walls revealing glowing plasma filaments inside, combining the CAD structure, photorealistic materials, and JOREK simulation data in a single unified scene.

---

## Challenges Identified

| Challenge | Detail |
|-----------|--------|
| **Windows vs. Linux divide** | Omniverse and its connectors are Windows-optimized; fusion HPC runs on Linux (SLURM). The Linux version lacks feature parity, and Nucleus requires internet access unavailable on HPC compute nodes. |
| **Missing scientific connectors** | No native Omniverse connectors exist for many scientific simulation tools; researchers must build their own, slowing adoption. |
| **Cloud and data residency** | Omniverse Cloud runs on NVIDIA NGC with limited Azure/AWS support, which may not meet fusion facilities' security requirements. On-premises deployment requires expensive GPU infrastructure (NVIDIA OVX). |
| **AR/VR limitations** | CloudXR is Windows-only, preventing use on Linux research systems for virtual inspections, training, and control room visualization. |
| **Scalability** | Traditional modeling approaches lack the scalability and real-time responsiveness needed for large projects like ITER, STEP, or CFETR. |

---

## Practical Takeaways for Scientists Building Digital Twins

1. **Use USD as your interchange format.** It is the closest thing to a universal standard for 3D scenes and is natively supported by Omniverse, Pixar tools, and an increasing number of CAD and simulation packages. Adopting USD early avoids painful format conversion later.

2. **Build the pipeline in stages.** The paper demonstrates a clear three-layer approach: (a) get the CAD geometry right first, (b) add realistic materials, (c) overlay simulation data. Each layer adds value independently and can be developed by different team members.

3. **Leverage existing connectors before writing custom code.** SketchUp-Omniverse and ParaView-Omniverse connectors handled the heavy lifting for CAD and simulation data import. Only build custom connectors when no existing one fits.

4. **PBR materials matter for stakeholder communication.** Photorealistic rendering is not cosmetic -- it helps engineers and non-specialists alike perceive depth, distinguish components, and make better design decisions during reviews.

5. **Plan for the Windows/Linux gap.** If your simulation codes run on Linux HPC clusters, budget time for bridging the data into the Windows-centric Omniverse ecosystem. ParaView as a middleman (Linux-friendly, has an Omniverse connector) is one proven approach.

6. **Stream, don't batch.** The paper advocates connecting live sensor feeds (via MQTT) and running simulations in real time within the digital twin, rather than treating it as a static post-processing visualization tool. This transforms the twin from a display into an operational decision-support system.

7. **Embed AI surrogate models.** Integrating machine-learning surrogates (e.g., for plasma behavior prediction or component wear) through Python APIs makes the digital twin predictive, enabling scenario exploration that would be too slow with full-physics codes.

8. **Omniverse Nucleus enables collaboration.** The centralized file server allows multiple teams across locations to work on the same USD scene simultaneously -- critical for large international projects.

9. **Consider on-premises GPU infrastructure early.** Cloud solutions may not satisfy data-residency or security policies common in national laboratories and fusion facilities. Factor NVIDIA OVX or equivalent on-premises GPU clusters into procurement plans.

10. **The digital twin is a living artifact.** The paper's vision is a twin that evolves throughout the facility lifecycle -- from design through construction, operation, and maintenance -- not a one-time visualization created for a single review milestone.

---

## Notable References

- **Grieves, M.** (2014). "Digital twin: Manufacturing excellence through virtual factory replication." -- The foundational white paper that coined the modern digital twin concept (Ref. 31).
- **NVIDIA Omniverse documentation** (2023). "The platform for building digital twins." -- Primary platform reference (Ref. 49).
- **Pixar / OpenUSD** (2023). "Universal scene description: A framework for interchangeable 3D formats." -- The file format underpinning the entire workflow (Ref. 50).
- **Hoelzl, M. et al.** (2021). "The JOREK non-linear extended MHD code and applications to large-scale instabilities." *Nuclear Fusion* 61, 065001. -- The plasma simulation code whose output is visualized in the digital twin (Ref. 60).
- **Squillacote, A.H. et al.** (2007). *The ParaView Guide.* Kitware. -- The scientific visualization tool used as the bridge between simulation output and Omniverse (Ref. 62).
- **Gopakumar, V. et al.** (2024). "Plasma surrogate modelling using Fourier neural operators." *Nuclear Fusion* 64, 056025. -- AI surrogate model integrated into the digital twin for predictive plasma modeling (Ref. 68).
- **Bhatia, N. et al.** (2025). "Advanced techniques for fusion data visualisation." *Frontiers in Physics* 13, 1569248. -- Companion paper from the same group on broader fusion visualization techniques (Ref. 23).
- **Page, B., Yorke-Biggs, and De Guido, S.** (2022). *IDE Digital Twin White Paper: Harnessing the Digital Twin for Real Competitive Advantage.* Loughborough University. -- Strategic perspective on digital twin value (Ref. 75).
- **Smith, S., Pamela, A. et al.** (2020). "Simulations of edge localised mode instabilities in MAST-U Super-X tokamak plasmas." *Nuclear Fusion* 60, 066021. -- The specific ELM simulation results visualized in the paper's figures (Ref. 65).
