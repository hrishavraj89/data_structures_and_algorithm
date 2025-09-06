#Define a class Person with instance object variables name and age.
#Set Instance object variables in __init__() method. Also define
#show() method to display name and age of a person.

class Person:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name, self.age)

p1 = Person("Rahul", 24)
p1.show()