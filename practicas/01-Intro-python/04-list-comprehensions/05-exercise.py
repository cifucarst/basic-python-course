# Ejercicio 5: Filtrar y convertir

# Dada la lista de cadenas frutas = ["manzana", "naranja", "uva", "kiwi", "mango"], genera 
# una lista con las frutas que contienen la letra "a", pero convierte sus nombres a mayúsculas.

frutas = ["manzana", "naranja", "uva", "kiwi", "mango"]

lista_final = [fruta.upper() for fruta in frutas if 'a' in fruta]
print(lista_final)