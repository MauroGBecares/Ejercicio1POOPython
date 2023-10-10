from datetime import date
import random
import string

class Libro:
    def __init__(self, nombre: str, autor: str) -> None:
        self.__nombre = nombre
        self.__autor = autor
        self.__fecha_lanzamiento = date.today()
        self.__isbn = self.generar_ISBN()

    #getter
    @property
    def nombre(self):
        return self.__nombre

    @property
    def autor(self):
        return self.__autor
    
    @property
    def fecha_lanzamiento(self):
        return self.__fecha_lanzamiento
    
    @property
    def isbn(self):
        return self.__isbn
    
    @classmethod
    def generar_ISBN() -> str:
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod