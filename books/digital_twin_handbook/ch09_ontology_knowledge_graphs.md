# Chapter 9 -- Ontology and Knowledge Graphs for Digital Twins

**Authors:** Chapter contributors

## Summary

This chapter addresses the semantic foundation of digital twins through ontologies and knowledge graphs. It argues that for DTs to achieve true interoperability -- both across domains and between different DT platforms -- they need formal, machine-readable descriptions of their structure, properties, relationships, and behaviours. Ontologies provide this formal vocabulary and knowledge graphs organise DT knowledge into queryable, interconnected structures. The chapter covers ontology engineering methodologies, existing DT-relevant ontologies, knowledge graph construction and querying, and the role of semantic web technologies (RDF, OWL, SPARQL) in DT systems.

## Key Concepts and Architectures

### Why Ontologies for DTs?
- **Interoperability** -- Different DTs built by different teams/vendors can communicate if they share a common ontological framework.
- **Knowledge reuse** -- Ontologies capture domain knowledge that can be reused across DT instances.
- **Automated reasoning** -- Formal ontologies enable logical inference over DT data (e.g., automatically detecting that a sensor reading violates a constraint).
- **Data integration** -- Knowledge graphs built on ontologies can integrate heterogeneous data sources (IoT, BIM, GIS, ERP) into a unified queryable structure.

### Key Ontologies and Standards
- **SSN/SOSA** (Semantic Sensor Network / Sensor, Observation, Sample, Actuator) -- W3C standard for describing sensors and their observations.
- **BOT** (Building Topology Ontology) -- W3C community group standard for building spatial structure.
- **SAREF** (Smart Applications REFerence ontology) -- ETSI standard for IoT device interoperability.
- **BrickSchema** -- Ontology for building metadata, particularly HVAC and energy systems.
- **IFC/ifcOWL** -- Industry Foundation Classes for BIM, with an OWL representation for semantic querying.
- **DTDL** (Digital Twin Definition Language) -- Microsoft's JSON-LD-based modelling language (covered in detail in Ch. 10).

### Knowledge Graph Architecture for DTs
1. **Data ingestion layer** -- ETL pipelines that transform raw sensor data, BIM models, and operational data into RDF triples.
2. **Ontology layer** -- Formal domain ontologies defining classes, properties, and relationships.
3. **Knowledge graph store** -- Triple store (e.g., Apache Jena, GraphDB, Stardog) or property graph database (Neo4j).
4. **Query and reasoning layer** -- SPARQL endpoints for querying; OWL reasoners for inference.
5. **Application layer** -- DT dashboards, analytics engines, and decision-support tools that consume knowledge graph data.

### Ontology Engineering for DTs
- **Competency questions** -- Start by defining what questions the DT needs to answer; these drive ontology scope.
- **Modular design** -- Build small, focused ontologies that can be composed rather than one monolithic ontology.
- **Alignment with existing standards** -- Reuse SSN/SOSA, BOT, SAREF where applicable rather than reinventing.
- **Versioning** -- Ontologies must evolve as the DT evolves; version management is essential.

## Practical Takeaways for Scientists

1. **Ontologies are the most underinvested component of DT projects** -- teams typically focus on sensors and visualisation while neglecting the semantic layer, which then becomes the bottleneck for data integration and interoperability.
2. **Start with competency questions** -- "What questions does my DT need to answer?" drives the ontology design far more effectively than trying to model everything.
3. **Reuse existing ontologies** (SSN/SOSA, BOT, SAREF) rather than building from scratch; ontology alignment tools can bridge gaps.
4. **Knowledge graphs enable powerful cross-domain queries** -- e.g., "Which rooms in this building have had temperature readings above 28C and are occupied by patients with respiratory conditions?" -- queries that span IoT, BIM, and health data.
5. **For scientific DTs, consider using property graph databases (Neo4j)** if your team lacks semantic web expertise; they are more accessible than triple stores while still supporting graph-based queries.
6. **JSON-LD (used by DTDL) bridges the gap** between developer-friendly JSON and semantic web technologies -- it is a pragmatic starting point.

## Notable References

- W3C SSN/SOSA Ontology -- https://www.w3.org/TR/vocab-ssn/
- Rasmussen, M.H. et al. (2020). BOT: the Building Topology Ontology of the W3C Linked Building Data Group. *Semantic Web*, 12(1):143--161.
- ETSI SAREF -- https://saref.etsi.org/
- Balaji, B. et al. (2018). Brick: Metadata schema for portable smart building applications. *Applied Energy*, 226:1273--1292.
