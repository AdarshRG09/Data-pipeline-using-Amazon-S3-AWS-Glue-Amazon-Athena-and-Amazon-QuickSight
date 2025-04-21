
# AWS Data Pipeline Project 

This project demonstrates how to build a basic **data pipeline on AWS** using:
- **Amazon S3** for data storage
- **AWS Glue** for data cleaning and transformation
- **Amazon Athena** for querying the data using SQL
- **Amazon QuickSight** for data visualization

---

# Tools Used

| Service          | Purpose                                 |
|------------------|------------------------------------------ |
| **S3**           | Store raw and cleaned CSV data            |
| **AWS Glue**     |PySpark script to clean and transform data |
| **Amazon Athena**| SQL queries on cleaned data               |
| **QuickSight**   | Dashboards and data visualizations        |

---

# Project Structure

```
aws-data-pipeline-project/
├── glue_etl_job.py         # Spark script to clean raw CSV
├── README.md
└── screenshots/            # Visuals of Athena and QuickSight
    ├── thumbnail.png
    ├── athena_query.png
    └── quicksight_dashboard.png
```

---

## How It Works

1. **Raw Data Storage**  
   Upload raw sales data CSV to:  
   `s3://adarsh.datapipeline/raw_data/`

2. **Data Cleaning with Glue**  
   Run the PySpark script using AWS Glue to:
   - Drop rows with NULL values in critical columns
   - Cast data types correctly
   - Format date column properly

3. **Cleaned Data Storage**  
   Output stored to:  
   `s3://adarsh.datapipeline/cleaned_data/output/`

4. **Athena Query**  
   Create a table in Athena pointing to cleaned data  
   Query to check for NULL values or get insights.

5. **QuickSight Visualization**  
   Connect Athena to QuickSight  
   Create interactive dashboards and graphs

