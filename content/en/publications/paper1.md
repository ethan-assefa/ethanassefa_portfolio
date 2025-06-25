---
title: 'Perceptions of the determinants of health across income and urbanicity levels in eight countries'
date: 2025-06-19T15:02:29+03:00
image: "/images/publications/paper1_square.png"
cover: "/images/publications/paper1.png"

# New image‐path params:
flowchart: "/images/publications/NEED.svg"
methodsGraphic: "/images/publications/NEED.svg"
resultsGraph: "/images/publications/NEED.svg"

purpose: "To explore how people from different income and urban backgrounds view the factors that affect health, with the goal to describe the relationship between socioeconomic and geographic backgrounds and general views towards what impacts health."
methods: "8,753 Participants from 8 countries (Brazil, China, Germany, Egypt, India, Indonesia, Nigeria, and the United States) were surveyed and respondents selected the most important factors for health from a list of ten choices."
findings: "Those with higher incomes tended to emphasize the importance of genetics more, while lower income individuals valued social support. People in urban areas prioritized healthcare, while those in non-urban areas valued social support."
skills:
  - "R & RStudio"
  - "`tidyverse` R Packages"
  - "Survey Analysis"
  - "Hypothesis/Significance Testing"
  - "Chi-Square Tests"
  - "Logistic Regression Modeling"
  - "Health Equity Analysis"
  - "Manuscript/Academic Writing"
pdf: "/pdfs/paper1.pdf"
link: "https://doi.org/10.1038/s43856-024-00493-z"
---

#### Study Details

Read on to get more specifics about the study conducted. For the full information and exact text of the study, click the download button to download the full study PDF or the link button to be directed to the journal's website.

#### Methods Details

- A cross-sectional, anonymous, online survey in **eight nations** between **September 16th, 2020, and November 1st, 2020**.
  - Adult (18+ years) internet users in **Brazil (n = 1,075)**, **China (n = 1,282)**, **Germany (n = 1,036)**, **Egypt (n = 1,082)**, **India (n = 1,173)**, **Indonesia (n = 1,026)**, **Nigeria (n = 1,014)**, and the **United States (n = 1,065)**.
  - The survey was seen by **37,566** individuals total, of those, **8,753** filled out the full survey, garnering a response rate of **23.3%**.
- R was used for data cleaning, analysis, and visualization.
  - Open-source packages `tidyverse`, `data.table`, `survey`, `srvyr`, `gt`, and `gtsummary` were utilized.
- Chose ten determinants of health for respondents to select from in the survey based on existing literature and established frameworks for key determinants of health. 
  1. Healthcare
  2. Education
  3. Built environment (e.g., housing or neighborhood conditions)
  4. Employment conditions
  5. Income & wealth
  6. Genetics
  7. Childhood conditions
  8. Culture
  9. Social support
  10. Politics
- Respondent socioeconomic status determined by stratifying into brackets (highest income, upper-middle income, middle income, lower-middle income, and lowest income) based on respondents’ **reported monthly household income** in the currency of their country of residence.
- Respondent urbanicity determined by aggregating the 4-choice *area of residence* variable (large city, suburb, small town/village, and rural area/farm) into an **urban/non-urban dichotomy**.
  - Those who selected **suburb**, **small town/village**, or **rural area/farms** were categorized as **non-urban residents**.
  - Those who chose **large city** were classified as **urban residents**.

#### Results & Discussion Details

> persons in the highest income group ranked genetics as an important determinant of heath substantially more often than did persons in all other income groups [...] These results may be explained by the observation that persons from a higher socioeconomic status being more likely to attribute successes, including better health outcomes, to their unique genetics and disposition. Moreover, the wealthy within a country often have greater educational access and exposure to genetic concepts and, thus, the differences by income level may be due to information bias.

> the lowest income group ranked social support as an important determinant of health at a substantially higher frequency than all other income groups. [...] This may reflect the fact that social support networks play an important role in lower income communities, sometimes serving as informal networks for health advice, coping tools, and sources for needed resources.

> We found [...] differences in ranking of health determinants by urbanicity status across countries, particularly on the importance of social support and healthcare. [...] Research has shown the importance of social support networks as foundations of physical and emotional wellbeing in rural settings. There is also some evidence of social support networks operating as informal sources of information and resources in rural communities where proper resources are scarce. Conversely, the higher ranking of healthcare as an important determinant of health among respondents living in urban settings could be due to higher exposure to healthcare systems.