import pandas as pd


def load_titanic_data():
    train_df = pd.read_csv('C:/view/opt/apps/ml-data/classify/titanic/train.csv')
    test_df = pd.read_csv('C:/view/opt/apps/ml-data/classify/titanic/test.csv')
    return train_df, test_df


load_titanic_data()
