import matplotlib.pyplot as plt

slices = [3, 5, 1]
activities = ["sleeping", "working", "playing"]
color_codes = ["r", "g", "b"]

plt.plot([], [], color="b", label="sleeping", linewidth="2")
plt.plot([], [], color="r", label="working", linewidth="2")
plt.plot([], [], color="g", label="playing", linewidth="2")

plt.pie(slices, labels=activities, colors=color_codes, startangle=90, shadow=False, explode=(0, 0, 0),
        autopct='%1.1f%%')

plt.title("Pie Plot")

plt.show()
