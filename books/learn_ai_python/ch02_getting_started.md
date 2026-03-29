# Chapter 2: Getting Started

## Summary

Chapter 2 walks the reader through the practical setup required to begin programming with Copilot. This includes installing Python, Visual Studio Code (VS Code), and the GitHub Copilot extension. The chapter then introduces fundamental programming concepts through small interactive examples: using the Python REPL (the `>>>` prompt), working with basic data types (strings, integers, floats), and understanding variables and assignment.

The chapter introduces the concept of a **function** as the core unit of work when programming with Copilot. A function has a name, parameters (inputs), and a return value (output). The authors show how to write a function header (`def` line) and a docstring that describes what the function should do, then let Copilot fill in the code body. This is the fundamental workflow used throughout the rest of the book.

Key Python concepts introduced include:
- String operations (concatenation, repetition, indexing, slicing)
- Numeric operations (arithmetic, integer vs. float division)
- Variables and assignment (`=`)
- The `input()` function for getting user input
- The `print()` function for displaying output
- Importing modules (e.g., `import math`)

## Key Techniques for AI-Assisted Coding

- **The function-first workflow:** Write the `def` line and a clear docstring, then let Copilot generate the function body. This is the core interaction pattern.
- **Using the Python REPL to explore:** Before writing full programs, use the interactive `>>>` prompt to test small expressions and understand how Python works.
- **Tab to accept, Ctrl+Enter to see alternatives:** Learn the keyboard shortcuts for interacting with Copilot suggestions.
- **Checking Copilot's work manually:** After Copilot generates code, run it with known inputs to verify the output matches expectations.

## Practical Takeaways for Scientists

- Setup is straightforward: Python + VS Code + Copilot extension. All are free (Copilot requires a subscription or educational access).
- The REPL is invaluable for quick experiments -- use it to test formulas, string manipulations, or small calculations before embedding them in functions.
- Start with very small functions (one clear task each) to build confidence in the Copilot workflow.
- Variables in Python work like labels pointing to values, not like boxes that hold values. Understanding this mental model prevents confusion later.

## Notable References

- Python 3 installation and PATH configuration
- Visual Studio Code as the recommended IDE
- GitHub Copilot extension for VS Code
- Python's built-in `math` module
