#!/usr/bin/env python3

# Class representing Vehicles
class Vehicles():
    def __init__(self, brand, model):
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
class Van(Vehicles):
    def load(self, loaded):
        self.loaded = loaded
        if self.loaded:
            return "The van is loaded"
        else:
            return "The van is not loaded"


# Inheritance
class Motorbike(Vehicles):
    wheelie = ""
    def do_wheelie(self):
        self.wheelie = "I'm doing a wheelie"
    
    def status(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nRunning: {self.is_running}\nAccelerating: {self.is_accelerating}\nBraking: {self.is_braking}\n {self.wheelie}")


class ElectricVehicles():
    def __init__(self):
        self.autonomy = 100

    def charge_energy(self):
        self.charging = True


# Instantiation
myMotorbike = Motorbike("Honda", "CBR")
myMotorbike.do_wheelie()
myMotorbike.status()

# Instantiation
myVan = Van("Renault", "Kangoo")
myVan.start()
myVan.status()
print(myVan.load(True))

# Multiple inheritance
class ElectricBike(Vehicles, ElectricVehicles):
    pass

# Instantiation
myEBike = ElectricBike("Orbea", "HK34")