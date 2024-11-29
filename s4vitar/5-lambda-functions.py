#!/usr/bin/env python3

# Lambda functions

# Lambda function that returns a string
my_function = lambda: "Hello world!"
# Uncomment line below to execute the lambda function and print the result
# print(my_function())

#______________________________________________

# Lambda function that sums two values
sums = lambda x, y: x + y
# Uncomment line below to execute the lambda function and print the result
# print(sums(73, 45))

#______________________________________________

numbers = [1, 2, 3, 4, 5]

# Using lambda function with map to square each element in the list 'numbers'
squares = list(map(lambda x: x**2, numbers))
# Printing the list of squared numbers
print(squares)

#______________________________________________

# Using lambda function with filter to get even numbers from the list 'numbers'
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Printing the list of even numbers
print(evens)

#______________________________________________

from functools import reduce

# Using lambda function with reduce to get the total sum of all elements in 'numbers'
total = reduce(lambda x, y: x + y, numbers)
# Printing the total sum
print(total)