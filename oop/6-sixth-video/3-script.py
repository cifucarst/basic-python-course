#!/usr/bin/env python3

class Book:
    """Represents a book with its author and title."""

    def __init__(self, author: str, title: str) -> None:
        """
        Initializes a Book object with the given author and title.

        Args:
            author: The author of the book (str).
            title: The title of the book (str).
        """
        self.author = author
        self.title = title

    def __str__(self) -> str:
        """
        Returns a string representation of the book in the format:
            "The book '{title}' has been written by '{author}'".

        Returns:
            A string representing the book.
        """
        return f'The book "{self.title}" has been written by "{self.author}"'

    def __eq__(self, __other: object) -> bool:
        """
        Checks if two books are equal.

        Two books are considered equal if they have the same author and title.

        Args:
            __other: The other book object to compare with.

        Returns:
            True if the books are equal, False otherwise.
        """
        if not isinstance(__other, Book):
            return False
        return self.author == __other.author and self.title == __other.title


# Creates two Book objects with the same author and title
book = Book("marcelo vasques", "how to be a lammer")
book_two = Book("marcelo vasques", "how to be a lammer")

# Prints the string representation of the first book
print(book)

# Checks if the two books are equal and prints the result
print(f'Are both books equal -> {book == book_two}')