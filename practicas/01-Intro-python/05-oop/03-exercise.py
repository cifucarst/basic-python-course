# 1. Sistema de Biblioteca

# Crea un programa para gestionar los préstamos de libros en una biblioteca.
# Requerimientos:

#     Clase Book:
#         Atributos: title, author, available (booleano).
#         Métodos:
#             borrow(): Cambia el estado de disponibilidad a False.
#             return_book(): Cambia el estado de disponibilidad a True.

#     Clase Library:
#         Atributos: Una lista de libros (books).
#         Métodos:
#             add_book(book: Book): Agrega un libro al catálogo.
#             list_books(): Muestra los libros y su estado de disponibilidad.
#             find_book(title): Busca un libro por título.
#             borrow_book(title): Permite a un usuario tomar prestado un libro.
#             return_book(title): Permite devolver un libro.

# Interfaz Interactiva:

# Crea un menú que permita al usuario:

#     Agregar libros al catálogo.
#     Buscar libros por título.
#     Listar libros disponibles.
#     Tomar libros prestados.
#     Devolver libros.


class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        if not isinstance(title, str):
            raise ValueError("Debes ingresar un título válido")
        if not isinstance(author, str):
            raise ValueError("Debes ingresar un autor válido")
        if not isinstance(available, bool):
            raise ValueError("Debes ingresar un booleano válido")
        
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if not self.available:
            print(f'❌ El libro "{self.title}" no está disponible para préstamo.')
        else:
            self.available = False
            print(f'✅ Has tomado prestado el libro "{self.title}".')

    def return_book(self):
        if self.available:
            print(f'❌ El libro "{self.title}" ya esta disponible.')
        else:
            self.available = True
            print(f'✅ El libro "{self.title}" ha sido devuelto correctamente.')

    def __str__(self):
        return f'Título: {self.title}, Autor: {self.author}, ¿Disponible? {"Sí" if self.available else "No"}.'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Solo puedes agregar objetos de tipo Book a la biblioteca")
        self.books.append(book)

    def find_book(self, titulo):
        for book in self.books:
            if book.title == titulo:
                print(f'✅ El libro "{book.title}" fue encontrado en la biblioteca.')
                return book
        print(f'❌ Libro con título "{titulo}" no encontrado en la biblioteca.')
        return None

    def list_books(self):
        if not self.books:
            print('❌ Aún no hay libros en la biblioteca.')
            return
        print('Libros disponibles en la biblioteca:')
        for book in self.books:
            print(f'✅ {book}')


def menu():
    biblioteca = Library()
    while True:
        print("""
              📚 Bienvenido a esta gran biblioteca 📚

              1 - Agregar libros 
              2 - Buscar libros por título.
              3 - Listar libros disponibles.
              4 - Tomar libros prestados.
              5 - Devolver libros.
              6 - Salir
              """)
        try:
            opcion = int(input('Escribe una opción: '))
            if opcion == 1:
                title = input('Escribe el título del libro: ').lower()
                author = input('Escribe el autor: ')
                book = Book(title, author)
                biblioteca.add_book(book)
            elif opcion == 2:
                titulo = input('Escribe el título del libro a buscar: ').lower()
                biblioteca.find_book(titulo)
            elif opcion == 3:
                biblioteca.list_books()
            elif opcion == 4:
                titulo = input('Escribe el título del libro que deseas tomar prestado: ').lower()
                book = biblioteca.find_book(titulo)
                if book:
                    book.borrow()
            elif opcion == 5:
                titulo = input('Escribe el título del libro que deseas devolver: ').lower()
                book = biblioteca.find_book(titulo)
                if book:
                    book.return_book()
            elif opcion == 6:
                print('Saliendo... ¡Gracias por utilizar nuestra biblioteca!')
                break
            else:
                print('❌ Opción no válida.')
        except ValueError:
            print('❌ Debes ingresar un número válido.')


if __name__ == '__main__':
    menu()