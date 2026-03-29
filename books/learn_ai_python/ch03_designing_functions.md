# Chapter 3: Designing Functions

## Summary

Chapter 3 deepens the reader's understanding of functions, which are the central building block for AI-assisted programming. The chapter emphasizes that functions should be small, focused, and well-documented. Each function should do one thing, and its docstring should precisely describe what it does, including the types and meanings of its parameters and return value.

The chapter introduces the concept of **function decomposition** -- breaking a larger task into smaller, reusable functions. This is important because Copilot generates better code when functions are small and have clear, specific docstrings. Large, vaguely described tasks produce unreliable results.

Several example functions are developed step by step, showing the full workflow: write the `def` line, write the docstring, let Copilot generate the body, and then test the result. The chapter also discusses:

- **Parameters vs. return values:** Functions receive input through parameters and communicate results through return values, not through `print()` (which is for display, not for returning data).
- **Scope:** Variables inside a function are local to that function and do not affect the outside world.
- **Reusability:** A well-designed function can be called from many places, making code more modular and maintainable.
- **Avoiding hardcoded values:** Use parameters instead of embedding specific numbers or strings directly in the code. This makes functions more general and reusable.

The chapter uses examples such as calculating areas, converting units, and formatting strings.

## Key Techniques for AI-Assisted Coding

- **Precise docstrings are the primary prompt mechanism:** Include parameter names, types, expected behavior, and edge cases in your docstrings.
- **One function, one task:** Copilot performs best when each function has a single, well-defined responsibility.
- **Include examples in docstrings:** Adding example inputs and outputs (in the `>>> function_name(args)` format) helps Copilot understand what you want and also serves as documentation.
- **Make functions general, not specific:** Use parameters for values that might change, rather than hardcoding them. This both improves reusability and gives Copilot better prompts.

## Practical Takeaways for Scientists

- Think of each function as a small, self-contained experiment: it takes inputs, processes them, and produces outputs. This maps naturally to scientific workflows.
- Resist the urge to write one giant function that does everything. Break your analysis into steps, each with its own function.
- The docstring is your specification. If you can describe what a function should do clearly in English, Copilot can usually generate correct code.
- Use `return` to get results out of functions, not `print()`. You can always print the returned value later, but you cannot do further computation on something that was only printed.

## Notable References

- Python docstring conventions (triple-quoted strings)
- The distinction between `print()` (side effect) and `return` (function output)
- The principle of avoiding "magic numbers" by using named parameters
