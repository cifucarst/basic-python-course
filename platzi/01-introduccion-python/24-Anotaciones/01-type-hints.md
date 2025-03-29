Los **Type Hints** en Python son anotaciones que permiten especificar los tipos de datos esperados en variables, parámetros de funciones y valores de retorno. Aunque Python es un lenguaje dinámico (no requiere declarar los tipos de las variables explícitamente), los **Type Hints** ayudan a mejorar la legibilidad, detectar errores en tiempo de desarrollo y facilitar el uso de herramientas como **mypy** para análisis estático de tipos.

---

## **Ejemplo Básico**
```python
def suma(a: int, b: int) -> int:
    return a + b
```
Aquí, `a` y `b` están anotados como **`int`**, y el retorno de la función también es un **`int`**.

Sin embargo, estas anotaciones no afectan la ejecución del código, solo sirven como guía.

---

## **Uso en Variables**
```python
nombre: str = "Andrés"
edad: int = 25
activo: bool = True
```
Esto no impide que la variable cambie a otro tipo en tiempo de ejecución, pero ayuda a herramientas de análisis de código.

---

## **Type Hints Avanzados**
La librería **`typing`** proporciona tipos más avanzados:

### **Listas y Diccionarios**
```python
from typing import List, Dict

numeros: List[int] = [1, 2, 3, 4, 5]
edades: Dict[str, int] = {"Andrés": 25, "Juan": 30}
```

### **Tuplas y Conjuntos**
```python
from typing import Tuple, Set

coordenadas: Tuple[float, float] = (19.45, -99.13)
colores: Set[str] = {"rojo", "azul", "verde"}
```

### **Funciones con Varios Tipos (Union)**
```python
from typing import Union

def obtener_longitud(objeto: Union[str, list]) -> int:
    return len(objeto)
```
Aquí, `objeto` puede ser una **cadena (`str`) o una lista (`list`)**.

---

## **Aplicación en Ciberseguridad**
### **Ejemplo: Filtrar direcciones IP válidas**
```python
from typing import List
import re

def filtrar_ips_validas(ips: List[str]) -> List[str]:
    patron_ip = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    return [ip for ip in ips if re.match(patron_ip, ip)]

lista_ips = ["192.168.1.1", "300.200.100.50", "10.0.0.1", "invalid_ip"]
print(filtrar_ips_validas(lista_ips))
```
🔹 Aquí, **`List[str]`** indica que la función recibe y devuelve una lista de cadenas.