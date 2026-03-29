# Chapter 7: Problem Decomposition

## Summary

Chapter 7 is one of the most important chapters in the book. It introduces **top-down design** (also called problem decomposition) as the critical skill for working with AI coding assistants on real-world problems. The core insight is that Copilot works well for small, well-defined functions, but struggles with large, complex tasks. The programmer's job is to break large problems into small pieces that Copilot can handle.

### The Top-Down Design Process

1. **Start with the overall goal** and identify the major subtasks needed to achieve it.
2. **For each subtask**, determine whether it is small enough for a single function. If not, break it down further.
3. **Visualize the decomposition as a tree:** the top-level function is the root, and it calls child functions, which may call their own children.
4. **Implement bottom-up:** Write the leaf functions first (those that do not depend on other functions you need to write), then work your way up to the top-level function. This ensures that when Copilot generates code for a parent function, the child functions already exist and Copilot can use them.

### The Authorship Identification Example

The chapter's main example is a substantial project: determining the likely author of a mystery text based on stylistic features. This involves:
- Reading text files
- Cleaning text (removing punctuation, splitting into words and sentences)
- Computing linguistic features (average word length, type-token ratio, Hapax Legomenon ratio, average sentence length, sentence complexity)
- Comparing features to known author profiles
- Determining the closest match

This is decomposed into many small functions, each responsible for one specific computation. The tree of functions is several levels deep, demonstrating that even a complex project becomes manageable through decomposition.

### The Function Design Cycle

The chapter formalizes a workflow (Figure 8.10 in the text):
1. Write the function header (`def` line)
2. Write the docstring with description, parameter types, return type, and examples
3. Let Copilot generate the code
4. Read and verify the code
5. Test with doctests
6. If incorrect, refine the prompt or decompose further

## Key Techniques for AI-Assisted Coding

- **Top-down design is the programmer's superpower with AI:** Copilot cannot decide how to decompose a problem. That is the human's job, and it is the most important skill.
- **Implement bottom-up after designing top-down:** Design from the big picture down to details, but code from the details up. This ensures Copilot has access to helper functions when generating higher-level code.
- **Each function should be testable in isolation:** If you cannot test a function independently, it may need to be broken down further.
- **Give Copilot the names of child functions in the parent's docstring:** If your top-level function should call `clean_text()` and `compute_features()`, mention these in the docstring so Copilot knows to use them.

## Practical Takeaways for Scientists

- Scientific analyses are naturally hierarchical: load data, clean data, compute statistics, visualize results, generate reports. Each of these is a subtask that can be decomposed further.
- The authorship identification example maps directly to many scientific workflows: read data, extract features, compare to references, determine the best match.
- Do not try to write one giant script that does everything. Break it into functions, each responsible for one step. This makes the code easier to test, debug, and reuse.
- The tree of functions is an excellent planning tool. Sketch it on paper before you start coding.

## Notable References

- Top-down design / stepwise refinement methodology
- The authorship identification project (text analysis, linguistic features)
- Type-token ratio and Hapax Legomenon ratio as text analysis metrics
- The function design cycle (Figure 8.10)
