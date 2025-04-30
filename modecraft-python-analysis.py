from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import pandas as pd

##################################################################
############      STEP 3 TRANSFORMATION AND ANALYSIS #############

##################################################################
###############      CONNECT TO SNOWFLAKE       ##################
conn = snowflake.connector.connect(
    user='xxxxxxxxxxxXZZZxxxxxxxxxx',
    password='xxxxxxxxxxxxxxxxxxxxx',
    account='xxxxxxxxxxxxxxxxxxxxxx',
    warehouse='COMPUTE_WH',
    database='MODECRAFT_ECOMMERCE',
    schema='PUBLIC'
)

# Query the data
query = "SELECT * FROM modecraft_blob_data"
df = pd.read_sql(query, conn)
df.columns.tolist()
df.dtypes

##################################################################
##################        DATA CLEANING         ##################       

df['INVOICEDATE'] = pd.to_datetime(df['INVOICEDATE'], format='%m/%d/%y %H:%M') # Fix invoice date data type
df = df.dropna() # Remove missing data
df = df[df['QUANTITY'] > 0] # Remove quantities less than 0
df = df[df['UNITPRICE'] > 0] # Remove prices less than 0

df.head()
df.dtypes


##################################################################
#################       FEATURE ENGINEERING     ##################

df['REVENUE'] = df['QUANTITY'] * df['UNITPRICE']
df['YEAR'] = df['INVOICEDATE'].dt.year
df['MONTH'] = df['INVOICEDATE'].dt.month
df['DAY'] = df['INVOICEDATE'].dt.day
df['HOUR'] = df['INVOICEDATE'].dt.hour
df['DAYOFWEEK'] = df['INVOICEDATE'].dt.dayofweek
df['WEEKEND'] = df['DAYOFWEEK'].isin([5, 6])
df['QUARTER'] = df['INVOICEDATE'].dt.quarter
df.head()

##################################################################
#################       PRODUCT HEALTH SCORE    ##################

# Group totals
product_quantity = df.groupby('STOCKCODE')['QUANTITY'].sum().reset_index()
product_revenue = df.groupby('STOCKCODE')['REVENUE'].sum().reset_index()
product_summary = pd.merge(product_quantity, product_revenue, on='STOCKCODE')

#  Description
product_description = df[['STOCKCODE', 'DESCRIPTION']].drop_duplicates('STOCKCODE')
product_summary = pd.merge(product_summary, product_description, on='STOCKCODE')

# Percentile Ranks
product_summary['REVENUE_PERCENTILE'] = product_summary['REVENUE'].rank(pct=True)
product_summary['QUANTITY_PERCENTILE'] = product_summary['QUANTITY'].rank(pct=True)

# Health Score
product_summary['HEALTHSCORE'] = product_summary['REVENUE_PERCENTILE'] + product_summary['QUANTITY_PERCENTILE']
product_summary['RANK'] = product_summary['HEALTHSCORE'].rank(ascending=False)
product_summary = product_summary.sort_values('HEALTHSCORE', ascending=False)
product_summary = product_summary[['STOCKCODE', 'QUANTITY', 'REVENUE', 'DESCRIPTION', 'HEALTHSCORE', 'RANK']]

##################################################################
##############       MARKET BASKET ANALYSIS          #############

# Filter popular products
popular_products = df['STOCKCODE'].value_counts()
popular_products = popular_products[popular_products >= 50].index
df_filtered = df[df['STOCKCODE'].isin(popular_products)]

basket_raw = df_filtered[['INVOICENO', 'STOCKCODE', 'QUANTITY']]
basket = basket_raw.pivot_table(index='INVOICENO', columns='STOCKCODE', values='QUANTITY', fill_value=0)
basket = basket.gt(0).astype(int)

# Co-occurrence matrix
co_occurrence = basket.T.dot(basket)
for col in co_occurrence.columns: #  Remove self-pairs
    co_occurrence.loc[col, col] = 0
co_occurrence = co_occurrence.reset_index()
co_occurrence_melted = co_occurrence.melt(id_vars='STOCKCODE', var_name='OTHER_PRODUCT', value_name='BOUGHT_TOGETHER')

top_pairs = co_occurrence_melted[top_pairs := co_occurrence_melted['BOUGHT_TOGETHER'] > 10].sort_values('BOUGHT_TOGETHER', ascending=False)

