import pandas as pd


def load_titanic_data():
    train_df = pd.read_csv('/opt/apps/ml-data/classify/titanic/train.csv')
    test_df = pd.read_csv('/opt/apps/ml-data/classify/titanic/test.csv')
    features = list(train_df)
    number_of_records = len(train_df)
    print("Variables are:", features)
    for f in features:
        print(train_df[f].dtype)
    print("Total number of records:", number_of_records)
    return train_df, test_df

load_titanic_data()
