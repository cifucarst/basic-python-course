#!/usr/bin/env python3

def my_decorator(function):  # higher-order function
    def wrapper():
        print("I'm greeting in the wrapper of the decorator before calling the function")
        function()  # call the original function
        print("I'm greeting in the wrapper of the decorator after calling the function")
    return wrapper


@my_decorator
def greeting():
    print("Hello, I'm greeting inside the function")

greeting()