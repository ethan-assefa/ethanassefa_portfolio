---
title: 'Racial/Ethnic Disparities in COVID Treatment/Hospitalization: Social Determinants & Special Populations'
date: 2022-12-02T16:45:51+03:00
image: "/images/publications/poster1_square.png"
cover: "/images/publications/poster1.png"

# New image‐path params:
flowchart: "/images/publications/poster1_flowchart_static.png"
# Optional interactive embed
flowchartEmbed: "https://observablehq.com/embed/@ethan-space/personal-portfolio-website-publications-poster-1?cells=svg%2Cviewof+stage"
methodsGraphic: "/images/publications/poster1_flowchart_static.png"
resultsGraph: "/images/publications/results-plot.svg"

purpose: "Examine equity in hospitalization after emergency department visit and, once hospitalized, in receiving treatment for COVID-positive patients across demographics such as race/ethnicity and different Social Determinants of Health (SDoH) variables. We also examined the same questions but with a focus on a vulnerable population of people experiencing housing instability (HI)."
methods: "Utilized the National Institute of Health National COVID Cohort Collaborative (N3C) database to select 823,398 patients with avaliable SDoH data who were either admitted into the emergency department or hospitalized. Of that SDoH cohort, there were 31,907 patients who were experiencing housing instability (HI). Model analysis was conducted focusing on whether patient was hospitalized given they entered the emergency department as the outcome for the emergency department group, and whether patient recieved Remdesivir treatment given they were hospitalized as the outcome for the hospitalized group. Generalized Estimating Equation (GEE) models were utilized for analysis of relationships between variables and differences in the outcomes of interest."
findings: "When not adjusting for SDoH variables, Black/African-American patients have lower odds of both being hospitalized after an ED visit, and receiving Remdesivir once hospitalized. After adjusting for SDoH variables, Black/African-American patients continued to have lower odds of hospitalization after an ED visit, but the significant difference in their odds of receiving remdesivir once they were hospitalized disappeared. Taken as a whole, adjusting for SDoH variables reduced racial disparities in Remdesivir administration but did not eliminate disparities in hospitalization rates for Black/African-American patients, suggesting persistent racial barriers in accessing care, even when treatment is equitable once care is initiated."
skills:
  - "R & RStudio"
  - "`tidyverse` R Packages"
  - "Python"
  - "`pyspark`, `pandas`, and `numpy` Python Libraries"
  - "Palantir Enclave System"
  - "Big Data Handling/Wrangling"
  - "Data Transformation"
  - "Distributed Data & Distributed Computing Systems"
  - "Hypothesis/Significance Testing"
  - "Generalized Estimating Equation (GEE) Modeling"
  - "Study Poster Design & Creation"
  - "Manuscript/Academic Writing"
  - "Health Equity Analysis"
  - "Special & Vulnerable Populations"
pdf: "/pdfs/poster1.pdf"
link: "https://doi.org/10.18130/7qk6-gq18"
---

#### Study Details
Read on to get more specifics about the study conducted. For the full information and exact text of the study, click the download button to download the full study PDF or the link button to be directed to the journal's website.

#### Methods Details

- Python was used for data cleaning and creating data pipelines within the distributed computing enviroment of Enclave; R was used for analysis and visualization.
  - Open-source libraries `pyspark`, `pandas`, and `numpy` were ultilized in Python.
  - Open-source packages `tidyverse`, `data.table`, `survey`, `srvyr`, `gt`, and `gtsummary` were utilized in R.
- Study data was queried from the **National Institute of Health (NIH) National COVID Cohort Collaborative (N3C)**, one of the largest national repositories of harmonized clinical data. The N3C database is compiled by a community of healthcare systems that report electronic health record information from patients with positive SARS-CoV-2 (COVID) tests and a random sampling of controls (negative COVID tests) at the same time point in a 1:2 ratio.
- Study began with overall cohort of 4,800,512 individuals, of which 808,956 visited the emergency department and 253,805 were hospitalized.
  - Overall sample was filtered to those with avaliable data for Social Determinants of Health (SDoH), consisting of 3,745,244 individuals, of which 627,854 visited the emergency department and 195,544 were hospitalized. These two cohorts (emergency department admitted & hospitalized) were the groups examined in our main analysis.
  - In secondary analysis, the SDoH sample was further filtered to those experiencing housing instability (HI). This group consisted of 31,907 inidivudals, of which 10,235 visited the emergency department and 3,634 were hospitalized.
- Generalized Estimating Equation (GEE) models were utilized as they control for site-level bias from the different institutions sending in health data.
  - Heavily skewed SDoH variables were adjusted for with Z-score transformations.
- Key outcome of interest for the emergency department visit group $\rightarrow$ hospitalization within 30 days of ED visit
- Key outcome of interest for the hospitalized group $\rightarrow$ Remdesivir treatment recieved

#### Results & Discussion Details

> [Regardless of cohort,] Black/AAs [Black and African American patients] consistently have lower odds of hospitalization after an ED visit.

> When not considering SDoH [Social Determinants of Health], race/ethnicity plays significant role in odds of hospitalization and receiving Remdesivir; after including SDoH [variables as covariates], race/ethnicity remains significant in odds of hospitalization but generally becomes non-significant in receiving treatment once hospitalized.

> [The] Housing Instability cohort follows similar pattern to the SDoH cohort, however smaller size resulted in greater uncertainty and wider confidence intervals.