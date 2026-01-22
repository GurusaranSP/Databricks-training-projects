# Databricks notebook source
spark_df = spark.table("ecommerce.gold_products")
spark_df.show(5)


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   product_id,
# MAGIC   revenue
# MAGIC FROM ecommerce.gold_products
# MAGIC ORDER BY revenue DESC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- "Which products generate the least revenue?"
# MAGIC SELECT
# MAGIC   product_id,
# MAGIC   revenue
# MAGIC FROM ecommerce.gold_products
# MAGIC ORDER BY revenue ASC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Natural language: "Top products by revenue"
# MAGIC SELECT
# MAGIC   product_id,
# MAGIC   revenue
# MAGIC FROM ecommerce.gold_products
# MAGIC ORDER BY revenue DESC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression


# COMMAND ----------

from pyspark.sql import functions as F

df = spark.table("ecommerce.gold_products") \
    .filter("revenue IS NOT NULL")

df.show(5)


# COMMAND ----------

df = df.withColumn(
    "label",
    (F.col("revenue") > 100).cast("int")
)

df.select("revenue", "label").show(5)


# COMMAND ----------

from pyspark.ml.feature import VectorAssembler

feature_cols = [c for c in df.columns if c not in ["revenue", "label"]]

assembler = VectorAssembler(
    inputCols=feature_cols,
    outputCol="features"
)

df_ml = assembler.transform(df).select("features", "label")


# COMMAND ----------

from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression()
model = lr.fit(df_ml)


# COMMAND ----------

model.transform(df_ml) \
    .select("label", "prediction", "probability") \
    .show(5)


# COMMAND ----------

import mlflow

with mlflow.start_run(run_name="day14_ai_analytics"):
    mlflow.log_param("model", "logistic_regression")
    mlflow.log_metric("rows_used", df_ml.count())
