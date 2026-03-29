# Chapter 4: Copilot and Application Creation

## Summary

This is the book's longest and most detailed technical chapter, covering the end-to-end process of building applications with Copilot assistance. Wienholt works through multiple application types: a calculator app (WPF desktop), a web API with .NET Core, and demonstrates how Copilot handles different architectural patterns.

The chapter begins with the calculator app as a practical example of generating a complete application from a wireframe screenshot. While the generated code works functionally, the author notes significant quality gaps -- the UI is basic, CSS styling is minimal, and the code needs human refinement for production use. This becomes a recurring theme: Copilot generates "good enough" starting points but rarely production-ready code.

A major section covers building .NET Core web applications, including creating controllers, services, data access layers, and middleware. The author demonstrates how to use Copilot with different architectural patterns (MVC, repository pattern, dependency injection) and how providing clear architectural constraints through comments and context produces better results.

The chapter also covers working with LLM code responses that include errors, the iterative process of fixing runtime exceptions through Copilot Chat, and the importance of maintaining manual control over architectural decisions. The dotnet CLI integration with Copilot is shown for scaffolding projects, adding NuGet packages, and generating boilerplate.

## Key AI Coding Techniques

- **Application scaffolding**: Use Copilot to generate project structure, then refine
- **Wireframe-to-code**: Paste UI screenshots/wireframes for Copilot to generate matching frontend code
- **Iterative error fixing**: When generated code fails at runtime, paste the error into Copilot Chat for fix suggestions
- **Architectural guidance via comments**: Write comments specifying design patterns (repository, DI, etc.) before asking for implementations
- **NuGet/package management**: Copilot can suggest and help install appropriate packages
- **Multi-file generation**: Use Chat to generate related files (controller, service, model, tests) in sequence
- **Data Transfer Objects (DTOs)**: Copilot excels at generating boilerplate mapping code between DTOs and domain models

## Practical Takeaways for Scientists

- AI-generated applications work but look basic -- expect to invest time in UI refinement
- For scientific applications, start by describing the data model and analysis pipeline in comments, then let Copilot generate the implementation
- Copilot is excellent at generating API endpoints for exposing analysis results as web services
- The iterative fix cycle (generate -> run -> error -> fix -> run) is the normal workflow, not a sign of failure
- Always maintain control of the overall architecture; Copilot is good at filling in implementations within a defined structure
- For complex applications, build incrementally rather than trying to generate everything at once
- The dotnet new template system combined with Copilot is effective for rapid prototyping

## Notable References

- .NET Core web application architecture patterns
- WPF desktop application development
- Calculator app wireframe-to-code example
- Dependency injection and repository pattern with Copilot
- Microsoft vendor reference architectures (eShopOnWeb)
