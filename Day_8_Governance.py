# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS ecommerce;
# MAGIC USE ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS ecommerce.bronze_events AS
# MAGIC SELECT * FROM default.bronze_events;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS ecommerce.silver_events AS
# MAGIC SELECT * FROM default.silver_events;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS ecommerce.gold_products AS
# MAGIC SELECT * FROM default.gold_products;
# MAGIC

# COMMAND ----------

# MAGIC %sql 
# MAGIC SHOW TABLES IN ecommerce;
# MAGIC SELECT COUNT(*) FROM ecommerce.gold_products;
# MAGIC