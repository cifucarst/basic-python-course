#!/usr/bin/env python3

# Parent class representing a book
class Book():
    IVA = 0.21  # VAT (Value Added Tax) percentage for regular books

    # Constructor to initialize book attributes
    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    # Class method to calculate price including VAT for a book
    @classmethod
    def price_with_iva(cls, price):
        return price + price * cls.IVA

# Child class inheriting from Book class for digital books
class DigitalBook(Book):
    IVA = 0.10  # VAT percentage for digital books

# Creating instances of Book and DigitalBook classes
my_book = Book("How to be a real Lammer", "Jhon Conor", 17.5)
my_digital_book = DigitalBook("Initiation to the lammer world", "Jhon Conor", 17.5)

# Displaying the price of the book with VAT applied
print(f'\n[+] The book price with VAT is {Book.price_with_iva(my_book.price)}')

# Displaying the price of the digital book with VAT applied
print(f'\n[+] The digital book price with VAT is {my_digital_book.price_with_iva(my_digital_book.price)}')