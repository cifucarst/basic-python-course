#!/usr/bin/env python3

# Asking the user to input a number
objective = int(input(f"\n[+] Write a number "))

# Setting a small value as the margin of error
epsilon = 0.01

# Calculating the step size for the approximation
step = epsilon**2

# Initializing the variable to hold the approximate square root
response = 0.0

# Looping until the approximation is within the acceptable margin of error
# or until it exceeds the objective
while abs(response**2 - objective) >= epsilon and response <= objective:
    print(abs(response**2 - objective), response) # Printing the difference between the actual value and the approximation
    response += step # Incrementing the approximation by the step size

# Checking if the approximation is within the acceptable margin of error
if abs(response**2 - objective) >= epsilon:
    print(f"\n[!] {objective} does not have an exact square root") # Printing a message if no exact square root is found
else:
    print(f"\n[+] The square root of {objective} is {response}") # Printing the approximate square root if found