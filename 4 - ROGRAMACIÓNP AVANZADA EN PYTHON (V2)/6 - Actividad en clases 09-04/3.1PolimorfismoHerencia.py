class Animal:
    def hablar(self):
        print("Este animal emite sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau!!!")
class Gato(Animal):
    def hablar(self):
        print("Miau!!")
class Vaca(Animal):
    def hablar(self):
        print("Muuuu!!!")

animales = [Perro(),Gato(),Vaca()]

for animal in animales:
    animal.hablar()