import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# LOAD DATA FROM FILE

# load the data from csv file
df = pd.read_csv('../../data/parkinsons_updrs.csv')

# print the data
print("Variables are:", list(df))
print("Total number of records", len(df))

# PREPARE THE TRAINING SET AND TEST SET

# Split the data to training set and test set

# train set 80%
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
print("Total number of records", len(train))

# test set 20%
test = df[~msk]
print("Total number of records", len(test))

# EXPLORATORY DATA ANALYSIS

# Scatter plot (motor_UPDRS - Jitter)
plt.scatter(train.Jitter, train.motor_UPDRS, marker='o')
# plt.show()

# LINEAR MODEL

# prepare training data
train_x1 = np.asarray(train.Jitter.values)
train_y = np.asarray(train.motor_UPDRS.values)

# prepare test data
test_x1 = np.asarray(test.Jitter.values)
test_y = np.asarray(test.motor_UPDRS.values)

# initialize the linear regr model
linear = linear_model.LinearRegression()

# TRAINING

# train the model
linear.fit(train_x1, train_y)

# VALIDATION

# predict the test set
predictions = linear.predict(test_x1)


# MODEL EVALUATION

# coefficients
print('Coefficients: \n', linear.coef_)
# mse
print("Mean Squared Error: \n %.2f"
      % mean_squared_error(predictions, test_y))
# variance score: 1 is perfect prediction
print('Variance Score: \n %.2f' % r2_score(test_y, predictions))

# plot the outputs
plt.scatter(test_x1, test_y, marker='o')
plt.scatter(test_x1, predictions, marker='x')

plt.show()
