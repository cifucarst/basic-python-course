#!/usr/bin/env python3

#string formatting

name = "jane"
rol = "lammer"
age = 35
print("Hello, my name is %s and I'm a %s, actually I'm %s years old" % (name, rol,age))
print()

print("Hello, I'm {}! and I'm {} years old".format(name,age))

#f-string
print(f"\nHello, I'm {name}! and I'm {age} years old")