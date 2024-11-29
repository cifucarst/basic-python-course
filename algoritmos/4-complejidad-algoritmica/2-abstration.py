#!/usr/bin/env python3

# Define a function named f that takes one parameter x
def f(x):
    # Initialize a variable named answer to 0
    answer = 0

    # Iterate 1000 times
    for i in range(1000):
        # Increment the answer by 1 in each iteration
        answer += 1

    # Iterate x times
    for i in range(x):
        # Increment the answer by x in each iteration
        answer += x
    
    # Iterate x times
    for i in range(x):
        # Iterate x times nested inside the outer loop
        for j in range(x):
            # Increment the answer by 1 in each iteration
            answer += 1
            # Increment the answer by 1 in each iteration
            answer += 1
            
    # Return the final value of the answer
    return answer