class MyFristClass:
     name='unknown' # attributes,variables
     bread='unknown'
     
     def bark(self,message): # method ,function,behaviour,action 
         '''self pass the object of the class to the function ''' #docstring
         print('inside')
        #  print(type(x),x) 
         print('woof!')

dog1 = MyFristClass() # create an object ,instance of the class

dog1.name = 'Tommy' # add attributes to the object, name is the parameter of the attribute
# dog1.age = 5
# dog1.breed = 'Labrador'
print(dog1.name)
print('outside',dog1)

dog1.bark('hello')