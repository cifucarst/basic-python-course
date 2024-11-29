class Vehicle:
    def __init__(self, license_plate, model):
        # Initialize a new Vehicle with a license plate, model, and it is initially available for rent.
        self.license_plate = license_plate
        self.model = model
        self.available = True

    def rent(self):
        # Method to rent the vehicle if it is available; otherwise, display a message.
        if self.available:
            self.available = False
        else:
            print(f"\n[!] The vehicle with license plate {self.license_plate} cannot be rented.")

    def return_vehicle(self):
        # Method to return the vehicle if it was rented; otherwise, display a message.
        if not self.available:
            self.available = True
        else:
            print(f"\n[!] The vehicle with license plate {self.license_plate} cannot be returned because it has not been rented to anyone.")

    def __str__(self):
        # String representation of the Vehicle, displaying license plate, model, and availability.
        return f"Vehicle(license_plate={self.license_plate}, model={self.model}, available={self.available})"


class Fleet:
    def __init__(self) -> None:
        # Initialize a fleet with an empty list of vehicles.
        self.vehicles = []

    def add_vehicle(self, vehicle):
        # Method to add a vehicle to the fleet.
        self.vehicles.append(vehicle)

    def rent_vehicle(self, license_plate):
        # Method to rent a vehicle from the fleet based on the provided license plate.
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                vehicle.rent()

    def return_vehicle(self, license_plate):
        # Method to return a vehicle to the fleet based on the provided license plate.
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                vehicle.return_vehicle()

    def __str__(self):
        # String representation of the Fleet, concatenating string representations of each vehicle.
        return "\n".join(str(vehicle) for vehicle in self.vehicles)


if __name__ == '__main__':
    # Example usage
    fleet = Fleet()

    # Adding two vehicles to the fleet.
    fleet.add_vehicle(Vehicle('BAD546', "Toyota Corolla"))
    fleet.add_vehicle(Vehicle("ARM", "Honda Civic"))

    print(f'\n[+] Initial Fleet:\n')
    print(fleet)

    # Renting a vehicle by license plate.
    fleet.rent_vehicle("BAD546")

    print(f"\n[+] Showing the fleet after renting the Toyota:")
    print(fleet)

    # Returning a vehicle by license plate.
    print(f"\n[+] Showing the fleet after the customer has returned the Toyota:\n")
    fleet.return_vehicle("BAD546")
    print(fleet)

    # Trying to return a vehicle that hasn't been rented (just to show the message).
    fleet.return_vehicle("BAD546")
