import matplotlib.pyplot as plt

x1 = ["red", "blue", "green", "orange", "yellow"]
y1 = [5, 2, 7, 8, 2]

x2 = ["red", "blue", "green", "orange", "yellow"]
y2 = [8, 6, 2, 5, 6]

plt.bar(x1, y1, label="Bar1")
plt.bar(x2, y2, label="Bar2", color="g")

plt.title("Bar Graph")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.legend()

plt.show()

