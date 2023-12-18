#!/usr/bin/env python3

class Animal:
    # constructor method
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    # description method
    def description(self):
        print(f"{self.name} is a {self.animal_type}")


# instantiate the class
cat = Animal("Tijuana", "Cat")
dog = Animal("Pancho", "Dog")

# call the description method
cat.description()
dog.description()