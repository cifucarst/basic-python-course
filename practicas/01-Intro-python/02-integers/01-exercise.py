# Ejercicio 1: Calculadora básica

# Crea un programa que:

#     Solicite al usuario que introduzca dos números (pueden ser enteros o decimales).
#     Realice y muestre las operaciones de suma, resta, multiplicación y división.
#     Muestra el resultado con 2 decimales para las operaciones con decimales.

def sumar():
    num1, num2 = askInfo()
    return num1 + num2

def restar():
    num1, num2 = askInfo()
    return num1 - num2

def multiplicar():
    num1, num2 = askInfo()
    return num1 * num2

def dividir():
    num1, num2 = askInfo()
    if num2 == 0:
        raise ZeroDivisionError("❌ No se puede dividir entre cero.")
    return num1 / num2

def askInfo():
    num_uno = float(input('👉 Escribe el primer número: '))
    num_dos = float(input('👉 Escribe el segundo número: '))
    return num_uno, num_dos

def run():
    while True:
        menu = """
        📟 Bienvenido a tu calculadora 📟

        1️⃣ - Sumar
        2️⃣ - Restar
        3️⃣ - Multiplicar
        4️⃣ - Dividir
        5️⃣ - Salir
        """
        print(menu)
        
        try:
            option = int(input("Elige una opción: "))
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número del 1 al 5.")
            continue

        if option == 1:
            print(f"Resultado: {sumar():.2f}")
        elif option == 2:
            print(f"Resultado: {restar():.2f}")
        elif option == 3:
            print(f"Resultado: {multiplicar():.2f}")
        elif option == 4:
            try:
                print(f"Resultado: {dividir():.2f}")
            except ZeroDivisionError as e:
                print(e)
        elif option == 5:
            print("👋 ¡Gracias por usar la calculadora! Hasta pronto.")
            break
        else:
            print("❌ Opción inválida. Por favor, elige un número entre 1 y 5.")

if __name__ == '__main__':
    run()