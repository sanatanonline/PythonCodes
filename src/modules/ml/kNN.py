import numpy as np
import operator


def create_sample_data():
    group1 = np.asarray([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels1 = ['A', 'A', 'B', 'B']
    return group1, labels1


def classify_0(inX, dataset, labels, k):
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




