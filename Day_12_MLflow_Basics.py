# Databricks notebook source
import mlflow
import mlflow.sklearn


# COMMAND ----------

df = spark.table("ecommerce.gold_products")
df.show(5)


# COMMAND ----------

pdf = df.toPandas()



# COMMAND ----------

pdf.columns


# COMMAND ----------

X = pdf[["product_id"]]
y = pdf["revenue"]


# COMMAND ----------

pdf.head()


# COMMAND ----------

pdf.isnull().sum()


# COMMAND ----------

pdf = pdf.dropna(subset=["revenue"])


# COMMAND ----------

input_example = X.head(3)


# COMMAND ----------

with mlflow.start_run(run_name="day12_baseline"):
    mlflow.log_metric("r2_score", r2)
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        input_example=input_example
    )
