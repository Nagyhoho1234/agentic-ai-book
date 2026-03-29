# Chapter 5: Flow Control, Data Handling and Transformation

## Comprehensive Summary

Chapter 5 is a dense, technical chapter covering two major domains: (1) flow control logic that makes workflows intelligent, and (2) data handling/transformation techniques that make data usable. The chapter bridges the gap from simple sequential workflows to sophisticated, branching automation systems.

### Part 1: Flow Control

**Sharing Workflows (5.1)**
- Workflows are saved as JSON files (digital blueprints)
- Three sharing methods: Copy/Paste (Ctrl+C/V for selected nodes), Import/Export Menu (download/upload full workflows as JSON), Command Line (bulk operations for power users)
- Always review shared workflows for sensitive data (API keys, emails, credentials)

**Flow Logic (5.2)**
- Data flows as "items" (like a deck of trading cards) -- each node processes individual items or the whole set
- **Splitting:** IF Node (binary yes/no) and Switch Node (multi-path routing) create decision branches
- **Merging:** Merge Node combines data streams back together; Compare Datasets finds matches/differences between lists; Code Node for custom merge rules
- **Looping:** n8n auto-loops most operations (100 items -> 100 automatic iterations). Custom loops needed for: (a) looping until a condition is met, (b) batch processing large datasets
- **Waiting:** Wait Node pauses execution for rate limiting, scheduled timing, or until external events

**Logic, Loops, and Complex Flows (5.3)**
- **IF Node:** Primary binary decision-maker with AND/OR condition combining
- **Switch Node:** Multi-path router for 3+ outcomes (e.g., sort files by type, route tickets by category)
- **Split in Batches:** Breaks large lists into manageable chunks for: respecting API rate limits, preventing memory issues, managing bulk campaigns
- **Parallel vs. Sequential Processing:** Sequential when output of A feeds input of B; Parallel (via Execute Workflow with "Wait" disabled) when tasks are independent
- **Sub-Workflows:** Reusable building blocks called via Execute Workflow node. Build once, use everywhere. Update in one place.

**Project: E-commerce Order Processing System** -- Multi-channel order intake, intelligent routing, parallel processing, error handling, real-time notifications, modular sub-workflow design

**Mastering Triggers (5.3 continued)**
- Manual Triggers: On-demand testing
- Schedule Triggers: Cron-like (seconds to months), advanced scheduling for complex patterns
- Webhook Triggers: Unique URL that fires workflow on incoming HTTP request (real-time, no polling waste)
- App-Specific Triggers: Gmail, Slack, Form triggers for near-real-time reaction without burning rate limits

**Project: Morning Briefing Automation** -- Schedule Trigger (6 AM) -> OpenWeatherMap -> Google Calendar -> Gmail -> Set Node (format) -> Email/Slack delivery

### Part 2: Data Handling and Transformation

**JSON Explained (5.4)**
- JSON (JavaScript Object Notation): Universal data format using key-value pairs
- Objects `{}` hold labeled collections; Arrays `[]` hold ordered lists
- Nesting: objects within objects, arrays within arrays (like Russian nesting dolls)
- Value types: strings, numbers, booleans, null
- Common mistakes: single quotes instead of double, trailing commas, confusing arrays and objects

**Expressions (5.5)**
- Expressions `{{ }}` dynamically reference data from other nodes
- `{{ $json }}` accesses all data from the previous node
- Dot notation: `{{ $json.customer.address.city }}` for nested fields
- Set Node (Edit Fields): Data sculptor for creating/modifying/combining fields
- Filter Node: Bouncer that only lets through items matching criteria

**Advanced Data Manipulation (5.6)**
- **HTTP Request Node:** Universal API connector (GET, POST, PUT, DELETE) with auth support (API keys, OAuth 2.0, Bearer Tokens)
- **Three Data Sculptors:** Set Node (daily cleanup), Merge Node (data matchmaker), Code Node (custom logic engine)
- **Multi-Source Integration:** Creating "Customer 360 View" by combining CRM, support, and purchase data; designate "source of truth" for each data type
- **Code Node (JavaScript):** `$input.all()` to get all incoming items, `$("NodeName").first().json` to reference any node, `DateTime.now()` for date math, always use try...catch for error safety

**Project: Multi-Source Analytics Dashboard** -- Four-layer architecture: Gather (API connections), Clean (Set/Code/Merge), Calculate (KPIs via Code), Present (charts via QuickChart + email/Slack delivery)

## Key n8n Workflow Concepts

- Data flows as arrays of JSON objects between nodes
- IF Node = 2 paths; Switch Node = N paths; Merge Node = combine paths
- Split in Batches + Wait Node = respectful API consumption
- Sub-workflows via Execute Workflow node enable modular, reusable design
- Webhooks eliminate polling overhead for real-time integrations
- `{{ $json.field }}` expressions are the core mechanism for dynamic data access
- Code Node with `$input.all()` and `$("NodeName")` for cross-node data access
- Set Node's "Keep Only Set Fields" option strips unnecessary data

## Practical Takeaways for Scientists

- **Batch processing for large datasets:** When processing thousands of records (e.g., sample metadata, sensor readings), use Split in Batches to avoid memory issues and API rate limits
- **Parallel processing for independent analyses:** Run multiple data source queries simultaneously (e.g., fetch from three databases at once) using Execute Workflow without wait
- **Sub-workflows for reusable lab procedures:** Create standardized data cleaning, quality checking, or notification sub-workflows that any main workflow can call
- **JSON fluency is essential:** Every API your instruments or databases expose speaks JSON. Understanding objects, arrays, and dot notation is the key to extracting exactly the data you need.
- **Expressions for dynamic behavior:** Use conditional expressions in Set nodes (e.g., temperature-based alerts, threshold-based classification) to make workflows adapt to each data point
- **Morning briefing pattern:** Scientists can adapt this to daily automated reports on instrument status, new publications, or data pipeline health
- **Code Node as escape hatch:** When built-in nodes cannot handle your specific transformation (custom statistical calculations, domain-specific data formats), the Code Node with JavaScript or Python gives you full flexibility

## Notable References

- JSON specification: JavaScript Object Notation
- QuickChart: External chart generation service for automated reporting
- n8n expressions documentation: `{{ $json }}`, `{{ $("NodeName") }}`, `{{ DateTime.now() }}`
