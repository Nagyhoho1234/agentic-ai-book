# Chapter 3: Getting Started with Copilot

## Summary

This chapter provides a hands-on walkthrough of setting up and using GitHub Copilot across different IDEs, with primary focus on Visual Studio and VS Code. It covers the various Copilot subscription tiers (Individual, Business, Enterprise), installation procedures, and the core interaction patterns developers use daily.

The chapter explores the different ways to interact with Copilot: inline code completion (the "gray text" suggestions), the Chat panel, the suggestion panel, prompt engineering techniques, and screen-shot prompting. Wienholt demonstrates how Copilot generates code through a practical example of building a simple .NET Core application, showing both the strengths (rapid boilerplate generation) and weaknesses (occasional incorrect suggestions) of the tool.

A significant portion covers the Copilot Chat window, explaining how to use slash commands, attach context via the `#` symbol, and leverage the different LLM models available (GPT-4o, o3-mini, Claude 3.7 Sonnet). The chapter also covers non-code file support, showing that Copilot can assist with markdown, YAML, JSON, and other configuration files.

The chapter includes a detailed comparison of Copilot in Visual Studio versus VS Code, noting that the VS Code experience is generally ahead in features. Pull request integration on GitHub.com is also covered, including AI-generated PR descriptions and code review suggestions.

## Key AI Coding Techniques

- **Inline completion**: Accept gray-text suggestions with Tab; cycle through alternatives with Alt+] and Alt+[
- **Chat-based interaction**: Use Copilot Chat for more complex requests, code explanation, and debugging
- **Context attachment**: Use `#file`, `#selection`, and `#codebase` to provide relevant context to Copilot
- **Slash commands**: `/explain`, `/fix`, `/tests`, `/doc` for common operations
- **Prompt engineering**: Write clear, specific comments to guide code generation; the "iCarly character" example shows how non-code prompts can test model behavior
- **Screen-shot prompting**: Paste screenshots of UI designs for Copilot to generate matching code
- **Model switching**: Select different LLM models (GPT-4o, o3-mini, Claude) for different tasks within the same session
- **Apply In Editor**: Use the "Apply In Editor" button to insert Chat-generated code directly into the active file

## Practical Takeaways for Scientists

- Start with the Copilot Individual plan ($10/month) to experiment before committing to enterprise adoption
- VS Code offers the most complete Copilot experience and is free
- Use comments as "prompts" -- write a descriptive comment about what you want, and Copilot will suggest the implementation
- For data analysis scripts, attach relevant data files or schema descriptions to the Chat context for better suggestions
- The suggestion panel (Ctrl+Enter) shows multiple alternatives, useful when the first suggestion is not quite right
- Copilot works with Jupyter Notebooks, making it directly useful for scientific computing workflows

## Notable References

- GitHub Copilot subscription tiers and pricing
- Visual Studio vs. VS Code feature comparison for Copilot
- GitHub.com PR integration with Copilot
- Copilot Chat slash commands reference
- Multiple LLM model options within Copilot
