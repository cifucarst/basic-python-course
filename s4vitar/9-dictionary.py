#!/usr/bin/env/ python3

# dictionaries

# Creating a dictionary 'my_dictionary' with various key-value pairs
my_dictionary = {
    "name": "s4vitar",
    "age": 28,
    "island": "Tenerife",
}

# Printing the type of 'my_dictionary'
print(type(my_dictionary))

# Accessing and printing specific values from the dictionary
# print(my_dictionary)
# print(my_dictionary["name"])

# Modifying the value associated with the "name" key in 'my_dictionary'
my_dictionary["name"] = "Lobotec"
print(my_dictionary["name"])

# Adding a new key-value pair to 'my_dictionary'
my_dictionary["profession"] = "lamer"

# Deleting the "age" key-value pair from 'my_dictionary'
del my_dictionary["age"]
print(my_dictionary)

# Checking if a specific key exists in the dictionary
if "island" in my_dictionary:
    print("This key is in my dictionary")
else:
    print("This key is in the dictionary")

#__________________________________________________________________

# Creating 'my_dictionary1' with similar key-value pairs
my_dictionary1 = {
    "name": "s4vitar",
    "age": 28,
    "island": "Tenerife",
}

# Iterating through the key-value pairs in 'my_dictionary1' and printing them
for key, value in my_dictionary1.items():
    pass
    # print(f"\nfor the key {key} we have the value {value}")

#__________________________________________________________________

# Creating a dictionary 'squares' using a dictionary comprehension
squares = {x: x**2 for x in range(5)}
# print(squares)
# print(squares.keys())
# print(squares.values())

#__________________________________________________________________

# Creating 'my_dictionary1' and 'my_dictionary2'
my_dictionary1 = {
    "name": "s4vitar",
    "age": 28,
    "island": "Tenerife",
}

my_dictionary2 = {
    "profession": "lamer",
    "pets": "cat",
}

# Merging 'my_dictionary2' into 'my_dictionary1'
my_dictionary1.update(my_dictionary2)
# print(my_dictionary1)
# print(my_dictionary1.get("nam","no found"))

#__________________________________________________________________

# Creating a dictionary 'my_dict' with nested dictionaries
my_dict = {
    "name": "s4vitar",
    "hobbies": {"first": "music", "second": "soccer"},
    "age": 28
}

# Accessing and printing a value from the nested dictionary within 'my_dict'
print(my_dict["hobbies"]["first"])
