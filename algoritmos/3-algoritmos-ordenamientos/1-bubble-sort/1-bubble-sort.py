#!/usr/bin/env python3

# Start comparing adjacent elements
# Repeat until a complete pass is made without any swaps

def bubbleSort(arr):
        n = len(arr)

        # Iterate over the array length
        for i in range(n):
                # Iterate over the unsorted portion of the array
                for j in range(0, n - i - 1):
                        # Compare adjacent elements and swap if necessary
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [190, 1200, 1, 2, 4, 55, 1000, 6, 800]

# Call the bubble sort function
bubbleSort(arr)

print("The array sorted in ascending order is:")
for i in range(len(arr)):
       print("%d" % arr[i])  # Print each element of the sorted array