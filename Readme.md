# 📘 Databricks 14 Days AI Challenge

**End-to-End Lakehouse, Analytics & ML Training (Day 0 – Day 14)**

## 📌 Overview

This repository/document captures my complete learning journey through the **Databricks 14 Days AI Challenge**, organized by **Indian Data Club** in collaboration with **Codebasics**, and sponsored by **Databricks**.

The objective of this program was to build **strong practical foundations** in:

*   Databricks Lakehouse architecture  
    
*   Apache Spark & Delta Lake  
    
*   Data engineering best practices  
    
*   Governance & performance optimization  
    
*   SQL analytics & dashboards  
    
*   Statistical analysis & machine learning  
    
*   MLflow experiment tracking  
    
*   AI-powered analytics concepts  
    

All work was performed using **Databricks Community Edition**, with clear handling of platform limitations where applicable.

## 🧱 Dataset Used

*   **E-commerce Behavior Dataset (2019 – Oct & Nov)  
    **
*   Source: Kaggle  
    
*   Scale: ~13M+ events  
    
*   Event types: view, cart, purchase, remove\_from\_cart  
    

This dataset was incrementally processed using **Bronze → Silver → Gold** layers.

## 📂 Project Structure (Day-wise)

Each day corresponds to a dedicated notebook/script focusing on a specific concept.

## 🟦 Day 0 – Environment Setup & Data Loading

**Objective:** Prepare Databricks workspace and ingest raw data.

**Key Activities:**

*   Created Databricks Community Edition account  
    
*   Configured Kaggle API credentials  
    
*   Created schemas and volumes  
    
*   Downloaded and extracted raw CSV data  
    
*   Loaded Oct & Nov 2019 data into Spark DataFrames  
    

**Outcome:  
**A reproducible, production-style ingestion setup.

## 🟦 Day 1 – PySpark Basics

**Objective:** Understand Spark DataFrames and basic operations.

**Key Concepts:**

*   Spark vs Pandas  
    
*   DataFrame creation  
    
*   Schema inspection  
    
*   Filtering and simple transformations  
    

**Outcome:  
**Comfort with basic PySpark syntax and execution model.

## 🟦 Day 2 – Apache Spark Fundamentals

**Objective:** Learn Spark’s core abstractions and transformations.

**Key Concepts:**

*   Spark architecture (driver, executors, DAG)  
    
*   Lazy evaluation  
    
*   DataFrames vs RDDs  
    
*   SQL temporary views  
    

**Outcome:  
**Ability to perform real analytical queries using Spark SQL and DataFrames.

## 🟦 Day 3 – PySpark Transformations Deep Dive

**Objective:** Perform complex data transformations.

**Key Concepts:**

*   Joins (inner, left, right, outer)  
    
*   Window functions (ranking, cumulative counts)  
    
*   Aggregations and pivots  
    
*   Feature bucketing and derived columns  
    

**Outcome:  
**Hands-on experience with advanced Spark transformations used in real pipelines.

## 🟦 Day 4 – Delta Lake Basics

**Objective:** Introduce Delta Lake and ACID reliability.

**Key Concepts:**

*   Delta vs Parquet  
    
*   ACID transactions  
    
*   Schema enforcement  
    
*   Managed tables  
    

**Outcome:  
**Reliable, transactional data storage using Delta Lake.

## 🟦 Day 5 – Delta Lake Advanced

**Objective:** Work with advanced Delta features.

**Key Concepts:**

*   Time Travel  
    
*   MERGE (upserts)  
    
*   OPTIMIZE and ZORDER  
    
*   VACUUM for cleanup  
    

**Outcome:  
**Understanding of how Delta Lake supports incremental and performant pipelines.

## 🟦 Day 6 – Medallion Architecture

**Objective:** Design a production-grade data pipeline.

**Layers Implemented:**

*   **Bronze:** Raw ingestion with audit metadata  
    
*   **Silver:** Cleaned, deduplicated, validated data  
    
*   **Gold:** Aggregated, business-ready datasets  
    

**Outcome:  
**Clear separation of concerns and scalable pipeline design.

## 🟦 Day 7 – Databricks Jobs & Orchestration

**Objective:** Automate pipelines using jobs.

