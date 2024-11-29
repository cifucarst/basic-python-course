#!/usr/bin/env python3

class Animal:
    def __init__(self, name, species) -> None:
        # Constructor to initialize an animal with a name, species, and set it as not fed
        self.name = name
        self.species = species
        self.fed = False

    def feed(self):
        # Method to mark the animal as fed
        self.fed = True

    def sell(self):
        # Method to mark the animal as not fed (sold)
        self.fed = False

    def __str__(self) -> str:
        # Special method to provide a string representation of the animal
        return f'{self.name}({self.species}) - {"Fed" if self.fed else "Hungry"}'
        

class AnimalStore:
    def __init__(self, name) -> None:
        # Constructor to initialize an animal store with a name and an empty list of animals
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        # Method to add an animal to the store
        self.animals.append(animal)

    def show_animals(self):
        # Method to display information about each animal in the store
        for animal in self.animals:
            print(animal)

    def feed_animals(self):
        # Method to feed all animals in the store
        for animal in self.animals:
            animal.feed()

    def sell_animal(self, name):
        # Method to sell (remove) a specific animal from the store based on its name
        for animal in self.animals:
            if animal.name == name:
                animal.sell()
                self.animals.remove(animal)
                return
        

if __name__ == '__main__':
    # Test the functionality of the animal store

    pet_store = AnimalStore('My Pet Store')

    cat = Animal('Tijuana', 'Cat')
    dog = Animal('Juan', 'Dog')

    pet_store.add_animal(cat)
    pet_store.add_animal(dog)

    pet_store.show_animals()
    pet_store.feed_animals()

    print(f'\n[+] Showing the animals after they have been fed:\n')

    pet_store.show_animals()
    pet_store.sell_animal('Tijuana')

    print(f'\n[+] Showing the animals after Tijuana has been sold:')
    pet_store.show_animals()