class Alumno:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    # def setEdad(self, nuevaEdad):
    #     self.__edad = nuevaEdad

    def setEdad(self, nuevaEdad):
        if nuevaEdad > 0:
            self.__edad = nuevaEdad
        else:
            print("Edad Invalida")


    def mostrarDatos(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)        

alumno1 = Alumno("Cesar", 47)
alumno2 = Alumno("Julieta", 44)

alumno1.mostrarDatos()
alumno2.mostrarDatos()

# print(alumno1.getNombre())
# print(alumno1.getEdad())
# print()
# print(alumno2.getNombre())
# print(alumno2.getEdad())