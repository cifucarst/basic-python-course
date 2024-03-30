#!/usr/bin/env python3

import time
import sys

# Print the current recursion limit
print(sys.getrecursionlimit())

# Set the recursion limit to 2000 to prevent stack overflow
sys.setrecursionlimit(2000)

# Function to calculate factorial iteratively
def factorial(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

# Function to calculate factorial recursively
def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)

if __name__ == '__main__':
    n = 1000

    # Measure the time taken to calculate factorial iteratively
    start = time.time()
    factorial(n)
    end = time.time()
    print("Time taken for iterative factorial calculation:", end - start)

    # Measure the time taken to calculate factorial recursively
    start = time.time()
    factorial_r(n)
    end = time.time()
    print("Time taken for recursive factorial calculation:", end - start)