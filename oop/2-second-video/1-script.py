#!/usr/bin/env python3

# This class represents a rectangle with properties for width and height.

class Rectangle:

    def __init__(self, width, height) -> None:
        """
        This method initializes a Rectangle object with its width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def area(self):
        """
        This property calculates and returns the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.width * self.height

    def __str__(self) -> str:
        """
        This method defines how the object will be printed as a string.

        Returns:
            A string representation of the rectangle showing its width and height.
        """
        return f'\n[+] Properties of the rectangle: [Width: {self.width}][Height: {self.height}]'

    def __eq__(self, other):
        """
        This method checks if two Rectangle objects are equal.

        Args:
            other: Another Rectangle object.

        Returns:
            True if the Rectangle objects have the same width and height, False otherwise.
        """
        return self.width == other.width and self.height == other.height

# Create two rectangle objects with the same width and height.

rect2 = Rectangle(20, 80)
rect1 = Rectangle(20, 80)

# Print the string representation of the first rectangle.

print(rect1)

# Print the area of the first rectangle using its property.

print(f'\n[+] The area is {rect1.area}')

# Check if the two rectangles are equal and print the result.

print(f'Are they equal? -> {rect1 == rect2}')