# Chapter 9: Building an Internal GitHub Copilot Community

## Summary

This chapter provides a practical playbook for organizations rolling out GitHub Copilot at scale. Drawing from the authors' experience supporting rollouts across dozens of organizations (from less than 100 to thousands of developers), it covers how to build internal communities of practice around AI-assisted development.

### Acknowledge the Learning Curve

The foundation of successful adoption is accepting that there is a real learning curve. Simply handing out licenses and expecting engineers to "figure it out" does not work. Teams that dismissed the learning curve saw low engagement and poor results. Successful rollouts include structured training, dedicated practice time, and ongoing support.

### Learning Categories

Two main approaches, and most people use both:

**Learning through training:**
- Follow a structured progression: Suggestions -> Inline suggestions -> Ask Mode -> Edit Mode -> Agent Mode (in the editor), then Chat in browser -> Create issues -> Fix pipelines -> PR review -> Coding Agent (on GitHub.com)
- Start gradually to keep expectations realistic; do NOT start with Agent Mode
- Offer both live training (for Q&A) and recorded sessions (for self-pacing)
- Schedule dedicated time for training -- pointing people to an e-learning platform alone is insufficient

**Learning from using the tools:**
- Hands-on exploration with personal projects
- Use Copilot Adventures (https://microsoft.github.io/CopilotAdventures) for guided exercises at different proficiency levels
- Apply tools to real work projects with defined tasks

### Internal Wikis

Create internal documentation covering:
- How to install editors and Copilot extensions
- How to get internal support, licenses, and access
- How to update editors and extensions (extension updates often require specific minimum editor versions)
- Internal guidelines for using GitHub Copilot
- Grouped information about new features
- Archive news bulletins and newsletters for later reference

### Weekly Q&A Sessions

Run weekly sessions for at least the first six months of a rollout:
- Drive community feeling through recurring questions and topic requests
- Connect people across departments who share useful flows and prompts
- Use questions to feed wiki updates, blog posts, and short knowledge-sharing videos
- Mini knowledge-sharing sessions from real users replace canned demos with authentic stories

### Newsletters

Regular newsletters help reach people who do not attend Q&A sessions or check wikis:
- Keep them informative with screenshots and visuals
- Combine weekly news with recurring Q&A topics and novel use cases
- Link back to Q&A sessions and wiki
- Use GitHub's Mona the Octocat mascot for visual appeal (https://myoctocat.com)
- News aggregator resource: https://github-copilot.xebia.ms

### Hackathons

Most effective for hands-on learning (2 hours to half a day):

**Option 1 -- New project hackathon:**
- Start from scratch, explore unfamiliar tools/languages
- Switch projects between teams at the two-thirds mark to learn different approaches
- Provides fresh perspective on coding processes

**Option 2 -- Own project hackathon:**
- Focus on technical debt, missing tests, documentation improvements
- Instructions: refrain from writing code manually; use GitHub Copilot for everything
- Forces adoption of chat interface and new features

**Best practices:**
- Open with a demo of a specific GitHub Copilot feature linked to a common goal
- Mix teams across departments, editors, and experience levels ("mix and mingle")
- End with presentations of learnings, not solutions -- prize the best story or lesson, not the best code
- Bring small prizes to celebrate openness and learning

### Surveys

Keep surveys short (4-6 questions maximum; never more than 10) and low-key:
- Ask targeted questions: "Does GitHub Copilot help in your day-to-day coding?" and "Would you like more training on specific topics?"
- Include open-ended questions for elaboration
- Do not ask for information you already have (language, SDK, experience)
- Do not make surveys mandatory to retain access -- this reduces response quality
- Happy users stay quiet; unhappy users are vocal -- design surveys accordingly

### Metrics

Measuring "developer productivity" with GitHub Copilot is complex and nuanced:
- Simple metrics (lines of code, PRs merged, story points) are insufficient
- Look at downstream impact: PR size changes, review comment patterns, CI build failure rates
- GitHub focuses on *usage* metrics rather than *productivity* metrics: which features are used, how often, by whom

**Available dashboards:**
1. **Metrics dashboard** (Insights tab): Daily/weekly active users, chat interactions, requests per chat mode, code completions, model usage
2. **Premium request analytics** (Billing tab): Costs per user, per product, per model

**Engineering System Success Playbook (ESSP):** GitHub's three-step process for measuring engineering improvements: https://resources.github.com/engineering-system-success-playbook

Recommendation: focus on *how* people use the tools, not just *whether* they do. Reach out to low-usage and high-usage users to learn from both.

## Key AI Coding Techniques

- **Structured learning progression**: Suggestions -> Chat -> Edit -> Agent -> Coding Agent
- **Copilot Adventures**: Guided hands-on exercises at https://microsoft.github.io/CopilotAdventures
- **Custom instructions as team agreements**: Document AI etiquette in `.github/copilot-instructions.md`
- **Hackathon format**: Two types (new project or own project) with team mixing and learning-focused prizes

## Practical Takeaways for Scientists

- If you are a PI or lab manager introducing AI coding tools, invest in structured training time -- simply providing licenses is not enough
- Start a lab wiki page documenting tips and patterns that work for your specific scientific domain
- Weekly or biweekly "AI tools" meetings where lab members share what worked and what did not can dramatically accelerate adoption
- For grant-funded work, track usage metrics to demonstrate productivity improvements in reports
- Hackathons focused on adding tests to existing analysis code are particularly valuable for improving confidence in scientific software
- Survey your lab regularly (keep it to 4-6 questions) to identify training needs and feature requests

## Notable References

- Copilot Adventures: https://microsoft.github.io/CopilotAdventures
- GitHub Community Discussions: https://github.com/orgs/community/discussions/86520
- News aggregator: https://github-copilot.xebia.ms
- myOctocat: https://myoctocat.com
- Engineering System Success Playbook: https://resources.github.com/engineering-system-success-playbook
