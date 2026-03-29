# Chapter 11 -- Digital Twins Services Implementation

**Authors:** Chapter contributors

## Summary

This chapter is the most hands-on in the book, providing a step-by-step guide to implementing digital twin services using Microsoft Azure. It covers the full implementation pipeline: setting up the Azure development environment, modelling physical entities using DTDL (from Ch. 10), provisioning and managing Azure Digital Twins (ADT) instances via both the Azure portal and programmatic APIs, and building applications that create, query, and manage digital twins and their relationships. The chapter distinguishes between control plane APIs (managing Azure resources) and data plane APIs (managing the DT content), and provides C# code examples for every operation.

## Key Concepts and Architectures

### Azure Digital Twins (ADT) Architecture
- **ADT instance** -- A cloud-hosted DT service that stores models, twins, and relationships as a knowledge graph.
- **Twin graph** -- The runtime graph of DT instances and their relationships within an ADT instance.
- **Event routing** -- ADT connects to Azure Event Grid, Event Hubs, and Service Bus for propagating DT state changes to downstream services.
- **Time series storage** -- ADT connects to Azure Data Explorer for historical data analysis (the twin graph itself only stores current state).

### Implementation Pipeline

1. **Environment setup:**
   - Visual Studio or VS Code with Azure SDK.
   - .NET CLI for package management.
   - Required NuGet packages: `Azure.Identity`, `Azure.ResourceManager`, `Azure.ResourceManager.DigitalTwins`, `Azure.DigitalTwins.Core`.

2. **Model management (DTDL models):**
   - **Upload:** `CreateModelsAsync` -- upload one or more DTDL model definitions.
   - **Get:** `GetModelAsync` -- retrieve a model by its DTMI.
   - **Decommission:** `DecommissionModelAsync` -- disable new twin creation from a model (existing twins unaffected).
   - **Delete:** `DeleteModelAsync` -- permanently remove a model.

3. **Twin management:**
   - **Create/Replace:** `CreateOrReplaceDigitalTwinAsync` -- create a twin with a model ID, twin ID, and property values. Uses `BasicDigitalTwin` class.
   - **Get:** `GetDigitalTwinAsync` -- retrieve a twin by ID.
   - **Update properties:** `UpdateDigitalTwinAsync` -- partial update using `JsonPatchDocument` (RFC 6902).
   - **Publish telemetry:** `PublishTelemetryAsync` -- send telemetry events (array, geospatial schemas supported).
   - **Delete:** `DeleteDigitalTwinAsync`.

4. **Relationship management:**
   - **Create/Replace:** `CreateOrReplaceRelationshipAsync` -- link two twins with a named, directed relationship.
   - **Get outgoing:** `GetRelationshipsAsync` -- list relationships from a source twin.
   - **Get incoming:** `GetIncomingRelationshipsAsync` -- list relationships targeting a twin.
   - **Delete:** `DeleteRelationshipAsync`.

5. **Querying the twin graph:**
   - ADT Query Language (SQL-like): supports `SELECT`, `FROM`, `WHERE`, `JOIN`, `MATCH`.
   - Query by property: `SELECT * FROM DIGITALTWINS T WHERE T.temperature > 0.3`
   - Query by model: `SELECT * FROM DIGITALTWINS WHERE IS_OF_MODEL('dtmi:dtdl:context:Robot;1')`
   - Query by function: `IS_DEFINED`, `IS_NUMBER`, `IS_STRING`, `IS_BOOL`, `STARTSWITH`, `ENDSWITH`, `CONTAINS`.
   - Operators: comparison (`=`, `!=`, `<`, `>`), containment (`IN`, `NIN`), logical (`AND`, `OR`, `NOT`).
   - **Limitations:** ~10 s latency for reflecting changes; only stores current state (historical queries require Azure Data Explorer).

### Control Plane vs. Data Plane APIs
| Aspect | Control Plane (ARM) | Data Plane (ADT Core) |
|--------|--------------------|-----------------------|
| Purpose | Manage Azure resources | Manage DT content |
| Library | `Azure.ResourceManager.DigitalTwins` | `Azure.DigitalTwins.Core` |
| Operations | Create/delete ADT instances | CRUD for models, twins, relationships |
| Auth | Azure Resource Manager | ADT instance endpoint + credential |

### Data Type Mapping (DTDL to C#)
- `boolean` -> `bool`; `date/dateTime/time/duration` -> `string` (ISO 8601); `double` -> `double`; `float` -> `float`; `integer` -> `int`; `long` -> `long`; `string` -> `string`; `object` -> `object{}` / anonymous type; `map` -> `Dictionary<string, string>`.

## Practical Takeaways for Scientists

1. **Azure Digital Twins is a graph database for DTs, not a time-series database** -- it stores the current state of twins and their relationships. For historical analysis, connect to Azure Data Explorer or another time-series store.
2. **Use `JsonPatchDocument` for property updates** rather than replacing the entire twin -- this is more efficient and supports concurrent updates.
3. **The query language has a ~10 s latency** for reflecting changes -- if your application needs immediate consistency, use the data plane API directly rather than querying.
4. **Authentication uses `DefaultAzureCredential`** which supports multiple credential types (managed identity, CLI login, environment variables) -- configure this correctly for both development and production.
5. **Model management follows a lifecycle:** upload -> use -> decommission -> delete. Decommissioning prevents new twin creation but preserves existing twins -- useful for versioned model migrations.
6. **For scientific applications, the query language's geospatial support is limited** -- consider complementing ADT with a spatial database if complex spatial queries are needed.
7. **Cost management:** ADT pricing is based on operations, messages, and query units. Telemetry-heavy applications can become expensive; batch telemetry where possible.

## Notable References

- Microsoft Azure Digital Twins documentation -- https://learn.microsoft.com/en-us/azure/digital-twins/
- Azure IoT Digital Twins client library -- https://learn.microsoft.com/en-us/dotnet/api/overview/azure/digitaltwins.core-readme
- Hofgen, J. et al. (2023). Architecture of a Versatile Digital Twin with Socket-Based Communication and Azure DT. *IEEE CASE 2023*.
- Pfeiffe, D. et al. (2022). Modeling capabilities of digital twin platforms -- old wine in new bottles? *The Journal of Object Technology*, 21(3).
