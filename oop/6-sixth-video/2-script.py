#!/usr/bin/env python3

class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        self.__mileage = 0  # Private attribute

    def drive(self, kilometers):
        if kilometers >= 0:
            self.__mileage += kilometers
        else:
            print(f'\n[+] The kilometers must be greater than 0\n')

    def show_mileage(self):
        return self.__mileage


car = Car("Toyota", "corolla")
car.drive(150)
print(car.show_mileage())

# the following is not done, it is better to do what we did above
print(car._Car__mileage)