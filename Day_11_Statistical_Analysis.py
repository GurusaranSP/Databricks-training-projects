# Databricks notebook source
events = spark.table("ecommerce.silver_events")


# COMMAND ----------

events.describe("price").show()


# COMMAND ----------

from pyspark.sql import functions as F

events = events.withColumn(
    "is_weekend",
    F.dayofweek("event_date").isin([1, 7])
)


# COMMAND ----------

events.groupBy("is_weekend", "event_type").count().orderBy("is_weekend").show()


# COMMAND ----------

events.stat.corr("price", "user_id")


# COMMAND ----------

events = (
    events
    .withColumn("hour", F.hour("event_time"))
    .withColumn("day_of_week", F.dayofweek("event_date"))
    .withColumn("price_log", F.log(F.col("price") + 1))
)


# COMMAND ----------

from pyspark.sql.window import Window

w = Window.partitionBy("user_id").orderBy("event_time")

events = events.withColumn(
    "time_since_first_event",
    F.unix_timestamp("event_time") -
    F.first("event_time").over(w).cast("long")
)


# COMMAND ----------

events.select(
    "price",
    "price_log",
    "hour",
    "day_of_week",
    "is_weekend",
    "time_since_first_event"
).show(5, truncate=False)


# COMMAND ----------

