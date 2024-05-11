"""
Operators
"""

# Arithmetic operators
print(f"Addition: 10 + 3 = {10 + 3}")
print(f"Subtraction: 10 - 3 = {10 - 3}")
print(f"Multiplication: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulus: 10 % 3 = {10 % 3}")
print(f"Exponentiation: 10 ** 3 = {10 ** 3}")
print(f"Floor division: 10 // 3 = {10 // 3}")

# Comparison operators
print(f"Equality: 10 == 3 is {10 == 3}")
print(f"Inequality: 10 != 3 is {10 != 3}")
print(f"Greater than: 10 > 3 is {10 > 3}")
print(f"Less than: 10 < 3 is {10 < 3}")
print(f"Greater than or equal to: 10 >= 10 is {10 >= 10}")
print(f"Less than or equal to: 10 <= 3 is {10 <= 3}")

# Logical operators
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 is {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 is {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 is {not 10 + 3 == 14}")

# Assignment operators
my_number = 11  # assignment
print(my_number)
my_number += 1  # addition and assignment
print(my_number)
my_number -= 1  # subtraction and assignment
print(my_number)
my_number *= 2  # multiplication and assignment
print(my_number)
my_number /= 2  # division and assignment
print(my_number)
my_number %= 2  # modulus and assignment
print(my_number)
my_number **= 1  # exponentiation and assignment
print(my_number)
my_number //= 1  # floor division and assignment
print(my_number)

# Identity operators
my_new_number = my_number
print(f"my_number is my_new_number is {my_number is my_new_number}")
print(f"my_number is not my_new_number is {my_number is not my_new_number}")

# Membership operators
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Bitwise operators
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Right shift: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Left shift: 10 << 2 = {10 << 2}")  # 101000

"""
Control Structures
"""

# Conditionals

my_string = "Brais"

if my_string == "MoureDev":
    print("my_string is 'MoureDev'")
elif my_string == "Brais":
    print("my_string is 'Brais'")
else:
    print("my_string is neither 'MoureDev' nor 'Brais'")

# Iteratives

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Exception handling
try:
    print(10 / 0)
except:
    print("An error occurred")
finally:
    print("Exception handling has finished")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
