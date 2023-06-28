'''class Supun: # Blueprint of entity
    pass


field = Supun() # Instance, create object

field.name = "Machine Learning"  # Parameters , attributes
field.subparts = "Deep Learning"

print(field.name, field.subparts)
'''


class Dog:
    name = ""
    bread = ""

    def bark(self, message):  # self is a reference to the current instance of the class, method
        print("bark bark bark", message)


dog1 = Dog()


dog1.name = "perera"
dog1.bread = "John"

print(dog1.name, dog1.bread)

dog1.bark('Gotha pala')  # calling the method


dog2 = Dog()

dog2.age = 56
dog2.name = "Kamal"

print(dog2.name)
