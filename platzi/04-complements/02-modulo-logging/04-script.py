import logging

# Configurar el logging para registrar en un archivo
logging.basicConfig(filename='intentos_login.log', level=logging.WARNING, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Simulación de intentos de inicio de sesión
usuarios = {
    "admin": "password123",
    "user1": "123456",
}

def autenticar(usuario, clave):
    if usuario not in usuarios:
        logging.warning(f"Intento de acceso con usuario no registrado: {usuario}")
        return False
    elif usuarios[usuario] != clave:
        logging.error(f"Fallo de autenticación para el usuario: {usuario}")
        return False
    else:
        logging.info(f"Acceso exitoso para el usuario: {usuario}")
        return True

# Simulación de intentos de inicio de sesión
autenticar("admin", "wrongpass")
autenticar("user2", "123456")
autenticar("admin", "password123")