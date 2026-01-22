# Databricks notebook source
events = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)

events.count()
events.printSchema()


# COMMAND ----------

events.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("events_delta")


# COMMAND ----------

spark.sql("DESCRIBE DETAIL events_delta").show(truncate=False)


# COMMAND ----------

spark.sql("""
CREATE TABLE IF NOT EXISTS events_delta_sql
USING DELTA
AS SELECT * FROM events_delta
""")


# COMMAND ----------

wrong_schema = spark.createDataFrame(
    [("a","b","c")],
    ["x","y","z"]
)

try:
    wrong_schema.write.format("delta") \
        .mode("append") \
        .saveAsTable("events_delta")
except Exception as e:
    print("Schema enforcement triggered")
    print(e)
