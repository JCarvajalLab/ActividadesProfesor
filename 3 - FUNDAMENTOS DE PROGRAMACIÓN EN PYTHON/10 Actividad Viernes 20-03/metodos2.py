set1 = {1,2,3}

#metodo .add{}
#anade un elemento al conjunto

print(set1)
set1.add(4)
print(set1)

#metodo .discard{}
#borra elemento de un item
set1.discard(4)
print(f"Los valores del conjunto son {set1}")

c1 = {1,2,3,4}
c2 = c1.copy()
print(c1,c2)

#metodo .clear{}
c1.clear()
print(c1)