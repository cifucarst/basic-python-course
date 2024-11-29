#!/usr/bin/env python3

import threading
import time

# Define a function called 'task' that takes a parameter 'num_task' representing the thread number
def task(num_task):
    # Print a message indicating the start of the thread with its corresponding thread number
    print(f"\n[+] Thread {num_task} starting")
    # Simulate some processing time by pausing the execution for 2 seconds
    time.sleep(2)
    # Print a message indicating the completion of the thread with its corresponding thread number
    print(f"\n[+] Thread {num_task} completed")

# Create thread objects, specifying the target function and its arguments
thread1 = threading.Thread(target=task, args=(1,))
thread2 = threading.Thread(target=task, args=(2,))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before continuing execution
thread1.join()
thread2.join()

# Print a message indicating that the threads have finished successfully
print(f"\n[+] The threads have completed successfully")