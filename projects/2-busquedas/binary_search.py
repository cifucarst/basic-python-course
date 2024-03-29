#!/usr/bin/env python3

# Asking the user to input a number
objective = int(input(f"\n[+] Write a number "))

# Setting a small value as the margin of error
epsilon = 0.01

# Setting the initial bounds for the binary search
low = 0.0
high = max(1.0, objective)

# Calculating the initial guess for the square root
response = (high + low) / 2

# Looping until the approximation is within the acceptable margin of error
while abs(response**2 - objective) >= epsilon:
    print(f"\n[+] low={low} high={high} response={response}") # Printing current bounds and guess
    if response**2 < objective:
        low = response # Adjusting the lower bound if the guess is too low
    else:
        high = response # Adjusting the upper bound if the guess is too high
    response = (high + low) / 2 # Calculating a new guess using binary search

# Printing the approximate square root
print(f"\n[+] The square root of {objective} is {response}")