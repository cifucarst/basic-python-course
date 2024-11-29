#!/usr/bin/env python3

# Dictionary example
fruits = {
    "apples": 1,
    "bananas": 5,
    "kiwis": 3,
}

for fruit, amount in fruits.items():
    print(f'There are {amount} {fruit}(s)')

# Nested loops
my_list = [
    [1, 4, 5],
    [2, 6, 8],
    [9, 4, 1]
]

# for element in my_list:
#     print(f"\n[+] Let's break down the list {element}")
#     for item in element:
#         print(item)

# List comprehensions (for)
odd_list = [1, 3, 5, 7, 9]

square = [i**2 for i in odd_list]
# print(square)

for i in range(10):
    if i == 10:
        break
else:
    print("Loop successfully concluded")

# -----------------------------------------
print('Continue with the rest of instructions')
# -----------------------------------------

# Ternary operator
age = 20
message = "You are of legal age" if age >= 18 else "You are underage"
print(message)

# Logical operators
nationality = "Mexican"

if age >= 18 and nationality == "Mexican":
    print("You can vote in Mexican elections")
else:
    print("You are not Mexican")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 2 == 0:
        print(f"{i} Even")
    else:
        print(f"{i} Odd")
