import pandas as pd

# load the data from csv file
df = pd.read_csv('/opt/apps/ml-data/class/titanic/train.csv')

# print the data
features = list(df)
number_of_records = len(df)
print("Variables are:", features)
print("Total number of records", number_of_records)



