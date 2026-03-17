#1 scope local -> alcance local
#==========================

def print_number():
    first_num = 1
    #print statement 1(imprimir declaracion)
    print("the first number defined is:", first_num)
print_number()

#2 global scope -> alcance global
#===============================

greeting = "hello"

def greeating_world():
    world = "world"
    print(greeting, world)

def greeting_name(name):
    print(greeting, name)

greeating_world()
greeting_name("samuel")

#keywords
#========================

for numero in range(5):
    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")