# 2. Sistema de Gestión de Empleados

# Crea un programa para gestionar empleados en una empresa.
# Requerimientos:

#     Clase Employee:
#         Atributos: name, position, salary.
#         Métodos:
#             give_raise(amount): Incrementa el salario del empleado.

#     Clase Company:
#         Atributos: Una lista de empleados (employees).
#         Métodos:
#             add_employee(employee: Employee): Agrega un empleado.
#             list_employees(): Muestra a todos los empleados.
#             remove_employee(name): Elimina un empleado por su nombre.
#             find_employee(name): Encuentra un empleado por su nombre.

# Interfaz Interactiva:

# Crea un menú que permita:

    # Agregar empleados.
    # Listar todos los empleados.
    # Buscar empleados.
    # Dar aumentos de sueldo.
    # Eliminar empleados.


class Employee:
    def __init__(self, name: str, position: str, salary):

        if not isinstance(name, str):
            raise ValueError("Debes ingresar un nombre de empleado válido")
        if not isinstance(position, str):
            raise ValueError("Debes ingresar una posicion válida")
        if not isinstance(salary, (float, int)):
            raise ValueError("Debes ingresar un salario válido")

        self.name = name
        self.position = position
        self.salary = salary

    
    def give_raise(self, amount):
        # Incrementa el salario del empleado
        if amount > 0:
            self.salary += amount
        return self.salary
    
    def __str__(self):
        return f'El empleado: {self.name}, con la posicion de {self.position}, recibe un salario de ${self.salary}'


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        # Agrega un empleado.
        if not isinstance(employee, Employee):
            raise ValueError("Solo puedes agregar objetos de tipo Employee al inventario")
        self.employees.append(employee)

    def list_employees(self): 
        # Muestra a todos los empleados.
        if not self.employees:
            print("El inventario de empleados está vacío.")
        else:
            for employee in self.employees:
                print(employee)

    def find_employee(self, name): 
        # Encuentra un empleado por su nombre.
        for employee in self.employees:
            if employee.name.title() == name.title():
                print(f'✅ El empleado "{employee.name}", posicion: {employee.position} y salario ${employee.salary}')
                return employee
        # raise ValueError(f"Empleado con nombre '{name}' no encontrado en el inventario de empleados")

    def remove_employee(self, name): 
        # Elimina un empleado por su nombre.
        for employee in self.employees:
            if employee.name.title() == name.title():
                self.employees.remove(employee)
                print(f"Empleado '{name}' eliminado del inventario de empleados.")
                return


def menu():
    company = Company()
    while True:
        print("""
              Bienvenido al inventario de empleados de Apple Inc

                 1 - Agregar empleados.
                 2 - Listar todos los empleados.
                 3 - Buscar empleados.
                 4 - Dar aumentos de sueldo.
                 5 - Eliminar empleados.
                 6 - salir.
              """)
        try:
            opcion = int(input('Escribe una opción: '))
            if opcion == 1:
                name = input('Escribe el nombre: ').title()
                position = input('Escribe la posicion del empleado: ').title()
                salary = float(input('Escribe el salario del empleado: '))
                employee = Employee(name, position, salary)
                company.add_employee(employee)
            elif opcion == 2:
                print("\n Lista de empleados ")
                print('-' * 30)
                company.list_employees()
            elif opcion == 3:
                name = input('Escribe el nombre del empleado a buscar: ').title()
                company.find_employee(name)
            elif opcion == 4:
                name = input('Escribe el nombre del empleado al que deseas agregarle el aumento: ').title()
                found = company.find_employee(name)
                if found:
                    amount = float(input('Escribe el aumento que deseas agregar: '))
                    found.give_raise(amount)
                else:
                    print('❌ No se encontro el empleado')
            elif opcion == 5:
                name = input('Escribe el nombre del empleado que deseas eliminar => ').title()
                company.remove_employee(name)
            elif opcion == 6:
                print('Saliendo... ¡Gracias por utilizar nuestro inventario de empleados!')
                break
            else:
                print('❌ Opción no válida.')
        except ValueError:
            print('❌ Debes ingresar un número válido.')


if __name__ == '__main__':
    menu()