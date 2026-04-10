class Alumno:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def mostrarDatos(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)        

alumno1 = Alumno("Cesar", 47)
alumno2 = Alumno("Julieta", 44)

# alumno1.mostrarDatos()
# alumno2.mostrarDatos()

print(alumno1.__nombre)
print(alumno1.__edad)