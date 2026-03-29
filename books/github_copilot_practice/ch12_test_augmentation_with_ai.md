# Chapter 12: Test Augmentation with AI

## Summary

This chapter demonstrates how Copilot can assist with both manual and automated testing, using Microsoft's eShopOnWeb sample application and Azure Test Plans as the integration platform. The author covers the full testing spectrum: manual test case generation, automated unit tests, integration tests, and Selenium-based UI tests.

The chapter begins by evaluating Azure Test Plans as a testing platform, noting its hierarchical structure (Test Plans -> Test Suites -> Test Cases) and integration with Azure DevOps. While not the most modern testing platform, it provides enterprise-grade traceability from requirements through test execution to defect tracking.

For manual testing, the author demonstrates asking ChatGPT and Claude 3.7 Sonnet to visit a deployed eShopOnWeb site and suggest manual test cases. The LLMs generated comprehensive test cases covering user accounts, catalog browsing, shopping cart, search, responsive design, performance, error handling, and security -- though some assumed functionality that the demo site lacked (like order confirmation emails).

The automated testing section is the chapter's core. The author shows how Copilot generates Selenium xUnit tests by opening the eShopOnWeb home page in Visual Studio and asking Copilot to generate browser-based tests. The generated tests cover page load verification, filter functionality, catalog display, and no-results handling. The tests use Chrome WebDriver in headless mode and follow the Arrange-Act-Assert pattern.

The integration between generated tests and Azure Test Plans is covered in detail, including the tedious but necessary process of connecting Visual Studio's Team Explorer to Azure DevOps and associating individual test methods with Test Case work items.

The key conclusion: **"For organizations that don't have a lot of automated testing in place, Copilot-generated tests are a great place to start getting coverage of existing functionality and preventing regression issues."**

## Key AI Coding Techniques

- **Manual test case generation**: Ask LLMs to visit a live application and suggest comprehensive test cases
- **Selenium test generation**: Open application pages in the IDE and ask Copilot to generate browser-based UI tests
- **Unit test generation**: Use `/tests` slash command or Chat to generate xUnit/NUnit/MSTest tests for existing code
- **Test pattern compliance**: Copilot generates tests following AAA (Arrange-Act-Assert) and Given-When-Then patterns
- **Framework-specific test generation**: Copilot adapts to xUnit, NUnit, MSTest, PyTest, Jest, and other frameworks
- **Test Case association**: Link generated tests to Azure Test Plans Test Cases for traceability

## Practical Takeaways for Scientists

- **Use Copilot to generate tests for existing untested code** -- this is one of its most immediately valuable applications
- For scientific software, generate tests that verify numerical outputs against known-good results
- Selenium tests can automate validation of web-based dashboards and visualization tools
- Start with unit tests for core computation functions, then expand to integration tests
- The Azure Test Plans integration provides audit trails useful for regulated research (GLP, GMP, FDA)
- LLM-generated manual test cases are a good starting point but need domain-specific refinement
- Copilot-generated tests follow standard patterns and are generally high quality, but always review edge case coverage
- The biggest value is introducing a "culture of automated testing" in teams that have historically tested manually

## Notable References

- Azure Test Plans (premium feature in Azure DevOps)
- eShopOnWeb sample application (github.com/dotnet-architecture/eShopOnWeb)
- Selenium WebDriver with ChromeDriver for UI testing
- xUnit testing framework for .NET
- Visual Studio Team Explorer integration with Azure DevOps
- Azure DevOps Build pipeline test execution
- Bugzilla (~33% market share) and Selenium (~23% market share) in QA tooling
