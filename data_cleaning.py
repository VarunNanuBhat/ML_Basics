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
# set datatype for column
df['usn'] = df['usn'].astype(str)
# Ensure column contains only numerical data
# Print data frame with string values in sub_1_marks column
print(df)
df['sub_1_marks'] = pd.to_numeric(df['sub_1_marks'], errors='coerce')
# The string values should be replaced with Null values now.
print(df)

# Handling null values using isnull()
# isnull() will return True/False at each position.
print(df.isnull())
# isnull().sum() will return total count of null values in each column.
print(df.isnull().sum())
# isnull().any() will return boolean True/False if null values are present.
print(df.isnull().any())
# isna() method is similar to isnull()
print(df.isna())

# Filling the missing values
# Replace missing values with fixed/default value
#df['sub_1_marks'] = df['sub_1_marks'].fillna(0)
#print(df)
# Replace missing value with mean i.e., average value of column
#df['sub_1_marks'] = df['sub_1_marks'].fillna(df['sub_1_marks'].mean())
#print(df)
# Replace missing value with median i.e., middle value of column
#df['sub_1_marks'] = df['sub_1_marks'].fillna(df['sub_1_marks'].median())
#print(df)
# Replace missing value with mode i.e., most common value of column
# mode()[0] accesses the first mode value if there are more than 1 modes.
#df['sub_1_marks'] = df['sub_1_marks'].fillna(df['sub_1_marks'].mode()[0])
#print(df)
# Forward Fill: Use the last valid value to fill missing data.
#df['sub_1_marks'] = df['sub_1_marks'].fillna(method='ffill')
#print(df)
#Backward Fill: Use the next valid value to fill missing data.
df['sub_1_marks'] = df['sub_1_marks'].fillna(method='bfill')
#print(df)

# Removing duplicates
# get the total no of duplicate rows
print(df.duplicated().sum())

# Handling outliers
# Detect outliers
# import matplotlib for plotting graph data
import matplotlib
# For detecting outliers we need to plot a graph using boxplot to display spread of data
df[['sub_1_marks']].boxplot()
matplotlib.pyplot.show()


# Fix the outliers with max cap value as 100
df['sub_1_marks'] = df['sub_1_marks'].clip(upper=100)
df[['sub_1_marks']].boxplot()
matplotlib.pyplot.show()
print(df)



