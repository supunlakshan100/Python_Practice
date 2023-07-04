# instance method- Pass the object as a frist parameter
# class method- Pass the class as a frist parameter
# static method- Don't pass the object or class as a frist parameter, it is a normal method'''

class Person:

    # class variable/attributes ,It is not a instance variable
    types = ['student', 'teacher', 'parent']
    name = "Unknown"

    def __init__(self, name):
        print("Hello from Person")
        self.name = name   # instance variable/attributes

    def print_name(self):  # In here cann't use cls, because it is a instance method
        print(type(self), self)
        print("Name is ", self.name)

    @classmethod  # Decorators, Use for access the class variable and give the long definition for the class variable
    def get_types(cls):  # In here cann't use self, because it is a class method
        print(type(cls), cls.name)
        return cls.types

    @staticmethod  # Not access the class variable and instance variable
    def get_person(name):
        print("Person type is", name)
        name = 'Niroshan'

    def get_age(today, dob):
        return today - dob


supun = Person("supun")  # Create a object

supun.print_name()  # Call the instance method
print(Person.types)  # Call the class variable
print(Person.get_types())  # Call the class method
supun.get_person()  # Call the static method
