#!/usr/bin/env python3

import time

# Define a function called 'tarea' that takes a parameter 'num_tarea' representing the task number
def task(num_task):
    # Print a message indicating the start of the task with its corresponding task number
    print(f"\n[+] Starting {num_task} task")
    # Simulate some processing time by pausing the execution for 2 seconds
    time.sleep(2)
    # Print a message indicating the completion of the task with its corresponding task number
    print(f"\n[+] Completed {num_task} task")

# Call the 'tarea' function with task number 1
task(1)
# Call the 'tarea' function with task number 2
task(2)