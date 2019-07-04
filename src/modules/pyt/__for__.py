fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 10, 2):
    print(x)

for x in range(6):
    print(x)
else:
    print("finally finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
