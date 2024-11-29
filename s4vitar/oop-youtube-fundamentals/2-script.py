#!/usr/bin/env python3

# Class representing a Car
class Car():
    def __init__(self):
        # Private attributes of the car
        self.__chassisLength = 250
        self.__chassisWidth = 120
        self.__wheels = 4
        self.__isRunning = False

    # Methods
    def start(self, start):
        self.__isRunning = start
        if self.__isRunning:
            return "The car is running"
        else:
            return "The car is stopped"

    def status(self):
        # Displaying car's information
        print(f"The car has {self.__wheels} wheels. Width: {self.__chassisWidth}, Length: {self.__chassisLength}")

# Instantiating a class (Creating an object)
myCar = Car()
print(myCar.start(True))  # Starting the car
myCar.status()  # Displaying the car's status

print("\n------Now we create the second object--------\n")

# Second instance
myCar2 = Car()
print(myCar.start(False))  # Stopping the first car
myCar2.__wheels = 2  # Modifying the number of wheels directly (incorrect approach)
myCar2.status()  # Displaying the status of the second car