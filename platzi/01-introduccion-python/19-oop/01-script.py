class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f'Hola, mi nombre es {self.name} y tengo {self.age}')


person1 = Person('Ana', 30)
person2 = Person('Luis', 25)

person1.saludar()
person2.saludar()