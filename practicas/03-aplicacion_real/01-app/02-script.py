import bcrypt

class User:
    def __init__(self, name, password):
        self.name = name
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    def __str__(self):
        return f"User(name={self.name})"

# Uso de ejemplo
user1 = User("Juan", "password123")

# Mostrar usuario
print(user1)

# Verificar contraseñas
if user1.verify_password("password123"):
    print("Contraseña correcta ✅")
else:
    print("Contraseña incorrecta ❌")