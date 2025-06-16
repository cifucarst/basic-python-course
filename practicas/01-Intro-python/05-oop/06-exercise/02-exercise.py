import json


class Vehicle:

    def __init__(self, license_plate: str, brand: str, year_model: int, is_available: bool = True):

        if not isinstance(license_plate, str):
            raise ValueError("Debes ingresar una liencica válida")
        if not isinstance(brand, str):
            raise ValueError("Debes ingresar una marca válida")
        if not isinstance(year_model, int):
            raise ValueError("Debes ingresar un ano de modelo válido")
        if not isinstance(is_available, bool):
            raise ValueError("Debes ingresar un booleano válido")
        
        self.license_plate = license_plate
        self.brand = brand
        self.year_model = year_model
        self.is_available = is_available

    def rent(self):
        if self.is_available:
            self.is_available = False
            print(f"✅ El vehículo de placas: {self.license_plate}, marca: {self.brand}, modelo: {self.year_model} ha sido arrendado.")
        else:
            print(f"❌ El vehículo de placas: {self.license_plate} ya fue arrendado.")
    
    def return_vehicle(self):
        if not self.is_available:
            self.is_available = True
            print(f'✅ El vehiculo de placas: "{self.license_plate}" ha sido devuelto correctamente.')
        else:
            print(f'❌ El vehiculo "{self.license_plate}" ya esta disponible.')

    def __str__(self):
        return f"vehiculo de placas: {self.license_plate}, marca: {self.brand}, modelo: {self.year_model}, esta disponible para ser rentado? {'si' if self.is_available else 'no'}"     


class Fleet:

    def __init__(self):
        self.vehicle_list = []
        self.load_vehicles()

    def add_vehicle(self, vehicle: Vehicle): 
        if isinstance(vehicle, Vehicle):
            self.vehicle_list.append(vehicle)
            print(f"El Vehiculo de placas {vehicle.license_plate} ha sido agregado correctamente.")
            self.save_vehicles()

    # def list_available_vehicles(self): 
    #     print("Vehiculos en nuestra flota listos para ser rentados:")
    #     if self.vehicle_list:
    #         for vehicle in self.vehicle_list:
    #             print(vehicle)

    def find_vehicle(self, license_plate):
        for vehicle in self.vehicle_list:
            if license_plate.lower() == vehicle.license_plate.lower():
                print(f"✅ Vehículo de placas: {license_plate} encontrado.")
                return vehicle
        print(f"❌ No se encontró el vehículo con placas: {license_plate}")
        return None

    def rent_vehicle(self, license_plate):
        vehicle = self.find_vehicle(license_plate)
        if vehicle:
            vehicle.rent()
            self.save_vehicles()

    def return_vehicle(self, license_plate):
        vehicle = self.find_vehicle(license_plate)
        if vehicle:
            vehicle.return_vehicle()

    def list_available_vehicles(self):
        disponibles = [v for v in self.vehicle_list if v.is_available]
        if disponibles:
            print("🚗 Vehículos disponibles para rentar:")
            for vehicle in disponibles:
                print(vehicle)
        else:
            print("❌ No hay vehículos disponibles actualmente.")

    def save_vehicles(self):
        data = []
        for v in self.vehicle_list:
            data.append({
                "license_plate": v.license_plate,
                "brand": v.brand,
                "year_model": v.year_model,
                "is_available": v.is_available
            })
        with open("vehiculos.json", "w") as file:
            json.dump(data, file, indent=4)
        print("💾 Vehículos guardados correctamente.")

    def load_vehicles(self):
        try:
            with open("vehiculos.json", "r") as file:
                data = json.load(file)
                for v in data:
                    vehicle = Vehicle(v["license_plate"], v["brand"], v["year_model"], v["is_available"])
                    self.vehicle_list.append(vehicle)
            print("📁 Vehículos cargados desde el archivo.")
        except FileNotFoundError:
            print("⚠️ No se encontró un archivo de vehículos. Se iniciará una nueva flota.")

    def remove_vehicle(self, license_plate):
        vehicle = self.find_vehicle(license_plate)
        if vehicle:
            self.vehicle_list.remove(vehicle)
            print(f"🗑️ Vehículo de placas {license_plate} eliminado correctamente.")
            self.save_vehicles()



def menu():
    flota = Fleet()

    while True:
        print("""
               Bienvenido a renting car

              1 - Agregar vehiculos 
              2 - Listar vehiculos disponibles
              3 - Buscar vehiculo por placa
              4 - Tomar carros prestados
              5 - Devolver un carro.
              6 - Eliminar un vehículo
              7 - Salir
              """)
        try:
            opcion = int(input('Escribe una opción: '))
            if opcion == 1:
                license_plate = input("Escribe la place del vehiculo: ")
                brand = input("Escribe la marca del vehiculo: ")
                year_model = int(input("Escribe el ano del modelo del vehiculo: "))
                vehicle = Vehicle(license_plate, brand, year_model)
                flota.add_vehicle(vehicle)
            elif opcion == 2:
                flota.list_available_vehicles()
            elif opcion == 3:
                license_plate = input("Escribe la placa del vehiculo que deseas buscar: ").lower()
                flota.find_vehicle(license_plate)
            elif opcion == 4:
                license_plate = input('Escribe la placa del vehiculo que deseas tomar prestado: ').lower()
                vehicle = flota.find_vehicle(license_plate)
                if vehicle:
                    vehicle.rent()
            elif opcion == 5:
                license_plate = input('Escribe la placa del vehículo que deseas devolver: ').lower()
                flota.return_vehicle(license_plate)
            elif opcion == 6:
                license_plate = input('Escribe la placa del vehículo que deseas eliminar: ').lower()
                flota.remove_vehicle(license_plate)
            elif opcion == 7:
                print('Saliendo... ¡Gracias por utilizar nuestra flota de vehiculos!')
                break
            else:
                print('❌ Opción no válida.')
        except ValueError:
            print('❌ Debes ingresar un número válido.')


if __name__ == '__main__':
    menu()