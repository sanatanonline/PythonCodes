import pandas as pd

import ml.classify.data as dt

df = dt.load_forestfires_data()

# check the shape of the dataset
print(df.shape)