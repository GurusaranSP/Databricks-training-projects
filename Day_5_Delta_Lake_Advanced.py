# Databricks notebook source
spark.sql("""
SELECT * FROM events_delta VERSION AS OF 0
""").show(5)


# COMMAND ----------

# DBTITLE 1,Cell 2
spark.sql("""
SELECT * FROM events_delta TIMESTAMP AS OF '2026-01-11 06:56:05'
""")

# COMMAND ----------

# DBTITLE 1,Cell 3
events = spark.read.table("events_delta")
updates = events.limit(100)

updates.createOrReplaceTempView("updates")

spark.sql("""
MERGE INTO events_delta t
USING updates s
ON t.user_id = s.user_id AND t.event_time = s.event_time
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
""")

# COMMAND ----------

spark.sql("""
OPTIMIZE events_delta
ZORDER BY (product_id)
""")


# COMMAND ----------

spark.sql("""
VACUUM events_delta RETAIN 168 HOURS
""")
