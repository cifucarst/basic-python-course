import hashlib
import logging

# Configurar logs de seguridad
logging.basicConfig(filename="security.log", level=logging.WARNING, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class User:
    """Clase para gestionar usuarios con autenticación y roles."""
    users_db = {}  # Simula una base de datos de usuarios

    def __init__(self, username, password, role="student"):
        """Registra un usuario con nombre, contraseña encriptada y rol."""
        if role not in ["admin", "professor", "student"]:
            raise ValueError("Rol inválido. Debe ser 'admin', 'professor' o 'student'.")

        self.username = username
        self.role = role
        self.__password = self.hash_password(password)
        User.users_db[username] = self  # Almacenar usuario

    def hash_password(self, password):
        """Convierte la contraseña en un hash seguro usando SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verifica si la contraseña ingresada coincide con el hash almacenado."""
        return self.__password == self.hash_password(password)

    @classmethod
    def authenticate(cls, username, password):
        """Autentica un usuario verificando su contraseña."""
        user = cls.users_db.get(username)
        if user and user.verify_password(password):
            return user
        logging.warning(f"Intento de acceso fallido para usuario: {username}")
        raise PermissionError("Usuario o contraseña incorrectos.")

class Student:
    """Clase para gestionar estudiantes con permisos basados en roles."""
    def __init__(self, name, age, user, grades=None):
        """Inicializa un estudiante con validaciones y autenticación."""
        if not isinstance(user, User):
            raise ValueError("Debe asignarse un usuario válido al estudiante.")
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena válida.")
        if not isinstance(age, int) or not (5 <= age <= 100):
            raise ValueError("La edad debe ser un número entre 5 y 100.")

        self.name = name
        self.age = age
        self.user = user  # Asigna un usuario con permisos
        self.__grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Solo los 'admin' pueden agregar calificaciones."""
        if self.user.role != "admin":
            logging.warning(f"Intento no autorizado de agregar calificación por {self.user.username} (Rol: {self.user.role})")
            raise PermissionError("No tienes permiso para agregar calificaciones.")

        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            logging.warning(f"Intento de agregar calificación inválida: {grade} por {self.user.username}")
            raise ValueError("La calificación debe ser un número entre 0 y 100.")

        self.__grades.append(grade)

    def average_grade(self):
        """Calcula y devuelve el promedio de calificaciones."""
        return sum(self.__grades) / len(self.__grades) if self.__grades else None

    def is_passing(self):
        """Retorna True si el promedio es mayor o igual a 60, False en caso contrario."""
        avg = self.average_grade()
        return avg is not None and avg >= 60

    def get_grades(self):
        """Solo 'admin' y 'professor' pueden ver las calificaciones."""
        if self.user.role not in ["admin", "professor"]:
            logging.warning(f"Intento no autorizado de ver calificaciones por {self.user.username} (Rol: {self.user.role})")
            raise PermissionError("No tienes permiso para ver las calificaciones.")

        return self.__grades.copy()

    def __str__(self):
        """Muestra información basada en el rol del usuario autenticado."""
        avg = self.average_grade()
        avg_text = f"Promedio: {avg:.2f}" if avg is not None else "Sin calificaciones"
        
        if self.user.role == "admin":
            return f"[ADMIN] {self.name}, Edad: {self.age}, {avg_text}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}, Notas: {self.__grades}"
        
        elif self.user.role == "professor":
            return f"[PROFESSOR] {self.name}, Edad: {self.age}, {avg_text}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}"
        
        else:  # student
            return f"[STUDENT] {self.name}, Estado: {'Aprueba' if self.is_passing() else 'Reprueba'}"

# --- PRUEBAS ---

# Crear usuarios con diferentes roles
admin_user = User("admin1", "securepassword", "admin")
professor_user = User("professor1", "teachsecure", "professor")
student_user = User("student1", "studentpass", "student")

# Intento de autenticación
try:
    logged_user = User.authenticate("admin1", "securepassword")  # Correcto
    print(f"Autenticado como: {logged_user.username}, Rol: {logged_user.role}")
except PermissionError as e:
    print(f"Error de autenticación: {e}")

try:
    logged_user = User.authenticate("student1", "wrongpassword")  # Fallará
except PermissionError as e:
    print(f"Error de autenticación: {e}")

# Crear estudiantes con usuarios autenticados
student1 = Student("Arturo", 16, admin_user, [55, 60, 23, 70])
student2 = Student("Sebastiana", 14, professor_user, [80, 60, 100, 75])

# Ver información según permisos
print(student1)
print(student2)

# Agregar calificación (solo admin puede)
try:
    student1.add_grade(95)  # Correcto
    print("Nueva calificación agregada.")
except PermissionError as e:
    print(f"Acceso denegado: {e}")

# Intento de agregar calificación sin permiso
try:
    student2.add_grade(85)  # Fallará porque el usuario es "professor"
except PermissionError as e:
    print(f"Acceso denegado: {e}")

# Intento de ver calificaciones sin permiso
try:
    print(student1.get_grades())  # Solo admin y professor pueden ver
except PermissionError as e:
    print(f"Acceso denegado: {e}")