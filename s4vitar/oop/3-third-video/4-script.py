#!/usr/bin/env python3

# This code defines a simple class for representing students.

class Students:
    """
    A class for representing students.

    Attributes:
        students: A list of students.
    """

    students = []

    def __init__(self, name, age) -> None:
        """
        Initializes the student's name and age.

        Args:
            nombre: The student's name.
            edad: The student's age.
        """
        self.name = name
        self.age = age

        # Add the student to the list of students.
        Students.students.append(self)

    @staticmethod
    def is_of_legal_age(age):
        """
        Returns True if the given age is greater than or equal to 18, False otherwise.

        Args:
            edad: The student's age.

        Returns:
            True if the student is of legal age, False otherwise.
        """
        return age >= 18

    @classmethod
    def create_student(cls, name, age):
        """
        Creates a new student object and adds it to the list of students if the student is of legal age.

        Args:
            name: The student's name.
            age: The student's age.

        Returns:
            The new student object if the student is of legal age, None otherwise.
        """
        if cls.is_of_legal_age(age):
            return cls(name, age)
        else:
            print(f"\n[!] Error: the student {name} is under legal age {age}")
            return None

    @staticmethod
    def show_students():
        """
        Prints a list of all the students, indexed by their number.
        """
        for i, student in enumerate(Students.students):
            print(f"\t[+] The student number [{i+1}]:  {student.name}")


# Create some students.
Students.create_student("hackermate", 43)
Students.create_student("S4vitar", 28)
Students.create_student("xerosec", 13)
Students.create_student("hackavis", 8)
Students.create_student("Lobotec", 1)

# Print a list of all the students.
print(f"\n[+] Listando los estudiantes existentes:\n")
Students.show_students()