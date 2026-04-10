class Perros:
    def __init__(self, nombre):
        self.__nombre = nombre # privado Atributo
    #getter con property
    @property
    def nombre(self):
        return self.__nombre
    #setter con validacion
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() !="":
            self.__nombre = nuevo_nombre
        else:
            print("Nombre invalido")
    #metodo para mostrar
    def mostrar_nombre(self):
        print("El nombre del perro es : ", self.__nombre)

# ================================= USO DEL PROGRAMA ============================
#crear objeto
perro1 = Perros("MAX")
#mostrar nombre original
perro1.mostrar_nombre()
#modificar el nombre
perro1.nombre = "cachupin"
print("El nuevo nombre del perro es: ", perro1.nombre)