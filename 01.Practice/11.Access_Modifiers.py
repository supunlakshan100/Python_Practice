class person:
    def __init__(self, name):
        self.name = name
        self.__age = 25  # private variable, 1st access modifier

    def set_age(self, age):  # setter method
        self.__age = age

    def get_age(self):  # getter method
        return self.__age

    def sleep(self):
        print("sleeping", self.name)


supun = person("supun")
supun.sleep()
supun.set_age(30)
supun.__age = 29  # this will not change the age, because it is a private variable
print("Name is", supun.name)
print("Age is", supun.get_age())
print("Age is", supun.__age)
