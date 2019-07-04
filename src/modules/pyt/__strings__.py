print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """This is a multi line string,
multi line means,
it is written in multiple lines"""
print(a)

a = "Hello, World!"
print(a[1])

b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

quantity = 3
item_no = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, item_no, price))

