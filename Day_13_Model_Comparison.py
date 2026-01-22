# Databricks notebook source
import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


# COMMAND ----------

df = spark.table("ecommerce.gold_products")
pdf = df.toPandas()


# COMMAND ----------

pdf.columns
pdf.head()


# COMMAND ----------

X = pdf.select_dtypes(include="number").drop(columns=["revenue"], errors="ignore")
y = pdf["revenue"]


# COMMAND ----------

models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "RandomForest": RandomForestRegressor(n_estimators=50, random_state=42)
}


# COMMAND ----------

pdf["revenue"].isna().sum()


# COMMAND ----------

pdf = pdf.dropna(subset=["revenue"])


# COMMAND ----------

X = pdf.select_dtypes(include="number").drop(columns=["revenue"], errors="ignore")
y = pdf["revenue"]


# COMMAND ----------

y.isna().sum()   # MUST be 0


# COMMAND ----------

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
model.score(X, y)


# COMMAND ----------

rf_model = models["RandomForest"]
rf_model.fit(X, y)

import pandas as pd

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": rf_model.feature_importances_
}).sort_values(by="importance", ascending=False)

feature_importance


# COMMAND ----------

spark_df.select("revenue").where("revenue IS NULL").count()


# COMMAND ----------

spark_df_clean = spark_df.filter("revenue IS NOT NULL")


# COMMAND ----------

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline

assembler = VectorAssembler(
    inputCols=[c for c in spark_df_clean.columns if c != "revenue"],
    outputCol="features"
)

lr = LinearRegression(
    featuresCol="features",
    labelCol="revenue"
)

pipeline = Pipeline(stages=[assembler, lr])
pipeline_model = pipeline.fit(spark_df_clean)


# COMMAND ----------

spark_df_filled = spark_df.fillna({"revenue": 0})
