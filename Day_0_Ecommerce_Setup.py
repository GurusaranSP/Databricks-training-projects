# Databricks notebook source
!pip install --upgrade kaggle


# COMMAND ----------

# MAGIC %restart_python
# MAGIC

# COMMAND ----------

import os

os.environ["KAGGLE_USERNAME"] = "gurusaransatsangip"
os.environ["KAGGLE_KEY"] = "988e78fab4dfb829d61eaf6faf092946"

print("Kaggle credentials configured")


# COMMAND ----------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS workspace.ecommerce
""")

spark.sql("""
CREATE VOLUME IF NOT EXISTS workspace.ecommerce.ecommerce_data
""")


# COMMAND ----------

import os

base_path = "/Volumes/workspace/ecommerce/ecommerce_data"

os.system(f"""
cd {base_path} &&
kaggle datasets download -d mkechinov/ecommerce-behavior-data-from-multi-category-store
""")


# COMMAND ----------

os.system(f"""
cd {base_path} &&
unzip -o ecommerce-behavior-data-from-multi-category-store.zip
""")


# COMMAND ----------

display(dbutils.fs.ls("/Volumes/workspace/ecommerce/ecommerce_data"))


# COMMAND ----------

df_oct = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv",
    header=True,
    inferSchema=True
)

df_nov = spark.read.csv(
    "/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv",
    header=True,
    inferSchema=True
)


# COMMAND ----------

print(f"October 2019 rows: {df_oct.count():,}")
print(f"November 2019 rows: {df_nov.count():,}")

df_oct.printSchema()


# COMMAND ----------

df_oct.show(5, truncate=False)
