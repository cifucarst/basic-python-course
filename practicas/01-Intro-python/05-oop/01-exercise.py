# Ejercicio 1: Gestión de Estudiantes

# Crea un programa en Python que implemente una clase llamada Student con las siguientes características:
# Atributos:

#     name: Nombre del estudiante.
#     age: Edad del estudiante.
#     grades: Una lista de calificaciones (puede estar vacía al inicio).

# Métodos:

#     add_grade(grade): Agrega una calificación a la lista de calificaciones.
#     average_grade(): Calcula y devuelve el promedio de las calificaciones. Si no hay calificaciones, devuelve None.
#     is_passing(): Devuelve True si el promedio es mayor o igual a 60, de lo contrario, devuelve False.

# Requisitos adicionales:

#     Incluye un constructor para inicializar los atributos de la clase.
#     Usa encapsulamiento para proteger el atributo grades.
#     Implementa una representación amigable para imprimir objetos de la clase Student.

# Prueba el código:

#     Crea dos estudiantes con nombres y edades.
#     Agrega varias calificaciones a cada estudiante.
#     Muestra el promedio de calificaciones y si están aprobando.

class Student:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise ValueError("Debes ingresar un nombre válido")
        if not isinstance(age, int):
            raise ValueError("Debes ingresar una edad válida")
        
        self.name = name
        self.age = age
        self.__grades = []

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and grade >= 0:
            self.__grades.append(grade)
        else:
            raise ValueError("La calificación debe ser un número positivo")
        return self.__grades

    def average_grade(self):
        if not self.__grades:
            return None
        return sum(self.__grades) / len(self.__grades)

    def is_passing(self):
        avg = self.average_grade()
        return avg is not None and avg >= 60

    def __str__(self):
        return f"Estudiante: {self.name}, Edad: {self.age}, Promedio: {self.average_grade():.2f}"

# Pruebas
try:
    student1 = Student("Andres", 23)
    student1.add_grade(30)
    student1.add_grade(80)
    print(student1)
    print(f"¿Aprueba? {'Sí' if student1.is_passing() else 'No'}")
except ValueError as e:
    print(f"Error: {e}")

try:
    student2 = Student("Mariana", 20)
    student2.add_grade(34)
    student2.add_grade(90)
    student2.add_grade(80)
    print(student2)
    print(f"¿Aprueba? {'Sí' if student2.is_passing() else 'No'}")
except ValueError as e:
    print(f"Error: {e}")

try:
    student3 = Student(True, 20)
except ValueError as e:
    print(f"Error: {e}")