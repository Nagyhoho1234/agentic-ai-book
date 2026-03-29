# Chapter 6: Collaborating with Copilot on GitHub.com: Issues, PRs, Reviews, and Coding Agent

## Summary

This chapter marks the transition from Copilot as a personal coding tool to Copilot as a collaborative team tool integrated directly into GitHub.com. It covers how Copilot can help with issues, pull requests, code reviews, security, and autonomous coding tasks.

### Issues and Discussions

Copilot Chat on GitHub.com can help draft issues, summarize discussion threads, suggest clarifying questions, and even create issues from repository context. In the immersive Copilot Chat on GitHub.com, you can use `@workspace` to summarize repositories and their key modules.

### Pull Request Summaries

When opening a PR, GitHub Copilot can automatically generate a summary of the changes, describing what was modified, why, and what reviewers should focus on. This uses a "copilot-genai-summary" label and can be regenerated as changes are pushed.

### Copilot as a PR Reviewer

You can assign GitHub Copilot as a reviewer on pull requests (via the Reviewers panel). Once added, Copilot can:
- Analyze changes and leave review comments
- Flag potential bugs, inconsistencies, or style issues
- Suggest improvements such as better test coverage or simplified code
- Generate PR summaries to help reviewers understand the scope

Copilot supports iterative conversation inside the PR -- you can ask it to clarify code blocks, expand on comments, or provide alternatives using `@copilot` mentions.

### Autofix (PR Reviews vs. Advanced Security)

Two distinct Autofix capabilities:
1. **PR review Autofix**: During code reviews, Copilot suggests inline fixes for risky or inefficient code (e.g., suggesting parameterized SQL queries instead of string interpolation)
2. **GitHub Advanced Security Autofix**: Responds to code scanning alerts (e.g., SQL injection, XSS) by proposing targeted remediation. Can be triggered from the alert details page via "Generate fix" button

**Security campaigns** let administrators group related vulnerabilities across many repositories and apply Copilot Autofix fixes in bulk.

### Coding Agent on GitHub.com

The most advanced feature: the Coding Agent lets you delegate entire development tasks to Copilot. You can:
- **Assign an issue to Copilot**: Select Copilot as assignee, and it will read the issue, create a branch, implement changes, run tests, and open a draft PR
- **Use the Agents panel**: A pop-up overlay from any GitHub page to describe tasks in natural language and launch the agent
- **Assign from your editor**: VS Code supports delegating tasks to the Coding Agent directly

The Coding Agent:
- Runs in a secure GitHub Actions workspace (locked-down network by default)
- Creates a new branch and applies changes
- Runs checks and iterates if needed
- Opens a draft PR with a WIP title
- Uses one premium request per session
- Can be extended with MCP servers for additional context

### Coding Agent vs. Agent Mode

- **Agent Mode (IDE)**: Interactive, local, you stay hands-on
- **Coding Agent (GitHub.com)**: Asynchronous, cloud-based, you hand off and review later

The Coding Agent works best for well-scoped tasks: fixing bugs, adding tests, updating documentation. It needs a good README, custom instructions, and existing tests to validate its work.

### Metrics and Activity Dashboards

Admins on Business/Enterprise plans can monitor Copilot adoption through three dashboards:
- **Copilot IDE usage**: Active users, agent adoption, chat requests per user
- **Premium request analytics**: Costs, billing, usage by product (Copilot, Coding Agent, Spark)
- **Detailed usage patterns**: Requests per chat mode (Ask, Edit, Agent), code completion acceptance rates, model usage per day

## Key AI Coding Techniques

- **Assigning Copilot as PR reviewer**: Add Copilot to the Reviewers panel to get automated code review feedback
- **@copilot mentions in PRs**: Ask Copilot to clarify specific code blocks, explain trade-offs, or suggest alternatives directly in PR comments
- **Coding Agent for contained tasks**: Delegate bug fixes, test creation, and documentation updates to the Coding Agent
- **Security campaigns with Autofix**: Use bulk Autofix across repositories to remediate common vulnerabilities
- **Iterative PR conversations**: Copilot maintains conversation context within a PR thread, allowing back-and-forth refinement

## Practical Takeaways for Scientists

- Use PR summaries to help collaborators understand what changed in your analysis code without reading every line
- Assign Copilot as a reviewer to catch common issues like missing error handling, unsafe file operations, or hardcoded paths
- The Coding Agent can be used to add unit tests to existing analysis scripts -- assign an issue like "Add tests for data_loader.py" and review the resulting PR
- Security Autofix can catch SQL injection or other vulnerabilities if your research involves web-facing tools or databases
- The Agents panel on GitHub.com lets you delegate tasks from your phone or tablet -- useful for triggering work while away from your development machine
- Dashboard metrics help PIs and lab managers understand how their team is using AI tools

## Notable References

- Each PR review request consumes one premium request
- Each Coding Agent session consumes one premium request regardless of file count
- Each `@copilot` interaction in a PR consumes a premium request
- Branch protection rulesets can require a second human approval even when Copilot opens a PR
- Smart integrations: teams have integrated Copilot into GitHub Actions workflows so that when a workflow fails, an issue is automatically created and assigned to the Coding Agent
