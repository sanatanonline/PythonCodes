fruits = {"banana", "apple", "cherry"}
print(fruits)
print(type(fruits))

for fruit in fruits:
    print(fruit)

if "mango" in fruits:
    print("mango is in fruits")
else:
    print("mango is not in fruit")

fruits.add("orange")
print(fruits)

fruits.update(["grapes"])
print(fruits)

print(len(fruits))

fruits.remove("orange")
print(fruits)
# fruits.remove("orange")
fruits.discard("orange")

fruits.pop()
print(fruits)

alpha_num = set(("a", "b", "c", "1", "2", "3"))
print(alpha_num)
alpha_num.clear()
print(alpha_num)
