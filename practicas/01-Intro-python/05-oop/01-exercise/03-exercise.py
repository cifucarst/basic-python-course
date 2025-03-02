import logging

# Configurar logs para auditoría
logging.basicConfig(filename="student_activity.log", level=logging.WARNING, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Student:
    def __init__(self, name, age, grades=None):
        """Inicializa un estudiante con validaciones de seguridad."""
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena válida.")
        if not isinstance(age, int) or not (5 <= age <= 100):  
            raise ValueError("La edad debe ser un número entero entre 5 y 100.")
        
        self.name = name
        self.age = age
        self.__grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Agrega una calificación validada y registra intentos sospechosos."""
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            logging.warning(f"Intento de agregar calificación inválida: {grade} por {self.name}")
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
        """Evita exposición excesiva de datos."""
        avg = self.average_grade()
        avg_text = f"Promedio: {avg:.2f}" if avg is not None else "Sin calificaciones"
        return f"Estudiante: {self.name}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}"

    @property
    def grades(self):
        """Devuelve una copia de las calificaciones para evitar manipulación directa."""
        return self.__grades.copy()

# Pruebas con validaciones de seguridad
try:
    student1 = Student("Arturo", 16, [55, 60, 23, 70])
    student2 = Student("Sebastiana", 14, [80, 60, 100, 75])
    
    print(student1)
    print(student2)
    
    student1.add_grade(85)  # Calificación válida
    student1.add_grade(-10)  # Intento inválido -> Se registrará en logs

except ValueError as e:
    print(f"Error: {e}")