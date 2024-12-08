# Ejemplo 2: Sistema de permisos con decoradores
# Descripción:
# Crear un sistema donde funciones específicas solo puedan ejecutarse si el usuario tiene permisos adecuados.


def requiere_permiso(permiso_requerido):
    def decorador(func):
        def envoltura(usuario, *args, **kwargs):
            if permiso_requerido in usuario["permisos"]:
                return func(usuario, *args, **kwargs)
            else:
                raise PermissionError(f"Usuario no tiene permiso: {permiso_requerido}")
        return envoltura
    return decorador

# Definir funciones con permisos
@requiere_permiso("admin")
def eliminar_usuario(usuario, user_id):
    return f"Usuario {user_id} eliminado por {usuario['nombre']}"

# Crear usuarios
admin = {"nombre": "Andrés", "permisos": ["admin", "editar"]}
visitante = {"nombre": "Juanito", "permisos": ["ver"]}

# Probar
print(eliminar_usuario(admin, 42))  # Salida: Usuario 42 eliminado por Andrés
# print(eliminar_usuario(visitante, 42))  # Error: PermissionError