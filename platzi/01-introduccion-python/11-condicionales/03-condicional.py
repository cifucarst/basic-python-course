# Ejemplos practicos

# Clasificar edades
edad = 25

if edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
# Salida: Eres un adulto



# validar contrasena
usuario = "admin"
contraseña = "1234"

entrada_usuario = input("Usuario: ")
entrada_contraseña = input("Contraseña: ")

if entrada_usuario == usuario and entrada_contraseña == contraseña:
    print("Acceso concedido")
else:
    print("Acceso denegado")
