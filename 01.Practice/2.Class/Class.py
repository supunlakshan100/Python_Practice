class PersonWithoutConstructor:
    name = ""
    age = ""


class PersonWithConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Using the class without a constructor
person1 = PersonWithoutConstructor()
person1.name = "Alice"
person1.age = 25

person2 = PersonWithoutConstructor()
person2.name = "Bob"
person2.age = 30

print(person1.name, person1.age)  # Output: Alice 25
print(person2.name, person2.age)  # Output: Bob 30

# Using the class with a constructor
person3 = PersonWithConstructor("Alice", 25)
person4 = PersonWithConstructor("Bob", 30)

print(person3.name, person3.age)  # Output: Alice 25
print(person4.name, person4.age)  # Output: Bob 30


# **********************************************************************************************************************

class Dog:
    name = "yh"
    bread = ""

    def set_name(self, name):
        self.name = name

    def bark(self, massage):  # massage is a parameter
        # self.name is a property
        msg = f"woof woof. My name is {self.name}. {massage}"
        print(msg)

    def walk(self):
        print("walking")


dog1 = Dog()  # dog1 is an object
dog1.name = "hsg"
dog1.set_name = "Scooby"
dog1.bark("Hi")

dog2 = Dog()
dog2.name = 'hhhh'
dog2.set_name = "droofy"
dog2.bark("Hello")

dog3 = Dog()
dog3.bark("gfd")
