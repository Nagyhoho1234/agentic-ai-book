# Chapter 7: Extending GitHub Copilot with the Model Context Protocol (MCP)

## Summary

This chapter introduces the Model Context Protocol (MCP), an open standard that lets AI tools like GitHub Copilot connect to external data sources and tools. MCP acts as a "universal plug" (like USB for AI) that provides a consistent interface for Copilot to interact with external systems.

### What is MCP?

MCP answers three fundamental questions:
1. **What can I read?** (Resources -- acceptance criteria, docs, logs, etc.)
2. **What can I do?** (Tools -- small actions with clear inputs/outputs like opening issues, searching logs)
3. **How do we talk safely?** (Transport -- standardized requests with authentication, timeouts, and error handling)

MCP servers expose resources and tools that MCP clients (editors like VS Code) can discover and use. Your prompt stays in natural language while Copilot automatically discovers the server's capabilities, selects the right tool, and sends properly authenticated requests.

### Installing the GitHub MCP Server in VS Code

1. Enable MCP Servers Marketplace in the VS Code Extensions panel
2. Search for and install "GitHub MCP Server"
3. Authenticate with your GitHub account
4. Manage the server via the MCP Server menu (Start/Stop/Restart/Show Configuration)

Once running, you can use GitHub Copilot Chat in Agent Mode to perform tasks directly against GitHub: listing issues, creating branches, managing PRs, all from natural language prompts.

### Security Considerations

- MCP tools work with your credentials and act in your name
- **Tools confusion**: Multiple MCP servers with overlapping tool names may cause Copilot to call the wrong one
- **Prompt injection attacks**: A compromised MCP server response could embed hidden malicious instructions
- VS Code implements guardrails: first-time tool execution requires user confirmation (Allow once, for session, for workspace, or always)
- Always review tool inputs before approving execution

### Local vs. Remote Servers

**Local servers** (run on your machine):
- Started from `mcp.json` or CLI
- Great for prototyping and offline work
- Secrets stay local (OS keychain or `.env` files)
- Can be installed via Python (uvx), NPM (npx), or Docker
- Must be started/stopped manually

**Remote servers** (run as a service):
- Reachable at a URL, no local process needed
- One setup for the whole team
- Centralized policies, authentication, and audit logs
- Require stable network connection
- Managed by server operator for security and updates

### Controlling Access for Organizations

Administrators can configure an MCP registry URL (a JSON file listing approved servers) to restrict which MCP servers are allowed. This ensures consistency and security across the organization.

### End-to-End Example: Azure + GitHub MCP

A single prompt chains two MCP servers:
1. **Azure MCP Server** fetches the latest exception from Azure Monitor
2. **GitHub Copilot** summarizes the error into a clear issue draft
3. **GitHub MCP Server** creates the issue in the repository

Result: one prompt, two MCP servers, one clean GitHub issue with title, labels, exception details, and log link.

### MCP with the Coding Agent (Jira Example)

The Coding Agent can use MCP servers configured at the repository level on GitHub.com:
1. Go to repo Settings > Code & automation > Copilot > Coding Agent
2. Paste MCP server JSON configuration (command, args, environment variables)
3. Store secrets as GitHub Actions secrets prefixed with `COPILOT_MCP_`
4. Enable firewall and recommended allowlist for security

Example: connecting to Jira so the Coding Agent can surface open issues, deadlines, and sprint data directly in Copilot Chat with Agent Mode.

## Key AI Coding Techniques

- **Chaining MCP servers**: Combine multiple servers in a single prompt to create end-to-end workflows (fetch data from one system, process it, create output in another)
- **Repository-level MCP configuration**: Configure MCP servers in GitHub.com repo settings so the Coding Agent can access external tools
- **Natural language tool invocation**: Simply describe what you want; Copilot discovers and calls the appropriate MCP tool automatically
- **Security-first approach**: Always review tool calls before approving, restrict MCP server access via registry URLs, use firewall and allowlist settings

## Practical Takeaways for Scientists

- MCP servers can connect Copilot to your lab's data systems, instrument APIs, or cloud resources without custom code
- Example: create an MCP server for your lab's data repository so Copilot can query experiment metadata directly from the chat
- The local server approach is ideal for prototyping: connect Copilot to local log files, databases, or processing pipelines
- For team environments, remote MCP servers ensure everyone uses the same data connections and tools
- The Azure MCP server example shows how to bridge monitoring/alerting with issue tracking -- applicable to any instrumented scientific pipeline
- MCP is an open standard (https://modelcontextprotocol.io) -- you can build custom servers for domain-specific tools

## Notable References

- MCP registry: https://github.com/mcp -- curated list of MCP servers
- MCP specification: https://modelcontextprotocol.io
- GitHub MCP Server access documentation: https://docs.github.com/en/copilot/how-tos/administer-copilot/configure-mcp-server-access
- MCP is supported in VS Code, Visual Studio, and the GitHub Copilot Coding Agent
- Community news aggregator: https://github-copilot.xebia.ms
