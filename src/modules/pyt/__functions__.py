def print_name(a_name="Sanatan"):
    print("Hi " + a_name)


print_name("John")
print_name()


def print_list(fruits1):
    for x in fruits1:
        print_name(x)


fruits = ["apple", "banana", "cherry"]
print_list(fruits)


def func_mul(x = 1):
    return x * 5


print(func_mul(10))
print(func_mul(4))


def func_recursion(num):
    res = "one"
    if num > 0:
        print(num)
        num = num - 1
        func_recursion(num)
    else:
        print("else called")
        res = "two"
    return res


val = func_recursion(6)
print(val)
