# Import Pandas library
import pandas as pd
dataframe_csv = pd.read_csv('data.csv')
# Print dataframe created using CSV data
print(dataframe_csv)

# Reading JSON data
dataframe_json = pd.read_json('data.json')
# Print dataframe created using Json data
print(dataframe_json)

# Print the first 3 rows of dataframe
dataframe = pd.read_csv('data.csv')
# Print first 3 rows
print(dataframe.head(3))
# To print first 5 rows
print(dataframe.head())


