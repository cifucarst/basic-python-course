#!/usr/bin/env python3

# Class representing a Car
class Car():
    # Properties of the car
    chassisLength = 250
    chassisWidth = 120
    wheels = 4
    isRunning = False

    # Methods
    def start(self):
        self.isRunning = True

    def status(self):
        if self.isRunning:
            return "The car is running"
        else:
            return "The car is stopped"


# Instantiate a class (Create an object)
myCar = Car()

# Accessing a property
print(f'The car\'s length is: {myCar.chassisLength}')
print(f'The car has {myCar.wheels} wheels')

# Starting the car
myCar.start()
print(myCar.status())