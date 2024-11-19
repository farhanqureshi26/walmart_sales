import pandas as pd
import psycopg2
from sqlalchemy import create_engine
df = pd.read_csv('C:/Users/farha/OneDrive/Desktop/Project_walmart/walmart-10k-sales-datasets/Walmart.csv', encoding_errors='ignore')
df.shape
df.head(4)
df.describe()
df.info()
#all duplicates
df.duplicated().sum()
#removing all duplicates
df.drop_duplicates(inplace=True)
df.duplicated().sum()
df.shape
#finding null values
df.isnull().sum()
#dropping all rows with missing records
df.dropna(inplace=True)
#verify
df.isnull().sum()
df.shape
df.dtypes
#changing datatype of unit_price
df['unit_price'] = df['unit_price'].str.replace('$','').astype(float)
df.head()
df.info()
df.columns
df.columns = df.columns.str.lower()
df.columns
df['Total'] = df['unit_price'] * df['quantity']
#df['Total']
df.head()
