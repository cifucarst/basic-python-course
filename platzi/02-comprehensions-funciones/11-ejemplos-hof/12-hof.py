# Ejemplo 5: Generar pipelines de tareas asíncronas
# Descripción:
# Implementar un pipeline donde cada tarea es una función asíncrona.


import asyncio

async def obtener_datos():
    await asyncio.sleep(1)  # Simula una operación lenta
    return [1, 2, 3, 4, 5]

async def procesar_datos(datos):
    await asyncio.sleep(1)  # Simula procesamiento
    return [x * 2 for x in datos]

async def guardar_datos(datos):
    await asyncio.sleep(1)  # Simula guardado
    print(f"Datos guardados: {datos}")
    return True

async def pipeline_asincrono():
    datos = await obtener_datos()
    datos_procesados = await procesar_datos(datos)
    exito = await guardar_datos(datos_procesados)
    return exito

# Ejecutar el pipeline asíncrono
asyncio.run(pipeline_asincrono())  # Salida: Datos guardados: [2, 4, 6, 8, 10]