#!/usr/bin/env python3

class Person:
    """
    Represents a person with a name and age.

    Attributes:
        name: The person's name (string).
        age: The person's age (integer).
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a Person object with the given name and age.

        Args:
            name: The name of the person (string).
            age: The age of the person (integer).
        """
        self.name = name
        self.age = age

    def presentation(self) -> None:
        """
        Prints a greeting message introducing the person.
        """
        print(f"Hello I'm {self.name} and I'm {self.age} years old.")

# Create a Person object named "marcelo" with name "Marcelo" and age 28
marcelo = Person("Marcelo", 28)

# Call the presentation method to introduce "marcelo"
marcelo.presentation()
