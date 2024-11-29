#!/usr/bin/env python3

"""
This code defines a simple calculator class.

The class has five methods:

* `sum()` - adds two numbers
* `subtraction()` - subtracts two numbers
* `times()` - multiplies two numbers
* `division()` - divides two numbers

The `division()` method handles the case of division by zero by printing an error message.

The code also prints the results of calling each of the methods with different input values.
"""


class Calculator:
    """
    A simple calculator class.
    """

    def __init__(self) -> None:
        """
        The constructor does nothing.
        """
        pass

    @staticmethod
    def sum(valor1, valor2):
        """
        Adds two numbers.

        Args:
            valor1: The first number.
            valor2: The second number.

        Returns:
            The sum of the two numbers.
        """
        return valor1 + valor2

    @staticmethod
    def subtraction(valor1, valor2):
        """
        Subtracts two numbers.

        Args:
            valor1: The first number.
            valor2: The second number.

        Returns:
            The difference of the two numbers.
        """
        return valor1 - valor2

    @staticmethod
    def times(valor1, valor2):
        """
        Multiplies two numbers.

        Args:
            valor1: The first number.
            valor2: The second number.

        Returns:
            The product of the two numbers.
        """
        return valor1 * valor2

    @staticmethod
    def division(valor1, valor2):
        """
        Divides two numbers.

        Args:
            valor1: The dividend.
            valor2: The divisor.

        Returns:
            The quotient of the two numbers, or an error message if the divisor is zero.
        """
        if valor2 != 0:
            return valor1 / valor2
        else:
            return f"\n[!] Error: cannot divide by zero."


print(Calculator.sum(2, 8))  # 10
print(Calculator.subtraction(8, 4))  # 4
print(Calculator.times(8, 4))  # 32
print(Calculator.division(8, 0))  # Error: cannot divide by zero.
print(Calculator.division(8, 3))  # 2.6666666666666665
