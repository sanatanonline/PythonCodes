fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)
print(type(fruit_list))

fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))

print(fruits[2])

# changing anf item is not allowed
# fruits[0] = "mango"

for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("apple is there in fruits")
else:
    print("apple is not in the fruits")

print(len(fruits))

alpha_num = tuple(("a", "b", "c", "1", "2", "3"))
print(alpha_num)
