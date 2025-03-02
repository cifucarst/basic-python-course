class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.__grades = grades if grades is not None else []  # Encapsulamiento

    def add_grade(self, grade):
        """Agrega una calificación válida entre 0 y 100."""
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("La calificación debe ser un número entre 0 y 100.")
        self.__grades.append(grade)

    def average_grade(self):
        """Calcula y devuelve el promedio de calificaciones o None si no hay calificaciones."""
        return sum(self.__grades) / len(self.__grades) if self.__grades else None

    def is_passing(self):
        """Retorna True si el promedio es mayor o igual a 60, False en caso contrario."""
        avg = self.average_grade()
        return avg is not None and avg >= 60

    def __str__(self):
        avg = self.average_grade()
        avg_text = f"Promedio: {avg:.2f}" if avg is not None else "Sin calificaciones"
        status = "Aprueba" if self.is_passing() else "Reprueba"
        return f"Estudiante: {self.name}, Edad: {self.age}, {avg_text}, Estado: {status}"

    @property
    def grades(self):
        """Permite acceder a las calificaciones sin modificarlas directamente."""
        return self.__grades.copy()

# Pruebas
student1 = Student("Arturo", 16, [55, 60, 23, 70])
student2 = Student("Sebastiana", 14, [80, 60, 100, 75])

print(student1)
print(student2)

# Agregar calificaciones válidas e inválidas
try:
    student1.add_grade(85)  # Correcto
    student1.add_grade(-4)  # Incorrecto
except ValueError as e:
    print(f"Error: {e}")

print(student1)