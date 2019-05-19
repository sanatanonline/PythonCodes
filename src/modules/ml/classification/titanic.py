import pandas as pd


# load the data from csv file
df = pd.read_csv('C:/view/opt/apps/code/local/ml-data/titanic/train.csv')

# print the data
print("Variables are:", list(df))
print("Total number of records", len(df))



