#!/usr/bin/env python3

"""
This code defines a simple hierarchy of classes for representing vehicles.

- `Vehicle`: The base class representing any kind of vehicle with attributes `brand` and `model`.
- `Car`: A subclass of `Vehicle` specifically representing cars.
- `Motorcycle`: Another subclass of `Vehicle` specifically representing motorcycles.

Each vehicle can be described using the `describe()` method.
"""


class Vehicle:
    """
    Represents a generic vehicle with brand and model attributes.

    Attributes:
        brand (str): The vehicle's brand or manufacturer.
        model (str): The vehicle's specific model name.
    """

    def __init__(self, brand: str, model: str) -> None:
        """
        Initializes the vehicle with its brand and model.

        Args:
            brand (str): The vehicle's brand or manufacturer.
            model (str): The vehicle's specific model name.
        """
        self.brand = brand
        self.model = model

    def describe(self) -> str:
        """
        Returns a descriptive string representation of the vehicle.

        Returns:
            str: A string describing the vehicle's brand and model.
        """
        return f"\n[+] Vehicle: {self.brand} {self.model}"


class Car(Vehicle):
    """
    Represents a specific type of vehicle: a car.

    Inherits attributes and methods from the `Vehicle` class.
    """

    def describe(self) -> str:
        """
        Overrides the `describe()` method to explicitly identify the vehicle as a car.

        Returns:
            str: A string describing the car's brand and model.
        """
        return f"Car: {self.brand} {self.model}"


class Motorcycle(Vehicle):
    """
    Represents another specific type of vehicle: a motorcycle.

    Inherits attributes and methods from the `Vehicle` class.
    """

    def describe(self) -> str:
        """
        Overrides the `describe()` method to explicitly identify the vehicle as a motorcycle.

        Returns:
            str: A string describing the motorcycle's brand and model.
        """
        return f"Motorcycle: {self.brand} {self.model}"


# Polymorphism: describe any vehicle using the same function
def describe_vehicle(vehicle):
    """
    Prints a description of any vehicle object passed in.

    Args:
        vehicle (Vehicle): Any object of type `Vehicle` or its subclasses.
    """
    print(vehicle.describe())


# Create some vehicle objects
car = Car("Toyota", "corolla")
motorcycle = Motorcycle("Honda", "CBR")

# Describe the vehicles using the same function
describe_vehicle(car)
describe_vehicle(motorcycle)
