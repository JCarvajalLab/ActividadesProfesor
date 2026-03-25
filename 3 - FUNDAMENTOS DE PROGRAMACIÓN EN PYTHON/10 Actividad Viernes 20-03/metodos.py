#append agrega un dato al final de la lista
lista = [1,2,3,4,5,6]
print(lista)
lista.append(7)
print(lista)

## metodo .insert()
## inserta el numero en la pisicion del indeice de una lista existente, desplazando el numero

lista.insert(2,99)
print(lista)

#Elimina el ultimo valor de la lista
lista.pop()
print(lista, "POP")


lista.insert(5, 5)
print(lista, "Insertar 5")
print(lista.count(5), "cuantos 5")

# metodo .clear()

# lista.clear()
# print(lista, "Lista elimidada")