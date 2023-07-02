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
