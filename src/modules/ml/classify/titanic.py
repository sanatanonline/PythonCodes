import pandas as pd

import ml.classify.data as dt

train, test = dt.load_titanic_data()

# check the shape of the datasets
print(train.shape)
print(test.shape)

# set the index to passengerId
train = train.set_index('PassengerId')

# identify data types of the 11 columns, add the stats to the datadict
datadict = pd.DataFrame(train.dtypes)
# print(datadict)

# identify missing values of the 11 columns,add the stats to the datadict
datadict['MissingVal'] = train.isnull().sum()
# print(datadict)

# Identify number of unique values, For object nunique will the number of levels
# Add the stats the data dict
datadict['NUnique'] = train.nunique()
# print(datadict)

# Identify the count for each variable, add the stats to datadict
datadict['Count'] = train.count()
# print(datadict)
# print(datadict.to_json(orient="table"))

# rename the 0 column
datadict = datadict.rename(columns={0: 'DataType'})
print(datadict)
print(datadict.shape)


# get descriptive statistics on "object" datatypes
# print(train.describe(include=['object']))

# get descriptive statistics on "number" datatypes
# print(train.describe(include=['number']))

# print(train.Survived.value_counts(normalize=True))
