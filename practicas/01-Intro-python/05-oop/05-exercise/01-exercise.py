# Sistema de Tienda Virtual

# Crea una aplicación para gestionar una tienda virtual que maneje productos y clientes.
# Requerimientos:

#     Clase Customer:
#         Atributos: name, cart (lista de productos).
#         Métodos:
#             add_to_cart(product: Product): Agrega un producto al carrito.
#             checkout(): Muestra los productos del carrito y calcula el total.

#     Clase Product:
#         Atributos: name, price, stock.
#         Métodos:
#             reduce_stock(quantity): Reduce el stock del producto.

#     Clase Store:
#         Atributos: Listas de productos y clientes.
#         Métodos:
#             add_product(product: Product): Agrega productos al inventario.
#             list_products(): Muestra los productos disponibles.
#             add_customer(customer: Customer): Registra nuevos clientes.
#             find_product(name): Busca un producto por nombre.
#             sell_product(customer_name, product_name, quantity): Gestiona la venta.

# Interfaz Interactiva:

# Crea un menú que permita:

#     Registrar nuevos clientes.
#     Listar productos disponibles.
#     Agregar productos al carrito de un cliente.
#     Realizar el pago del carrito.
#     Agregar o eliminar productos del inventario.


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"No hay suficiente stock para {self.name}. Stock disponible: {self.stock}")
            return False

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Stock: {self.stock})"


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def checkout(self):
        total = 0
        print(f"\n--- Factura de {self.name} ---")
        for product, quantity in self.cart:
            subtotal = product.price * quantity
            print(f"{product.name} x{quantity}: ${subtotal:.2f}")
            total += subtotal
        print(f"Total: ${total:.2f}\n")
        self.cart = []  # Vaciar el carrito después de la compra


class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if not self.products:
            print("No hay productos disponibles.")
        else:
            print("\n--- Productos Disponibles ---")
            for product in self.products:
                print(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def find_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None

    def sell_product(self, customer_name, product_name, quantity):
        customer = self.find_customer_by_name(customer_name)
        product = self.find_product(product_name)

        if not customer:
            print(f"Cliente '{customer_name}' no encontrado.")
            return
        if not product:
            print(f"Producto '{product_name}' no encontrado.")
            return
        if product.reduce_stock(quantity):
            customer.add_to_cart(product, quantity)
            print(f"{quantity} unidad(es) de {product.name} agregadas al carrito de {customer.name}.")
        else:
            print(f"No se pudo agregar {product_name} al carrito de {customer_name}.")


# Crear una instancia de la tienda
store = Store()

# Agregar productos de ejemplo
store.add_product(Product("Manzana", 1.5, 10))
store.add_product(Product("Banana", 0.8, 5))
store.add_product(Product("Naranja", 1.2, 8))

# Menú interactivo
while True:
    print("\n--- Tienda Virtual ---")
    print("1. Registrar nuevo cliente")
    print("2. Listar productos")
    print("3. Agregar producto al carrito")
    print("4. Realizar pago")
    print("5. Salir")
    option = input("Seleccione una opción: ")

    if option == "1":
        name = input("Ingrese el nombre del cliente: ").strip()
        if store.find_customer_by_name(name):
            print("Este cliente ya está registrado.")
        else:
            store.add_customer(Customer(name))
            print(f"Cliente '{name}' registrado con éxito.")
    elif option == "2":
        store.list_products()
    elif option == "3":
        customer_name = input("Ingrese el nombre del cliente: ").strip()
        product_name = input("Ingrese el nombre del producto: ").strip()
        try:
            quantity = int(input("Ingrese la cantidad: "))
            if quantity <= 0:
                print("La cantidad debe ser un número positivo.")
            else:
                store.sell_product(customer_name, product_name, quantity)
        except ValueError:
            print("Debe ingresar un número válido para la cantidad.")
    elif option == "4":
        customer_name = input("Ingrese el nombre del cliente: ").strip()
        customer = store.find_customer_by_name(customer_name)
        if customer:
            customer.checkout()
        else:
            print("Cliente no encontrado.")
    elif option == "5":
        print("Gracias por usar la Tienda Virtual. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")