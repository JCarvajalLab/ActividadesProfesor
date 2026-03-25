#crea un programa que tenga un alista precargada de numeros y elimine un elemento por indice utilizando "del". debe imprimir la lista original y la lista modificada con sus respectivos tamanos

lista = [10,20,30,40,50]
    #    0  1  2  3  4

print(f"La lista de numeros original es: {lista}")
print("La cantidad de elementos de la lista es: ", len(lista))

del lista[3]
print(f"lista con el elemento 40 Eliminado: ", lista)
print("La cantidad de elementos de la lista es: ", len(lista))