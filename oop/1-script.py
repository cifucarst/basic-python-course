#!/usr/bin/env python3

class Person:
    # constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # greeting method
    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# instantiate the class
marcelo = Person("Marcelo", 28)
print(marcelo.greeting())

juan = Person("Juan", 21)
print(juan.greeting())