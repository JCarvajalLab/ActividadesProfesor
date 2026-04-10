class Gato:
    def hablar(self):
        print("Miau!!!")

class Perro:
    def hablar(self):
        print("Guau!!")

class Vaca:
    def hablar(self):
        print("Muuuu!!!")

def hablarMascota(mascota):
    mascota.hablar()

miGato = Gato()
miPerro = Perro()
miVaca = Vaca()
hablarMascota(miGato)
hablarMascota(miPerro)
hablarMascota(miVaca)
# print("\n=== PERRO ===")
# perro1 = Perro()
# perro1.hablar()
# print("\n=== GATO ===")
# gato1 = Gato()
# gato1.hablar()

