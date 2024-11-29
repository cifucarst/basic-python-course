#!/usr/bin/env python3

# Asking the user to enter a number
objective = int(input("Write a number: "))

# Initializing the variable "response"
response = 0

# Loop that runs while the square of "response" is less than "objective"
while response**2 < objective:
    # Printing the current value of "response"
    print(response)

    # Incrementing the value of "response" by 1
    response += 1

# Checking if the square of "response" is equal to "objective"
if response**2 == objective:
    # Printing a message with the square root of "objective"
    print(f"\n[+] The square root of {objective} is {response}")
else:
    # Printing a message indicating that "objective" does not have an exact square root
    print(f"\n[!] {objective} does not have an exact square root")