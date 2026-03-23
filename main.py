# OOP
from pyscript import document, display

class Section:# creating the class
    def __init__(self, numstudents, name, level, adviser,):
        self.numstudents = numstudents #attributes
        self.name = name #attributes
        self.level = level #attributes
        self.adviser = adviser  #attributes

# Instantiating an object
section1 = Section(24, 'Topaz', 10, 'Sir Cortez')
section2 = Section(25, 'Sapphire', 10, 'Sir de Guzman')

display(f'{section1.level}-{section1.name} is part of Red Bulldogs', target='output')
display(f'{section2.level}-{section2.name} is part of Green Hornets', target='output')

class Dog:
    def __init__(self, breed, age, name, owner):
        self.breed = breed
        self.age = age
        self.name = name
        self.owner = owner

    def bark(self):
        display('Arf'*3, target='output')

dog1 = Dog('Shih tzu', 2, 'Theo', 'Bea')
dog1.bark()
dog2 = Dog('American Bully', 1, 'Marie', 'Skyler')

display(f'{dog1.name} is owned by {dog1.owner}', target='output')

# creating a child class
class GermanShepherd(Dog):
    pass

dog1 = GermanShepherd('German Shepherd', 10, 'Jack', 'Simran')

display(f'{dog1.name} is owned by {dog1.owner}', target='output')


class user(Dog):
    pass

def user_input(e):
    breed = document.getElementById('input1').value
    age = document.getElementById('input2').value
    name = document.getElementById('input3').value
    owner = document.getElementById('input4').value

    dog1 = Dog(breed, age, name, owner)
    display(f'{dog1.name} is a {dog1.breed} owned by {dog1.owner}; the dog is {dog1.age} years old.', target='output2')
        
        

