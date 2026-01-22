# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT product_id,
# MAGIC        SUM(revenue) AS total_revenue
# MAGIC FROM ecommerce.gold_products
# MAGIC GROUP BY product_id
# MAGIC ORDER BY total_revenue DESC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS total_views,
# MAGIC   COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS total_purchases,
# MAGIC   COUNT(CASE WHEN event_type = 'purchase' THEN 1 END)
# MAGIC     / COUNT(CASE WHEN event_type = 'view' THEN 1 END) * 100
# MAGIC     AS conversion_rate
# MAGIC FROM ecommerce.silver_events;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ecommerce.gold_products AS
# MAGIC SELECT
# MAGIC   product_id,
# MAGIC   COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS views,
# MAGIC   COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchases,
# MAGIC   SUM(CASE WHEN event_type = 'purchase' THEN price END) AS revenue
# MAGIC FROM ecommerce.silver_events
# MAGIC GROUP BY product_id;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ecommerce.gold_products AS
# MAGIC SELECT
# MAGIC   product_id,
# MAGIC   COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS views,
# MAGIC   COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchases,
# MAGIC   SUM(CASE WHEN event_type = 'purchase' THEN price END) AS revenue
# MAGIC FROM ecommerce.silver_events
# MAGIC GROUP BY product_id;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   SUM(views) AS total_views,
# MAGIC   SUM(purchases) AS total_purchases,
# MAGIC   SUM(purchases) / SUM(views) * 100 AS conversion_rate
# MAGIC FROM ecommerce.gold_products;
# MAGIC