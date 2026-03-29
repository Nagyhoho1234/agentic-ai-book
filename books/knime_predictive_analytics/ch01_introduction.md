# Chapter 1: Introduction to Predictive Analytics

## Summary

This chapter establishes the foundation for the entire book by defining predictive analytics, placing it in context within the broader analytics landscape, and introducing the CRISP-DM process model that structures all subsequent work. Acito distinguishes between descriptive analytics (what happened), predictive analytics (what will happen), and prescriptive analytics (what should we do). The book focuses squarely on predictive analytics -- building models that learn from historical data to make predictions about new, unseen observations.

The chapter introduces two fundamental types of predictive models:
- **Supervised learning:** Models that learn from labeled data with a known target variable (classification for categorical targets, regression for continuous targets)
- **Unsupervised learning:** Models that discover structure in data without a pre-defined target (primarily cluster analysis)

A central argument is that predictive analytics is not just for data scientists with programming skills. The rise of visual, low-code/no-code tools like KNIME has democratized access to these techniques. The concept of the "citizen data scientist" is introduced -- a domain expert who can apply analytics tools without deep programming expertise.

## The CRISP-DM Process

The Cross-Industry Standard Process for Data Mining (CRISP-DM) is presented as the organizing framework:

1. **Business understanding** -- Define the problem and objectives
2. **Data understanding** -- Explore and assess available data
3. **Data preparation** -- Clean, transform, and structure data for modeling
4. **Modeling** -- Select and apply appropriate algorithms
5. **Evaluation** -- Assess model quality and business relevance
6. **Deployment** -- Put the model into production use

The process is iterative, not linear. Findings at any stage may require revisiting earlier steps.

## Key Visual Programming Techniques

- Introduction to the concept of visual workflow-based analytics
- The idea of connecting nodes in a pipeline replaces writing code
- KNIME is positioned as the primary tool, with R and Python available as extensions when needed

## Practical Takeaways for Scientists

- You do not need to be a programmer to do serious predictive analytics
- Start with a clear business question before touching data or tools
- The CRISP-DM cycle is iterative -- expect to revisit earlier steps as you learn more
- Model accuracy alone is not enough; business value and deployability matter
- The field has matured to the point where visual tools can handle most standard predictive modeling tasks

## Notable References

- CRISP-DM process model documentation
- The concept of "citizen data scientist" (Gartner terminology)
- KDnuggets surveys on analytics tool usage and deployment rates
