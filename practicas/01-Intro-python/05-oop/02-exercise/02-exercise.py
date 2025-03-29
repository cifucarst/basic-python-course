import re

class Product:
    def __init__(self, nombre: str, precio: float, stock: int):
        # Validar nombre (solo letras, números, espacios y guiones bajos)
        if not re.match(r'^[a-zA-Z0-9_ ]+$', nombre):
            raise ValueError("El nombre del producto contiene caracteres no permitidos.")

        if not (0 <= precio <= 1000000):
            raise ValueError("El precio debe estar entre 0 y 1,000,000.")

        if not (0 <= stock <= 100000):
            raise ValueError("El stock debe estar entre 0 y 100,000.")

        self.nombre = nombre
        self.precio = float(precio)
        self.stock = stock

    def add_stock(self, quantity):
        if quantity > 0 and isinstance(quantity, int):
            self.stock += quantity
        else:
            raise ValueError("La cantidad debe ser un número entero positivo")

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a 0.")
        if quantity > self.stock:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}")
        self.stock -= quantity

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock} unidades"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Solo puedes agregar objetos de tipo Product al inventario")

        # Evitar duplicados
        for p in self.products:
            if p.nombre.lower() == product.nombre.lower():
                raise ValueError("El producto ya existe en el inventario.")

        self.products.append(product)
        print(f"Producto '{product.nombre}' agregado con éxito.")

    def find_product(self, name):
        for product in self.products:
            if product.nombre.lower() == name.lower():
                return product
        raise ValueError("Producto no encontrado.")

    def sell_product(self, name, quantity):
        product = self.find_product(name)
        product.sell(quantity)
        print(f"Se vendieron {quantity} unidades de '{name}'.")

    def remove_product(self, name):
        product = self.find_product(name)
        self.products.remove(product)
        print(f"Producto '{name}' eliminado con éxito.")

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

        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: ").strip())
                stock = int(input("Cantidad en inventario: ").strip())

                producto = Product(nombre, precio, stock)
                inventario.add_product(producto)

            elif opcion == "2":
                inventario.list_products()

            elif opcion == "3":
                nombre = input("Nombre del producto a vender: ").strip()
                cantidad = int(input("Cantidad a vender: ").strip())
                inventario.sell_product(nombre, cantidad)

            elif opcion == "4":
                nombre = input("Nombre del producto: ").strip()
                cantidad = int(input("Cantidad a agregar al stock: ").strip())
                producto = inventario.find_product(nombre)
                producto.add_stock(cantidad)

            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ").strip()
                inventario.remove_product(nombre)

            elif opcion == "6":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Inténtalo de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print("Ha ocurrido un error inesperado. Contacta al administrador.")


if __name__ == "__main__":
    menu()
