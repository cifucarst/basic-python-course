#!/usr/bin/env python3


def recursive(number):
    """
    This function takes an integer 'number' as input and recursively prints 
    the numbers from 'number' to 5.

    Args:
        number: An integer representing the starting number for the recursion.

    Returns:
        The value 5, but this doesn't affect the printed output. 
    """

    print(number)  # Print the current value of number
    if number < 5:
        recursive(number + 1)  # Call the function recursively with incremented number
    else:
        return 5  # Unnecessary return statement, function already reached base case

recursive(1)  # Call the recursive function with starting value 1
