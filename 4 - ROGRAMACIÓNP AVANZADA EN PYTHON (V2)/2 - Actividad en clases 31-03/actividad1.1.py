class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self):
        print(self.nombre, "Esta ladrando: guau guau")

perro1= Perro("Firulax")
perro2= Perro("Godarx")

perro1.ladrar()
perro2.ladrar()