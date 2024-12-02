# sintaxis basica
variable = input("Mensaje al usuario: ")

# ejemplo basico
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")


# conversion de tipos
edad = input("¿Cuántos años tienes? ")
edad = int(edad)  # Conversión explícita a entero
print(f"Tendrás {edad + 1} años el próximo año.")


# validar un numero decimal
altura = input("Introduce tu altura en metros: ")
altura = float(altura)  # Conversión explícita a flotante
print(f"Tu altura es {altura} metros.")


# como manejar multiples entradas
datos = input("Introduce tu nombre y edad separados por un espacio: ").split()
nombre = datos[0]
edad = int(datos[1])
print(f"Hola, {nombre}. Tienes {edad} años.")