# Prepare descriptions
descriptions = df[['STOCKCODE', 'DESCRIPTION']].drop_duplicates('STOCKCODE')
descriptions_other = descriptions.rename(columns={'STOCKCODE': 'OTHER_PRODUCT', 'DESCRIPTION': 'DESCRIPTION_B'})
top_pairs = top_pairs.merge(descriptions, on='STOCKCODE')
top_pairs = top_pairs.rename(columns={'DESCRIPTION': 'DESCRIPTION_A'})
top_pairs = top_pairs.merge(descriptions_other, on='OTHER_PRODUCT')

top_pairs_final = top_pairs[['DESCRIPTION_A', 'DESCRIPTION_B', 'BOUGHT_TOGETHER']]
top_pairs_final['Product_A_Final'] = top_pairs_final[['DESCRIPTION_A', 'DESCRIPTION_B']].min(axis=1)
top_pairs_final['Product_B_Final'] = top_pairs_final[['DESCRIPTION_A', 'DESCRIPTION_B']].max(axis=1)
top_pairs_final['PAIR'] = top_pairs_final['Product_A_Final']+" - "+top_pairs_final['Product_B_Final']
top_pairs_final = top_pairs_final[['Product_A_Final', 'Product_B_Final', 'PAIR', 'BOUGHT_TOGETHER']]

# Remove duplicate pairs
top_pairs_final = top_pairs_final.drop_duplicates()
top_pairs_final = top_pairs_final.rename(columns={'Product_A_Final': 'DESCRIPTION_A','Product_B_Final': 'DESCRIPTION_B' })
top_pairs_final = top_pairs_final.sort_values('BOUGHT_TOGETHER', ascending=False)
print(top_pairs_final.head(10))


##################################################################
####################      RFM ANALYSIS       #####################

# Create Revenue column
df['REVENUE'] = df['QUANTITY'] * df['UNITPRICE']

# RFM Segmentation
df['INVOICEDATE'] = pd.to_datetime(df['INVOICEDATE'])
reference_date = df['INVOICEDATE'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CUSTOMERID').agg(
    LAST_PURCHASE=('INVOICEDATE', 'max'),
    FREQUENCY=('INVOICENO', 'nunique'),
    MONETARY=('REVENUE', 'sum')
).reset_index()

rfm['RECENCY'] = (reference_date - rfm['LAST_PURCHASE']).dt.days
rfm = rfm.drop(columns=['LAST_PURCHASE'])
rfm.columns = ['CUSTOMERID', 'RECENCY', 'FREQUENCY', 'MONETARY']

# Normalize using percentile rank
rfm['RECENCY_RANK'] = rfm['RECENCY'].rank(pct=True, ascending=True)
rfm['FREQUENCY_RANK'] = rfm['FREQUENCY'].rank(pct=True)
rfm['MONETARY_RANK'] = rfm['MONETARY'].rank(pct=True)

rfm['RFM_SCORE'] = rfm['RECENCY_RANK'] + rfm['FREQUENCY_RANK'] + rfm['MONETARY_RANK']

# Simple Customer Segment based on RFM_SCORE
def rfm_segment(score):
    if score >= 2.5:
        return 'VIP'
    elif score >= 2.0:
        return 'Frequent Buyer'
    elif score >= 1.5:
        return 'Potential Loyalist'
    else:
        return 'Lost Customer'

rfm['SEGMENT'] = rfm['RFM_SCORE'].apply(rfm_segment)

# Final RFM table
rfm_final = rfm[['CUSTOMERID', 'RECENCY', 'FREQUENCY', 'MONETARY', 'RFM_SCORE', 'SEGMENT']]


##########################################################################
########################### STEP 4: SERVING ##############################

# Save mini-analysis and upload tables back to Snowflake

success, nchunks, nrows, _ = write_pandas(
    conn=conn,
    df=product_summary,
    table_name='PRODUCT_SUMMARY_SF'
)

success, nchunks, nrows, _ = write_pandas(
    conn=conn,
    df=top_pairs_final,
    table_name='TOP_PAIRS_FINAL_SF'
)

success, nchunks, nrows, _ = write_pandas(
    conn=conn,
    df=rfm_final,
    table_name='CUSTOMER_RFM_SF'
)