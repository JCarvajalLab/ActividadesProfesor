# nombre = "julieta"
# edad = 15
"""
Programacion estructurada se centra mas en:

funciones
pasos del algoritmo
flujos del programa

"""
# def saludar(nombre):
#     print("Hola",nombre)

# saludar(nombre)

"""
Programacion orientada a objetos (POO) se centra mas en:
clases
objetos
atributos
metodos

"""

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         print("Hola, soy", self.nombre,"y Tengo", self.edad)

# p1 = Persona("Julieta", 44)
# p1.saludar()
"""
class Auto:
    pass

a1 = Auto()
"""

# Que representa auto => es la clase
# que es a1 => es un objeto a partir de la clase auto
# a1 tambien es una instancia de Auto

#Que son los atributos

"""class Perro():
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
"""

#Son atributos de instancia

#el estado de un objeto es ""como esta el objeto en este momento

"""class Lampara:
    def __init__(self, color, encendida):
        self.color = color
        self.encendida = encendida
lampara1 = Lampara("Blanca", False)
print(lampara1.color)
print(lampara1.encendida)

lampara1.encendida = True
print("lampara.color")
print(lampara1.encendida)
"""

#Que son los metodos: los metodos son funciones que pertenecen a una clase y que describen lo que el objeto puede hacer

"""class Perro:
    def ladrar(self):
        print("guau guau!!!!")

perro1 = Perro()
perro1.ladrar()

"""

#Que hace __init__()
# class Perro:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
# perro1 = Perro("Godar", 3)

"""class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        print(self.nombre, "dice: Guau Guau!!")
    def mostrarDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

perro1 = Perro("Godar", 3)
perro2 = Perro("Firulais", 3)

perro1.mostrarDatos()
perro1.ladrar()

print()

perro2.mostrarDatos()
perro2.ladrar()
"""
#ejemplo 

"""class Perro:
    especie = "canino"

    def __init__(self, nombre):
        self.nombre = nombre

perro1 = Perro("firulais")
perro2 = Perro("Max")

print(perro1.nombre)
print(perro2.nombre)

print(perro1.especie)
print(perro2.especie)

"""

##Metodo de instancia

"""class Perro:
    def ladrar(self):
        print("Guau!!!")
"""

##Metodo de clase => trabaja con cls, es decir con la clase

"""class Perro:
    especie = "canino"
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrarNombre(self):
        print("Nombre: ", self.nombre)

    @classmethod
    def mostrarEspecie(cls):
        print("La especie es:", cls.especie)

perro1 = Perro("Firulais")

perro1.mostrarNombre()
perro1.mostrarEspecie()
"""

#Ejemplo

"""class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print("El auto ha arrancado")
        
"""
#Encapsulamiento

"""class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrarSaldo(self):
        print("Saldo:", self.__saldo)
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
"""

##Getter an setter

"""class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

p1 = Persona("ANA")
print(p1.getNombre())

p1.setNombre("Maria")
print(p1.getNombre())

"""