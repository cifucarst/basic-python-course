#!/usr/bin/env python3

# Functions

# Function that greets a person
def greeting(name):
    print(f'\nHello, {name}!')

# Uncomment line below to execute the greeting function
# greeting("Manuel")

#____________________________________________________

# Function to calculate the sum of two values
def sum_values(value1, value2):
    return value1 + value2

result = sum_values(2, 5)
# Uncomment line below to print the result of the sum
# print(f'\n[+] The sum of both values is {result}')

#____________________________________________________

# Variable Scope

global_variable = "I'm a global variable"

# Function demonstrating local variable scope
def my_function():
    my_local_variable = "I'm a local variable"
    print(my_local_variable)

my_function()

# The line below would cause an error as my_local_variable is not accessible outside the function
# print(my_local_variable) #not accessible
