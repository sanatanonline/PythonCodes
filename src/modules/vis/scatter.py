import matplotlib.pyplot as plt

x1 = [3, 5, 4, 7, 3]
y1 = [5, 2, 7, 8, 2]

x2 = [3, 5, 4, 7, 3]
y2 = [8, 6, 2, 5, 6]

plt.scatter(x1, y1, label="first set", color="b")
plt.scatter(x2, y2, label="second set", color="r")

plt.title("Scatter Plot")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.legend()

plt.show()
