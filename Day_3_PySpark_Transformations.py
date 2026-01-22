# Databricks notebook source
events = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)

print(events.count())
events.printSchema()


# COMMAND ----------

events = events.select(
    "event_time",
    "event_type",
    "product_id",
    "category_code",
    "brand",
    "price",
    "user_id"
)


# COMMAND ----------

products = events.select("product_id", "brand", "category_code").dropDuplicates()
users = events.select("user_id").dropDuplicates()


# COMMAND ----------

inner_join = events.join(products, on="product_id", how="inner")
inner_join.show(5)


# COMMAND ----------

left_join = events.join(products, on="product_id", how="left")
left_join.show(5)


# COMMAND ----------

outer_join = events.join(products, on="product_id", how="outer")
outer_join.show(5)


# COMMAND ----------

from pyspark.sql import functions as F

revenue = (
    events
    .filter(F.col("event_type") == "purchase")
    .groupBy("product_id")
    .agg(F.sum("price").alias("revenue"))
    .orderBy(F.desc("revenue"))
    .limit(5)
)

revenue.show()


# COMMAND ----------

from pyspark.sql.window import Window

user_window = Window.partitionBy("user_id").orderBy("event_time")


# COMMAND ----------

events_with_running = events.withColumn(
    "cumulative_events",
    F.count("*").over(user_window)
)

events_with_running.select(
    "user_id", "event_time", "event_type", "cumulative_events"
).show(10)


# COMMAND ----------

rank_window = Window.partitionBy("user_id").orderBy(F.desc("event_time"))

events_ranked = events.withColumn(
    "rank", F.row_number().over(rank_window)
)

events_ranked.show(5)


# COMMAND ----------

event_counts = (
    events
    .groupBy("category_code", "event_type")
    .count()
)


# COMMAND ----------

pivoted = (
    event_counts
    .groupBy("category_code")
    .pivot("event_type")
    .sum("count")
)


# COMMAND ----------

conversion = pivoted.withColumn(
    "conversion_rate",
    (F.col("purchase") / F.col("view")) * 100
)

conversion.show(10)


# COMMAND ----------

events_features = events.withColumn(
    "price_bucket",
    F.when(F.col("price") < 50, "low")
     .when(F.col("price") < 200, "medium")
     .otherwise("high")
)

events_features.select("price", "price_bucket").show(10)


# COMMAND ----------

revenue.write.mode("overwrite").csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/day3_top_revenue_products"
)
