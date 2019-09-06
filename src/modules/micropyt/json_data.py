import pandas as pd

housing = pd.read_csv('/opt/apps/ml-data/quant/housing/housing.csv')
meta_data = pd.DataFrame(housing.dtypes)
meta_data.reset_index()
meta_data['MissingVal'] = housing.isnull().sum()
print(meta_data)
print(meta_data.to_json())
