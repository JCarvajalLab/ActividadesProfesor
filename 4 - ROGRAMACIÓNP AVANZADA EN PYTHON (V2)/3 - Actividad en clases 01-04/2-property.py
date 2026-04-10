#sin propierty
"""class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
alumno1 = Alumno("Cesar")
print(alumno1.getNombre())"""

#con propierty
"""class Alumno:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
alumno1 = Alumno("Cesar")
print(alumno1.nombre)"""

class Alumno:
    def __init__(self, nombre):
        self.__nombre = nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevoNombre):
        if nuevoNombre.strip() !="":
            self.__nombre = nuevoNombre
        else:
            print("nombre invalido")

alumno1 = Alumno("Cesar")
print(alumno1.nombre)

alumno1.nombre = "carlos"
print(alumno1.nombre)