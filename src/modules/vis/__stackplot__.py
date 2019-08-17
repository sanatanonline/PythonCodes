import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

sleeping = [8, 6, 7, 6, 4, 6, 8]
working = [12, 12, 10, 9, 11, 10, 8]
playing = [2, 2, 3, 2, 1, 3, 3]

plt.plot([], [], color="b", label="sleeping", linewidth="2")
plt.plot([], [], color="r", label="working", linewidth="2")
plt.plot([], [], color="g", label="playing", linewidth="2")

plt.stackplot(days, sleeping, working, playing, colors=["b", "r", "g"])

plt.title("Stack Plot")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")

plt.legend()

plt.show()
