# Chapter 8: Infrastructure as Code

## Summary

This chapter demonstrates how Copilot can generate Infrastructure as Code (IaC) artifacts, covering Azure bicep files, ARM templates, Terraform, and deployment pipelines. The author argues that IaC is one of the areas where Copilot provides the most immediate value, since infrastructure code is highly repetitive, pattern-based, and well-represented in training data.

The chapter walks through generating Azure resources using bicep templates with Copilot assistance, including App Services, databases, storage accounts, and networking configurations. Wienholt shows how Copilot can generate complete deployment pipelines for both Azure DevOps (YAML pipelines) and GitHub Actions, including build, test, and deployment stages.

IaC design patterns are covered, including resource naming conventions, environment parameterization (dev/staging/production), and the declarative framework approach where infrastructure state is defined and the platform handles convergence. The chapter also covers IaC as design -- using infrastructure definitions as architectural documentation.

DACPAC files for SQL Server database deployment are covered as a specific example of database IaC. The chapter demonstrates how Copilot can generate deployment scripts, rollback procedures, and environment-specific configuration transforms.

A practical section covers DevOps pipeline generation, showing how Copilot can create CI/CD pipelines that build, test, and deploy applications automatically. The integration between infrastructure definitions and deployment pipelines is emphasized as a key area where Copilot accelerates development.

## Key AI Coding Techniques

- **Bicep/ARM template generation**: Copilot generates Azure infrastructure templates from natural language descriptions
- **Terraform generation**: Copilot can produce HCL code for multi-cloud infrastructure
- **Pipeline YAML generation**: Generate Azure DevOps or GitHub Actions pipeline definitions
- **Resource parameterization**: Copilot helps create parameterized templates for multi-environment deployments
- **DACPAC generation**: Generate SQL Server Database Projects for schema version control
- **Automated tuning operations**: Generate scripts for database and infrastructure auto-tuning
- **Auto-scaling configuration**: Copilot generates scaling rules for cloud resources

## Practical Takeaways for Scientists

- IaC is one of Copilot's strongest areas -- even non-DevOps specialists can generate quality infrastructure code
- Use Copilot to generate reproducible research environments (Docker containers, VM configurations, cloud resources)
- For HPC workloads, Copilot can generate Azure Batch or AWS Batch configurations
- Database deployment automation (DACPAC) eliminates manual schema migration errors
- Always parameterize infrastructure for different environments (dev for testing, production for results)
- Copilot-generated pipelines can automate the entire build-test-deploy cycle for scientific applications
- Review generated infrastructure for cost implications -- Copilot may default to expensive configurations
- Infrastructure code should be version-controlled alongside application code

## Notable References

- Azure bicep template language
- ARM (Azure Resource Manager) templates
- Terraform by HashiCorp
- Azure DevOps YAML pipelines
- GitHub Actions workflow definitions
- DACPAC (SQL Server Data-Tier Application) files
- Azure App Service, Kubernetes, and container deployment patterns
- New-AzResourceGroup and Azure PowerShell commands
