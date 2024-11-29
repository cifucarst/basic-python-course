#!/usr/bin/env python3

"""
Operations
"""

s1 = "Hello"
s2 = "Python"

# Concatenation
print(s1 + ", " + s2 + "!")

# Repetition
print(s1 * 3)

# Indexing
print(s1[0] + s1[1] + s1[2] + s1[3])

# Length
print(len(s2))

# Slicing
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Search
print("a" in s1)
print("i" in s1)

# Replacement
print(s1.replace("o", "a"))

# Division
print(s2.split("t"))

# Uppercase, lowercase, and title case
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Removing spaces
s1 = "Hello"
s2 = "Python"

# Concatenation
print(s1 + ", " + s2 + "!")

# Repetition
print(s1 * 3)

# Indexing
print(s1[0] + s1[1] + s1[2] + s1[3])  # Beginning and end
print(" brais moure ".strip())

# Search at the beginning and end
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Position search
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Occurrence search
print(s3.lower().count("m"))

# Formatting
print("Greeting: {}, language: {}!".format(s1, s2))

# Interpolation
print(f"Greeting: {s1}, language: {s2}!")

# Transforming into a list of characters
print(list(s3))

# Transforming list into string
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Numeric transformations
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Various checks
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
Extra
"""


def check(word1: str, word2: str):

    # Palindromes
    print(f"Is {word1} a palindrome?: {word1 == word1[::-1]}")
    print(f"Is {word2} a palindrome?: {word2 == word2[::-1]}")

    # Anagrams
    print(f"Is {word1} an anagram of {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograms

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"Is {word1} an isogram?: {isogram(word1)}")
    print(f"Is {word2} an isogram?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
# check("love", "rome")