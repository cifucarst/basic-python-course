#!/usr/bin/env python3

import random

def binary_search(sorted_list, start_index, end_index, target):
    print(f"Searching {target} between {sorted_list[start_index]} and {sorted_list[end_index - 1]}")
    if start_index > end_index:
        return False 
    middle_index = (start_index + end_index) // 2

    if sorted_list[middle_index] == target:
        return True
    elif sorted_list[middle_index] < target:
        return binary_search(sorted_list, middle_index + 1, end_index, target)
    else:
        return binary_search(sorted_list, start_index, middle_index - 1, target)
    
if __name__ == '__main__':
    list_size = int(input("How long will the list be? "))
    target = int(input(f"Which number do you want to find? "))

    sorted_list = sorted([random.randint(0,101) for _ in range(list_size)])

    print(sorted_list)
    found = binary_search(sorted_list, 0, len(sorted_list), target)
    print(f"The element {target} {'is' if found else 'is not'} in the list.")