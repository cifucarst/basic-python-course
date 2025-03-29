### ✅ **Librería `collections` en Python**
La librería `collections` es un módulo del estándar de Python que proporciona estructuras de datos especializadas que extienden las capacidades de los tipos básicos como `dict`, `list`, `set` y `tuple`. Estas estructuras optimizan el rendimiento y facilitan la manipulación de datos.

---

### 📌 **1. `namedtuple()`**
Es una subclase de `tuple` que permite crear objetos inmutables con campos nombrados, lo que hace el código más legible y accesible.

✅ **Sintaxis**:
```python
from collections import namedtuple
Persona = namedtuple('Persona', ['nombre', 'edad'])
```

✅ **Ejemplo práctico**:
```python
from collections import namedtuple

# Definir el namedtuple
Persona = namedtuple('Persona', ['nombre', 'edad'])

# Crear una instancia
p = Persona(nombre='Ana', edad=30)

print(p)                 # Persona(nombre='Ana', edad=30)
print(p.nombre)          # Ana
print(p.edad)            # 30
```

👉 **¿Por qué usar `namedtuple`?**
- Es más eficiente en memoria que un `dict`.
- Hace que el código sea más descriptivo y fácil de leer.

---

### 📌 **2. `deque` (Double-Ended Queue)**
Es una lista optimizada para operaciones rápidas en ambos extremos (izquierda y derecha).

✅ **Sintaxis**:
```python
from collections import deque
```

✅ **Ejemplo práctico**:
```python
from collections import deque

# Crear una deque
cola = deque(['A', 'B', 'C'])

# Operaciones rápidas
cola.append('D')        # Añadir al final
cola.appendleft('Z')    # Añadir al inicio

print(cola)             # deque(['Z', 'A', 'B', 'C', 'D'])

# Eliminar elementos
cola.pop()              # Quita del final
cola.popleft()          # Quita del inicio

print(cola)             # deque(['A', 'B', 'C'])
```

👉 **¿Cuándo usar `deque`?**
- Cuando necesitas añadir o eliminar elementos con eficiencia en ambos extremos.

---

### 📌 **3. `Counter`**
Es una subclase de `dict` que cuenta la frecuencia de los elementos en un iterable.

✅ **Sintaxis**:
```python
from collections import Counter
```

✅ **Ejemplo práctico**:
```python
from collections import Counter

texto = "banana"

contador = Counter(texto)
print(contador)          # Counter({'a': 3, 'n': 2, 'b': 1})

# Obtener elementos más comunes
print(contador.most_common(2))  # [('a', 3), ('n', 2)]
```

👉 **¿Cuándo usar `Counter`?**
- Para contar ocurrencias en listas, cadenas u otros iterables.

---

### 📌 **4. `defaultdict`**
Es similar a un `dict`, pero proporciona un valor predeterminado para claves no existentes.

✅ **Sintaxis**:
```python
from collections import defaultdict
```

✅ **Ejemplo práctico**:
```python
from collections import defaultdict

# Crear un defaultdict con valor por defecto int (0)
contadores = defaultdict(int)

# Contar elementos
palabras = ['rojo', 'azul', 'rojo', 'verde']
for palabra in palabras:
    contadores[palabra] += 1

print(contadores)  # defaultdict(<class 'int'>, {'rojo': 2, 'azul': 1, 'verde': 1})
```

👉 **¿Cuándo usar `defaultdict`?**
- Cuando quieres evitar errores de `KeyError` y necesitas un valor predeterminado.

---

### 📌 **5. `OrderedDict`**
Es una subclase de `dict` que mantiene el orden de inserción de los elementos (en Python 3.7+ los `dict` normales ya mantienen el orden).

✅ **Sintaxis**:
```python
from collections import OrderedDict
```

✅ **Ejemplo práctico**:
```python
from collections import OrderedDict

# Crear un OrderedDict
ordenado = OrderedDict()
ordenado['a'] = 1
ordenado['b'] = 2
ordenado['c'] = 3

print(ordenado)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

👉 **¿Cuándo usar `OrderedDict`?**
- Cuando necesitas asegurarte de que el orden de los elementos es importante (en Python 3.7+ no suele ser necesario).

---

### 📌 **6. `ChainMap`**
Combina varios diccionarios en una única vista lógica.

✅ **Sintaxis**:
```python
from collections import ChainMap
```

✅ **Ejemplo práctico**:
```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combinado = ChainMap(dict1, dict2)
print(combinado)      # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print(combinado['b']) # 2 (Toma el primer valor encontrado)
```

👉 **¿Cuándo usar `ChainMap`?**
- Cuando deseas fusionar múltiples `dict` sin copiarlos.

---

## ✅ **Enumeraciones (`enum`) en Python**
El módulo `enum` permite crear conjuntos de valores con nombres (enumeraciones), mejorando la legibilidad y evitando errores en el código.

✅ **Sintaxis**:
```python
from enum import Enum
```

---

### 📌 **1. Crear una Enumeración**
```python
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
```

### 📌 **2. Acceder a los Miembros**
```python
print(DiaSemana.LUNES)    # DiaSemana.LUNES
print(DiaSemana.LUNES.name) # LUNES
print(DiaSemana.LUNES.value) # 1
```

---

### 📌 **3. Iterar en una `Enum`**
```python
for dia in DiaSemana:
    print(dia.name, dia.value)
```

✅ **Salida**:
```
LUNES 1
MARTES 2
MIERCOLES 3
```

---

### 📌 **4. Comparar Miembros de `Enum`**
```python
if DiaSemana.LUNES == DiaSemana.MARTES:
    print("Iguales")
else:
    print("Diferentes")  # Diferentes
```

---

### 📌 **5. `auto()` para Asignar Valores Automáticos**
```python
from enum import Enum, auto

class Color(Enum):
    ROJO = auto()
    VERDE = auto()
    AZUL = auto()

print(Color.ROJO.value)  # 1
print(Color.VERDE.value) # 2
```

---

### 📌 **6. Usar Enumeraciones en Funciones**
```python
def es_fin_de_semana(dia):
    return dia in (DiaSemana.SABADO, DiaSemana.DOMINGO)

print(es_fin_de_semana(DiaSemana.LUNES))   # False
```

👉 **¿Cuándo usar `enum`?**
- Cuando necesitas valores constantes con significado.
- Para evitar errores de comparación con cadenas o números.