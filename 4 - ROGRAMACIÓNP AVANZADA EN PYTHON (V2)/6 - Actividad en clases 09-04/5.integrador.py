class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def describir(self):
        print(f"Soy un animal llamado {self.nombre} y tengo {self.edad} years")
    def hablar(self):
        print("Hago un sonido")

class Mascota:
    def jugar(self):
        print("Estoy jugando con mi dueno")

class Gato(Animal,Mascota):
    def hablar(self):
        print("Miau!!!")
class Perro(Animal,Mascota):
    def hablar(self):
        print("Guau!!!")

def hacerHablar(animal):
    animal.hablar()

gato1 = Gato("Michi", 3)
perro1 = Perro("Godar",5)

print("\n==== F. Describir ====")
gato1.describir()
perro1.describir()

print("\n==== F. Jugar ====")
perro1.jugar()
gato1.jugar()

print("\n==== F. Hablar ====")
hacerHablar(gato1)
hacerHablar(perro1)

animal1 = Animal("Godar",5)
animal1.hablar()


print(isinstance(perro1, Perro))
print(isinstance(perro1,Animal))
print(isinstance(gato1, Gato))
print(isinstance(gato1, Animal))