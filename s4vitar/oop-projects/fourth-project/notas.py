#!/usr/bin/env python3

class Nota:
    def __init__(self,contenido) -> None:
        self.contenido = contenido

    def coincide(self,texto_busqueda):
        return texto_busqueda in self.contenido
        

    def __str__(self) -> str:
        return self.contenido