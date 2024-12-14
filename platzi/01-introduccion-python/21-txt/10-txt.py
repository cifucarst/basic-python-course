# Dividir un archivo grande en varios archivos pequeños
# Útil para procesar archivos de gran tamaño, como logs o datos.

# Código:


def dividir_archivo(archivo, lineas_por_archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    for i in range(0, len(lineas), lineas_por_archivo):
        with open(f"parte_{i // lineas_por_archivo + 1}.txt", "w") as salida:
            salida.writelines(lineas[i:i + lineas_por_archivo])

dividir_archivo("archivo_grande.txt", 100)
print("Archivo dividido en partes más pequeñas.")