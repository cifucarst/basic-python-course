# Ejercicio 5: Calculadora de propinas

# Crea un programa que:

#     Solicite al usuario el total de una cuenta de restaurante (puede ser un número decimal).
#     Pregunte al usuario qué porcentaje de propina desea dejar (por ejemplo, 10, 15, 20).
#     Calcule el monto de la propina y el total a pagar.
#     Muestra los resultados con 2 decimales.


def calcular_propina(total_cuenta, porcentaje_propina):
    """Calcula el monto de la propina y el total a pagar.

    Args:
        total_cuenta: El total de la cuenta.
        porcentaje_propina: El porcentaje de propina a dejar.

    Returns:
        Una tupla con el monto de la propina y el total a pagar.
    """
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina
    return propina, total_a_pagar

if __name__ == "__main__":
    print("💵 Calculadora de propinas 💵\n")
    try:
        # Solicitar datos al usuario
        total = float(input("Ingrese el total de la cuenta: "))
        propina_porcentaje = float(input("Ingrese el porcentaje de propina (sin el símbolo %): "))

        # Validar entradas
        if total < 0 or propina_porcentaje < 0:
            print("❌ Por favor, ingrese valores positivos.")
        else:
            # Calcular propina y total
            propina, total_con_propina = calcular_propina(total, propina_porcentaje)

            # Mostrar resultados
            print("\n✅ Resultados:")
            print(f"- La propina es: ${propina:.2f}")
            print(f"- El total a pagar es: ${total_con_propina:.2f}")
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingrese números válidos.")
