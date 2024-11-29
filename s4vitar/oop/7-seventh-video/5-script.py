#!/usr/bin/env python3

# **kwargs

def presentation(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


presentation(name="marcelo", age=28, city="santa cruz de tenerife", profession="lammer")