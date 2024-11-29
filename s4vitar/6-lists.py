#!/usr/bin/env/ python3

# list

# Initializing a list of Common Vulnerabilities and Exposures (CVEs)
cve_list = ["CVE-2023-1435", "CVE-2022-45656", "CVE-2023-7863"]

# Removing a specific CVE, 'CVE-2023-7863', from the list
cve_list.remove('CVE-2023-7863')

#__________________________________________________________________

# Initializing a list of TCP ports
tcp_ports = [21, 22, 80, 8080, 443, 445, 69]

# Appending a new port number, 1337, to the list
tcp_ports.append(1337)

# Sorting the TCP ports in ascending order
tcp_ports.sort()

#__________________________________________________________________

# Initializing a list of various cyber attacks
attacks = ["phishing", "DDOS", "SQL Injection", "Man In The Middle", "Cross-Site Scripting"]

# Displaying the list of attacks
print(attacks)

# Slicing the list to create a new list starting from the 4th attack
another_attacks_list = attacks[3:]

# Iterating through the attacks list using enumeration
for idx, attack in enumerate(attacks):
    pass  # Printing the position and attack (currently commented out)

#__________________________________________________________________

# Creating a new list by converting all attacks to uppercase
attacks_uppercase = [attack.upper() for attack in attacks]

#__________________________________________________________________

# Initializing lists of names and their respective ages
names = ["s4vitar", "hackermate", "lobotec", "hackavis"]
ages = [27, 45, 13, 20]

# Uncomment to print names and ages together using zip()
# for name, age in zip(names, ages):
#     print(f'{name} is {age} years old')

#__________________________________________________________________

# Deleting elements from the 'names' list by index, value, and popping
del names[2]  # Deleting the element at index 2

names.remove('hackavis')  # Removing the element 'hackavis'

deleted_usr = names.pop(1)  # Removing and storing the element at index 1
print(f'{deleted_usr}')  # Displaying the removed user

# Clearing the entire 'names' list
# names.clear()

print(names)  # Displaying the modified 'names' list

#__________________________________________________________________

# Modifying elements in the 'names' list by index and inserting new elements
names[2] = "chema alonso"  # Modifying the element at index 2
names.insert(2, "cifucarst")  # Inserting a new element at index 2

print(names)  # Displaying the final 'names' list
