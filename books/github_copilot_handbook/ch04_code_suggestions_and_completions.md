# Chapter 4: Using GitHub Copilot for Code Suggestions and Completions

## Summary

This chapter focuses on the core inline code suggestion experience -- the "ghost text" that appears as you type. It covers how suggestions work, how to accept/reject them, and techniques for getting better completions.

### How Inline Suggestions Work

When you type code, GitHub Copilot analyzes the current file, nearby open files, and your cursor position to predict what you want to write next. The suggestion appears as grayed-out "ghost text" that you can accept (Tab), reject (Esc), or partially accept (Ctrl+Right arrow for word-by-word acceptance).

### Context Matters

The quality of suggestions depends entirely on the context Copilot has available:
- **Current file content**: The most important context source
- **Open tabs**: Copilot uses other open files to understand patterns and types
- **File name and extension**: Helps Copilot understand what language and framework you are using
- **Comments and documentation**: Descriptive comments above your code dramatically improve suggestion quality
- **Cursor position**: Copilot looks at code before and after the cursor

### Next Edit Suggestions (NES)

A newer feature where Copilot predicts not just what code to write, but where you need to make your next edit. After accepting a suggestion, Copilot may highlight another location in the file where a related change is needed (e.g., after adding a method, it suggests adding the corresponding test).

### Inline Chat

Without leaving your code, you can press Ctrl+I to open an inline chat prompt right at your cursor position. This lets you ask Copilot to modify, explain, or extend the selected code without switching to a full chat panel.

### Vision Support

Some models support vision -- you can attach screenshots or images to chat prompts, and Copilot can generate code based on UI mockups or diagrams.

## Key AI Coding Techniques

- **Comment-driven development**: Write a descriptive comment explaining what you want, then let Copilot suggest the implementation
- **Partial acceptance**: Use Ctrl+Right to accept suggestions word by word, maintaining control over what gets inserted
- **Open relevant files**: Keep related files open in tabs so Copilot can use them as context for better suggestions
- **Pattern establishment**: Write one example (e.g., one test case, one API endpoint) and let Copilot follow the pattern for the rest
- **Next Edit Suggestions**: After accepting a suggestion, watch for Copilot to suggest related edits elsewhere in the file
- **Inline chat (Ctrl+I)**: Quick, targeted code modifications without switching to the chat panel

## Practical Takeaways for Scientists

- Write comments describing your intent before writing code -- "# Calculate the Pearson correlation coefficient for columns X and Y" will produce better suggestions than starting from scratch
- For repetitive data processing tasks (e.g., loading multiple CSV files, applying the same transformation to multiple columns), write one example and let Copilot suggest the rest
- Partial acceptance (word by word) is useful when the suggestion is mostly right but needs tweaking -- common with scientific code where variable names or parameters need domain-specific values
- Keep your data processing pipeline files open in tabs so Copilot understands your data structures and naming conventions
- Vision support can be used to generate code from hand-drawn flowcharts or diagrams of algorithms

## Notable References

- Keyboard shortcuts for accepting/rejecting suggestions vary by editor
- Next Edit Suggestions (NES) is a relatively new feature that may not be available in all editors
- The chapter emphasizes that suggestions are starting points, not finished code -- always review and validate
