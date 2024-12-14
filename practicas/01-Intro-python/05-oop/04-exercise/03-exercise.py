# funcionalidad adicional: importar datos desde un archivo CSV, lo cual permitirá cargar empleados en masa.

import csv

class Employee:
    def __init__(self, name: str, position: str, salary, department: str = "General"):
        if not isinstance(department, str):
            raise ValueError("Debes ingresar un departamento válido")
        self.department = department
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        # Incrementa el salario del empleado
        if amount > 0:
            self.salary += amount
        return self.salary
    
    def __str__(self):
        return (f'Empleado: {self.name}, Posición: {self.position}, Salario: ${self.salary}, '
                f'Departamento: {self.department}')


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

    def export_to_csv(self, filename='employees.csv'):
        if not self.employees:
            print("❌ No hay empleados para exportar.")
            return
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir encabezados
            writer.writerow(['Nombre', 'Posición', 'Salario'])
            # Escribir datos de empleados
            for employee in self.employees:
                writer.writerow([employee.name, employee.position, employee.salary])
        
        print(f"✅ Los datos de empleados se han exportado correctamente a '{filename}'.")

    def list_by_department(self, department):
        department = department.title()
        filtered = [emp for emp in self.employees if emp.department == department]
        if not filtered:
            print(f"❌ No hay empleados en el departamento '{department}'.")
        else:
            print(f"Empleados en el departamento '{department}':")
            for emp in filtered:
                print(emp)

    def import_from_csv(self, filename='employees.csv'):
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar los encabezados del archivo CSV
                
                count = 0
                for row in reader:
                    if len(row) != 4:
                        print(f"❌ Registro inválido en el archivo CSV: {row}")
                        continue
                    
                    name, position, salary, department = row
                    try:
                        salary = float(salary)
                        employee = Employee(name.strip().title(), position.strip().title(), salary, department.strip().title())
                        self.add_employee(employee)
                        count += 1
                    except ValueError:
                        print(f"❌ Datos inválidos en el registro: {row}")
                
                print(f"✅ Se han importado {count} empleados desde '{filename}'.")
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo '{filename}'.")
        except Exception as e:
            print(f"❌ Error al importar datos: {e}")


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
                 6 - Salir.
                 7 - Exportar datos a CSV.
                 8 - Listar empleados por departamento.
                 9 - Importar empleados desde archivo CSV.
              """)
        try:
            opcion = int(input('Escribe una opción: '))
            if opcion == 1:
                name = input('Escribe el nombre: ').title()
                position = input('Escribe la posición del empleado: ').title()
                try:
                    salary = float(input('Escribe el salario del empleado: '))
                    if salary <= 0:
                        print('❌ El salario debe ser un valor positivo.')
                        continue
                except ValueError:
                    print('❌ Debes ingresar un valor numérico para el salario.')
                    continue
                department = input('Escribe el departamento (por defecto: General): ').title()
                if not department:
                    department = "General"
                employee = Employee(name, position, salary, department)
                company.add_employee(employee)
            elif opcion == 2:
                company.list_employees()
            elif opcion == 3:
                name = input('Escribe el nombre del empleado a buscar: ').title()
                company.find_employee(name)
            elif opcion == 4:
                name = input('Escribe el nombre del empleado para aumento: ').title()
                found = company.find_employee(name)
                if found:
                    try:
                        amount = float(input('Escribe el aumento: '))
                        found.give_raise(amount)
                    except ValueError:
                        print('❌ Debes ingresar un valor numérico.')
                else:
                    print('❌ Empleado no encontrado.')
            elif opcion == 5:
                name = input('Escribe el nombre del empleado a eliminar: ').title()
                company.remove_employee(name)
            elif opcion == 6:
                print('Saliendo... ¡Gracias por utilizar nuestro inventario!')
                break
            elif opcion == 7:
                filename = input("Escribe el nombre del archivo CSV (por defecto: 'employees.csv'): ").strip()
                if not filename:
                    filename = 'employees.csv'
                company.export_to_csv(filename)
            elif opcion == 8:
                department = input("Escribe el departamento que deseas listar: ").title()
                company.list_by_department(department)
            elif opcion == 9:
                filename = input("Escribe el nombre del archivo CSV para importar (por defecto: 'employees.csv'): ").strip()
                if not filename:
                    filename = 'employees.csv'
                company.import_from_csv(filename)
            else:
                print('❌ Opción no válida.')
        except ValueError:
            print('❌ Debes ingresar un número válido.')


if __name__ == '__main__':
    menu()