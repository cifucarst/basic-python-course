____

## 📌 **Siguientes temas a explorar en POO:**

1. **Polimorfismo** (Sobrescritura y sobrecarga de métodos)
2. **Clases y métodos abstractos**
3. **Encapsulación y propiedades en Python**
4. **Composición en POO**
5. **Excepciones personalizadas en POO**
6. **Aplicación de POO en ciberseguridad**

Para mantener el aprendizaje práctico, empecemos con **polimorfismo**.

---

## 🔥 **1. Polimorfismo: La clave de la flexibilidad en POO**

### ¿Qué es?

Polimorfismo significa "muchas formas". En POO, esto permite que diferentes clases respondan de manera distinta al mismo método. Se logra de dos maneras principales:

1. **Sobrescritura de métodos (Overriding)**: Una subclase redefine un método heredado de la clase padre.
2. **Sobrecarga de métodos (Overloading)**: En Python, se logra usando argumentos con valores por defecto o con `*args` y `**kwargs`.

---

### 📌 **Ejemplo 1: Sobrescritura de métodos**

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def acceder(self):
        return f"{self.nombre} ha accedido al sistema."

class Administrador(Usuario):
    def acceder(self):
        return f"Administrador {self.nombre} ha accedido con permisos elevados."

class Invitado(Usuario):
    def acceder(self):
        return f"Invitado {self.nombre} ha accedido con permisos restringidos."

# Uso del polimorfismo
usuarios = [Administrador("Andrés"), Invitado("Carlos"), Usuario("Luis")]

for usuario in usuarios:
    print(usuario.acceder())  # Cada clase ejecuta su propia versión del método acceder()
```

### 🔥 **¿Qué notarás aquí?**

- **Cada clase redefine el método `acceder` a su manera**.
- **El mismo método se comporta de forma diferente según la clase que lo implemente**.

---

### 📌 **Ejemplo 2: Sobrecarga de métodos**

Python no soporta sobrecarga como Java o C++, pero podemos simularla con argumentos opcionales:

```python
class Calculadora:
    def sumar(self, a, b, c=0):  # c es opcional, por defecto es 0
        return a + b + c

calc = Calculadora()
print(calc.sumar(2, 3))      # 5 (usa solo dos argumentos)
print(calc.sumar(2, 3, 4))   # 9 (usa tres argumentos)
```

Aquí, el método `sumar` se adapta según la cantidad de argumentos.

---

## 🚀 **Ejercicio práctico**

Crea una jerarquía de clases para representar **distintos tipos de dispositivos de seguridad** en una red (firewall, IDS, antivirus).  
Cada dispositivo debe sobrescribir un método `analizar_trafico()`, con un comportamiento específico.

Ejemplo de ejecución esperada:

```python
dispositivos = [Firewall(), IDS(), Antivirus()]

for d in dispositivos:
    print(d.analizar_trafico())
```

Salida esperada:

```
El firewall está bloqueando tráfico sospechoso.
El IDS está detectando patrones maliciosos.
El antivirus está escaneando archivos en busca de malware.
```

🔹 **Objetivos:**

- Aplicar **sobrescritura de métodos**.
- Usar **polimorfismo** para manejar diferentes dispositivos de forma uniforme.

💡 **Resuelve el ejercicio y compárteme tu código!** 🚀