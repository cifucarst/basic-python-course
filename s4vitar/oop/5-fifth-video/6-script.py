#!/usr/bin/env python3

"""
This code demonstrates inheritance and constructor calls in Python.

- Class `A`: Defines a base class with an attribute `x` and a constructor that prints the value of `x`.
- Class `B`: Subclasses `A` and adds another attribute `y`. Its constructor calls the `super()` method to initialize the inherited attribute `x` from `A` and then prints the value of `y`.

Running the code creates an instance of `B` and prints the values of both `x` and `y`.
"""


class A:
    """
    Base class with an attribute `x`.

    Attributes:
        x (int): The value stored in the attribute.
    """

    def __init__(self, x: int) -> None:
        """
        Initializes the `x` attribute and prints its value.

        Args:
            x (int): The initial value for the `x` attribute.
        """
        self.x = x
        print(f'value in x: {self.x}')


class B(A):
    """
    Subclass of `A` with an additional attribute `y`.

    Attributes:
        x (int): Inherited from `A`.
        y (int): The value stored in the attribute.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes the `x` and `y` attributes and prints their values.

        Args:
            x (int): The initial value for the inherited `x` attribute.
            y (int): The initial value for the `y` attribute.
        """
        super().__init__(x)  # Call the `A` constructor to initialize `x`
        self.y = y
        print(f'value in y: {self.y}')


# Create an instance of `B` with specific values for `x` and `y`
b = B(2, 10)

# Output shows the values of both `x` and `y`
"""
value in x: 2
value in y: 10
"""
