# Databricks 14 Days AI Challenge

# 

**End-to-End Lakehouse, Analytics & ML Training (Day 0 – Day 14)**

* * *

##   

## Author

# 

**Name:** Guru Saran Satsangi Peddinti  
**Program:** BS in Data Science & Applications – IIT Madras  
**Community:** Indian Data Club  
**Challenge:** Databricks 14 Days AI Challenge  
**Duration:** 09 Jan 2026 – 22 Jan 2026  
**Platform:** Databricks Community Edition

* * *

##   

## About This Document

# 

This document serves as a **comprehensive training log and technical summary** of my work during the **Databricks 14 Days AI Challenge**, organized by **the Indian Data Club**, delivered in collaboration with **Codebasics**, and sponsored by **Databricks**.

The goal of this challenge was to **build real-world, hands-on foundations** in:

*   Databricks Lakehouse Architecture
    
*   Apache Spark & Delta Lake
    
*   Data Engineering pipelines
    
*   Governance, performance, and orchestration
    
*   SQL analytics & dashboards
    
*   Statistical analysis & Machine Learning
    
*   MLflow & AI-powered analytics concepts
    

All implementations were done using **Databricks Community Edition**, with transparent handling of platform limitations.

##   

## Project Folder Structure

# 

    databricks-14-days-ai-challenge/
    │
    ├── Day_0_Ecommerce_Setup.py
    ├── Day_1_PySpark_Basics.py
    ├── Day_2_Apache_Spark_Fundamentals.py
    ├── Day_3_PySpark_Transformations.py
    ├── Day_4_Delta_Lake_Basics.py
    ├── Day_5_Delta_Lake_Advanced.py
    ├── Day_6_Medallion_Architecture.py
    │
    ├── Day_7_Bronze_Job.py
    ├── Day_7_Silver_Job.py
    ├── Day_7_Gold_Job.py
    ├── Day_7_Job_Controller.py
    ├── Day_7_Verify.py
    │
    ├── Day_8_Governance.py
    ├── Day_9_SQL_Analytics.py
    ├── Day_10_Performance.py
    ├── Day_11_Statistical_Analysis.py
    ├── Day_12_MLflow_Basics.py
    ├── Day_13_Model_Comparison.py
    ├── Day_14_AI_Powered_Analytics.py
    │
    └── README.md  (this document)
    

* * *

##   

## Dataset Used

# 

*   **E-commerce Behavior Dataset (2019 – October & November)**
    
*   Source: Kaggle
    
*   Scale: ~13+ million events
    
*   Event types: `view`, `cart`, `purchase`, `remove_from_cart`
    

This dataset was processed using the **Bronze → Silver → Gold (Medallion) Architecture**.

* * *

##   

## Day-wise Training Summary

# 

* * *

###   

### Day 0 – Setup & Data Loading

# 

**Focus:** Environment preparation and ingestion

*   Databricks Community Edition setup
    
*   Kaggle API configuration
    
*   Schema & volume creation
    
*   Raw CSV download and ingestion
    

**Outcome:** Reliable, repeatable data loading pipeline.

* * *

### Day 1 – PySpark Basics

# 

**Focus:** Spark fundamentals

*   DataFrames vs Pandas
    
*   Basic transformations
    
*   Schema inspection and filtering
    

**Outcome:** Comfort with Spark syntax and execution.

* * *

###   

### Day 2 – Apache Spark Fundamentals

# 

**Focus:** Spark internals

*   Driver, executors, DAG
    
*   Lazy evaluation
    
*   Spark SQL & temp views
    

**Outcome:** Ability to reason about Spark execution.

* * *

###   

### Day 3 – PySpark Transformations

# 

**Focus:** Advanced transformations

*   Joins (inner, left, right, outer)
    
*   Window functions
    
*   Aggregations, pivots
    
*   Derived features
    

**Outcome:** Production-style data transformations.

* * *

###   

### Day 4 – Delta Lake Basics

# 

**Focus:** Reliable storage

*   Delta vs Parquet
    
*   ACID transactions
    
*   Schema enforcement
    

**Outcome:** Transaction-safe data lake.

