#!/usr/bin/env python3

import pickle
from notas import Nota

class GestorNotas:
    def __init__(self,archivos_notas="notas.pkl") -> None:
        self.archivos_notas = archivos_notas

        try:
            with open(self.archivos_notas, "rb") as f:
                self.notas = pickle.load(f)
        except FileNotFoundError:
            self.notas = []
    
    def guardar_notas(self):
        with open(self.archivos_notas, "wb") as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self,contenido):  
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def leer_notas(self):
        return self.notas 
    
    def buscar_nota(self,texto_busqueda):
        return [nota for nota in self.notas if nota.coincide(texto_busqueda)]
    
    def eliminar_nota(self,index):
        if index < len(self.notas):
            del self.notas[index]
            self.guardar_notas()
        else:
            print(f"\n[!] El indice proporcionado es incorrecto\n")