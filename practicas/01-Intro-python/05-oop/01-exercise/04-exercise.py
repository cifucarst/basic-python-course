import logging

# Configurar logs para auditoría de accesos no autorizados
logging.basicConfig(filename="security.log", level=logging.WARNING, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Student:
    def __init__(self, name, age, role="student", grades=None):
        """Inicializa un estudiante con validaciones y roles de acceso."""
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena válida.")
        if not isinstance(age, int) or not (5 <= age <= 100):
            raise ValueError("La edad debe ser un número entre 5 y 100.")
        if role not in ["admin", "professor", "student"]:
            raise ValueError("El rol debe ser 'admin', 'professor' o 'student'.")

        self.name = name
        self.age = age
        self.role = role  # Define el rol del usuario
        self.__grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Solo los 'admin' pueden agregar calificaciones."""
        if self.role != "admin":
            logging.warning(f"Intento no autorizado de agregar calificación por {self.name} (Rol: {self.role})")
            raise PermissionError("No tienes permiso para agregar calificaciones.")

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

    def get_grades(self):
        """Solo los 'admin' y 'professor' pueden ver las calificaciones."""
        if self.role not in ["admin", "professor"]:
            logging.warning(f"Intento no autorizado de ver calificaciones por {self.name} (Rol: {self.role})")
            raise PermissionError("No tienes permiso para ver las calificaciones.")

        return self.__grades.copy()

    def __str__(self):
        """Muestra información basada en el rol del usuario."""
        avg = self.average_grade()
        avg_text = f"Promedio: {avg:.2f}" if avg is not None else "Sin calificaciones"
        
        if self.role == "admin":
            return f"[ADMIN] {self.name}, Edad: {self.age}, {avg_text}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}, Notas: {self.__grades}"
        
        elif self.role == "professor":
            return f"[PROFESSOR] {self.name}, Edad: {self.age}, {avg_text}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}"
        
        else:  # student
            return f"[STUDENT] {self.name}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}"

# Pruebas con roles
try:
    admin = Student("Dr. Smith", 40, "admin", [90, 85, 78])
    professor = Student("Ms. Johnson", 35, "professor", [88, 92, 79])
    student = Student("Arturo", 16, "student", [55, 60, 23, 70])

    print(admin)  # Ver todo
    print(professor)  # Ver sin notas
    print(student)  # Ver solo si aprueba o reprueba

    # Agregar calificaciones (solo admin puede)
    admin.add_grade(95)
    print(admin)

    # Intentar agregar calificación sin permiso
    professor.add_grade(85)  # Debería fallar
except (ValueError, PermissionError) as e:
    print(f"Error: {e}")

# Intentar ver notas sin permiso
try:
    print(student.get_grades())  # No debería tener acceso
except PermissionError as e:
    print(f"Acceso denegado: {e}")