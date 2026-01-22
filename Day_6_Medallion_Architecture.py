# Databricks notebook source
from pyspark.sql import functions as F

raw = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)

raw.withColumn("ingestion_ts", F.current_timestamp()) \
   .write.format("delta") \
   .mode("overwrite") \
   .saveAsTable("bronze_events")


# COMMAND ----------

bronze = spark.read.table("bronze_events")

silver = (
    bronze
    .filter(F.col("price") > 0)
    .filter(F.col("price") < 10000)
    .dropDuplicates(["user_session", "event_time"])
    .withColumn("event_date", F.to_date("event_time"))
)

silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_events")


# COMMAND ----------

gold = (
    silver
    .groupBy("product_id")
    .agg(
        F.count("*").alias("events"),
        F.sum(F.when(F.col("event_type")=="purchase", F.col("price"))).alias("revenue")
    )
)

gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_products")
