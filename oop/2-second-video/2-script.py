#!/usr/bin/env python3

# class Book():
#     def __init__(self,title,author,price,bestseller_value = 5000) -> None:
#         self.title = title
#         self.author = author
#         self.price = price
#         self.bestseller_value = bestseller_value

#     @staticmethod
#     def is_best_seller(instance,total_sales):
#         return total_sales > instance.bestseller_value


# my_book = Book("How to be a real Lammer","Jhon Conor",17.5)
# print(Book.is_best_seller(my_book,7000))


######################################################################################

# This class defines a Book object with its attributes.

class Book():
    # The title of the book.
    title: str

    # The author of the book.
    author: str

    # The price of the book.
    price: float

    # The minimum sales for a book to be considered a bestseller (default value).
    bestseller_value: int = 5000

    def __init__(self, title: str, author: str, price: float, bestseller_value: int = 5000) -> None:
        """
        This method initializes a Book object with its information.

        Args:
            title: The title of the book (required).
            author: The author of the book (required).
            price: The price of the book (required).
            bestseller_value (optional): The minimum sales for a bestseller (defaults to 5000).
        """
        self.title = title
        self.author = author
        self.price = price
        self.bestseller_value = bestseller_value

    # This method checks if a Book instance is considered a bestseller based on its total sales.

    @staticmethod
    def is_best_seller(instance: 'Book', total_sales: int) -> bool:
        """
        This static method checks if a Book instance has achieved bestseller status.

        Args:
            instance: The Book object to be evaluated.
            total_sales: The total sales of the book.

        Returns:
            True if the total sales exceed the book's bestseller value, False otherwise.
        """
        return total_sales > instance.bestseller_value

# Create a Book object.

my_book = Book("How to be a real Lammer", "Jhon Conor", 17.5)

# Check if the book is a bestseller based on its current sales (7000).

print(Book.is_best_seller(my_book, 7000))