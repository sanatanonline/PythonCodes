import pandas as pd


# LOAD DATA FROM FILE

# load the data from csv file
df = pd.read_csv('/opt/apps/code/ml-data/train.csv')

# print the data
print("Variables are:", list(df))
print("Total number of records", len(df))



