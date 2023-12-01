#!/usr/bin/env/ python3

# sets

# Creating a set 'my_set' with initial values and adding elements
my_set = {1, 2, 3}
my_set.update({4, 5, 6})  # Adding multiple elements
my_set.add(7)  # Adding a single element

my_set.remove(2)  # Removing an element from the set
my_set.discard(8)  # Discarding an element that may not exist in the set
# print(my_set)

#__________________________________________________________________

# Creating two sets 'my_first_set' and 'my_second_set'
my_first_set = {1, 2, 3, 4, 5}
my_second_set = {2, 9, 1, 8, 15}

# Finding the intersection of the two sets
final_set = my_first_set.intersection(my_second_set)
# print(final_set)

#__________________________________________________________________

# Checking if 'set1' is a subset of 'set2'
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))

#__________________________________________________________________

# Creating a list 'my_list' with duplicate values
my_list = [1, 2, 3, 4, 5, 6, 3, 1, 2, 5, 6, 7, 8, 9, 7, 6, 5, 4, 3]

# Removing duplicates by converting the list to a set and then back to a list
no_repeat = list(set(my_list))
# print(no_repeat)

#__________________________________________________________________

# Creating a set 'my_sets' containing a range of numbers from 0 to 9999
my_sets = set(range(10000))
# print(1234 in my_sets)  # Checking if a specific number is present in the set

#__________________________________________________________________

# Creating sets representing users on different platforms
facebook_users = {"ana", "s4vitar", "hackermate", "lobotec"}
x_users = {"hackermate", "s4vitar", "manolo", "lucia"}

# Finding common users between the platforms and performing set operations
both_platforms = facebook_users.intersection(x_users)  # Users present in both platforms
all_users = facebook_users.union(x_users)  # All unique users across both platforms
difference_between_platforms = facebook_users.difference(x_users)  # Users unique to Facebook
print(difference_between_platforms)  # Outputting the users unique to Facebook

#__________________________________________________________________