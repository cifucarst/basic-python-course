# Concatenar múltiples archivos
# Supongamos que tienes varios archivos .txt y quieres combinarlos en uno solo.

# Código:


import glob

def concatenar_archivos(directorio, archivo_salida):
    archivos = glob.glob(f"{directorio}/*.txt")
    with open(archivo_salida, "w") as salida:
        for archivo in archivos:
            with open(archivo, "r") as entrada:
                salida.write(entrada.read() + "\n")

concatenar_archivos("archivos", "resultado.txt")
print("Archivos combinados exitosamente.")