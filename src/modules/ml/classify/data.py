import pandas as pd


def load_titanic_data():
    t_df = pd.read_csv('/opt/apps/ml-data/classify/titanic/train.csv')
    features = list(t_df)
    number_of_records = len(t_df)
    print("Variables are:", features)
    print("Total number of records:", number_of_records)
    return t_df



