#!/usr/bin/env python3
# This script performs basic operations in Python

# Define two numbers
first_number = 12
second_number = 7

# Exponentiation: raising the first number to the power of the second
result = first_number ** second_number
# Print the result formatted with thousand separators
print("{:,}".format(result).replace(",", "."))

# Modulo: finding the remainder of the division of the first number by the second
result = first_number % second_number
print(f'\n {result}')  # Print the modulo result

# String manipulation
first_str = "Hello"
second_str = " "
third_str = "world"

print(first_str + second_str + third_str)  # Print the concatenation of strings

# Lists: creating lists of odd and even numbers
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

# Creating a combined list with all numbers
result_list = odd_numbers + even_numbers
print(result_list)  # Print the combined list

# Summing elements from lists at corresponding positions using map and zip
result_join = list(map(sum, zip(odd_numbers, even_numbers)))
print(result_join)  # Print the list of sums of elements at the same positions in the lists