* * *

###   

### Day 5 – Delta Lake Advanced

# 

**Focus:** Data evolution & optimization

*   Time Travel
    
*   MERGE (upserts)
    
*   OPTIMIZE & ZORDER
    
*   VACUUM
    

**Outcome:** Incremental and performant pipelines.

* * *

###   

### Day 6 – Medallion Architecture

# 

**Focus:** Pipeline design

*   Bronze: raw ingestion
    
*   Silver: cleaned & deduplicated
    
*   Gold: business aggregates
    

**Outcome:** Scalable, maintainable data architecture.

* * *

###   

### Day 7 – Databricks Jobs & Orchestration

# 

**Focus:** Automation

*   Notebook parameterization
    
*   Multi-task workflows
    
*   Dependencies (Bronze → Silver → Gold)
    
*   Job controller logic
    

**Outcome:** Fully automated pipelines.

* * *

###   

### Day 8 – Unity Catalog & Governance

# 

**Focus:** Data governance

*   Catalog → Schema → Table hierarchy
    
*   Permissions & access control
    
*   Controlled views
    
*   Lineage awareness
    

**Outcome:** Secure and discoverable data platform.

* * *

###   

### Day 9 – SQL Analytics & Dashboards

# 

**Focus:** Business analytics

*   Analytical SQL queries
    
*   Revenue trends
    
*   Funnels & conversion analysis
    

**Outcome:** Insight generation from Gold data.

* * *

###   

### Day 10 – Performance Optimization

# 

**Focus:** Speed & efficiency

*   Query plans
    
*   Partitioning
    
*   OPTIMIZE & ZORDER
    
*   Benchmarking
    

**Outcome:** Performance-aware Spark usage.

* * *

###   

### Day 11 – Statistical Analysis & ML Prep

# 

**Focus:** ML readiness

*   Descriptive statistics
    
*   Hypothesis testing
    
*   Correlation checks
    
*   Feature engineering
    

**Outcome:** Clean, ML-ready datasets.

* * *

###   

### Day 12 – MLflow Basics

# 

**Focus:** Experiment tracking

*   MLflow runs
    
*   Parameter & metric logging
    
*   Model artifacts
    
*   Handling NULL/NaN labels
    

**Outcome:** Reproducible ML experiments.

* * *

###   

### Day 13 – Model Comparison

# 

**Focus:** Model evaluation

*   Multiple regression models
    
*   Metric comparison
    
*   Feature importance
    
*   Spark ML pipelines
    

**Outcome:** Informed model selection.

* * *

###   

### Day 14 – AI-Powered Analytics

# 

**Focus:** AI in analytics

*   Databricks Genie (NL → SQL concept)
    
*   Mosaic AI overview
    
*   AI-assisted analytics
    
*   Spark ML–based AI demo
    
*   MLflow logging for AI workflows
    

**Note:** Full GenAI features require paid Databricks workspaces; Community Edition constraints were handled transparently.

**Outcome:** Clear understanding of AI’s role in modern data platforms.

* * *

##   

## Next Phase: Capstone Project (Codebasics)

# 

With the 14-day foundation complete, the next step is the **Codebasics Capstone Project**, where:

*   A real-world problem statement will be provided
    
*   End-to-end data engineering, analytics, and ML will be applied
    
*   Best practices learned here will be consolidated into a production-grade solution
    

This training phase focused on **fundamentals, correctness, and reasoning**, ensuring readiness for the capstone.

* * *

##   

## Key Takeaways

# 

*   Built a complete **Lakehouse pipeline** from raw data to AI insights
    
*   Learned to debug **real platform and data issues**
    
*   Practiced governance, performance, and ML workflows
    
*   Developed habits aligned with **industry-grade data engineering**
    

* * *



## Acknowledgements

# 

*   **Databricks** – Platform & ecosystem
    
*   **Indian Data Club** – Community & challenge organization
    
*   **Codebasics** – Structured learning & capstone phase
    

* * *

_This document represents a complete, hands-on Databricks learning journey from Day 0 to Day 14 and serves as the foundation for the upcoming capstone project._

* * *
