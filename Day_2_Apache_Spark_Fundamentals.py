# Databricks notebook source
spark


# COMMAND ----------

events = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)


# COMMAND ----------

events.printSchema()
events.show(5, truncate=False)


# COMMAND ----------

type(events)


# COMMAND ----------

filtered_events = events.filter(events.price > 100)


# COMMAND ----------

filtered_events.count()


# COMMAND ----------

events.select("event_type", "brand", "price").show(10)


# COMMAND ----------

events.groupBy("event_type").count().show()


# COMMAND ----------

top_brands = (
    events.groupBy("brand")
          .count()
          .orderBy("count", ascending=False)
          .limit(5)
)

top_brands.show()


# COMMAND ----------

events.orderBy(events.price.desc()).select("brand", "price").show(10)


# COMMAND ----------

from pyspark.sql import functions as F

event_counts = (
    events
    .groupBy("event_type")
    .agg(F.count("*").alias("total"))
    .orderBy(F.col("total").desc())
)

event_counts.show()


# COMMAND ----------

events.createOrReplaceTempView("events")

event_counts = spark.sql("""
    SELECT event_type, COUNT(*) AS total
    FROM events
    GROUP BY event_type
    ORDER BY total DESC
""")

event_counts.show()


# COMMAND ----------

# MAGIC %fs ls /Volumes/workspace/ecommerce/ecommerce_data
# MAGIC

# COMMAND ----------

top_brands.write.mode("overwrite").csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/top_brands"
)


# COMMAND ----------

# MAGIC %fs ls /Volumes/workspace/ecommerce/ecommerce_data/top_brands
# MAGIC