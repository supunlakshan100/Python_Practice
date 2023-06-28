class Person:

    # Constructor
    def __init__(self, name, age, Hometown):
        self.name = name
        self.age = age
        self.Hometown = Hometown

    def introduce(self):
        print(
            f"Hi, my name is {self.name} and I am {self.age} years old and I'm from {self.Hometown}.")


# Creating instances
person1 = Person("Sudantha", 25, 'Buththala')  # object
person2 = Person("Tharidu", 30, 'Badulla')
person3 = Person("dantha", 28, 'thalawa')

# Calling the introduce method
person1.introduce()  # Output: Hi, my name is Alice and I am 25 years old.
person2.introduce()  # Output: Hi, my name is Bob and I am 30 years old.
person3.introduce()
