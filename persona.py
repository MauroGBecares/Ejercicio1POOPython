from abc import ABC
from datetime import date

class Persona(ABC):
    def __init__(self) -> None:
        self.__nombre = None
        self.__apellido = None
        self.__fecha_nac = None
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def fecha_nac(self):
        return self.__fecha_nac
    
    @property
    def edad(self):
        if (self.__fecha_nac):
            return date.today().year - self.__fecha_nac.year
        else:
            return "No se encuentra cargada la fecha de nacimiento."
    
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    
    @fecha_nac.setter
    def fecha_nac(self, fecha_nac: date):
        self.__fecha_nac = fecha_nac
    
    @apellido.setter
    def apellido(self, apellido: str):
        self.__apellido = apellido
    


