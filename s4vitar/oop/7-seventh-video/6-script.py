#!/usr/bin/env python3


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # Getter
    def radius(self):
        return self._radius

    @property  # Getter
    def diameter(self):
        return 2 * self._radius

    @property  # Getter
    def area(self):
        return 3.1415 * (self.radius ** 2)

    @radius.setter  # Setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be a positive number!")


c = Circle(5)  # Create a circle with radius 5
print(c.radius)  # Print the circle's radius (5)
print(c.diameter)  # Print the circle's diameter (10)
print(round(c.area, 2))  # Print the circle's area, rounded to 2 decimal places (≈78.54)

print()  # New line for separation

c.radius = 10  # Set the circle's radius to 10

print(c.radius)  # Print the updated radius (10)
print(c.diameter)  # Print the updated diameter (20)
print(round(c.area, 2))  # Print the updated area, rounded to 2 decimal places (≈314.16)