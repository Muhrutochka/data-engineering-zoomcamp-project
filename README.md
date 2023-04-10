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

1. **Data Collection**: Raw data is collected from BigQuery public NCAA dataset and stored in GCS.
2. **Data Transformation**: dbt is used to clean, transform, and model the data for analysis.
3. **Data Loading**: The transformed data is loaded into BigQuery for analysis.
4. **Data Analysis**: SQL queries are used to analyze the data and extract insights.
5. **Data Visualization**: Power BI is used to create interactive visualizations and dashboards.

## Data Visualization

[Report](https://app.powerbi.com/view?r=eyJrIjoiOTM1YTIxZWQtOGE0Zi00NTdjLWI1NzQtNTgyZmJkMWQ5MTA0IiwidCI6IjQ4MjQxNjNlLTEzZGYtNDRiNC04YjM0LTU4YTNiMTkxOTVlNCJ9) is available in Power BI cloud service by this link (https://app.powerbi.com/view?r=eyJrIjoiOTM1YTIxZWQtOGE0Zi00NTdjLWI1NzQtNTgyZmJkMWQ5MTA0IiwidCI6IjQ4MjQxNjNlLTEzZGYtNDRiNC04YjM0LTU4YTNiMTkxOTVlNCJ9) 

![Alt text](/images/ncaa_report.png "Dashboard overview")

## Getting Started

To get started with the project, follow these steps:

1. Create [Google Cloud Platform](https://cloud.google.com/) account. The [Google Cloud SDK](https://cloud.google.com/sdk). OAuth 2.0 for authentication and authorization.
1. Create project on [Google Cloud Platform](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
1. Clone the repository to your virtual/local machine.
1. Install Terraform and Prefect on your machine.
1. Change project name in variables.tf file.
1. Deploy the Terraform infrastructure using `terraform apply`. Will create a GCS bucket to store raw and transformed data and BigQuery dataset to store transformed data.
1. Register a Prefect agent and start the Prefect server using `prefect server start`.
1. Run the data pipeline using `python ingestion\load_data.py`.
1. Install dbt, build your models: `dbt run`. This will execute the SQL code in your models and create the corresponding tables/views in your data warehouse.
1. Use any data visualization tool to biuld data model and dashboard, like Power BI, Tableau, Qlik.


## Conclusion

This project demonstrates how various tools and technologies can be used to process, transform, and analyze NCAA basketball data. The pipeline can be extended to include additional data sources, transformations, and analyses. The insights gained from this analysis can inform decision-making in the world of college basketball.

## Thank You to DataTalksClub for Data Engineering Zoomcamp Training

I would like to express my sincere gratitude to [DataTalksClub]( http://datatalks.club) for organizing and providing the [Data Engineering Zoomcamp training](https://github.com/DataTalksClub/data-engineering-zoomcamp). The training has been an excellent opportunity for me to learn and improve my skills in data engineering.

The course material was well-structured and presented in an easy-to-understand format. The instructors were knowledgeable and supportive, providing valuable insights and answering all our questions promptly.

I have gained a deeper understanding of the data engineering concepts and techniques, including data modeling, ETL processes, and database management. The hands-on exercises and projects were particularly helpful in reinforcing my learning and providing practical experience.

Overall, I feel much more confident in my abilities as a data engineer, thanks to the Data Engineering Zoomcamp training. I would highly recommend this training to anyone who is interested in learning about data engineering.

Once again, thank you to DataTalksClub for providing this fantastic training opportunity!
