# Databricks notebook source
# MAGIC %sql 
# MAGIC SHOW DATABASES;
# MAGIC SHOW TABLES IN default;
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %sql 
# MAGIC SHOW DATABASES;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS ecommerce;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE ecommerce.gold_products AS
# MAGIC SELECT * FROM default.gold_products;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC USE ecommerce;
# MAGIC

# COMMAND ----------

spark.read.table("gold_products").count()


# COMMAND ----------

spark.read.table("ecommerce.gold_products").count()


# COMMAND ----------

spark.sql("SELECT COUNT(*) FROM ecommerce.gold_products").show()


# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES;
# MAGIC SHOW TABLES IN default;
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC

# COMMAND ----------

spark.sql("SELECT COUNT(*) FROM ecommerce.gold_products").show()
