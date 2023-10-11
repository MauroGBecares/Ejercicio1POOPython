from datetime import date
from persona import *

class Usuario(Persona):
    def __init__(self, user_name: str, email: str, password) -> None:
        super().__init__()
        self.__user_name = user_name
        self.__email = email
        self.__estado = True
        self.__fecha_alta = date.today()
        self.__password = password
        self.__fecha_baja = None

    @property
    def password(self):
        return self.__password
    
    @property
    def email(self):
        return self.__email
    
    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    @property
    def fecha_baja(self):
        return self.__fecha_baja
    
    @password.setter
    def password(self, password: str):
        self.__password = password

    @email.setter
    def email(self, email: str):
        self.__email = email

    @fecha_baja.setter
    def fecha_baja(self, fecha_baja):
        self.__fecha_baja = fecha_baja
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    
    def validar_credenciales(self, usuario: str, password: str) -> bool:
         return self.user_name == usuario and self.password == password

    def baja_usuario(self) -> None:
        self.estado = False
        self.fecha_baja = date.today()

    def agregar_libro(self, nuevo_libro: object) -> str:
        self.__libros.append(nuevo_libro)
        return f"El libro {nuevo_libro} se agrego exitosamente !"

    def quitar_libro(self, libro: object) -> str:
        self.__libros.pop(libro)
        return f"El libro {libro} se borro exitosamente !"
    
    def leyo_libro(self, nombre: str) -> bool:
        for libro in self.__libros:
            if libro.nombre == nombre:
                return True        
        return False
        
