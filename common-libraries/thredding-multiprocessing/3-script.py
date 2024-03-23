#!/usr/bin/env python3

import multiprocessing
import time

# Define a function called 'task' that takes a parameter 'num_task' representing the process number
def task(num_task):
    # Print a message indicating the start of the process with its corresponding process number
    print(f'\n[+] Process {num_task} starting')
    # Simulate some processing time by pausing the execution for 2 seconds
    time.sleep(2)
    # Print a message indicating the completion of the process with its corresponding process number
    print(f"\n[+] Process {num_task} completed")

# Create process objects, specifying the target function and its arguments
process1 = multiprocessing.Process(target=task, args=(1,))
process2 = multiprocessing.Process(target=task, args=(2,))

# Start both processes
process1.start()
process2.start()

# Wait for both processes to finish before continuing execution
process1.join()
process2.join()

# Print a message indicating that the processes have finished successfully
print(f"\n[+] The processes have completed successfully\n")
