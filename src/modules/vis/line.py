import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

x1 = [1, 2, 3]
y1 = [4, 3, 1]

x2 = [1, 2, 3]
y2 = [2, 4, 1]

plt.plot(x1, y1, "g", label="Line1", linewidth=2)
plt.plot(x2, y2, "c", label="Line2", linewidth=2)

plt.title("Information")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.legend()
plt.grid(True, color="k")

plt.show()