**Key Concepts:**

*   Notebook parameters (dbutils.widgets)  
    
*   Multi-task job orchestration  
    
*   Task dependencies (Bronze → Silver → Gold)  
    
*   Job controller notebook  
    
*   Error handling and job exits  
    

**Outcome:  
**End-to-end automated pipeline execution.

## 🟦 Day 8 – Unity Catalog & Governance

**Objective:** Apply data governance concepts.

**Key Concepts:**

*   Catalog → Schema → Table hierarchy  
    
*   Managed vs external tables  
    
*   Access control (GRANT / REVOKE)  
    
*   Controlled views  
    
*   Lineage awareness  
    

**Outcome:  
**Governed, discoverable, and secure data access.

## 🟦 Day 9 – SQL Analytics & Dashboards

**Objective:** Perform analytics using SQL.

**Key Concepts:**

*   Analytical SQL queries  
    
*   Revenue analysis  
    
*   Funnels and conversion rates  
    
*   Aggregations for dashboards  
    

**Outcome:  
**Business-focused insights derived directly from Gold tables.

## 🟦 Day 10 – Performance Optimization

**Objective:** Improve query performance.

**Key Concepts:**

*   Query execution plans  
    
*   Partitioning strategies  
    
*   OPTIMIZE & ZORDER  
    
*   Benchmarking  
    
*   Caching considerations (CE-aware)  
    

**Outcome:  
**Ability to reason about and improve Spark performance.

## 🟦 Day 11 – Statistical Analysis & ML Preparation

**Objective:** Prepare data for machine learning.

**Key Concepts:**

*   Descriptive statistics  
    
*   Hypothesis testing (weekday vs weekend)  
    
*   Correlation analysis  
    
*   Feature engineering  
    
*   Time-based features  
    

**Outcome:  
**ML-ready feature set derived from clean data.

## 🟦 Day 12 – MLflow Basics

**Objective:** Track ML experiments.

**Key Concepts:**

*   MLflow runs  
    
*   Parameter & metric logging  
    
*   Model logging  
    
*   Handling missing labels (NaN / NULL)  
    

**Outcome:  
**Reproducible ML experimentation workflow.

## 🟦 Day 13 – Model Comparison & Feature Engineering

**Objective:** Compare multiple ML models.

**Key Concepts:**

*   Linear Regression, Decision Trees, Random Forest  
    
*   R² metric comparison  
    
*   Feature importance  
    
*   Spark ML pipelines  
    
*   Handling NULL labels in Spark ML  
    

**Outcome:  
**Model selection based on metrics and data understanding.

## 🟦 Day 14 – AI-Powered Analytics (Conceptual + Practical)

**Objective:** Understand AI’s role in modern analytics.

**Key Concepts:**

*   Databricks Genie (NL → SQL concept)  
    
*   Mosaic AI overview  
    
*   AI-assisted analytics  
    
*   Simple classification using Spark ML  
    
*   MLflow logging for AI workflows  
    

**Note:  
**Full Genie and Mosaic AI features require paid Databricks workspaces; Community Edition limitations were handled transparently.

**Outcome:  
**Clear understanding of how GenAI integrates with governed data platforms.

## 🚀 What Comes Next: Capstone Project (Codebasics)

With the 14-day foundation complete, the next phase is the **Codebasics Capstone Project**, where:

*   A real-world problem statement will be provided  
    
*   End-to-end data engineering, analytics, and ML will be applied  
    
*   Best practices learned here will be consolidated into a production-style project  
    

This training phase was intentionally focused on **depth, correctness, and fundamentals**, not shortcuts.

## 🎯 Key Takeaways

*   Built a complete **Lakehouse pipeline** from raw data to AI insights  
    
*   Understood **why** things break, not just how to fix them  
    
*   Learned to work within **real platform constraints  
    **
*   Developed habits aligned with **industry-grade data engineering  
    **

## 📎 Acknowledgements

*   **Databricks** – Platform & learning ecosystem  
    
*   **Indian Data Club** – Community & challenge organization  
    
*   **Codebasics** – Structured learning and capstone phase  
    

📌 _This document represents a complete hands-on learning journey from Day 0 to Day 14 and serves as the foundation for the upcoming capstone project._



