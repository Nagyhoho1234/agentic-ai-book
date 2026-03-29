# Chapter 11: Code Migrations and Refactoring

## Summary

This chapter provides a deeply pragmatic -- and often cautionary -- examination of using AI tools for code migration and refactoring. Wienholt draws on extensive experience with enterprise code bases to demonstrate the subtle and dangerous bugs that AI-introduced code changes can produce.

The chapter opens with the COBOL migration problem: 43% of international banking systems still run COBOL, and organizations spent $308 billion on Y2K remediation. IBM has built an AI assistant (watsonx) for COBOL-to-Java conversion, but the chapter demonstrates that even simple language ports are fraught with subtle bugs.

The centerpiece example is a C# to VB.NET port of a simple `GetContentType` function. The Telerik Code Converter produces code with at least four errors in this trivial function. Copilot does better but still introduces subtle bugs, particularly around VB's bizarre `Or` operator (which is actually a bitwise operator, not a logical one), the lack of short-circuit evaluation in VB's `If` statements, and the `ByVal` keyword's different behavior with reference types versus value types.

The author demonstrates a critical point: **every LLM tested (via Copilot in VS Code) got the VB.NET payroll example wrong**, using `&&` (short-circuit AND) instead of the correct single `&` (bitwise AND) when porting VB's `And` operator. The deterministic converter (iCSharp/Roslyn-based) gets it right.

The refactoring section is equally cautionary. The author demonstrates that 100% unit test coverage does NOT guarantee bug-free code, using the NTFS file streams exploit (document.docx::$DATA bypasses file extension checks) as a compelling example. The key advice: **"Use Copilot and LLMs for code reviews. Use a mature deterministic tool like JetBrains Resharper for performing the actual refactoring. Copilot is good for adding unit tests prior to a refactoring exercise."**

Three migration approaches are compared: manual ports (ugly but controllable), deterministic transpilers (repeatable, verifiable), and AI tools (fast but potentially buggy). The recommendation: use deterministic tools when available, AI for augmentation, and always validate extensively.

## Key AI Coding Techniques

- **Code review with Copilot**: Use Copilot Chat to review code for potential bugs, security issues, and performance problems
- **Unit test generation before refactoring**: Generate comprehensive tests with Copilot BEFORE making structural changes
- **Language porting assistance**: Copilot can assist with cross-language ports but requires careful validation
- **Bug detection**: LLMs can sometimes identify subtle bugs that automated tools miss
- **Port testing**: Use Copilot to generate test suites specifically designed to validate ported code behavior
- **Refactoring review**: Have Copilot review proposed refactorings for potential side effects

## Practical Takeaways for Scientists

- **If a deterministic tool exists for your migration task, use it instead of AI** -- transpilers like c2go, Swiftify, and iCSharp are more reliable
- AI-assisted code porting introduces subtle bugs that are extremely hard to detect -- even in trivial functions
- Always generate comprehensive tests BEFORE refactoring or porting code
- 100% test coverage does NOT mean bug-free code -- be aware of edge cases (file streams, encoding issues, platform-specific behavior)
- For scientific code migration (e.g., MATLAB to Python, Fortran to C++), validate numerical results against the original implementation
- The refactoring advice is definitive: use deterministic tools (Resharper, Rider) for the actual refactoring, use Copilot for code reviews and test generation
- Legacy code migrations should start with thorough testing of the existing system to establish a behavioral baseline
- "Should existing bugs be ported?" is a critical question -- porting may expose latent bugs that never manifested in the original system

## Notable References

- Google's paper: "How Is Google Using AI for Internal Code Migrations?" (arxiv.org/pdf/2501.06972) -- state-of-the-art guidance for AI-based migration
- COBOL migration challenges and IBM watsonx
- Telerik Code Converter limitations
- iCSharp/Roslyn open-source C# to VB.NET converter (github.com/icsharpcode)
- JetBrains Resharper for deterministic refactoring
- "When Does a Refactoring Induce Bugs?" academic study
- "The Impact of Coverage on Bug Density in a Large Industrial Software Project" (SAP HANA study)
- NTFS file streams security exploit (IIS 5.1 vulnerability)
- Microsoft Trustworthy Computing Initiative ($100M+ investment)
- Kent Beck and Martin Fowler's refactoring principles
- VB.NET `Or` vs `OrElse`, `And` vs `AndAlso` operator semantics
