def mostrarPersona(persona):
    print(persona["nombre"] + ", Edad: "+ str(persona["edad"]))

datos = {
    "nombre":"jose",
    "edad":25
}

mostrarPersona(datos)