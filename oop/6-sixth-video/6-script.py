#!/usr/bin/env python3

# Define a class called "Pizza"
class Pizza:

    # Constructor for the class
    def __init__(self, size, *ingredients):
        # Store the size of the pizza in centimeters in "self.size"
        self.size = size
        # Store the list of ingredients in "self.ingredientes"
        self.ingredients = ingredients

    # Define a method called "descripcion" (description)
    def description(self):
        # Join the list of ingredients with commas and a space between them
        ingredient_string = ", ".join(self.ingredients)
        # Print a description of the pizza using the size and ingredients
        print(f'This pizza has {self.size} cm in diameter and includes the following ingredients: {ingredient_string}')

# Create a "Pizza" object
pizza = Pizza(12, "chorizo", "bacon", "cheese", "onion")

# Call the "descripcion" method to print the pizza's description
pizza.description()