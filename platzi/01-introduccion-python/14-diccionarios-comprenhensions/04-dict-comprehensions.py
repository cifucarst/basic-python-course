# Aplicaciones del mundo real
# Procesamiento de datos: Convertir datos no estructurados en diccionarios para análisis.

registros = ["Juan,23", "Ana,21", "Luis,25"]
diccionario = {registro.split(",")[0]: int(registro.split(",")[1]) for registro in registros}
print(diccionario)  
# Salida: {'Juan': 23, 'Ana': 21, 'Luis': 25}



# Optimización en algoritmos: Crear mapas o índices para búsquedas rápidas.

# Trabajo con APIs: Transformar respuestas de JSON en estructuras manejables.

# Generación de reportes: Contabilizar y agrupar información como ventas, resultados de encuestas, etc.

# 6. Buenas prácticas
# Evitar expresiones complejas: Mantén el código legible; si la expresión es muy compleja, considera usar un bucle for.
# Filtrar datos apropiadamente: Usa condiciones para asegurar que el diccionario solo contenga datos válidos.
# Usar nombres descriptivos: En bucles, usa nombres claros para mejorar la comprensión.