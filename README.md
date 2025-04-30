# 🛒 Ecommerce Data Pipeline and Analysis

## Objective
This project was developed for the 2025 DubsTech x UWashington Datathon and simulates a real-world BI and consulting workflow. Data from Modecraft’s e-commerce platform was loaded from Azure Blob Storage into Snowflake, where it was transformed using SQL and Python in VS Code.

Analyses included product health scoring, RFM segmentation, and market basket insights. Results were written back to Snowflake and visualized in Tableau to highlight key revenue drivers and customer behavior.

The data architecture was designed to apply core tools and processes as part of a learning exercise and will be iterated over time to improve efficiency, scalability, and analytical depth. Additional analyses and architectural enhancements are planned as the project evolves.

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
- Step 3.1: Transformation - Python Feature Engineering, and Data Analysis + Step 4.1: Staging [code](https://github.com/maicorebong/Datathon2025-DubsTechUW/blob/main/step3-4-modecraft-python-analysis.py)
- Step 3.2: Transformation - SQL Exploratory Data Analysis + Step 4.1: Staging [code]
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

## Step 3.1: Python Transformation and Analysis + Step 4: Serving

With the data staged in Snowflake, the VS Code environment was configured by installing required Python packages and setting session parameters to enable Snowflake-Python integration.
![3connect](https://github.com/user-attachments/assets/e1eea522-6816-4de0-b9ab-840cca3adfe3)

Data cleaning and feature engineering
![3cleaning](https://github.com/user-attachments/assets/9ef91b5a-058c-4567-acb6-ed052192f197)

Analyzing Product Health Score
![3analysis1](https://github.com/user-attachments/assets/0f5a1fe6-9f5c-467c-b567-98123efce616)

Performing Market Basket Analysis
![3analysis2](https://github.com/user-attachments/assets/c7670b86-813d-497d-916f-3e00e9c30e80)

Performing RFM Analysis
![3analysis3](https://github.com/user-attachments/assets/538f71aa-0718-4c9e-8e2d-d32121702447)

Once dataframes have been set up via Python, these mini tables will be uploaded to Snowflake which will serve as our data marts.
![serving](https://github.com/user-attachments/assets/310a6400-7bd6-44f8-b982-c3cb1415a495)


## Step 3.2: SQL Transformation and Analysis + Step 4: Serving

Exploratory Data Analysis (EDA) was conducted directly in Snowflake using SQL. For each insight, a dedicated query was written to generate aggregated results which were then saved as data marts. The process includes table creation or replacement, followed by data insertion using CREATE OR REPLACE and INSERT INTO statements. This ensures reproducibility and modular access to curated insights in downstream analyses or dashboards.
![sql1](https://github.com/user-attachments/assets/5f9f04ef-fa0d-4c5d-af00-71697f56a288)
![sql2](https://github.com/user-attachments/assets/552400a6-c7e6-4796-8991-fc21f2cc80f7)
![sql3](https://github.com/user-attachments/assets/1254c9dc-ff1c-434d-8021-eea14a60a260)
![sql4](https://github.com/user-attachments/assets/ec76cd81-e7b0-4053-a56e-641dc5d68602)
![sql5](https://github.com/user-attachments/assets/1aa74eb0-7510-41c6-a6df-2fa4970f4e00)



