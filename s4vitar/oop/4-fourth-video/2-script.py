#!/usr/bin/env python3

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.

    Attributes:
        number: The initial number used for calculations (integer).
    """

    def __init__(self, number: int) -> None:
        """
        Initializes the calculator with a starting number.

        Args:
            number: The initial number to use for calculations (integer).
        """
        self.number = number

    def sum(self, another_number: int) -> int:
        """
        Adds another number to the calculator's current number.

        Args:
            another_number: The number to add to the current number (integer).

        Returns:
            The sum of the current number and the provided number (integer).
        """
        return self.number + another_number

    def double_sum(self, num1: int, num2: int) -> None:
        """
        Performs two separate sums using the calculator's current number and
        two provided numbers, then prints the results.

        Args:
            num1: The first number to add to the current number (integer).
            num2: The second number to add to the current number (integer).

        Returns:
            None (prints the results of the two sums).
        """
        first_sum = self.sum(num1)
        second_sum = self.sum(num2)
        print(f"The sum of {self.number} and {num1} is: {first_sum}")
        print(f"The sum of {self.number} and {num2} is: {second_sum}")

# Create a calculator object with an initial number of 5
calc = Calculator(5)

# Print the sum of the calculator's number and 8
print(f"The sum of {calc.number} and 8 is: {calc.sum(8)}")

# Perform two sums using the calculator's number and print the results
calc.double_sum(2, 9)