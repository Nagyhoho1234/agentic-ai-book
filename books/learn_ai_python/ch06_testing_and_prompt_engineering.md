# Chapter 6: Testing and Prompt Engineering

## Summary

Chapter 6 addresses two critical skills: testing code to ensure it is correct, and engineering better prompts when Copilot does not produce the desired result on the first attempt.

### Testing

The chapter introduces systematic testing as a discipline. Since Copilot-generated code is not guaranteed to be correct, the programmer must verify it. The chapter covers:

- **Doctest:** Python's built-in testing mechanism where you embed example function calls and expected outputs directly in the docstring. These serve double duty as documentation and automated tests. Running `python -m doctest your_file.py` executes all doctests.
- **Choosing good test cases:** The chapter teaches how to select test inputs that cover different scenarios:
  - Normal/typical inputs
  - Boundary/edge cases (empty strings, zero, negative numbers, single-element lists)
  - Cases that test different code paths (triggering different branches of `if/elif/else`)
- **Testing systematically:** Rather than running a function once and declaring it correct, test it with multiple carefully chosen inputs.

### Prompt Engineering

When Copilot generates incorrect code, the solution is often to improve the prompt rather than to manually fix the code. The chapter covers strategies for better prompts:

- **Be more specific:** Add details about edge cases, expected format, and constraints.
- **Add examples to the docstring:** Concrete examples of input/output pairs help Copilot understand the expected behavior.
- **Break the problem down further:** If a function is too complex for Copilot to get right, split it into smaller functions.
- **Try different phrasings:** Sometimes rewording the docstring produces better results.
- **Use Copilot Chat:** Have a conversation with Copilot about what you need, then use the insights to write a better prompt.

## Key Techniques for AI-Assisted Coding

- **Doctest as a verification workflow:** Write the docstring with examples first, let Copilot generate the code, then run doctests to verify. This is a test-driven development approach adapted for AI-assisted coding.
- **Iterative prompt refinement:** Treat prompt writing as an iterative process. If the first attempt does not produce correct code, refine the prompt rather than giving up or manually editing the code.
- **Edge case awareness:** Always think about what could go wrong: empty inputs, extreme values, unusual formats. Include these in your doctests.

## Practical Takeaways for Scientists

- Testing is not optional. AI-generated code can look correct but contain subtle bugs. Always verify with known inputs and expected outputs.
- Doctests are particularly useful for scientists because they serve as both documentation ("here is how this function works") and verification ("and here is proof that it works").
- When your data analysis pipeline produces unexpected results, the first step is to test each function individually with small, controlled inputs.
- Edge cases matter enormously in scientific computing: division by zero, empty datasets, NaN values, negative numbers where only positives are expected, etc.

## Notable References

- Python's `doctest` module
- Test-driven development (TDD) concepts adapted for AI-assisted coding
- The relationship between prompt quality and code quality
