#!/usr/bin/env python3

"""
Value and Reference
"""

# Value types

my_int_a = 10                   # Assigns the integer value 10 to my_int_a
my_int_b = my_int_a             # Copies the value of my_int_a into my_int_b
my_int_b = 20                   # Overrides the value of my_int_b with 20
# my_int_a = 30                 # This comment suggests my_int_a can be changed to 30
print(my_int_a)                 # Prints the current value of my_int_a
print(my_int_b)                 # Prints the current value of my_int_b

# Reference types

my_list_a = [10, 20]            # Creates a list with elements 10 and 20 and assigns it to my_list_a
my_list_b = my_list_a           # Assigns my_list_a reference to my_list_b
my_list_b.append(30)            # Adds element 30 to my_list_b
print(my_list_a)                # Prints the current elements of my_list_a
print(my_list_b)                # Prints the current elements of my_list_b

# Functions with value data


def my_int_func(my_int: int):
    my_int = 20                  # Assigns 20 to my_int
    print(my_int)


my_int_c = 10                   # Assigns the integer value 10 to my_int_c
my_int_func(my_int_c)           # Calls my_int_func with my_int_c as argument
print(my_int_c)                 # Prints the current value of my_int_c

# Functions with reference data


def my_list_func(my_list: list):
    my_list.append(30)          # Appends 30 to the list

    my_list_d = my_list         # Assigns my_list to my_list_d
    my_list_d.append(40)        # Appends 40 to my_list_d

    print(my_list)              # Prints the current elements of my_list
    print(my_list_d)            # Prints the current elements of my_list_d


my_list_c = [10, 20]            # Creates a list with elements 10 and 20 and assigns it to my_list_c
my_list_func(my_list_c)         # Calls my_list_func with my_list_c as argument
print(my_list_c)                # Prints the current elements of my_list_c

"""
Extra
"""

# By value


def value(value_a: int, value_b: int) -> tuple:
    temp = value_a               # Assigns the value of value_a to temp
    value_a = value_b            # Assigns the value of value_b to value_a
    value_b = temp               # Assigns the value of temp to value_b
    return value_a, value_b      # Returns value_a and value_b as a tuple


my_int_d = 10                   # Assigns the integer value 10 to my_int_d
my_int_e = 20                   # Assigns the integer value 20 to my_int_e
my_int_f, my_int_g = value(my_int_d, my_int_e)  # Calls value function with my_int_d and my_int_e as arguments
print(f"{my_int_d}, {my_int_e}")  # Prints the current values of my_int_d and my_int_e
print(f"{my_int_f}, {my_int_g}")  # Prints the swapped values of my_int_d and my_int_e

# By reference


def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a               # Assigns the reference of value_a to temp
    value_a = value_b            # Assigns the reference of value_b to value_a
    value_b = temp               # Assigns the reference of temp to value_b
    return value_a, value_b      # Returns value_a and value_b as a tuple


my_list_e = [10, 20]            # Creates a list with elements 10 and 20 and assigns it to my_list_e
my_list_f = [30, 40]            # Creates a list with elements 30 and 40 and assigns it to my_list_f
my_list_g, my_list_h = ref(my_list_e, my_list_f)  # Calls ref function with my_list_e and my_list_f as arguments
print(f"{my_list_e}, {my_list_f}")  # Prints the current elements of my_list_e and my_list_f
print(f"{my_list_g}, {my_list_h}")  # Prints the swapped elements of my_list_e and my_list_f