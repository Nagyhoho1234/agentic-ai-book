# Chapter 10 -- Digital Twin Modelling with DTDL

**Authors:** Chapter contributors

## Summary

This chapter provides a detailed technical guide to the Digital Twin Definition Language (DTDL), Microsoft's open modelling language for describing digital twins. DTDL is a JSON-LD-based language that defines the structure, properties, telemetry, commands, relationships, and components of digital twin models. The chapter covers DTDL syntax, semantic types, model composition, and practical modelling patterns for creating interoperable DT definitions that can be deployed on Azure Digital Twins and other compatible platforms.

## Key Concepts and Architectures

### DTDL Fundamentals
- **JSON-LD based** -- DTDL models are valid JSON-LD documents, providing compatibility with semantic web technologies.
- **Interface** -- The top-level construct in DTDL; defines a type of digital twin. Each interface has an `@id` (a DTMI -- Digital Twin Model Identifier), a `@type` of "Interface", and optional `contents`.
- **DTMI format:** `dtmi:<domain>:<model>;<version>` (e.g., `dtmi:com:example:Thermostat;1`).

### DTDL Content Types
1. **Property** -- Writable state data stored on the DT. Has a name, schema (data type), and can be read/updated. Examples: temperature setpoint, device name, firmware version.
2. **Telemetry** -- Time-series event data streaming from the physical entity. Not stored on the DT itself but processed as events. Examples: current temperature reading, vibration measurement.
3. **Command** -- An operation that can be invoked on the DT (and forwarded to the physical device). Has request and response schemas. Examples: reboot, calibrate, set_mode.
4. **Relationship** -- A directed link between two DT instances. Has a name, target interface (optional), and optional properties. Examples: "contains", "isPartOf", "controls".
5. **Component** -- An embedded interface within another interface, enabling model composition. Example: A "Room" interface containing a "Thermostat" component.

### DTDL Data Schemas
- **Primitive types:** boolean, date, dateTime, double, duration, float, integer, long, string, time.
- **Complex types:**
  - **Array** -- Ordered collection of elements of a single schema type.
  - **Enum** -- Named set of values.
  - **Map** -- Key-value pairs with defined key and value schemas.
  - **Object** -- Structured type with named fields.
- **Geospatial types:** point, multiPoint, lineString, multiLineString, polygon, multiPolygon (GeoJSON compatible).

### Model Composition Patterns
- **Inheritance** via `extends` -- An interface can extend one or two other interfaces, inheriting all their contents.
- **Component composition** -- Interfaces can contain components that reference other interfaces, enabling nested structures.
- **Relationship graphs** -- Interfaces declare relationships to other interfaces, forming a graph of DT types.

### Semantic Types (Annotations)
- DTDL supports semantic annotations that add physical-unit meaning to properties and telemetry.
- Examples: Temperature, Humidity, Pressure, Velocity, Acceleration, each with associated units.
- Enables automatic unit conversion and validation.

## Practical Takeaways for Scientists

1. **Property vs. Telemetry distinction is critical** -- use Property for state that changes infrequently and needs to be stored (e.g., calibration parameters); use Telemetry for continuous measurement streams (e.g., sensor readings). Getting this wrong leads to either excessive storage costs or lost data.
2. **Model your domain hierarchy using inheritance and components** -- e.g., a "WeatherStation" extends "SensorDevice" and contains components for "TemperatureSensor", "HumiditySensor", etc.
3. **Use semantic types** when they exist for your domain -- this enables automatic unit handling and interoperability with other DTDL-based systems.
4. **DTDL is platform-independent in principle** -- while Microsoft created it for Azure Digital Twins, the JSON-LD format means models can be parsed and used by any system.
5. **Version your models** using the DTMI version number; breaking changes require a version increment.
6. **Geospatial schemas are built in** -- if your DT has a spatial component (most scientific DTs do), use the GeoJSON-compatible geospatial types rather than encoding coordinates as raw numbers.

## Notable References

- Microsoft (2022). DTDL specification v2 -- https://github.com/Azure/opendigitaltwins-dtdl
- Azure Digital Twins documentation -- https://learn.microsoft.com/en-us/azure/digital-twins/
- JSON-LD specification -- https://www.w3.org/TR/json-ld/
