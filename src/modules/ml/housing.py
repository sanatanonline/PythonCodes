import ml.data as dt


housing = dt.load_housing_data()
housing.info()

print(housing["ocean_proximity"].value_counts())
print(housing.describe())

print(housing.shape)
print(housing.columns)

print(housing.head())
