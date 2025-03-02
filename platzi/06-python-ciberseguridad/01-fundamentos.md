 Comenzaremos con los fundamentos de la Programación Orientada a Objetos (POO) en Python. Lo haré paso a paso, explicando cada concepto con ejemplos prácticos orientados a ciberseguridad.

---

### **Lección 1: Introducción a la Programación Orientada a Objetos (POO)**

#### **¿Qué es la POO?**
La POO es un paradigma de programación que organiza el código en torno a **objetos** y **clases**, en lugar de funciones y procedimientos como en la programación estructurada. Es muy útil en ciberseguridad porque nos permite modelar y manejar estructuras complejas, como usuarios, conexiones de red o dispositivos, de manera más eficiente y modular.

---

#### **Conceptos clave de la POO**

1. **Clases**: Son plantillas o moldes para crear objetos. Definen las características (atributos) y comportamientos (métodos) de los objetos.
2. **Objetos**: Instancias de una clase. Representan elementos concretos que tienen atributos y pueden realizar acciones.
3. **Atributos**: Variables que almacenan datos de un objeto.
4. **Métodos**: Funciones que realizan acciones en los objetos.
5. **Encapsulamiento**: Restricción del acceso directo a los datos de un objeto.
6. **Herencia**: Permite que una clase herede atributos y métodos de otra.
7. **Polimorfismo**: Permite usar un mismo método con diferentes tipos de objetos.

---

#### **Ejemplo práctico inicial: Modelando usuarios de un sistema**

Imaginemos que necesitamos gestionar usuarios en un sistema, algo muy común en ciberseguridad (por ejemplo, usuarios con diferentes roles y permisos).

```python
# Definimos la clase Usuario
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre  # Atributo para el nombre del usuario
        self.rol = rol        # Atributo para el rol (ejemplo: admin, usuario, invitado)
    
    def mostrar_informacion(self):
        # Método para mostrar información del usuario
        print(f"Nombre: {self.nombre}, Rol: {self.rol}")

# Creamos un objeto de la clase Usuario
usuario1 = Usuario("Andrés", "admin")

# Llamamos al método mostrar_informacion
usuario1.mostrar_informacion()
```

---

#### **Explicación del código:**
1. La clase `Usuario` tiene dos **atributos** (`nombre` y `rol`) y un **método** (`mostrar_informacion`).
2. El método especial `__init__` se ejecuta automáticamente al crear un objeto de la clase. Sirve para inicializar los atributos.
3. Creamos un objeto `usuario1` con la clase `Usuario` y le asignamos un nombre y un rol.
4. Llamamos al método `mostrar_informacion` para mostrar los datos del usuario.

---

#### **Tarea práctica:**
1. Modifica la clase para agregar un atributo adicional llamado `contraseña`.
2. Crea un método llamado `verificar_contraseña` que reciba una contraseña como argumento y compare si coincide con la del usuario.
3. Prueba la clase con diferentes contraseñas.