#!/usr/bin/env python3

# *args

def suma(*args):
    """
    Calculates the sum of a list of numbers.

    Args:
        args: A list of numbers.

    Returns:
        The sum of the numbers in the list.
    """

    return sum(args)

print(suma(3, 2, 3, 4, 5, 6, 3, 5))