#!/usr/bin/env python3

import random

def bubble_sort(lists):
    """
    Bubble sort algorithm implementation.
    
    Args:
    lists (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(lists)

    for i in range(n):
        # Iterate through the list
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
            # If the current element is greater than the next one, swap them
            if lists[j] > lists[j+1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]

    return lists


if __name__ == '__main__':
    # Take input for the size of the list
    list_size = int(input(f"\n[+] How big will the list be?  "))
    
    # Generate a random list of integers
    lists = [random.randint(0, 100) for i in range(list_size)]
    print(lists)

    # Sort the list using bubble sort
    sort_list = bubble_sort(lists)
    print(sort_list)