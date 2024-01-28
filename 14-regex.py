#!/usr/bin/env python3

import re

text = "car, cart, chew, magicarp"

# Print all occurrences of "car" regardless of their position
all_car = re.findall("car", text)
print(all_car)

# Print only those that start with "car"
starts_with_car = re.findall(r"\bcar", text)
print(starts_with_car)

###########################################################

text1 = "Today is 10/10/2023 and tomorrow will be 11/10/2023"
pattern1 = r"\b(\d{2}\/\d{2}\/\d{4})\b"

# Uncomment the line below to print the dates found in the text
# print(re.findall(pattern1, text1))

# Iterate over matches and print details
for match in re.finditer(pattern1, text1):
    print(f'The date is: {match.group(0)}, starting at position {match.start()} and ending at position {match.end()}')