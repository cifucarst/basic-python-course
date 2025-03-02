#!/usr/bin/env python3


class Rectangulo():
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto
    
    def __str__(self) -> str:
        return "Este metodo"

rect1 = Rectangulo(20,80)
print(f"\n[+] El area es {rect1.area}")
print(rect1) # Este metodo