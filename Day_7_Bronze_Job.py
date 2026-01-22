# Databricks notebook source
# Parameters
dbutils.widgets.text("run_date", "")
run_date = dbutils.widgets.get("run_date")

print(f"Bronze job running for date: {run_date}")

from pyspark.sql import functions as F

# Read raw data
raw = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)

# Add ingestion timestamp
bronze = raw.withColumn("ingestion_ts", F.current_timestamp())

# Write Bronze table
bronze.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_events")

# IMPORTANT: return value for controller
dbutils.notebook.exit("Bronze completed successfully")
