#!/usr/bin/env python3

class Counter:
    """
    This class defines an iterable Counter object that generates a sequence of numbers.

    Attributes:
        limit (int): The upper limit of the sequence (exclusive).

    Methods:
        __init__(limit): Initializes the Counter object with the given limit.
        __iter__(): Prepares the Counter object for iteration by resetting the counter.
        __next__(): Returns the next number in the sequence or raises StopIteration if the limit is reached.
    """

    def __init__(self, limit):
        """
        Initializes the Counter object with the provided limit.

        Args:
            limit (int): The upper limit of the sequence (exclusive).
        """
        self.limit = limit

    def __iter__(self):
        """
        Prepares the Counter object for iteration by resetting the internal counter.

        Returns:
            The Counter object itself, ready for iteration.
        """
        self.counter = 0
        return self

    def __next__(self):
        """
        Returns the next number in the sequence or raises StopIteration if the limit is reached.

        Returns:
            int: The next number in the sequence.

        Raises:
            StopIteration: If the limit of the sequence has been reached.
        """
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

# Create a Counter object with a limit of 15
c = Counter(15)

# Loop through the Counter object and print each number
for i in c:
    print(i)