class Animal:
    def __init__(self, breed):
        self.breed = breed
        print('Hello from Animal')

    def talk(self):
        print("Animal is talking...")

    def move(self):
        print("Animal is moving....")


class Memal:
    def __init__(self):
        print('Hello from Memal')

    def feed(self):
        print("Drinking milk...")


class cat(Animal, Memal):
    def __init__(self):
        pass


class Dog(Animal, Memal):
    def __init__(self, name='unknown', breed='unknown'):
        # super() is used to call the parent class constructor, overriding the parent class constructor
        super().__init__(breed)
        # calling the Memal parent class constructor, overriding the parent class constructor
        Memal.__init__(self)
        print("supun")
        self.name = name

    def set_name(self, name):
        self.name = name

    # overriding the parent class method

    def talk(self):
        print("Dog is talking...")
        super().talk()  # super() is used to call the parent class method, otherwise we can use super(Dog, self).talk()

    def bark(self, message):
        msg = f"woof woof. My name is {self.name}. {message}"
        print(msg)

    '''    def feed(self):
        print("Drinking juice ...")
        super().feed()'''

    def walk(self):
        print("Walking...")


dog1 = Dog("Scooby")
# dog1.talk()
dog1.feed()

'''dog2 = Dog()
dog2.bark("Hello")'''
