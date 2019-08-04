import ml.classify.kNN as kNN
import matplotlib.pyplot as plt

# kNN algorithm using sample data
group, labels = kNN.create_sample_data()
print(group)
print(group[1:])
print(labels)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(group[:1], group[:1])
plt.show()

predicted_class = kNN.classify_0([0, 0], group, labels, 3)
print(predicted_class)
