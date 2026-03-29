# Chapter 3: Setting Up and Configuring GitHub Copilot

## Summary

This chapter is a comprehensive guide to getting GitHub Copilot installed, configured, and running across different editors and plans. It covers the full range of subscription tiers, editor integrations, and organizational configuration options.

### Subscription Plans

- **Copilot Free**: 2,000 code completions + 50 chat messages per month; no credit card required; limited to GPT-4o and Claude Sonnet 3.5
- **Copilot Pro**: $10/month; unlimited completions and chat; access to all models including GPT-4o, Claude Sonnet 3.7, Gemini 2.5 Pro; 300 premium requests/month
- **Copilot Pro+**: $39/month; same as Pro but with 1,500 premium requests/month and access to the most powerful models
- **Copilot Business**: $19/user/month; organizational management, policy controls, IP indemnity, content exclusion settings
- **Copilot Enterprise**: $39/user/month; everything in Business plus knowledge bases, fine-tuned models for your codebase, Bing search integration

### Premium Requests

The chapter introduces the concept of "premium requests" -- advanced operations that consume from a monthly allocation. These include using high-end models (Claude Sonnet 3.7, Gemini 2.5 Pro, GPT-o1/o3-mini), Agent Mode sessions, and the Coding Agent on GitHub.com. Base-tier requests (GPT-4o, Claude Sonnet 3.5) are unlimited for paid plans.

### Editor Setup

Detailed setup instructions are provided for:
- **VS Code**: Install the GitHub Copilot and GitHub Copilot Chat extensions
- **Visual Studio**: Built-in support starting from VS 2022 17.10+
- **JetBrains IDEs**: Plugin available for IntelliJ, PyCharm, WebStorm, etc.
- **Neovim**: Via the copilot.vim plugin
- **GitHub Copilot CLI**: Command-line integration for terminal workflows

### Custom Instructions

A key feature is the ability to create custom instruction files (`.github/copilot-instructions.md`) that tell Copilot about your project's conventions, preferred libraries, coding standards, and domain-specific rules. These instructions are automatically included as context in every interaction.

## Key AI Coding Techniques

- **Custom instructions files**: Create `.github/copilot-instructions.md` to encode your project's conventions so Copilot follows them automatically
- **Content exclusion**: Organizations can exclude specific files or repositories from Copilot's context to protect sensitive data
- **Model switching**: Switch between models mid-conversation to get different perspectives or optimize for speed vs. quality
- **Policy controls**: Admins can control which features are available, which models can be used, and whether suggestions matching public code are blocked

## Practical Takeaways for Scientists

- Start with the Free tier to evaluate whether Copilot helps your workflow before committing to a paid plan
- Create a custom instructions file describing your scientific domain, preferred libraries (numpy, pandas, scipy, etc.), and coding conventions
- The content exclusion feature is important for sensitive research data -- configure it to prevent proprietary data from being sent to the model
- For academic institutions, check whether your university has a GitHub Education or Enterprise agreement that may include Copilot
- Premium requests are consumed by Agent Mode and advanced models -- monitor usage if you are on a budget

## Notable References

- GitHub Copilot plans comparison: https://github.com/features/copilot
- Custom instructions documentation: `.github/copilot-instructions.md`
- IP indemnity is only available on Business and Enterprise plans
- GitHub Copilot Trust Center for security and privacy details
