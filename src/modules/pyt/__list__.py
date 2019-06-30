fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[2])
print(len(fruits))

fruits[1] = "mango"
print(fruits)

for fruit in fruits:
    print(fruit)

if "gold" in fruits:
    print("gold is a fruit")
else:
    print("gold is not a fruit")

fruits.append("orange")
print(fruits)

fruits.insert(2, "pineapple")
print(fruits)

new_fruits = fruits.copy()

fruits.remove(fruits[2])
print(fruits)

fruits.pop()
print(fruits)

del fruits[0]
print(fruits)

fruits.clear()
print(fruits)

print(new_fruits)
new_list = list(new_fruits)
print(new_list)

alphabets = list(["a", "b"])
print(alphabets)

mixed_list = list(("a", "b", 1, 2))
print(mixed_list)

for x in mixed_list:
    print(type(x))
