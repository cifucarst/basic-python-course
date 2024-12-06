# Ejercicio 2: Inventario de Productos

# Crea un programa en Python que implemente un sistema básico para gestionar un inventario de productos en una tienda.
# Requisitos:

#     Clase Product:
#         Atributos:
#             name: Nombre del producto.
#             price: Precio del producto (float).
#             stock: Cantidad en inventario (entero).
#         Métodos:
#             add_stock(quantity): Aumenta la cantidad en inventario.
#             sell(quantity): Reduce la cantidad en inventario. Si no hay suficiente stock, debe lanzar un error.
#             __str__: Devuelve una representación amigable del producto.

#     Clase Inventory:
#         Atributos:
#             products: Una lista de objetos Product que representa el inventario.
#         Métodos:
#             add_product(product): Agrega un producto al inventario.
#             find_product(name): Busca un producto por nombre y lo devuelve. Si no existe, lanza un error.
#             sell_product(name, quantity): Reduce el inventario del producto especificado.
#             list_products(): Muestra todos los productos del inventario.

# Prueba el código:

#     Crea un inventario.
#     Agrega al menos tres productos.
#     Realiza algunas ventas y añade stock.
#     Intenta vender una cantidad mayor a la disponible y maneja el error.

class Product:
    def __init__(self, nombre: str, precio: float, stock: int):
        if not isinstance(nombre, str):
            raise ValueError("Debes ingresar un nombre de producto válido")
        if not isinstance(precio, (float, int)):
            raise ValueError("Debes ingresar un precio válido")
        if not isinstance(stock, int):
            raise ValueError("Debes ingresar un stock válido")

        self.nombre = nombre
        self.precio = float(precio)
        self.stock = stock

    def add_stock(self, quantity):
        if quantity > 0 and isinstance(quantity, int):
            self.stock += quantity
        else:
            raise ValueError("La cantidad debe ser un número entero positivo")

    def sell(self, quantity):
        if quantity > 0 and isinstance(quantity, int) and quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError(f"No se puede vender la cantidad solicitada ({quantity}). Stock disponible: {self.stock}")

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock} unidades"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Solo puedes agregar objetos de tipo Product al inventario")
        self.products.append(product)

    def find_product(self, name):
        for product in self.products:
            if product.nombre.lower() == name.lower():
                return product
        raise ValueError(f"Producto con nombre '{name}' no encontrado en el inventario")

    def sell_product(self, name, quantity):
        product = self.find_product(name)
        product.sell(quantity)

    def remove_product(self, name):
        for product in self.products:
            if product.nombre.lower() == name.lower():
                self.products.remove(product)
                print(f"Producto '{name}' eliminado del inventario.")
                return
        raise ValueError(f"Producto con nombre '{name}' no encontrado en el inventario")

    def list_products(self):
        if not self.products:
            print("El inventario está vacío.")
        else:
            for product in self.products:
                print(product)


def menu():
    inventario = Inventory()

    while True:
        print("\n=== Menú de Inventario ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Vender producto")
        print("4. Agregar stock a un producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                stock = int(input("Cantidad en inventario: "))
                producto = Product(nombre, precio, stock)
                inventario.add_product(producto)
                print(f"Producto '{nombre}' agregado al inventario.")

            elif opcion == "2":
                print("\n=== Lista de productos ===")
                inventario.list_products()

            elif opcion == "3":
                nombre = input("Nombre del producto a vender: ")
                cantidad = int(input("Cantidad a vender: "))
                inventario.sell_product(nombre, cantidad)
                print(f"Se vendieron {cantidad} unidades de '{nombre}'.")

            elif opcion == "4":
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad a agregar al stock: "))
                producto = inventario.find_product(nombre)
                producto.add_stock(cantidad)
                print(f"Se agregaron {cantidad} unidades al stock de '{nombre}'.")

            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                inventario.remove_product(nombre)

            elif opcion == "6":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")


# Ejecutar el menú interactivo
menu()