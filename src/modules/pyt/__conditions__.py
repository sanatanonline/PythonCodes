x = 33
y = 200

if x > y:
    print("33 is greater than 200")
else:
    print("33 is less than 200")

a = 33
b = 3
c = 40
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")


print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

if c > a > b:
    print("Both conditions are True")
