#!/usr/bin/env python3

import re

# First example: Extracting dates from a text
text = "Today is the date 10/10/2023, tomorrow will be 11/10/2023"
matches = re.findall("\d{2}\/\d{2}\/\d{4}", text)
# Matches will contain a list of date strings found in the text.

################################################################
# Second example: Extracting email addresses from a text
text2 = "Users can contact us at support@hack4u.io or info@hack4u.io"
matches2 = re.findall("(\w+)@(\w+\.\w{2,})", text2)
# Matches2 will contain a list of tuples, each representing a matched email address.

################################################################

# Substitutions: Replacing words in a text
text3 = "My cat is on the roof, and my dog is in the garden"
new_text = re.sub("cat", "dog", text3)
# 'new_text' will contain the original text with 'cat' replaced by 'dog'.

# Splitting a string into a list using a delimiter
text4 = "field1,field2,field3,field4,field5"
new_with_split = re.split(",", text4)
# 'new_with_split' will be a list containing individual fields separated by commas.
# Uncomment the next line to print the third field: 
# print(new_with_split[2])