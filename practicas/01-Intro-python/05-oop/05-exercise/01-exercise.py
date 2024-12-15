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
        if isinstance(quantity, int) and quantity > 0  and quantity <= self.stock:
            self.stock -= quantity
            print(f'Cantidad de {self.name} en stock es: {self.stock}')
    
    def __str__(self):
        return f'Producto: {self.name}, precio ${self.price}, cantidad {self.stock}'


class Customer:
    def __init__(self, name: str):
        self.name = name 
        self.cart = []

    def add_to_cart(self, product: Product):
        if isinstance(product, Product):
            self.cart.append(product)
       
    def checkout(self):
        if len(self.cart) > 0:
            print('Productos agregados al carrito de compras')
            for product in self.cart:
                print(product)
        
    def __str__(self):
        return f'El cliente {self.name}, {"tiene" if self.cart else "no tiene"} productos agregados'

class Store:
    def __init__(self):
        self.customers = []
        self.products = []

    def add_product(self, product: Product): 
        # Agrega productos al inventario.
        self.products.append(product)
        print(f'producto {product.name} con {product.stock}, agregado al inventario')

    def list_products(self): 
        # Muestra los productos disponibles.
        if len(self.products) > 0:
            for product in self.products:
                print(product)


    def add_customer(self, customer: Customer): 
        # Registra nuevos clientes.
        self.customers.append(customer)
        print(f'{customer.name} agregado correctamente.')

    def list_customers(self):
        if not self.customers:
            print('❌ Aún no hay clientes agregados a la tienda.')
            return
        print('Clientes en la tienda:')
        for customer in self.customers:
            print(f'✅ {customer}')
    
    def find_product(name): 
        # Busca un producto por nombre.
        pass
            
    def sell_product(customer_name, product_name, quantity): 
        # Gestiona la venta.
        pass


# Interfaz Interactiva:

# Crea un menú que permita:

    # Registrar nuevos clientes.
    # Listar productos disponibles.
    # Agregar productos al carrito de un cliente.
    # Realizar el pago del carrito.
    # Agregar o eliminar productos del inventario.

while True:
    store = Store()
    print("""
        Bienvenido a tu tienda virtual favorita.
        
            1 - Registrar nuevos clientes.
            2 - Listar clientes
            3 - Listar productos disponibles.
            4 - Agregar productos al carrito de un cliente.
            5 - Realizar el pago del carrito.
            6 - Agregar o eliminar productos del inventario.
            7 - salir
          
""")
    
    opcion = int(input('Elige una opcion (del 1 al 6): '))

    if opcion == 1:
        name = input('Escribe tu nombre: ')
        user = Customer(name)
        store.add_customer(user)
    elif opcion == 2:
        store.list_customers()
    elif opcion == 7:
        print('Gracias por visitar esta gran tienda, vuelva cuando quieras!')
        break
    else:
        print('Opcion no valida')