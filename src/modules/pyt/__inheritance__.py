class Person:
    def __init__(self, f_name, l_name):
        print("parent test is called")
        self.f_name = f_name
        self.l_name = l_name

    def tell_my_name(self):
        return "My name is " + self.f_name + " " + self.l_name


x = Person("John", "Doe")
(x.tell_my_name())


class Student(Person):
    def __init__(self, f_name, l_name, age):
        print("child test is called")
        Person.__init__(self, f_name, l_name)
        self.age = age

    def tell_my_name(self):
        return "My name is " + self.f_name + " " + self.l_name + ". My age is ", self.age


x = Student("Mike", "Doe", 36)
print(x.tell_my_name())
