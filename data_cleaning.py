# Import Pandas library
import pandas as pd
# load CSV data into dataframe
df = pd.read_csv('data.csv')

# Rename columns to a common syntax
# Print column names before changing
print(df.columns)
df.columns = df.columns.str.lower().str.replace(' ', '_')
# Print column names after changing
print(df.columns)

Set


# Handling null values using isnull()
# isnull() will return True/False at each position.
print(df.isnull())
# isnull().sum() will return total count of null values in each column.
print(df.isnull().sum())
# isnull().any() will return boolean True/False if null values are present.
print(df.isnull().any())

print(df.isna().any())