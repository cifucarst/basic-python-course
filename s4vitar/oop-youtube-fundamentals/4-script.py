#!/usr/bin/env python3

# Class representing Vehicles
class Vehicles():
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        self.is_running = False
        self.is_accelerating = False
        self.is_braking = False

    def start(self):
        self.is_running = True
    
    def accelerate(self):
        self.is_accelerating = True

    def brake(self):
        self.is_braking = True

    def status(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nRunning: {self.is_running}\nAccelerating: {self.is_accelerating}\nBraking: {self.is_braking}")

# Inheritance
class Motorbike(Vehicles):
    pass

# Instantiate
myMotorbike = Motorbike("Honda", "CBR")
myMotorbike.status()