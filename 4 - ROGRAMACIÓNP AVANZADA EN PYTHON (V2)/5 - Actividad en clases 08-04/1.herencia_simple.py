class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Supervisor(Persona):
    def __init__(self, nombre, edad, rol, tareas):
        super().__init__(nombre, edad)
        self.rol = rol
        self.tareas = tareas
    def mostrar_supervisor(self):
        print(f"{self.nombre} es {self.rol}, tiene {self.edad} anos y se dedica a {self.tareas}")

# p1 = Persona("Julieta", 41)
# p1.mostrar_datos()
print("\n=============================\n")
sup1 = Supervisor("Cesar", 47,"Jefe","Coordinar equipo")
sup2 = Supervisor("Ana", 21, "Encargada","Supervisar turnos")
print()
sup1.mostrar_datos()
sup1.mostrar_supervisor()

print()
# print(f"Rol: {sup1.rol}")
# print(f"Tareas: {sup1.tareas}")
sup2.mostrar_datos()
sup2.mostrar_supervisor()
