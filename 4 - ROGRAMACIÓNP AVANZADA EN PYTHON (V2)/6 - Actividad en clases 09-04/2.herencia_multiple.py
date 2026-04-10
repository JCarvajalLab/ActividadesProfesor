#Herencia multiple

"""
class Hija(padre1, padre2)
    pass
"""
class Trabajador:
    def __init__(self, empresa):
        self.empresa = empresa
    def trabajar(self):
        print(f"Estoy trabajando en la empresa {self.empresa}")

class Estudiante:
    def __init__(self, carrera):
        self.carrera = carrera
    def estudiar(self):
        print(f"Estoy estudiando en la carrera de {self.carrera}")

class Becario(Trabajador, Estudiante):
    def __init__(self, empresa, carrera):
        Trabajador.__init__(self, empresa)
        Estudiante.__init__(self, carrera)

b1 = Becario("Inacap", "UDEMY")

b1.estudiar()
b1.trabajar()

print(Becario.__mro__)