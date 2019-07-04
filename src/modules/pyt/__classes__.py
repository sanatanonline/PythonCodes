class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        print("init is called")
        self.name = name
        self.age = age

    def tell_my_name(self):
        return "Hello, my name is " + self.name


p1 = Person("John", 36)
print(p1.age)
print(p1.name)
greetings = p1.tell_my_name()
print(greetings)


