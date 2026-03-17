class Estudiantes:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    #Metodo, por que esta a dentro de una clase/ si estuviera afuera seria una funcion
    def saludar(self):
        if self.edad >= 18:
            print(f"Hola, soy {self.nombre}y tengo {self.edad} años.")
        else:
            print(f"Hola, soy {self.nombre}. Soy menor de edad.")

#crear un estudiante mayor de edad

estudiante1 = Estudiantes("Julieta", 22, "Programacion")
estudiante1.saludar()

#crear un estudiante menor de edad

estudiante2 = Estudiantes("Ana",15,"segundo Medio")
estudiante2.saludar()



