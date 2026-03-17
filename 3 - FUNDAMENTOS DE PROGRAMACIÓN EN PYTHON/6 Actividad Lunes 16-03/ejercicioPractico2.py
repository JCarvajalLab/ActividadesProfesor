agenda = {}

print("=== AGENDA DE CONTACTOS ===")

while True:
    nombre = input("\nIngrese un nombre (o escriba 'salir' para terminar): ").strip()

    if nombre.lower() == 'salir':
        break

    if nombre in agenda:
        print("!Ese nombre ya existe en la agenda. Intente con otro.")
        continue

    telefono = input("Ingrese el número de teléfono: ").strip()
    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")

print(("\n=== Agenda Final ==="))
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")