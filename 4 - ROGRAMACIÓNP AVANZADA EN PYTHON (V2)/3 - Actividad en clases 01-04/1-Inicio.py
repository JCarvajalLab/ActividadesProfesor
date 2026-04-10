class Alumno:
    pass
#Atributos
nombre = ""
leccion = "Programacion orientada a objetos"
#constructor

def __init__(self, parametroNombre):
    self.nombre = parametroNombre
    self.boActivo = True
    