import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

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

# plt.show()
fig = plt.figure()
buf = BytesIO()
plt.savefig(buf, format='png')
print(type(buf.getvalue()))
buf.close()
