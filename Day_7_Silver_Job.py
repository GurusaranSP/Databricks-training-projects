# Databricks notebook source
# Parameters
dbutils.widgets.text("run_date", "")
run_date = dbutils.widgets.get("run_date")

print(f"Silver job running for date: {run_date}")

from pyspark.sql import functions as F

# Read Bronze table
bronze = spark.read.table("bronze_events")

# Clean & validate
silver = (
    bronze
    .filter(F.col("price").isNotNull())
    .filter(F.col("price") > 0)
    .filter(F.col("price") < 10000)
    .dropDuplicates(["user_session", "event_time"])
    .withColumn("event_date", F.to_date("event_time"))
)

# Write Silver table
silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_events")

dbutils.notebook.exit("Silver completed successfully")
