#!/usr/bin/env python3

import random

def linear_search(list, target):
    match = False  # Initialize a variable to track whether the target is found in the list

    for element in list:  # Iterate through each element in the list
        if element == target:  # Check if the current element matches the target
            match = True  # If found, set match to True
            break  # Exit the loop since the target has been found

    return match  # Return whether the target was found in the list or not


if __name__ == '__main__':
    list_size = int(input(f'\n[+] What will be the size of the list? '))  # Ask user for the size of the list
    target = int(input(f'\n[+] Which number do you want to find? '))  # Ask user for the number to find

    list = [random.randint(0, 100) for i in range(list_size)]  # Generate a random list of integers

    found = linear_search(list, target)  # Perform linear search on the list for the target
    print(list)  # Print the generated list
    print(f'\n[+] The element {target} {"is" if found else "is not"} in the list')  # Print whether the target was found in the list or not