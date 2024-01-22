#!/usr/bin/env python3

#self.__dinero  #private
#self._dinero  #protected

class Example:
    def __init__(self) -> None:
        # protected attribute
        self._atributo_protegido = 'I am a protected attribute and you should not be able to see me'
        self.__atributo_privado = 'I am a private attribute and you should not be able to see me'


example = Example()
print(Example._atributo_protegido)

# way to access a private attribute
print(example._Example__atributo_privado)

# throws an error because it does not allow access to a private attribute
print(example.__atributo_privado)