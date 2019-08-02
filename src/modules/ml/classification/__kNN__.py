import numpy as np
import operator
import matplotlib.pyplot as plt


def createDataSet():
    group1 = np.asarray([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels1 = ['A', 'A', 'B', 'B']
    return group1, labels1


def classify0(inX, dataset, labels, k):
    dataSetSize = dataset.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


group, labels = createDataSet()
print(group)
print(group[1:])
print(labels)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(group[1:0], group[2:0])
plt.show()

predicted_class = classify0([0, 0], group, labels, 3)
print(predicted_class)


