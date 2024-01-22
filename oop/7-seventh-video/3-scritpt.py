#!/usr/bin/env python3

import time

time.sleep(5)

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args)
        end = time.time()

        print(f"Total time elapsed in the {function.__name__}: {end - start}")

        if args and kwargs:
            print(args)
            print(kwargs)
    return wrapper

@timer
def short_pause(*args, **kwargs):
    time.sleep(1)

@timer
def long_pause(*args, **kwargs):
    time.sleep(2)

short_pause(1, 2, 3, 4, 5, 6, 7, nombre="marcelo", edad=17)
long_pause()