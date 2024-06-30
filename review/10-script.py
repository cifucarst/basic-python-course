#!/usr/bin/env python3

from functools import lru_cache
# lru => Least Recently used Cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the inpout is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
for n in range(1,501):
    print(n, ":", fibonacci(n))