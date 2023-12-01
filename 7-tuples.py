#!/usr/bin/env/ python3

# tuples

# Creating a tuple named 'example' containing various data types
example = (1, "test", [1, 2, 3], 4, True, {"manzanas": 1, "peras": 5}, 5)

# Creating a list named 'example1' with similar elements to 'example'
example1 = [1, "test", [1, 2, 3], 4, True, {"manzanas": 1, "peras": 5}, 5]

# Creating a tuple named 'my_tuple' with numeric elements
my_tuple = (1, 2, 3, 4)

# Unpacking the 'my_tuple' into individual variables a, b, c, d
a, b, c, d = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4

#__________________________________________________________________

# Creating a tuple named 'my_first_tuple' with sequential numbers
my_first_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Creating a list 'even_numbers' by filtering even numbers from 'my_first_tuple'
even_numbers = [i for i in my_first_tuple if i % 2 == 0]

print(even_numbers)  # Output: [2, 4, 6, 8]
