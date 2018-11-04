from numpy import *


def create_data_set():
    group1 = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels1 = ['A', 'A', 'B', 'B']
    return group1, labels1


group, labels = create_data_set()
print(group)
print(labels)
