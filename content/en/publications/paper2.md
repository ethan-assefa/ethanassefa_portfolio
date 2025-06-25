---
title: 'Increased stroke severity and mortality in patients with SARS-CoV-2 infection: An analysis from the N3C database'
date: 2023-01-10T16:13:06+03:00
image: "/images/publications/paper2_square.png"
cover: "/images/publications/paper2.png"

# New image‐path params:
flowchart: "/images/publications/purpose-chart.svg"
flowchartEmbed: ""
methodsGraphic: "/images/publications/methods-graphic.svg"
resultsGraph: "/images/publications/results-plot.svg"

purpose: "To test the hypothesis that patients with ischemic stroke and concurrent SARS-CoV-2 infection had increased stroke severity, that this association persisted throughout the first year of the pandemic, and that a similar increase in stroke severity was present in patients with hemorrhagic stroke."
methods: "Utilized the National Institute of Health National COVID Cohort Collaborative (N3C) database to identify a cohort of 61,402 patients with stroke hospitalized in the United States between March 1, 2020 and February 28, 2021. This cohort was then given propensity scores and patients with concurrent stroke and COVID were matched to patients with just stroke at a 1:3 ratio based on propensity scores. Using a variety of statistical models, we examined outcomes of stroke severity as measured by admission NIH Stroke Scale (NIHSS) scores, death, length of stay, and the temporal relationship between time of SARS-COV-2 diagnosis and incidence of stroke."
findings: "The study found that stroke patients (both ischemic and hemorrhagic) with concurrent SARS-COV-2 had increased NIHSS scores, length of stay, and higher odds of death, even after being propensity matched for their co-variates. Temporally, the highest incidence of stroke diagnosis on the same day as SARS-COV-2 diagnosis, with a logarithmic decline in counts as time went on."
skills:
  - "R & RStudio"
  - "Python"
  - "`pyspark`, `pandas`, and `numpy` Python Libraries"
  - "Palantir Enclave System"
  - "Big Data Handling/Wrangling"
  - "Distributed Data & Distributed Computing Systems"
  - "Hypothesis/Significance Testing"
  - "Propensity Score Matching"
  - "Time Series Analysis"
  - "Logistic Regression Modeling"
  - "Cox Proportional Hazard Modeling"
  - "Generalized Linear Modeling"
  - "Poisson Regression Modeling"
  - "Manuscript/Academic Writing"
pdf: "/pdfs/paper2.pdf"
link: "https://doi.org/10.1016/j.jstrokecerebrovasdis.2023.106987"
---

#### Study Details

Read on to get more specifics about the study conducted. For the full information and exact text of the study, click the download button to download the full study PDF or the link button to be directed to the journal's website.

#### Methods Details

- Python was used for data cleaning and creating data pipelines within the distributed computing enviroment of Enclave; R was used for analysis and visualization.
  - Open-source libraries `pyspark`, `pandas`, and `numpy` were ultilized in Python.
  - Open-source packages `tidyverse`, `data.table`, `survey`, `srvyr`, `gt`, and `gtsummary` were utilized in R.
- Study data was queried from the **National Institute of Health (NIH) National COVID Cohort Collaborative (N3C)**, one of the largest national repositories of harmonized clinical data. The N3C database is compiled by a community of healthcare systems that report electronic health record information from patients with positive SARS-CoV-2 (COVID) tests and a random sampling of controls (negative COVID tests) at the same time point in a 1:2 ratio.
  - Study population consisted of US patients aged 18+ hospitalized for Ischemic and Hemorrhagic stroke between March 1, 2020 and February 28, 2021.
  - 61,402 hospitalizations that met eligiblity criteria
    - 5,765 Ischemic stroke patients with concurrent COVID, and 37,530 Ischemic Stroke patients without COVID
    - 2,114 Hemorrhagic stroke patients with concurrent COVID infection and 15,993 Hemorrhagic stroke patients without COVID
- Propensity score matching was used to balance covariates between concurrent and non-concurrent groups
  - 1:3 ratio for matching concurrent COVID-stroke infection to non-concurrent stroke patients
    - After matching, final sample of 841 Ischemic stroke & concurrent COVID patients, and 2,402 matched non-concurrent Ischemic stroke patients.
    - After matching, final sample of 237 Hemorrhagic stroke & concurrent COVID patients, and 647 matched non-concurrent Hemorrhagic stroke patients.
  - Exact matching for race/ethnicity & N3C health center site 
  - Nearest Neighbor matching (caliper of 0.25) for other clinical and demographic factors
- Group differences in NIHSS scores on admission, mortality, time from stroke hospitalization until death, and the log-transformed length of hospital stay were examined and compared utilizing comprehensive analysis methodology appropriate to the form of the data
  - NIHSS scores (right skewed continuous variable) $\rightarrow$ Poisson Regression Model
  - Mortality (dichotomous binary variable) $\rightarrow$ Conditional Logistic Regression Model
  - Time from stroke hospitalization (time data) $\rightarrow$ Stratified Cox Proportional Hazard Model
  - Length of hospital stay (log-transformed, continuous variable) $\rightarrow$ Generalized Linear Model

#### Results & Discussion Details

> In this large sample of patients from the NIH N3C data repository, we found that both IS [Ischemic Stroke] and HS [Hemorrhagic Stroke] severity as measured by NIHSS [scores] was greater in patients with concurrent SARS-COV-2 [COVID]

> [We found] increased mortality in patients with both IS and HS with concurrent SARS-COV-2 [COVID] infection

> Demographically, we found that the concurrent SARS-COV-2 IS [COVID and Ischemic Stroke] group had more Hispanic or Latino, Black/African American Non-Hispanic, and Asian Non-Hispanic patients than the non-concurrent group.