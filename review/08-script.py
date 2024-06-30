#!/usr/bin/env python3

"""
**Exercise Description:**

* **Understand Recursion:** Write a recursive function named `countdown` 
  that prints numbers from 100 down to 0.

* **Optional Challenge:** Use recursion to solve these additional problems:
    * **Factorial:** Create a function `factorial` that calculates the factorial 
      of a given number (the function receives the number as input). 
      Factorial is the product of all positive integers less than or equal 
      to the given number (e.g., factorial(5) = 5 * 4 * 3 * 2 * 1 = 120).
    * **Fibonacci Sequence:** Implement a function `fibonacci` that 
      determines the value at a specific position in the Fibonacci sequence. 
      The Fibonacci sequence is a series of numbers where each number is the 
      sum of the two preceding numbers (0, 1, 1, 2, 3, 5, 8, ...). The function 
      receives the position (index) as input.
"""

def countdown(number: int):
    """
    This function recursively prints numbers from a given starting number down to 0.

    Args:
        number: The integer value from which to begin the countdown.
    """

    if number >= 0:
        print(number)
        countdown(number - 1)  # Recursive call with decremented number

# countdown(100)  # Uncomment to run the countdown function


"""
Extra: Factorial
"""

def factorial(number: int):
    """
    This function calculates the factorial of a given non-negative integer.

    Args:
        number: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of the given number.

    Raises:
        ValueError: If a negative number is provided.
    """

    if number < 0:
        print("Negative numbers aren't allowed")
        raise ValueError("Factorial is not defined for negative numbers")
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)  # Recursive call with decremented number

# print(factorial(5))  # Uncomment to run the factorial calculation


"""
Extra: Fibonacci Sequence
"""

def fibonacci(number: int):
    """
    This function calculates the value at a specific position in the Fibonacci 
    sequence.

    Args:
        number: The position (index) in the Fibonacci sequence for which to find the value.

    Returns:
        The value at the specified position in the Fibonacci sequence.

    Raises:
        ValueError: If a negative number is provided for the position.
    """

    if number < 0:
        print(f"\n[!] It isn't allowed to use negative numbers")
        raise ValueError("Fibonacci sequence definition doesn't include negative positions")
    elif number <= 2:
        return number - 1  # Base cases for the first two numbers (0 and 1)
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)  # Recursive calls to calculate previous values

print(fibonacci(17))  # Print the 17th Fibonacci number (15)