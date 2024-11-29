#!/usr/bin/env python3

"""
This code defines a simple car class.

The class has three methods:

* `__init__()` - initializes the car's brand and model
* `sports()` - creates a new car object with the given brand and the model "sports"
* `sean()` - creates a new car object with the given brand and the model "sean"
* `__str__()` - returns a string representation of the car

The code also prints the results of calling each of the methods with different input values.
"""


class Car:
    """
    A simple car class.
    """

    def __init__(self, brand, model) -> None:
        """
        Initializes the car's brand and model.

        Args:
            brand: The car's brand.
            model: The car's model.
        """
        self.brand = brand
        self.model = model

    @classmethod
    def sports(cls, brand):
        """
        Creates a new car object with the given brand and the model "sports".

        Args:
            brand: The car's brand.

        Returns:
            The new car object.
        """
        return cls(brand, "sports")

    @classmethod
    def sean(cls, brand):
        """
        Creates a new car object with the given brand and the model "sean".

        Args:
            brand: The car's brand.

        Returns:
            The new car object.
        """
        return cls(brand, "sean")

    def __str__(self) -> str:
        """
        Returns a string representation of the car.

        Returns:
            A string representation of the car.
        """
        return f"The car brand is {self.brand} and the model is {self.model}"


sport = print(Car.sports("Ferrari"))  # Prints "The car brand is Ferrari and the model is sports"
sean = print(Car.sean("Toyota"))  # Prints "The car brand is Toyota and the model is sean"
