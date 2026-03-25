# borrar a elemntos listas 

miLista = [10,20,30,40]
del miLista[1]
print(miLista)

# borrar a datos en diccionarios 

miDiccionario = {
    "nombre":"Ana",
    "edad": 25
}
del miDiccionario["edad"]
print(miDiccionario)

#set (Conjuntos)

miSet = {5,10,15}
for elemento in miSet:
    print(elemento)