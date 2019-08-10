import ml.classify.data as loader
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.preprocessing import LabelEncoder

train_df, test_df = loader.load_titanic_data()
# print(train_df)
# print(test_df)


data = train_df
submit = test_df

lb = LabelEncoder()
data['Embarked'] = lb.fit_transform(data['Embarked'].astype(str))
data['Sex'] = lb.fit_transform(data['Sex'].astype(str))
data['Cabin'] = lb.fit_transform(data['Cabin'].astype(str))
data = data.fillna(data.median())

train = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin']]
target = data[['Survived']]
submit = submit[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin']]

decision_tree = DecisionTreeClassifier(random_state=10)
out = cross_val_score(decision_tree, train, target, cv=30).mean()
print(out)

