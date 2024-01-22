#!/usr/bin/env python3

"""
This code demonstrates inheritance and method overriding in Python.

- Class `A`: Defines a base class with a `greet()` method that returns a simple greeting message.
- Class `B`: Subclasses `A` and overrides the `greet()` method to:
    - Call the `greet()` method from the parent class using `super()` to get the original greeting.
    - Combine the original greeting with an additional message specific to `B`.
    - Return the combined greeting message.

Running the code creates an instance of `B` and calls its `greet()` method, resulting in a greeting message that includes both the base class and subclass greetings.
"""


class A:
    """
    Base class with a simple `greet()` method.

    Methods:
        greet(): Returns a basic greeting message.
    """

    def greet(self):
        """
        Returns a basic greeting message.

        Returns:
            str: The greeting message.
        """
        return f"Greetings from A"


class B(A):
    """
    Subclass of `A` that overrides the `greet()` method.

    Methods:
        greet(): Combines the base class greeting with an additional message specific to `B`.

    """

    def greet(self):
        """
        Combines the base class greeting with an additional message specific to `B`.

        Returns:
            str: The combined greeting message.
        """
        original_greeting = super().greet()  # Call the `greet()` method from the parent class
        return f"{original_greeting}, but also greetings from B"


# Create an instance of `B`
greeting = B()

# Call the `greet()` method and print the result
print(greeting.greet())