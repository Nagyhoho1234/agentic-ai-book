# Chapter 13: Cluster Analysis

## Summary

This chapter covers cluster analysis, an unsupervised learning technique for grouping observations based on similarity. Unlike the supervised methods in previous chapters, clustering has no target variable -- the goal is to discover natural structure in the data. The chapter covers hierarchical clustering, k-means, DBSCAN, and fuzzy clustering, with practical guidance on every step of the process.

### How Many Clusters Are There?

The chapter begins with the fundamental challenge: the number of clusters is not always obvious, and different methods may yield different answers. It presents the "Clustering Illusion" -- the fact that clustering algorithms will always find clusters, even in random data. This makes validation critical.

The number of possible clusterings grows astronomically with the number of objects (e.g., 10 objects can be clustered in 115,975 different ways), making exhaustive search impossible.

### Recommended Steps for Running a Cluster Analysis

1. **Clearly state the objective** -- Why are you clustering? (market segmentation, anomaly detection, data simplification, etc.)
2. **Select variables** -- Choose attributes relevant to the clustering goal; variable type and scale matter
3. **Check that clusters exist** -- Visualize data (scatterplots, PCA plots); use the Hopkins statistic to test for spatial randomness
4. **Select a proximity measure** -- The choice of distance metric fundamentally affects results
5. **Select a clustering algorithm** -- Match the algorithm to the data characteristics
6. **Validate results** -- Use internal and external validation methods
7. **Describe the clusters** -- Compute cluster profiles (means, frequencies) for interpretation

### Proximity Measures

- **Euclidean distance:** Most common; sensitive to variable scale -- **always standardize first**
- **Manhattan distance:** Sum of absolute differences; more robust to outliers; better than Euclidean when dimensions exceed 20
- **Cosine similarity:** Measures directional similarity; useful for text data and term-frequency vectors; insensitive to magnitude
- **Tanimoto similarity:** For binary vectors; counts shared presences but ignores shared absences

The chapter provides worked numerical examples showing how unstandardized Euclidean distances can be dominated by high-magnitude variables (e.g., income vs. age), producing misleading results.

### Hierarchical Clustering

Bottom-up (agglomerative) approach:
1. Start with each observation as its own cluster
2. Merge the two closest clusters
3. Repeat until all observations are in one cluster
4. Visualize as a **dendrogram** -- cut at the desired height to determine the number of clusters

**Linkage methods** (how to measure distance between clusters):
- **Single linkage:** Minimum distance between any pair of points -- tends to produce long, chain-like clusters
- **Complete linkage:** Maximum distance between any pair of points -- more compact, spherical clusters
- **Average linkage:** Mean distance between all pairs of points -- compromise between single and complete

**Example:** US crime rates by state (48 states, 7 crime categories, averaged over 1960-2019). Six clusters were identified using Euclidean distance and complete linkage. Cluster 5 had above-average rates for all crime categories. Clusters showed some geographic correspondence.

Advantages: no need to pre-specify k; dendrogram provides rich visual information; can detect non-spherical clusters.
Disadvantages: O(n-cubed) computation; not scalable beyond a few thousand observations; greedy (no backtracking).

### k-Means Clustering

Partitioning approach:
1. Choose k initial centroids (randomly or from the data)
2. Assign each observation to the nearest centroid
3. Recompute centroids as cluster means
4. Repeat steps 2-3 until convergence

**Determining k:**
- **Elbow method:** Plot within-cluster sum of squares vs. k; look for an "elbow" where the rate of decrease slows
- **Silhouette coefficient:** For each point, compare cohesion (distance to own cluster) with separation (distance to nearest other cluster); SC = (B-A)/max(A,B); values above 0.7 indicate strong structure, 0.5-0.7 reasonable, below 0.5 weak

**Example:** Mall customer segmentation (200 customers, age/income/spending score). Both elbow and silhouette methods indicated 5 clusters. Workflow: File Reader -> Normalizer (z-score) -> k-Means -> Joiner (to add original variables) -> GroupBy (cluster profiles). Five distinct customer segments emerged (e.g., young high-spenders, older high-income low-spenders).

