#  Ejercicio 1: Filtrar direcciones IP duplicadas
# Dado un conjunto de direcciones IP, elimina las duplicadas y muestra solo las únicas.

# 📌 Instrucciones:

# Crea una lista con direcciones IP (algunas repetidas).
# Convierte la lista en un conjunto para eliminar duplicados.
# Muestra las direcciones IP únicas.
# 🔹 Ejemplo de entrada:

# ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.2", "10.0.0.1"]
# 🔹 Salida esperada:

# {"192.168.1.1", "10.0.0.1", "172.16.0.2"}

ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.2", "10.0.0.1"]

def eliminar_duplicados(ips):
    return set(ips)

result = eliminar_duplicados(ips)
print(result)