persona = {
    "nombre": "ana",
    "edad": 20,
    "ciudad": "santiago",
    "comuna": "providencia"
}
print(persona)

##metodo .get()
print(persona.get("nombre", "no se encuentra"))

#metodo key.()

print(persona.keys())

#metodo value()
print("Los valores del diccionario son: ")
print(persona.values())

for clave, valor in persona.items():
    print(f"")