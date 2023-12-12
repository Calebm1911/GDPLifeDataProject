#CSCI 422 Project - Caleb Myhra
Life Expectancy Project

- [Overview]
- [Ingestion]
- [Transformation]
- [Serving]

## Overview 

The primary goal of this project is to analyze the correlation between Gross Domestic Product (GDP) per capita and life expectancy and to create a model that represents this relationship. This analysis is driven by the observation that life expectancy varies significantly between different countries, often linked to the wealth and development status of those countries. With data sources providing life expectancy data for the years 2000, 2010, 2015, and 2019, we aim to explore how changes in GDP correlate with changes in life expectancy.

## Ingestion

In this phase, we acquire data from two distinct sources, each offering valuable insights into our project's core metrics: GDP and life expectancy. Here's a detailed breakdown of our data ingestion process:

### Life Expectancy Data

Our primary source for life expectancy data is the World Health Organization (WHO), a renowned authority in global health statistics. This dataset encompasses life expectancies for each country, covering both genders and providing data on male and female life expectancies. The data is accessible using the OData protocol, a standardized way to interact with web services. 

The ingestion process involves accessing the WHO data through the OData protocol, and the extracted data is then stored as a raw CSV file. This CSV file is subsequently saved to the Azure storage account established for this project.

### GDP per Capita Data

The second source of data is Kaggle.com, a popular platform for data science and analytics. The dataset obtained from Kaggle features GDP per capita information for countries spanning the years from 1960 to 2020. This dataset offers crucial insights into the economic prosperity of nations over several decades.

Similar to the life expectancy data, the GDP dataset is also saved as a raw CSV file. It is stored in the same Azure storage account, but in a distinct file directory to ensure clear separation and organization.

The ingestion phase sets the foundation for our project, bringing together essential data sources to facilitate further analysis and insights.


## Transformation

The transformation phase of this project plays a pivotal role in preparing the data for analysis. Key aspects of data transformation include:

- **Data Cleaning**: The datasets contain a substantial amount of null or missing data. Data cleaning involves removing or filling in missing values to ensure the quality and reliability of the data.

- **Joining Datasets**: The two datasets may not share identical sets of countries, which requires a careful merging process. We will join the datasets based on common identifiers, such as country codes, to create a unified dataset for analysis.

- **Column Selection**: In the process of data preparation, several columns that do not contribute to the analysis will be excluded. This includes redundant or irrelevant information, streamlining the dataset for analysis.

## Serving

The serving phase will focus on conducting a comprehensive analysis of the data. This will involve employing analytical methods, specifically regression analysis, to gain insights into the relationships between GDP and life expectancy. Here's an outline of what the serving phase encompasses:

- **Regression Analysis**: We will employ regression analysis to quantitatively determine the correlation between a country's GDP and life expectancy. This statistical method will provide valuable insights into how changes in GDP are associated with changes in life expectancy.

- **Gender-Based Analysis**: We will explore whether there are differences in the correlation between GDP and life expectancy for males and females. This comparative analysis may reveal gender-specific trends.

- **Regional Correlations**: The analysis will be extended to understand how correlations between GDP and life expectancy vary across different regions or continents. This regional breakdown will provide a broader perspective on the impact of economic prosperity on life expectancy.

- **Outlier Detection and Handling**: As part of our data analysis, we will pay particular attention to the identification and treatment of outliers. Outliers, or data points significantly deviating from the norm, can impact the accuracy of our analysis. We will employ appropriate techniques to detect and manage outliers, ensuring that our findings are robust and reliable.

The serving phase aims to provide a comprehensive and nuanced understanding of the relationships between GDP, life expectancy, and associated factors, while also ensuring the quality and reliability of our analysis through outlier handling.
