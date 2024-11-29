#!/usr/bin/env python3

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclasses must implement this method')


class Cat(Animal):
    def speak(self):
        return f'Meow!'


class Dog(Animal):
    def speak(self):
        return f'Woof!'


# Polymorphism
def make_speak(object):
    print(f"{object.name} says {object.speak()}")


cat = Cat("Firulais")
dog = Dog("Alfredo")

make_speak(cat)
make_speak(dog)
