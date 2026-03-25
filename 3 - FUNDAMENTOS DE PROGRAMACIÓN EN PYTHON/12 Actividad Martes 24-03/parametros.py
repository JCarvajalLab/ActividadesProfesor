def saludar(nombre, mensaje ="que bueno conocerte"):
    print("buen dia", nombre, mensaje)

#valor por defecto ->mensaje
saludar("Jose", "un gusto")

#parametro posicional
saludar(mensaje="un gusto", nombre="pepe")