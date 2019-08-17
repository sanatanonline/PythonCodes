import matplotlib.pyplot as plt

x = [3, 22, 3, 12, 234, 45, 56, 56, 78, 12, 45, 23, 45, 67]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(x, bins, histtype="step", rwidth=0.8)

plt.title("Histogram")
plt.xlabel("X-axis data")

plt.legend()

plt.show()
