#!/usr/bin/env python3


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age

    @property
    def age(self):  # Getter
        return self._age

    @age.setter  # setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError('[!] Age cannot be 0 or a negative number')


manolo = Person('manolo', 23)
manolo.age = -4  # Setter
print(manolo._age)  # Getter