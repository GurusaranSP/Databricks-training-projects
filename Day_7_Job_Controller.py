# Databricks notebook source
# DBTITLE 1,Cell 1
run_date = "2026-01-16"

try:
    print("Starting Bronze Job...")
    bronze_result = dbutils.notebook.run(
        "Day_7_Bronze_Job",
        0,
        {"run_date": run_date}
    )
    print(bronze_result)
except Exception as e:
    raise Exception(f"Bronze Job Failed: {e}")

try:
    print("Starting Silver Job...")
    silver_result = dbutils.notebook.run(
        "Day_7_Silver_Job",
        0,
        {"run_date": run_date}
    )
    print(silver_result)
except Exception as e:
    raise Exception(f"Silver Job Failed: {e}")

try:
    print("Starting Gold Job...")
    gold_result = dbutils.notebook.run(
        "Day_7_Gold_Job",
        0,
        {"run_date": run_date}
    )
    print(gold_result)
except Exception as e:
    raise Exception(f"Gold Job Failed: {e}")

print("Bronze → Silver → Gold pipeline completed successfully")
