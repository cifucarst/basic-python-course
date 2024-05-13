#!/usr/bin/env python3

"""
Structures
"""

# Lists
my_list: list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor")  # Insertion
my_list.append("Castor")
print(my_list)
my_list.remove("Brais")  # Deletion
print(my_list)
print(my_list[1])  # Access
my_list[1] = "Cuervillo"  # Update
print(my_list)
my_list.sort()  # Sorting
print(my_list)
print(type(my_list))

# Tuples
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Access
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Sorting
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")  # Insertion
my_set.add("mouredev@gmail.com")
print(my_set)
my_set.remove("Moure")  # Deletion
print(my_set)
my_set = set(sorted(my_set))  # Cannot be sorted
print(my_set)
print(type(my_set))

# Dictionary
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
my_dict["email"] = "mouredev@gmail.com"  # Insertion
print(my_dict)
del my_dict["surname"]  # Deletion
print(my_dict)
print(my_dict["name"])  # Access
my_dict["age"] = "37"  # Update
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Sorting
print(my_dict)
print(type(my_dict))

"""
Extra
"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Enter the contact's phone number: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "You must enter a phone number with a maximum of 11 digits.")

    while True:

        print("")
        print("1. Search contact")
        print("2. Insert contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("\nSelect an option: ")

        match option:
            case "1":
                name = input("Enter the name of the contact to search for: ")
                if name in agenda:
                    print(
                        f"The phone number of {name} is {agenda[name]}.")
                else:
                    print(f"The contact {name} does not exist.")
            case "2":
                name = input("Enter the name of the contact: ")
                insert_contact()
            case "3":
                name = input("Enter the name of the contact to update: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"The contact {name} does not exist.")
            case "4":
                name = input("Enter the name of the contact to delete: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"The contact {name} does not exist.")
            case "5":
                print("Exiting the agenda.")
                break
            case _:
                print("Invalid option. Choose an option from 1 to 5.")


my_agenda()