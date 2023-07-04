class Person:
    def __init__(self, name):
        self.__age = 25
        '''1st access modifier. It is "private"  access modifier.
        It can be access only in the class. It can't be access in the child class'''
        print('tharidu')

        self._city = "Badulla"
        '''2nd access modifier.It is "protected"  access modifier. It can be access only in the class and in the child class'''

        self.name = name
        # 3rd access modifier  public variable

    def _calculate_age(self):
        return 30

    def set_age(self, age=20):  # setter method, public method, use for set the private variable
        self.__age = age

    def get_age(self):  # getter method, public method, use for return the private variable
        return self.__age

    def sleep(self):
        print("sleeping", self.name)


class Student(Person):
    def __int__(self, name):
        super(Student, name).__init__(name)

    def _calculate_age(self):
        # this is the way to access the protected method in the parent class, overriding the method
        age = super()._calculate_age()
        return age-5

    def print_age(self):
        print("Age is", self.__age)

    def print_city(self):
        print(self._city)


supun = Student("supun")
supun.sleep()
# supun.set_age()
supun.__age = 29  # this will not change the age, because it is a private variable
# print("Name is", supun.name)
print("Age is", supun.get_age())
# print("Age is", supun.__age)

# supun.print_age()

supun.print_city()
print(supun._city)
'''this is the way to access the protected variable in the parent class, protected variable can be access in the out side. 
This is the exception in the protected variable.'''
