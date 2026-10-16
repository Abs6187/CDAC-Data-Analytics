## Phase 1: Ingestion & Foundation (Wrangling & SQL)

* **Core Nomenclature:** Data Ingestion, Relational Extraction, Schema Normalization, Memory Downcasting, Hierarchical Slicing, Vectorized Parsing.
* **Granular Scenarios Handled:**
  * **Memory Optimization:** Ingesting multi-gigabyte transactional logs using streaming chunk sizes (`chunksize=N`) and downcasting data types (e.g., converting 64-bit integers to 8-bit integers to reduce RAM footprints).
  * **Data Sanitization:** Standardizing string columns via `snake_casing`, stripping whitespace, and parsing ISO-8601 date formats.
  * **Relational Aggregation:** Executing conditional metrics via SQL `CASE WHEN` clauses, partition-based row ranking (`ROW_NUMBER() OVER`), and multi-level hierarchy traversal using recursive Common Table Expressions (CTEs).
  * **Multidimensional Panel Wrangling:** Setting multi-index axes (`set_index([L1, L2])`) to execute hierarchical slicing and melting wide-format tables into long-format structures.

---

## Phase 2: Auditing & Profiling (EDA)

* **Core Nomenclature:** Automated Profiling, Schema Enforcement, Missing Data Taxonomy, Collinearity Diagnostics, Non-Linear Association, Confounding Identification.
* **Granular Scenarios Handled:**
  * **Automated Data Quality Audits:** Generating instant HTML profiling reports (via YData-Profiling or Sweetviz) to inspect missingness percentages, duplicate entity keys, and memory allocations.
  * **Missing Data Classification:** Systematically diagnosing whether missing values follow MCAR (Missing Completely at Random), MAR (Missing at Random), or MNAR (Missing Not at Random) patterns.
  * **Multicollinearity Isolation:** Calculating Variance Inflation Factors (VIF) to detect and eliminate redundant predictor features that inflate regression coefficient variances.
  * **Confounding & Bias Detection:** Identifying Simpson’s Paradox where aggregate trends reverse or distort when data is segmented across localized cohorts.

---

## Phase 3: Feature Engineering & Economic Alignment (KPIs)

* **Core Nomenclature:** Categorical Encoding, Bayesian Smoothing, Power Transformation, Cyclical Feature Extraction, Unit Economics, Cohort Retention.
* **Granular Scenarios Handled:**
  * **High-Cardinality Handling:** Applying smoothed Target (Mean) Encoding to high-cardinality strings (like postal codes) by blending category means with global averages using smoothing parameters.
  * **Distribution Normalization:** Mitigating extreme skewness in financial distributions using Log, Box-Cox, and Yeo-Johnson power transformations.
  * **Temporal Boundary Resolution:** Applying Sine and Cosine cyclical transformations to hours of the day or months of the year to ensure continuous circular distance metrics without boundary jumps.
  * **Monetization & Retention Modeling:** Calculating Customer Acquisition Cost (CAC), historical versus predictive Customer Lifetime Value (LTV), logo/revenue churn, and period-over-period cohort retention matrices.

---

## Phase 4: Communication & Storytelling (Visualization)

* **Core Nomenclature:** Multi-Plot Faceting, Accessibility Standardization, Responsive GridSpec Layouts, Spatial Choropleth Aggregation, The Pyramid Principle.
* **Granular Scenarios Handled:**
  * **Multi-Variable Comparison:** Building complex panel visualizations using Seaborn `FacetGrid` and `PairGrid` structures to contrast distributions across segments.
  * **Interactive Drill-Down Exploration:** Designing responsive Plotly dashboards with hover tooltips, sunburst hierarchies, and financial waterfall charts for stakeholders.
  * **Geospatial Density Mapping:** Plotting geographic coordinate scatter points and aggregating metrics across regional state polygons using choropleth maps.
  * **Cognitive Load Reduction:** Structuring executive presentations using the Pyramid Principle (conclusion first, supporting evidence second) to bridge technical metrics with business outcomes.

---

## Phase 5: Advanced Intelligence (Unsupervised & Predictive Modeling)

* **Core Nomenclature:** Inertia Minimization, Silhouette Optimization, Orthogonal Projection, Additive Explanations, Stratified K-Fold Cross-Validation.
* **Granular Scenarios Handled:**
  * **Unsupervised Behavioral Segmentation:** Grouping customers into actionable RFM (Recency, Frequency, Monetary) tiers using K-Means inertia minimization, elbow plots, and DBSCAN density-based noise handling.
  * **Dimensionality Compression:** Projecting correlated features onto orthogonal axes via Principal Component Analysis (PCA) to capture maximum variance and reduce visual clutter.
  * **Supervised Predictive Classification & Forecasting:** Training logistic regressions and gradient models while evaluating performance via Precision-Recall curves, F1-scores, and MAPE metrics.
  * **Black-Box Interpretability:** Decomposing complex model predictions into cooperative game theory Shapley values (SHAP) to explain individual predictions to regulatory auditors.

---

## Phase 6: Validation & Causal Impact (Experimentation)

* **Core Nomenclature:** Power Analysis, Minimum Detectable Effect (MDE), Family-Wise Error Rate (FWER), Multi-Armed Bandit Allocation, Difference-in-Differences (DiD).
* **Granular Scenarios Handled:**
  * **Rigorous Experiment Sizing:** Calculating statistical power, significance thresholds ($\alpha$), and sample size durations to prevent underpowered tests.
  * **Multi-Testing Correction:** Applying Bonferroni and False Discovery Rate (FDR) corrections when evaluating multiple secondary guardrail metrics simultaneously.
  * **Adaptive Traffic Routing:** Deploying Multi-Armed Bandit algorithms (such as Thompson Sampling) to dynamically route user traffic toward winning variant arms in real time.
  * **Quasi-Experimental Causal Inference:** Estimating true causal impact in observational settings using Propensity Score Matching (PSM) and Difference-in-Differences (DiD) estimators to eliminate omitted variable bias.