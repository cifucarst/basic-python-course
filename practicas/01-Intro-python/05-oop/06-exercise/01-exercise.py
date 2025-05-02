# Sistema de Gestión de Vehículos

# Crea un programa para gestionar un parque vehicular.
# Requerimientos:

#     Clase Vehicle:
#         Atributos: license_plate, brand, model, is_available.
#         Métodos:
#             rent(): Marca el vehículo como no disponible.
#             return_vehicle(): Marca el vehículo como disponible.

#     Clase Fleet:
#         Atributos: Lista de vehículos (vehicles).
#         Métodos:
#             add_vehicle(vehicle: Vehicle): Agrega un vehículo.
#             list_available_vehicles(): Muestra los vehículos disponibles.
#             find_vehicle(license_plate): Busca un vehículo por placa.
#             rent_vehicle(license_plate): Permite rentar un vehículo.
#             return_vehicle(license_plate): Permite devolver un vehículo.

# Interfaz Interactiva:

# Crea un menú que permita:

#     Registrar vehículos en el sistema.
#     Listar vehículos disponibles para renta.
#     Rentar vehículos.
#     Devolver vehículos.


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

    def rent(self, license_plate):
        if self.license_plate == license_plate:
            if self.is_available:
                self.is_available = False
                print(f"✅ El vehiculo de placas: {license_plate}, marca: {self.brand}, modelo: {self.year_model} ha sido arrendado.")
            else:
                print(f"El vehiculo de placas: {self.license_plate} ya fue arrendado, por lo tanto no se .lo podemos arrendar")
        else:
            return print(f"❌No contamos con el vehiculo solicitado.")
        
    def return_vehicle(self):
        if not self.available:
            self.available = True
            print(f'✅ El vehiculo de placas: "{self.license_plate}" ha sido devuelto correctamente.')
        else:
            print(f'❌ El vehiculo "{self.license_plate}" ya esta disponible.')

    def __str__(self):
        return f"vehiculo de placas: {self.license_plate}, marca: {self.brand}, modelo: {self.year_model}, esta disponible para ser rentado? {'si' if self.is_available else 'no'}"     


class Fleet:

    def __init__(self):
        self.vehicle_list = []

    def add_vehicle(self, vehicle: Vehicle): 
        if isinstance(vehicle, Vehicle):
            self.vehicle_list.append(vehicle)
            print(f"El Vehiculo de placas {vehicle.license_plate} ha sido agregado correctamente.")
        else:
            raise ValueError("Solo puedes agregar objetos de tipo Vehicle a la flota")
    
    def list_available_vehicles(self): 
        print("Vehiculos en nuestra flota listos para ser rentados:")
        if self.vehicle_list:
            for vehicle in self.vehicle_list:
                print(vehicle)

    def find_vehicle(self, license_plate): 
        if self.vehicle_list:
            for vehicle in self.vehicle_list:
                if license_plate == vehicle.license_plate.lower():
                    print(f"Vehiculo de placas: {license_plate} encontrado")
                    return vehicle
                else:
                    print(f"No se encontro el vehiculo en la lista")
        else:
            print("No hay vehiculos en la lista")

    def rent_vehicle(self, license_plate): 
        vehicle = self.find_vehicle(license_plate)
        vehicle.rent()

    def return_vehicle(self,  license_plate): 
        # falta completar
        pass


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
              6 - Salir
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
                    vehicle.rent(license_plate)
            elif opcion == 5:
                license_plate = input('Escribe la placa del vehiculo que deseas devolver: ').lower()
                # vehicle.return_vehicle(license_plate)
                # falta completar
            elif opcion == 6:
                print('Saliendo... ¡Gracias por utilizar nuestra flota de vehiculos!')
                break
            else:
                print('❌ Opción no válida.')
        except ValueError:
            print('❌ Debes ingresar un número válido.')


if __name__ == '__main__':
    menu()         