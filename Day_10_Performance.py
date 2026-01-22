# Databricks notebook source
spark.sql("""
SELECT * FROM ecommerce.silver_events
WHERE event_type = 'purchase'
""").explain(True)


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS ecommerce.silver_events_part
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (event_type)
# MAGIC AS
# MAGIC SELECT * FROM ecommerce.silver_events;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE ecommerce.silver_events_part;
# MAGIC

# COMMAND ----------

import time

start = time.time()
spark.sql("""
SELECT * FROM ecommerce.silver_events_part
WHERE event_type = 'purchase'
""").count()

print("Time:", time.time() - start)


# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS ecommerce.silver_events_part
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (event_type)
# MAGIC AS
# MAGIC SELECT * FROM ecommerce.silver_events;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM ecommerce.silver_events_part;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED ecommerce.silver_events_part;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES;
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM ecommerce.silver_events_part;
# MAGIC

# COMMAND ----------

df = spark.sql("SELECT * FROM ecommerce.silver_events_part")
df.show(5)


# COMMAND ----------

df = spark.table("ecommerce.silver_events_part")
type(df)



# COMMAND ----------

df = spark.table("ecommerce.silver_events_part")
df.count()
