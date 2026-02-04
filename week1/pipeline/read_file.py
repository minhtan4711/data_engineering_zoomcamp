import pandas as pd

# read a sample of data
path = 'data/yellow_tripdata_2021-01.csv.gz'
df = pd.read_csv(path, nrows=100)

# display the first rows
df.head()

# check the data types
df.dtypes

# check the data shape
df.shape
