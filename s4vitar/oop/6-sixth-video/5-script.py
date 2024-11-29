#!/usr/bin/env python3

# Define a class called "Caja" (Box)
class Box:

    # Constructor for the class
    def __init__(self, *items):
        # Store the items passed to the constructor in a list named "items"
        self.items = items

    # Define a magic method to determine the length of the box
    def __len__(self):
        # Return the length of the list of items (number of items in the box)
        return len(self.items)

# Create an instance of the "Caja" class
caja = Box("apple", "banana", "kiwi", "pear", "peach")

# Print the length of the box (number of items) using the magic method
print(caja.__len__())