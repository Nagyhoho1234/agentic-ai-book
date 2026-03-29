# Chapter 6: Security

## Summary

This chapter addresses the security implications of using AI coding tools, covering both the risks of AI-generated code and the security features built into GitHub's platform. The author examines GitHub Advanced Security (GHAS) and its Azure DevOps variant (GHASADO), which provide code scanning, secret detection, and dependency vulnerability analysis.

Wienholt discusses the fundamental tension between AI-generated code velocity and security review capacity. When developers produce code faster with Copilot, the volume of code needing security review also increases. The chapter covers practical security measures including secret scanning (detecting accidentally committed API keys, passwords), code scanning for vulnerability patterns, and dependency review for known CVEs in third-party packages.

The privacy and data handling aspects of Copilot are examined in detail, including what code is transmitted to GitHub's servers, data retention policies, and the differences between Individual, Business, and Enterprise tiers in terms of data handling. The author provides guidance on configuring Copilot's privacy settings for sensitive codebases and regulated industries.

A notable section covers DevOps vulnerabilities -- the risks introduced in build pipelines, deployment scripts, and infrastructure code that AI tools may generate without adequate security consideration.

## Key AI Coding Techniques

- **Secret scanning**: Enable GitHub's secret scanning to catch accidentally committed credentials in AI-generated code
- **Code scanning**: Use GHAS/GHASADO to automatically scan AI-generated code for known vulnerability patterns
- **Dependency review**: Automatically check AI-suggested package dependencies against CVE databases
- **Privacy configuration**: Configure Copilot data retention and telemetry settings based on organizational requirements
- **Prompt injection awareness**: Be aware that AI-generated code may include patterns vulnerable to prompt injection attacks
- **GNU GPL license filtering**: Enable Copilot's filter to block suggestions that match GPL-licensed code

## Practical Takeaways for Scientists

- Always enable secret scanning if working with API keys, database credentials, or other sensitive tokens
- For regulated research (HIPAA, ITAR, export-controlled), understand exactly what data Copilot transmits and configure privacy settings accordingly
- AI-generated infrastructure code (Terraform, bicep) may have security gaps -- always review deployment configurations
- Use the Copilot Business tier ($19/user/month) for research that cannot have code snippets retained by GitHub
- The GNU GPL filter is important if your research software has specific licensing requirements
- DevOps pipeline security is often overlooked -- review AI-generated CI/CD configurations carefully
- Information leakage through AI tools is a real risk in competitive research environments

## Notable References

- GitHub Advanced Security (GHAS) features and pricing
- GHASADO (GitHub Advanced Security for Azure DevOps)
- Copilot privacy settings documentation
- CVE database integration for dependency scanning
- GNU GPL code suggestion filtering
- IsDLEnabledInAD -- checking security feature availability
