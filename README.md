# 🛒 Ecommerce Data Pipeline and Analysis

## Objective
This project was developed for the 2025 DubsTech x UWashington Datathon and simulates a real-world BI and consulting workflow. Data from Modecraft’s e-commerce platform was loaded from Azure Blob Storage into Snowflake, where it was transformed using SQL and Python in VS Code.

Analyses included product health scoring, RFM segmentation, and market basket insights. Results were written back to Snowflake and visualized in Tableau to highlight key revenue drivers and customer behavior.

The data architecture was designed to apply core tools and processes as part of a learning exercise and will be iterated over time to improve efficiency, scalability, and analytical depth. Additional analyses and architectural enhancements are planned as the project evolves.



## Table of Content

- [Dataset Used](#dataset-used)
- [Technologies](technologies)
- [Data Pipeline Architecture](#data-pipeline-architecture)
- [Date Modeling](#data-modeling)
- [Step 1: Cleaning and Transformation](#step-1-cleaning-and-transformation)
- [Step 2: Storage](#step-2-storage)
- [Step 3: ETL / Orchestration](#step-3-etl--orchestration)
- [Step 4: Analytics](#step-4-analytics)
- [Step 5: Dashboard](#step-5-dashboard)

## Dataset Used
This project uses anonymized e-commerce transaction data from Modecraft, shared as part of the Dubstech x University of Washington Datathon 2025. The dataset contains detailed order-level information such as invoice number, product stock code, item description, quantity purchased, invoice date and time, unit price, customer ID, and country.

More information about the dataset:
- Context: Provided by Dubstech x University of Washington Datathon 2025
- Fields: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- Raw Data (CSV): https://github.com/maicorebong/Datathon2025-DubsTechUW/blob/main/modecraft_ecommerce_compressed_data.gz

## Technologies

The following technologies are used to build this project:
- Language: Python, SQL
- Storage: Azure Blob Storage
- Data warehouse: Snowflake
- Development environment: VS Code
- Dashboard: Tableau

## Data Pipeline Architecture
<img width="682" alt="Untitled" src="https://github.com/user-attachments/assets/c3c8bbc0-4ecd-4737-b3e6-0de784063029" />

Files in the following stages:
- Step 1: Data Ingestion and Storage
- Step 2: Staging
- Step 3.1: Transformation: Feature Engineering, and Data Analysis (Python) x
- Step 3.2: Transformation: Exploratory Data Analysis (SQL) x
- Step 4: Serving
- Step 5.1: BI & Insights: Dashboard x
- Step 5.2: BI & Insights: Deck x
