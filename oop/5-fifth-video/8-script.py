#!/usr/bin/env python3

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'


class Employee(Person):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary

    def greet(self):
        return f'{super().greet()}, and I earn {self.salary} euros per year'


person = Employee('Alicia', 23, 35000)
print(person.greet())
