import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType, DoubleType

# Initialize Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load data from S3
input_path = "s3://adarsh.datapipeline/raw_data/sales_data_sample.csv"
df = spark.read.option("header", True).csv(input_path)

# Drop rows with nulls in important columns
df_cleaned = df.dropna(subset=["ORDERNUMBER", "QUANTITYORDERED", "PRICEEACH", "ORDERDATE"])

# Convert datatypes
df_cleaned = df_cleaned.withColumn("QUANTITYORDERED", col("QUANTITYORDERED").cast(IntegerType()))
df_cleaned = df_cleaned.withColumn("PRICEEACH", col("PRICEEACH").cast(DoubleType()))
df_cleaned = df_cleaned.withColumn("ORDERNUMBER", col("ORDERNUMBER").cast(IntegerType()))

# ✅ Fix the date parsing here
df_cleaned = df_cleaned.withColumn("ORDERDATE", to_date(col("ORDERDATE"), "M/d/yyyy H:mm"))

# Remove duplicates (optional)
df_cleaned = df_cleaned.dropDuplicates()

# Save the cleaned data
output_path = "s3://adarsh.datapipeline/cleaned_data/output/"
df_cleaned.write.mode("overwrite").option("header", True).csv(output_path)

print("✅ Cleaning complete and data written to:", output_path)
