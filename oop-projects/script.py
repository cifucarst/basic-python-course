#!/usr/bin/env python3

class Book:
    def __init__(self, id_book, author, book_name) -> None:
        # Constructor to initialize book attributes
        self.id_book = id_book
        self.author = author
        self.book_name = book_name
        self.is_borrowed = False

    def __str__(self) -> str:
        # Special method to provide a string representation of the book
        return f'Book({self.id_book}, {self.author}, {self.book_name})'

    def __repr__(self) -> str:
        # Representation method that calls __str__
        return self.__str__()

class Library:
    def __init__(self) -> None:
        # Constructor to initialize the Library with an empty dictionary of books
        self.books = {}

    def add_book(self, book):
        # Method to add a book to the library
        if book.id_book not in self.books:
            self.books[book.id_book] = book
        else:
            print(f'It is not possible to add the book with ID {book.id_book}')

    def lend_book(self, id_book):
        # Method to lend a book by marking it as borrowed
        if id_book in self.books and not self.books[id_book].is_borrowed:
            self.books[id_book].is_borrowed = True
        else:
            print(f'\n[!] It is not possible to lend the book with ID {id_book}')

    @property
    def show_books(self):
        # Property to get a list of available books in the library
        return [book for book in self.books.values() if not book.is_borrowed]

    @property
    def show_borrowed_books(self):
        # Property to get a list of borrowed books in the library
        return [book for book in self.books.values() if book.is_borrowed]

class ChildrensLibrary(Library):
    def __init__(self) -> None:
        # Constructor to initialize ChildrensLibrary with an empty dictionary of books for children
        super().__init__()
        self.books_for_children = {}  # -> {1: False, 2: True}

    def add_book(self, book, is_for_children):
        # Method to add a book to the children's library, along with information about whether it's for children
        super().add_book(book)
        self.books_for_children[book.id_book] = is_for_children

    def lend_book(self, id_book, is_child):
        # Method to lend a book from the children's library based on whether it's for children or not
        if id_book in self.books and self.books_for_children[id_book] == is_child and not self.books[id_book].is_borrowed:
            self.books[id_book].is_borrowed = True
        else:
            print(f'\n[!] It is not possible to lend the book with ID {id_book}')

    @property
    def show_state_of_books_for_children(self):
        # Property to get the state of books (whether for children or not) in the children's library
        return self.books_for_children

if __name__ == '__main__':
    # Test the library functionality

    library = ChildrensLibrary()

    book1 = Book(1, "Marcelo Vasquez", "How to be a lammer of maximum power?")
    book2 = Book(2, "Pepito Manolete", "Learn to color from scratch")

    library.add_book(book1, is_for_children=False)
    library.add_book(book2, is_for_children=True)

    print(f'\n[+] Books in the library: {library.show_books}')

    library.lend_book(1, is_child=False)

    print(f'\n[+] Books in the library: {library.show_books}')

    print(f'\n[+] Borrowed books: {library.show_borrowed_books}')

    print(f'\n[+] Books for children: {library.show_state_of_books_for_children}')