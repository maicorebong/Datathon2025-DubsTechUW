# 🛒 Ecommerce Data Pipeline and Analysis

## Objective
This project was developed for the 2025 DubsTech x UWashington Datathon and simulates a real-world BI and consulting workflow. Data from Modecraft’s e-commerce platform was loaded from Azure Blob Storage into Snowflake, where it was transformed using SQL and Python in VS Code.

Analyses included product health scoring, RFM segmentation, and market basket insights. Results were written back to Snowflake and visualized in Tableau to highlight key revenue drivers and customer behavior.

The data architecture was designed to apply core tools and processes as part of a learning exercise and will be iterated over time to improve efficiency, scalability, and analytical depth. Additional analyses and architectural enhancements are planned as the project evolves.



## Table of Content

- [Dataset Used](#dataset-used)
- [Technologies](technologies)
- [Data Pipeline Architecture](#data-pipeline-architecture)
- [Step 1: Data Ingestion and Storage](#step-1-data-ingestion-and-storage)
- [Step 2: Staging](#step-2-staging) 
- [Step 3.1: Transformation and Analysis: Python](#step-31-transformation-and-analysis-python)
- [Step 3.2: Transformation and Analysis: SQL](#step-32-transformation-and-analysis-sql)
- [Step 4: Serving](#step-4-serving)
- [Step 5.1: BI & Insights - Dashboard](#step-51-bi-insights-dashboard)
- [Step 5.2: BI & Insights - Executive Deck](#step-52-bi-insights-executive-deck)


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
![pipeline](https://github.com/user-attachments/assets/a11b140e-b22a-43b3-bc54-723879e5e055)

Files in the following stages:
- Step 1: Data Ingestion and Storage
- Step 2: Staging
- Step 3.1: Transformation: Feature Engineering, and Data Analysis (Python) x
- Step 3.2: Transformation: Exploratory Data Analysis (SQL) x
- Step 4: Serving
- Step 5.1: BI & Insights: Dashboard x
- Step 5.2: BI & Insights: Deck x

### Step 1: Data Ingestion and Storage
Created a resource group and storage account, then uploaded the raw modecraft_online_retail.csv file to a blob container.
![1blob](https://github.com/user-attachments/assets/1e0c23e5-0986-499f-bbb9-5c4d5128f536)
![2blob](https://github.com/user-attachments/assets/87fae726-e6ab-4908-8afa-0fc1f72a5e20)

## Step 2: Staging
Configured Shared Access Signature (SAS) settings to enable secure and controlled access for data exchange from Azure. Set start and expiry date/time as needed and generate a SAS token. Set up external stage referencing SAS token from Azure container to Snowflake. [reference](https://docs.snowflake.com/en/user-guide/data-load-azure-config) 
![3blob](https://github.com/user-attachments/assets/c8314968-f57b-4477-8bc9-06faeb00a0a9)
![2stage](https://github.com/user-attachments/assets/01baefcb-1d7c-4cd1-a84a-23ae8ac040b3)

## Step 3.1: Transformation and Analysis: Python
Set up VS Code environment by installing necessary Python packages and session parameters to connect to Snowflake with Python
![3connect](https://github.com/user-attachments/assets/e1eea522-6816-4de0-b9ab-840cca3adfe3)

Data cleaning and feature engineering
![3cleaning](https://github.com/user-attachments/assets/9ef91b5a-058c-4567-acb6-ed052192f197)

Analyzing Product Health Score
![3analysis1](https://github.com/user-attachments/assets/0f5a1fe6-9f5c-467c-b567-98123efce616)

Performing Market Basket Analysis
![3analysis2](https://github.com/user-attachments/assets/c7670b86-813d-497d-916f-3e00e9c30e80)

Performing RFM Analysis
![3analysis3](https://github.com/user-attachments/assets/538f71aa-0718-4c9e-8e2d-d32121702447)

## Step 3.2: Transformation and Analysis: SQL


