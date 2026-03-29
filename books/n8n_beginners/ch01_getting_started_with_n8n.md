# Chapter 1: Getting Started with n8n

## Comprehensive Summary

Chapter 1 serves as the onboarding guide to n8n, an open-source workflow automation platform. The author positions n8n as a powerful alternative to proprietary tools like Zapier and Make, emphasizing two key advantages: **control** (your data stays on your servers) and **cost** (n8n charges per workflow run, not per step -- a workflow with 20 steps counts as one execution, not 20 billable tasks).

The chapter walks through three installation methods:
1. **n8n Cloud** -- instant access, zero setup, ideal for beginners. Sign up at n8n.io with a free trial.
2. **Local Installation (npm)** -- requires Node.js 16+. Install via `npm install n8n -g`, then run `n8n` and access at `http://localhost:5678`.
3. **Docker** -- the recommended production method. Uses a single `docker run` command to pull and start the n8n container on port 5678. Provides clean isolation and easy scaling.

After installation, the chapter guides you through:
- Creating your owner account (first-time self-hosted access)
- Navigating the dashboard (Overview, Workflows, Credentials, Executions tabs)
- Understanding the workflow editor canvas, left sidebar (Overview, Credentials, Templates, Variables), the Node Library (400+ integrations), and the Execution Area for testing
- Building a "Hello World" demo workflow: Manual Trigger -> Set Node (message: "Hello, World!") -> Execute -> verify output

## Key n8n Workflow Concepts

- **Visual Workflow Builder:** Drag-and-drop interface; no programming required for building complex automations
- **Node Library:** 400+ pre-built integrations (Gmail, Slack, Google Sheets, Twitter, databases, AI models)
- **Three Node Categories:** Trigger nodes (start workflows), Action nodes (do things), Logic nodes (make decisions)
- **Execution Model:** Per-workflow-run pricing (not per-step), making complex workflows cost-effective
- **Credentials System:** Secure, encrypted storage for API keys and OAuth tokens; set up once, reuse across workflows
- **AI-Friendly Architecture:** Built-in support for LLMs (GPT-4, Gemini) to create intelligent agents

## Practical Takeaways for Scientists

- **Zero-cost self-hosting:** The community edition is free when self-hosted, making it ideal for academic labs with limited budgets
- **Docker deployment is recommended** for any persistent/production use -- provides reproducibility and isolation, concepts familiar to computational scientists
- **No vendor lock-in:** All workflows are exportable; you maintain full ownership of your automation logic and data
- **Quick validation:** The "Hello World" workflow takes under 5 minutes to build and confirms your installation is working
- **Extensibility:** If a specific instrument API or data source lacks a built-in node, custom integrations can be created

## Notable References

- n8n website: https://n8n.io
- Docker Desktop: https://docker.com
- n8n runs on port 5678 by default (http://localhost:5678)
