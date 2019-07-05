price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

quantity = 3
item_no = 567
price = 49
my_order = "I want {} pieces of item number {} for {:.2f} dollars."
print(my_order.format(quantity, item_no, price))

my_order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(my_order.format(quantity, item_no, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

my_order = "I have a {car_name}, it is a {model}."
print(my_order.format(car_name="Ford", model="Mustang"))
