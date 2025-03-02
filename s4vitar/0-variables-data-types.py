#!/usr/bin/env python3

# Define the IP address and print it to the console
ip_address = "192.168.1.39"
print(f"The IP address is: {ip_address}")

# Define a floating-point number and print it to the console
number = 6.7
print(f"The floating-point number is: {number}")

# Create a list of ports
my_ports = [22, 80, 443, 8080, 445]
print(f"The initial list of ports is: {my_ports}")

# Extend the list of ports using the extend() method
my_ports.extend([6500, 54])
print(f"The extended list of ports is: {my_ports}")

# Append additional ports to the list using the += operator
my_ports += [86, 87]
print(f"The updated list of ports is: {my_ports}")

# Sort the list of ports in ascending order
sorted_ports = sorted(my_ports)
print(f"The sorted list of ports is: {sorted_ports}")

# Remove the first item from the list using the del keyword
del my_ports[0]
print(f"The list of ports after removing the first item is: {my_ports}")

# Iterate through the list of ports and print each port to the console
for port in my_ports:
    print(f"Port: {port}")

# Print the length of the list of ports using the len() function
print(f"The list of ports has {len(my_ports)} items")

# Additional methods for lists in Python:

# Check if an item exists in a list using the in keyword
if 80 in my_ports:
    print("Port 80 is in the list of ports")

# Count the number of occurrences of an item in a list using the count() method
print(f"The number of occurrences of port 443 in the list is: {my_ports.count(443)}")

# Insert an item into a specific position in the list using the insert() method
my_ports.insert(2, 8000)
print(f"The list after inserting port 8000 at index 2 is: {my_ports}")

# Remove an item from the list by value using the remove() method
my_ports.remove(87)
print(f"The list after removing port 87 is: {my_ports}")

# Reverse the order of the list using the reverse() method
my_ports.reverse()
print(f"The reversed list of ports is: {my_ports}")