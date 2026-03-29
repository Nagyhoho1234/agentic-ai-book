# Chapter 5: Chatting with GitHub Copilot

## Summary

This chapter covers the full chat experience in GitHub Copilot, which goes far beyond simple code completion. The chat interface provides three distinct modes -- Ask Mode, Edit Mode, and Agent Mode -- each suited to different workflows.

### Ask Mode

The default conversational mode. You ask questions and Copilot responds with explanations, code snippets, or suggestions. It is read-only -- it does not modify your files. Best for:
- Understanding unfamiliar code
- Exploring architectural options
- Getting explanations of errors or concepts
- Researching before making changes

### Edit Mode

A directed editing mode where you select code and tell Copilot how to change it. Copilot proposes specific modifications to your files, shown as a diff that you can accept or reject. Best for:
- Refactoring existing code
- Adding error handling or logging
- Converting between formats or patterns
- Targeted modifications to specific files

### Agent Mode

The most powerful and autonomous mode. You describe a goal, and Copilot iteratively works to achieve it: planning steps, reading files, making edits, running terminal commands, executing tests, and iterating until the task is complete. Agent Mode can:
- Create entire new features across multiple files
- Run tests and fix failures automatically
- Install dependencies and configure build tools
- Iterate on its own work based on error feedback

### Chat Participants and Slash Commands

Special prefixes let you direct questions to specific contexts:
- `@workspace`: Searches across your entire project
- `@vscode`: Questions about VS Code settings and features
- `@terminal`: Helps with command-line tasks
- `/fix`: Fix a problem in the selected code
- `/tests`: Generate tests for selected code
- `/doc`: Generate documentation
- `/explain`: Explain the selected code

### Context Variables

You can explicitly add context to your prompts using `#` references:
- `#file`: Reference a specific file
- `#selection`: The currently selected code
- `#codebase`: Search the entire codebase
- `#terminalLastCommand`: Include the last terminal output
- `#symbol`: Reference a specific function, class, or variable

### Custom Chat Modes

Users can create reusable custom chat modes (saved as `.chat` files) that define specific behaviors, constraints, and system prompts for specialized tasks.

## Key AI Coding Techniques

- **Progressive complexity**: Start with Ask Mode for research, move to Edit Mode for targeted changes, and use Agent Mode for multi-step tasks
- **Context stacking**: Combine multiple `#` references to give Copilot rich context about your task
- **Conversation management**: Start fresh conversations when switching tasks to avoid context pollution
- **Agent Mode for TDD**: Describe what you want, let Agent Mode write tests first, then implement the code to pass them
- **Custom instructions**: Use `.github/copilot-instructions.md` to set project-level defaults for all chat interactions
- **Model switching mid-chat**: Switch to a more capable model (e.g., Claude Sonnet 3.7) for complex reasoning tasks

## Practical Takeaways for Scientists

- Use Ask Mode to understand unfamiliar libraries or code patterns before attempting modifications
- Edit Mode is excellent for repetitive refactoring tasks like adding type hints, docstrings, or error handling to existing scripts
- Agent Mode can scaffold entire analysis pipelines -- describe your data processing steps and let it create the code, tests, and documentation
- Use `@workspace` to ask questions about your entire project: "Where do I load the calibration data?" or "Which files handle the statistical analysis?"
- Reference specific files with `#file` when asking about data formats or processing steps: "Given #file:data_loader.py, add validation for missing values"
- Custom chat modes can encode domain-specific instructions, e.g., "Always use numpy for array operations, prefer vectorized operations over loops"
- The `/tests` command can generate unit tests for your analysis functions, improving confidence in your code

## Notable References

- Agent Mode uses premium requests from your monthly allocation
- The `@workspace` participant uses an index of your project for semantic search
- Custom chat modes are stored as `.chat` files and can be shared with team members
- The GitHub Copilot CLI (`gh copilot`) provides chat capabilities in the terminal
- Copilot Chat is also available on GitHub.com in the immersive view for repository-level interactions
