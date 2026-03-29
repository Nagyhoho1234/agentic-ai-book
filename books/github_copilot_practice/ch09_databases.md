# Chapter 9: Databases

## Summary

This chapter covers Copilot's capabilities for database development, focusing on SQL Server, Azure SQL, and Entity Framework. The author demonstrates how Copilot can generate SQL queries, stored procedures, database schemas, and data access code, while highlighting important caveats about AI-generated database code.

The chapter opens by positioning databases as an under-explored area for AI assistance. Wienholt shows how Copilot works with the Azure Data Studio and VS Code SQL extensions to provide intelligent SQL completion and generation. Entity Framework integration is covered, demonstrating how Copilot generates data models, DbContext configurations, and LINQ queries from natural language descriptions.

A significant section covers the SQL DacPac file workflow -- creating SQL Server Database Projects in Visual Studio, managing schema changes through version control, and deploying database changes through automated pipelines. The author demonstrates how Copilot can generate foreign key relationships, common table expressions (CTEs), stored procedures, and complex joins.

The chapter also covers database-specific concerns: performance implications of AI-generated queries (missing indexes, inefficient joins), the importance of understanding query execution plans, and the risks of generating data access code that works in development but fails under production load. The SSMS-style querying experience through VS Code extensions is also demonstrated.

Data analysis expressions (DAX) for Power BI and business intelligence scenarios receive brief coverage, showing that Copilot can assist with analytical query formulation.

## Key AI Coding Techniques

- **SQL generation from natural language**: Describe the query intent in comments and let Copilot generate the SQL
- **Entity Framework code generation**: Generate data models, DbContext, and LINQ queries from descriptions
- **Stored procedure generation**: Copilot can generate complex stored procedures with proper parameter handling
- **CTE (Common Table Expression) generation**: Complex hierarchical queries generated from descriptions
- **Database Project scaffolding**: Generate SQL Server Database Projects with schema, procedures, and seed data
- **Foreign key and relationship generation**: Describe entity relationships for Copilot to generate constraints
- **Data Workspace extension**: Use VS Code extensions for database development with Copilot

## Practical Takeaways for Scientists

- Copilot is excellent for generating SQL queries for data extraction and analysis -- describe what you need in plain English
- For scientific databases, use comments to describe the data model (instruments, measurements, samples) before generating schemas
- Always review generated queries for performance -- AI-generated SQL may work correctly but perform poorly on large datasets
- Entity Framework with Copilot can rapidly create data access layers for research data management applications
- CTE generation is particularly useful for hierarchical scientific data (taxonomies, organizational hierarchies, nested measurements)
- Database Projects provide version control for schemas -- essential for reproducible research
- Be cautious with AI-generated queries on production databases; test on representative data volumes first

## Notable References

- SQL Server and Azure SQL database development
- Entity Framework (.NET ORM) integration
- Azure Data Studio and VS Code database extensions
- SQL Server Database Projects (DacPac)
- Common Table Expressions (CTEs) for complex queries
- Data Analysis Expressions (DAX) for business intelligence
- AdventureWorks sample database
- Oracle and PostgreSQL database alternatives
