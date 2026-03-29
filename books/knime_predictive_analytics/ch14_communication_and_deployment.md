# Chapter 14: Communication and Deployment

## Summary

This chapter addresses the "endgame" of analytics projects -- communicating results effectively and deploying models into production. A sobering statistic opens the discussion: a KDnuggets poll found that fewer than 20% of predictive models are ever successfully deployed. The three elements of the endgame are: (1) a final written report, (2) a presentation, and (3) deployment of the model.

### Writing and Presenting the Final Report

Every report or presentation should include:
1. Statement of the original business problem (and any revisions made during the project)
2. Steps followed in the analysis
3. Summary of models and findings
4. Recommendation on whether to deploy
5. Conclusions and recommendations for further work

#### Technical vs. Non-Technical Audiences

The chapter provides a detailed comparison table for tailoring content:
- **Non-technical:** Focus on business impact, use high-quality visuals, avoid jargon, discuss accuracy in non-technical terms
- **Technical:** Include modeling details, algorithm selection rationale, variable lists, assumptions, validation results, ROC curves

#### Presentation Structure

Two approaches:
- **Story format (Dykes, 2020):** Setting -> Hook -> Insights -> Aha Moment -> Recommendations
- **Inverted pyramid:** Lead with the bottom line (most important findings and recommendations), then provide supporting information, then details. Better for time-pressed executives who may leave mid-presentation.

### Data Visualization

The chapter covers principles of effective data visualization for analytics results:

- **Data selection:** Choose what to include carefully; omission can mislead, but so can clutter
- **Encoding data into graphical form:** Based on Bertin's (1967/1983) visual variables: shape, curvature, size, orientation, color, texture, line width, color intensity, position, blur
- **Constructing the image:** Visualization is a craft drawing from statistics, graphic design, cartography, and cognitive science
- **Avoid chart junk:** No 3D effects, unnecessary backgrounds, redundant labels, borders, shadows

Four purposes of visualization:
1. Making comparisons (line charts, bar charts, dot charts)
2. Showing composition (stacked bars, Sankey diagrams, treemaps)
3. Demonstrating relationships (scatterplots, network charts, chord diagrams)
4. Showing distributions (histograms, box plots, violin plots, density plots)

KNIME's built-in graphics are useful for exploration but may not be publication-ready. Data can be exported to Excel, Power BI, Tableau, or other visualization tools.

### Deploying Predictive Models

#### Scope of Deployment
- **Individual/team use:** Developer runs the model as needed
- **Production process:** Integrated into organizational systems
- **External availability:** Available to customers, suppliers, or the public

As scope increases, so do requirements for: data privacy and security, robustness to input variation, usability, maintenance, and performance monitoring.

#### Deployment Using KNIME

KNIME provides an Integrated Deployment mechanism using three node types:
- **Capture Workflow Start / End:** Captures a segment of the workflow (data prep and/or model prediction)
- **Workflow Combiner:** Merges captured segments into a single deployable workflow
- **Workflow Writer:** Saves the combined workflow to disk

The chapter demonstrates this with the employee retention logistic regression model from Chapter 7:
1. Two workflow segments are captured: data preparation (log transformation) and model prediction (logistic regression)
2. The segments are combined and written to a file
3. A new, minimal workflow reads the saved workflow and applies it to new data: Workflow Reader -> Workflow Executor (with File Reader for new data)

This creates a self-contained prediction pipeline that anyone with KNIME can use.

#### Deployment Using Excel

For models with simple formulas (e.g., logistic regression), the model coefficients can be exported and implemented directly in an Excel spreadsheet:
- Extract coefficients from the Logistic Regression Learner's middle output port
- Build a worksheet that computes the probability of the target event from the input features
- Add data validation to check input ranges
- The worksheet serves as a user-friendly prediction tool without requiring KNIME

#### Other Deployment Options

- **PMML (Predictive Model Markup Language):** A standard XML format for exporting models from one tool and importing into another; supports decision trees, regression, and other model types
- **Cloud services:** KNIME Server, IBM SPSS Modeler, Amazon ML, SAS Enterprise Model
- **Translation to code:** Convert the model logic to C#, Java, or Python for integration into production systems

### Model Monitoring

Deployed models require ongoing monitoring because:
- The data distribution may change over time (concept drift)
- The assumptions may no longer hold
- Business conditions may evolve
- Performance should be tracked periodically and the model retrained when accuracy degrades

## Key Visual Programming Techniques

- **Capture Workflow Start / Capture Workflow End nodes:** Delimit sections of a workflow to be saved for deployment
- **Workflow Combiner node:** Merges multiple captured workflow segments into one
- **Workflow Writer node:** Saves the combined workflow to a specified location
- **Workflow Reader node:** Loads a saved workflow
- **Workflow Executor node:** Runs the loaded workflow with new input data
- **Logistic Regression Learner middle output port:** Extracts model coefficients for Excel deployment
- **File Reader node:** In the deployed workflow, reads new data for prediction
- **Line Plot, Bar Chart, Scatter Plot nodes:** For creating visualizations in reports

## Practical Takeaways for Scientists

- A model that is never deployed still has value if the insights inform strategy or decision-making
- Tailor your presentation to the audience: executives want the bottom line first; technical audiences want methodology details
- Lead with recommendations and results, not with the analysis process
- KNIME's deployment workflow (Capture/Combine/Write/Read/Execute) provides a simple path from analysis to reusable prediction tool
- Excel deployment is viable for simple models (logistic regression) and makes the model accessible to anyone with a spreadsheet
- PMML provides vendor-neutral model portability
- Always document how missing values, transformations, and normalization were handled -- the deployment workflow must replicate all preprocessing steps exactly
- Plan for model monitoring from the start; all models degrade over time
- Most models fail to deploy not for technical reasons but for organizational ones (lack of buy-in, unclear ROI, political roadblocks)
- The workflow itself is documentation: a well-annotated KNIME workflow shows exactly what was done and can be re-executed or modified

## Notable References

- Abbott, D. (2014). Applied predictive analytics
- Bertin, J. (1983). Semiology of graphics
- Davenport, T. (2015). Why data storytelling is so important
- Dykes, B. (2020). Effective data storytelling
- EMC Educational Services (2015). Data science and big data analytics
- Kirk, A. (2012). Data visualization: A successful design process
- Knaflic, C. N. (2015). Storytelling with data
- Raja, A. A. (2022). Data visualization best practices
- Siegel, E. (2022). Models are rarely deployed (KDnuggets)
