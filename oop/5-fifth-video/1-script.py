#!/usr/bin/env python3

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def speak(self):
        raise NotImplementedError('Defined subclasses must implement this method')


class Cat(Animal):
    def speak(self):
        return f'{self.name} says Miau!'
    
class Dog(Animal):
    def speak(self):
        return f'{self.name} says wau!'
       
        
cat = Cat("Firulais")
dog = Dog("Alfredo")
print(cat.speak())
print(dog.speak())

# jump an error NotImplementedError 
cat2 = Animal("Mimi")
print(cat2.speak())