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

        # Internal check before starting the car
        if self.__isRunning:
            check = self.__internal_check()

        if self.__isRunning and check:
            return "The car is running"
        elif self.__isRunning and not check:
            return "Something went wrong in the check, we can't start"
        else:
            return "The car is stopped"

    def status(self):
        # Displaying car's information
        print(f"The car has {self.__wheels} wheels. Width: {self.__chassisWidth}, Length: {self.__chassisLength}")

    # Private method for internal checks
    def __internal_check(self):
        print(f'Performing internal check')

        self.gas = 'ok'
        self.oil = 'ok'
        self.doors = 'closed'

        if self.gas == 'ok' and self.oil == 'ok' and self.doors == 'closed':
            return True
        else:
            return False


# Instantiating a class
myCar = Car()
print(myCar.start(True))  # Starting the car
myCar.status()  # Displaying the car's status

print("\n------Now we create the second object--------\n")

# Second instance
myCar2 = Car()
print(myCar2.start(False))  # Stopping the car
myCar2.status()  # Displaying the status of the second car