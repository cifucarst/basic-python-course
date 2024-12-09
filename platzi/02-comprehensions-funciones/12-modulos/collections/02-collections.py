# 2. defaultdict
# Es similar a un diccionario normal, pero proporciona un valor predeterminado para claves que no existen.

# Ejemplo: Agrupar elementos por longitud


from collections import defaultdict

palabras = ["gato", "perro", "ratón", "pez"]
grupo = defaultdict(list)

for palabra in palabras:
    grupo[len(palabra)].append(palabra)

print(grupo)  # Salida: defaultdict(<class 'list'>, {4: ['gato', 'perro'], 5: ['ratón'], 3: ['pez']})