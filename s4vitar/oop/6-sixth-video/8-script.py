#!/usr/bin/env python3

from typing import Any


class Greeting:
    def __init__(self,greeting) -> None:
        self.greeting = greeting

    def __call__(self, name) -> Any:
        return f'{self.greeting} {name}!'

hello = Greeting("Hi")
print(hello("Luis"))
print(hello("Alberto"))