# Import Pandas library
import pandas as pd
# load CSV data into dataframe
df = pd.read_csv('data.csv')
# Info method can be used to get the high level information
print(df.info())

# describe method can be used to get statistical information
print(df.describe())

# Get the statistical information for all the columns
print(df.describe(include="all"))
