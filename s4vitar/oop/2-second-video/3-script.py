#!/usr/bin/env python3

# Class representing a book
class Book():
    # VAT (Value Added Tax) percentage
    IVA = 0.21
    
    def __init__(self, title, author, price) -> None:
        # Initializing book attributes
        self.title = title
        self.author = author
        self.price = price
    
    # Static method to calculate price including VAT
    @staticmethod
    def price_with_iva(price):
        return price + price * Book.IVA

# Creating an instance of the Book class
my_book = Book("How to be a real Lammer", "Jhon Conor", 17.5)

# Displaying the book price with VAT applied
print(f'\n[+] The book price with VAT is {round(Book.price_with_iva(my_book.price), 2)}')