Advantages: scalable to millions of observations; O(n) complexity.
Disadvantages: sensitive to initial centroids (use fixed seed for reproducibility); must pre-specify k; assumes spherical clusters.

### Density-Based Clustering (DBSCAN)

- Identifies clusters as dense regions separated by sparse regions
- Two parameters: **epsilon** (neighborhood radius) and **minimum points** (minimum density)
- Core points, border points, and noise points
- Can discover **arbitrarily shaped clusters** including rings, crescents, and irregular shapes
- Demonstrated with a complex dataset containing a ring, crescents, and compact clusters that neither hierarchical nor k-means could correctly identify

Advantages: discovers arbitrary shapes; robust to outliers (labels them as noise); only two parameters.
Disadvantages: sensitive to epsilon setting; struggles with varying-density clusters; can be slow with many features.

### Fuzzy Clustering

- Each observation has a probability of belonging to each cluster (soft assignment) rather than a hard assignment to one cluster
- **Fuzzy c-means** in KNIME: requires setting number of clusters c and fuzziness parameter m (default m=2.0; m=1.0 reduces to hard k-means)
- Useful when cluster boundaries are not sharp
- Advantages: handles overlapping clusters; robust to outliers; captures uncertainty
- Disadvantages: must pre-specify c and m; no firm theoretical guidance for parameter selection

### Cluster Validation

- **Internal validation:** Silhouette coefficient, within-cluster sum of squares, dendrogram inspection
- **External validation:** Compare cluster memberships with external variables not used in clustering (e.g., do customer clusters differ on purchasing behavior?)
- **Stability assessment:** Run k-means with different seeds and check if results are stable

## Key Visual Programming Techniques

- **Hierarchical Clustering node:** Settings include number of output clusters, distance function (Euclidean), and linkage type (single/complete/average)
- **k-Means node:** Settings include number of clusters and random initialization seed
- **DBSCAN node:** Available through KNIME extensions
- **Fuzzy c-Means node:** For soft clustering
- **Normalizer node:** Z-score normalization (critical for distance-based clustering)
- **Distance Matrix Calculate node:** Offers six distance metrics
- **Silhouette Coefficient node:** Within Parameter Optimization Loop for determining optimal k
- **R Snippet node:** Used for the elbow method via the factoextra library
- **GroupBy node:** Computing cluster profiles (means of original variables by cluster)
- **Joiner node:** Merging cluster labels back with original data
- **RowID node:** Setting row IDs to meaningful identifiers (e.g., state names)
- **Column Filter node:** Selecting clustering variables
- **Line Plot node:** Visualizing elbow and silhouette plots
- **Value Counter node:** Counting observations per cluster

## Practical Takeaways for Scientists

- **Always standardize** variables before clustering (z-score or min-max) unless you intentionally want certain variables to dominate
- Beware the Clustering Illusion: algorithms will always find clusters, even in random data; validate your results
- Try multiple clustering methods and compare: hierarchical, k-means, and DBSCAN may give different but complementary insights
- Use both the elbow method and silhouette coefficient to determine the number of clusters; they do not always agree
- For large datasets, use k-means (scales linearly); hierarchical clustering is limited to a few thousand observations
- Run k-means multiple times with different seeds to check stability
- DBSCAN is the only option for discovering non-spherical cluster shapes
- Fuzzy clustering is valuable when you expect overlapping groups
- The ultimate validation of clustering is interpretability and actionability: do the clusters make sense and can you act on them?
- Cluster analysis is descriptive, not predictive -- but cluster memberships can become target variables or features for subsequent predictive models

## Notable References

- Ester, M. H., et al. (1996). DBSCAN algorithm
- Kaufman, L., & Rousseeuw, P. J. (2005). Finding groups in data
- Han, J., Kamber, M., & Pei, J. (2012). Data mining concepts and techniques
- Harmouch, M. (2021). 17 types of similarity and dissimilarity measures
- Everitt, S., & Landau, B. S. (2011). Data mining concepts and technique
- Bezdek, J. C. (1981). Fuzzy objective function algorithms
- Ullmann, T., et al. (2022). Validation of cluster analysis results
- Kapri, B. (2019). Clustering illusion
- Aggarwal, C. C. (2015). Data mining
