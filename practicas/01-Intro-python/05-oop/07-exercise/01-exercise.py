# Sistema de Notas Estudiantiles (Avanzado)

# Crea una aplicación para registrar estudiantes, asignaturas y sus calificaciones.
# Requerimientos:

#     Clase Student:
#         Atributos: name, grades (diccionario con asignaturas y calificaciones).
#         Métodos:
#             add_grade(subject, grade): Agrega una calificación a una asignatura.
#             calculate_average(): Calcula el promedio de calificaciones.

#     Clase School:
#         Atributos: Lista de estudiantes (students).
#         Métodos:
#             add_student(student: Student): Registra un estudiante.
#             list_students(): Lista todos los estudiantes.
#             find_student(name): Busca un estudiante por su nombre.
#             add_grade_to_student(name, subject, grade): Agrega calificación a un estudiante.

# Interfaz Interactiva:

# Crea un menú que permita:

#     Registrar estudiantes.
#     Agregar calificaciones a estudiantes.
#     Calcular promedios.
#     Buscar estudiantes.


class Student:
    def __init__(self, name: str, grades: dict):
        self.name = name
        self.grades = grades 

    def add_grade(self, subject: str, grade: float):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average_grade(self, subject: str) -> float:
        if subject in self.grades and self.grades[subject]:
            return sum(self.grades[subject]) / len(self.grades[subject])
        return 0.0

    def __str__(self) -> str:
        grades_info = ", ".join([f"{subject}: {grades}" for subject, grades in self.grades.items()])
        return f"Nombre del estudiante: {self.name}, Calificaciones: {{{grades_info}}}"

class School:
    def __init__(self):
        self.student_list = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise ValueError("Debes agregar un estudiante de clase Student")
        self.student_list.append(student)
        print(f"Estudiante {student.name} agregado correctamente.")

    def list_students(self):
        for student in self.student_list:
            print(student)

    def find_student(self, name):
        for student in self.student_list:
            if student.name == name:
                return student
        return None

    def add_grade_to_student(self, name, subject, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(subject, grade)
            print(f"Calificación {grade} añadida a {name} en {subject}")
        else:
            print(f"Estudiante {name} no encontrado.")

# Estudiantes de prueba
student1 = Student("Carlos", {"Math": [5, 4, 3, 2], "Programming": [4, 5], "Algorithms": [5]})
student2 = Student("Alberto", {"Computer": [5, 4, 3, 2], "Algorithms": [3, 4, 2]})
students = (student1, student2)

def run():
    school = School()
    while True:
        print("""
        === Menú Principal ===
        1 - Agregar estudiante de la lista predefinida
        2 - Listar estudiantes
        3 - Buscar estudiante por nombre
        4 - Agregar calificación a estudiante
        5 - Calcular promedio de una materia
        6 - Salir
        """)
        option = input("Elige una opción: ")

        if option == "1":
            student_name = input("Nombre del estudiante a agregar: ")
            found = False
            for s in students:
                if s.name == student_name:
                    school.add_student(s)
                    found = True
                    break
            if not found:
                print(f"No encontramos {student_name} en la lista")
        elif option == "2":
            school.list_students()
        elif option == "3":
            name = input("Nombre del estudiante: ")
            student = school.find_student(name)
            print(student if student else "No encontrado")
        elif option == "4":
            name = input("Nombre del estudiante: ")
            subject = input("Materia: ")
            try:
                grade = float(input("Nota: "))
                school.add_grade_to_student(name, subject, grade)
            except ValueError:
                print("Nota inválida.")
        elif option == "5":
            name = input("Nombre del estudiante: ")
            subject = input("Materia: ")
            student = school.find_student(name)
            if student:
                average = student.calculate_average_grade(subject)
                print(f"Promedio de {subject} para {name}: {average:.2f}")
            else:
                print("Estudiante no encontrado.")
        elif option == "6":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    run()