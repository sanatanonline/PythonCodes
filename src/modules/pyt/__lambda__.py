x = lambda a: a + 5
print(type(x))
print(x(5))

x = lambda a, b, c: a + b + c
print(x(2, 3, 4))


def my_func(n):
    return lambda a: a * n


my_doubler = my_func(2)
print(my_doubler)

print(my_doubler(11))


def mul_func(n):
  return lambda a : a * n


my_doubler = mul_func(2)
my_tripler = mul_func(3)

print(my_doubler(11))
print(my_tripler(11))
