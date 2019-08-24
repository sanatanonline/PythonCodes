import pandas as pd


def load_titanic_data():
    train_df = pd.read_csv('/opt/apps/ml-data/class/titanic/train.csv')
    test_df = pd.read_csv('/opt/apps/ml-data/class/titanic/test.csv')
    return train_df, test_df


def load_forestfires_data():
    forestfires = pd.read_csv('/opt/apps/ml-data/quant/forestfires/forestfires.csv')
    return forestfires


load_titanic_data()

load_forestfires_data()
