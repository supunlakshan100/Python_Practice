'''Encapsulation is one of the fundamental concepts of object-oriented programming. 
It refers to the bundling of data and methods together within a class, where the data is 
hidden or protected from direct access by external code. Encapsulation helps in achieving 
data abstraction and provides control over access to the class's internal data.

In the provided code, encapsulation is demonstrated through the use of private variables 
and accessor methods (getters and setters):
'''


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25  # private variable

    def set_age(self, age):  # setter method
        self.__age = age

    def get_age(self):  # getter method
        return self.__age

    def sleep(self):
        print("Sleeping", self.name)


'''Here, the __age variable is defined with double underscores (__age), making it a private variable. 
It indicates that the variable is intended to be accessed and modified only within the class itself. 
The private variable __age is encapsulated within the Person class.
To access or modify the private variable __age, the class provides accessor methods (get_age() and set_age(age)) which 
encapsulate the interaction with the private variable.
The set_age() method allows setting a new value for __age, and the get_age() 
method returns the current value of __age. By encapsulating the access to the private variable through these methods, 
the class maintains control over the integrity and manipulation of the __age attribute.
Using encapsulation, the code ensures that the private __age variable can only be accessed and modified through the 
defined setter and getter methods. This protects the data from unintended modifications or direct access from external code.

'''

supun = Person("Supun")
supun.set_age(30)
print("Name is", supun.name)
print("Age is", supun.get_age())

'''The set_age(30) method sets the __age attribute to 30, and the get_age() method retrieves and returns the value of __age. This encapsulated approach allows controlled access to the private variable, promoting data abstraction and maintaining the class's internal integrity.
Attempting to access the private variable directly (supun.__age) will create a new instance variable __age in the object, 
instead of modifying the private variable. Thus, it is important to use the provided accessor methods to interact with 
encapsulated data, as demonstrated in the code.
'''
