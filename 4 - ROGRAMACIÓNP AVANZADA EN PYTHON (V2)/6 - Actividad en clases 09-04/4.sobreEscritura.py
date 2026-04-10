class Animal:
    def hablar(self):
        print("Este animal emite sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau!!!")

p1 = Perro()
p1.hablar()