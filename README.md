# Data engineering zoomcamp project - NCAA Basketball Data Analysis

## Overview
This project analyzes NCAA basketball data using various tools and technologies, including Terraform, Google Cloud Storage (GCS), Google BigQuery, dbt for transformations, Prefect for orchestration, and Power BI for visualization.

## Background

The NCAA (National Collegiate Athletic Association) is a nonprofit organization that regulates and governs college athletics in the United States. NCAA basketball is a popular college sport that draws millions of fans each year. The NCAA provides a wealth of data on college basketball games, including scores, team statistics, player statistics, and more. This project aims to analyze this data and extract insights that can inform decision-making in the world of college basketball.

## Technologies Used

This project uses several technologies to process, transform, and analyze NCAA basketball data. These technologies include:

- **Terraform**: Infrastructure as code tool used to manage the deployment of cloud resources
- **Python**: Programming language used to load dataset from Google BigQuery open dataset to Google cloud storage
- **Prefect**: Workflow management tool used to orchestrate data pipelines
- **Google Cloud Storage (GCS)**: Cloud storage service used to store raw data and transformed data
- **Google BigQuery**: Cloud-based data warehouse used to query and analyze large datasets
- **dbt**: Data transformation tool used to clean, transform, and model data for analysis
- **Power BI**: Business intelligence tool used to visualize and explore data

## Data Sources

The project uses NCAA basketball data from several sources, including:

- **NCAA**: The NCAA provides game-level and player-level data for men's and women's college basketball games.
- **Sports Reference**: Sports Reference provides extensive data on college basketball teams and players, including team rankings, player statistics, and more.

## Data Pipeline

The project follows a typical data pipeline for processing and analyzing data. The pipeline consists of the following steps:

1. **Data Collection**: Raw data is collected from NCAA and Sports Reference and stored in GCS.
2. **Data Transformation**: dbt is used to clean, transform, and model the data for analysis.
3. **Data Loading**: The transformed data is loaded into BigQuery for analysis.
4. **Data Analysis**: SQL queries are used to analyze the data and extract insights.
5. **Data Visualization**: Power BI is used to create interactive visualizations and dashboards.

## Data Visualization

[Report](https://app.powerbi.com/view?r=eyJrIjoiOTM1YTIxZWQtOGE0Zi00NTdjLWI1NzQtNTgyZmJkMWQ5MTA0IiwidCI6IjQ4MjQxNjNlLTEzZGYtNDRiNC04YjM0LTU4YTNiMTkxOTVlNCJ9) is available in Power BI cloud service by this link (https://app.powerbi.com/view?r=eyJrIjoiOTM1YTIxZWQtOGE0Zi00NTdjLWI1NzQtNTgyZmJkMWQ5MTA0IiwidCI6IjQ4MjQxNjNlLTEzZGYtNDRiNC04YjM0LTU4YTNiMTkxOTVlNCJ9) 

![Alt text](/images/ncaa_report.png "Dashboard overview")

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Set up a GCS bucket to store raw and transformed data.
3. Set up a BigQuery dataset to store transformed data.
4. Install Terraform and Prefect on your local machine.
5. Deploy the Terraform infrastructure using `terraform apply`.
6. Register a Prefect agent and start the Prefect server using `prefect server start`.
7. Run the data pipeline using `prefect run start`.

## Conclusion

This project demonstrates how various tools and technologies can be used to process, transform, and analyze NCAA basketball data. The pipeline can be extended to include additional data sources, transformations, and analyses. The insights gained from this analysis can inform decision-making in the world of college basketball.
