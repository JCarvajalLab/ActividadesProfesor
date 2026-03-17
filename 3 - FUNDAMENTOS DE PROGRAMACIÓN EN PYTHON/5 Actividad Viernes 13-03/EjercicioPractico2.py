# solicitar al usuario el numero base
numero = int(input("Ingrese un numero: "))

#crear lista vacia
lista = []

for i in range(1, 11):
    resultado = numero * i
    print(numero, "X", i, "=", resultado)
    lista.append(resultado)
print("\nLa tabla almacenada es: ")
print(lista)