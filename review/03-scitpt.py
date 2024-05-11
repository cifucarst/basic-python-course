#!/usr/bin/env python3

"""
User-defined Functions
"""

# Simple
def greet():
    print("Hello, Python!")

greet()

# With return
def return_greet():
    return "Hello, Python!"

print(return_greet())

# With one argument
def arg_greet(name):
    print(f"Hello, {name}!")

arg_greet("Brais")

# With arguments
def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Brais")
args_greet(name="Brais", greet="Hi")

# With a default argument
def default_arg_greet(name="Python"):
    print(f"Hello, {name}!")

default_arg_greet("Brais")
default_arg_greet()

# With arguments and return
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Brais"))

# With multiple return values
def multiple_return_greet():
    return "Hello", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# With a variable number of arguments
def variable_arg_greet(*names):
    for name in names:
        print(f"Hello, {name}!")

variable_arg_greet("Python", "Brais", "MoureDev", "community")

# With variable keyword arguments
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)

"""
Functions within Functions
"""

def outer_function():
    def inner_function():
        print("Inner Function: Hello, Python !")
    inner_function()

outer_function()

"""
Built-in Functions
"""

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

"""
Local and Global Variables
"""

global_var = "Python"

def hello_python():
    local_var = "Hello"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) Cannot be accessed from outside the function

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))