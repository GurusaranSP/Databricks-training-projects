# Databricks notebook source
spark

# COMMAND ----------

data = [
    ("iPhone", 999),
    ("Samsung", 799),
    ("MacBook", 1299)
]


# COMMAND ----------

df = spark.createDataFrame(data, ["product", "price"])


# COMMAND ----------

df.show()


# COMMAND ----------

df.printSchema()


# COMMAND ----------

df.filter(df.price > 1000).show()


# COMMAND ----------

df.count()


# COMMAND ----------

df.orderBy(df.price.desc()).show()
