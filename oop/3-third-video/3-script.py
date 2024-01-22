#!/usr/bin/env python3

# This code defines a simple class for representing students.

class Students:
    """
    A class for representing students.

    Attributes:
        students: A list of students.
    """

    students = []

    def __init__(self) -> None:
        """
        The constructor initializes the list of students.
        """
        self.students = []

    @classmethod
    def create_student(cls, name, age):
        """
        Creates a new student object and adds it to the list of students.

        Args:
            nombre: The student's name.
            edad: The student's age.

        Returns:
            A string indicating whether the student was added to the list.
        """
        if age >= 18:
            return f"{name} was added to the list of students."
        else:
            return f"\n[!] {name} is not old enough to be added to the list."


Students.create_student("hackermate", 43)  # Prints "hackermate was added to the list of students."
Students.create_student("S4vitar", 28)  # Prints "S4vitar was added to the list of students."
Students.create_student("xerosec", 13)  # Prints "[!] xerosec is not old enough to be added to the list."
Students.create_student("hackavis", 8)  # Prints "[!] hackavis is not old enough to be added to the list."

print(Students.students)  # Prints [['hackermate', 43], ['S4vitar', 28]]