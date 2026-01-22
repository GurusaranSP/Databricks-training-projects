# Databricks notebook source
# Parameters
dbutils.widgets.text("run_date", "")
run_date = dbutils.widgets.get("run_date")

print(f"Gold job running for date: {run_date}")

from pyspark.sql import functions as F

# Read Silver table
silver = spark.read.table("silver_events")

# Business aggregates
gold = (
    silver
    .groupBy("product_id")
    .agg(
        F.count("*").alias("events"),
        F.sum(
            F.when(F.col("event_type") == "purchase", F.col("price"))
        ).alias("revenue")
    )
)

# Write Gold table
gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_products")

dbutils.notebook.exit("Gold completed successfully")
