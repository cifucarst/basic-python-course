#!/usr/bin/env python3

# Find the smallest number in the array
# Create two sub-arrays to control the algorithm flow
# Print the sorted result

import random

def selection_sort(lists):
    # Iterate through the entire array
    for i in range(len(lists)):
        # Find the remaining minimum value within the unsorted part of the array
        idxDes = i
        for j in range(i + 1, len(lists)):
            if lists[idxDes] > lists[j]:
                idxDes = j

        # Once the minimum number is found, swap it with the first value in the unsorted part
        lists[i], lists[idxDes] = lists[idxDes], lists[i]

    return lists

if __name__ == '__main__':
    list_size = int(input(f"\n[+] How big will the list be? "))

    lists = [random.randint(1, 100) for i in range(list_size)]
    print(lists)

    sorted_list = selection_sort(lists)
    print(sorted_list)