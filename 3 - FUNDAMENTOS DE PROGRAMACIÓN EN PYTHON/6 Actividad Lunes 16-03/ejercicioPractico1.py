numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese ultimo numero: "))

if numero1 > numero2 and  numero1 > numero3:
    print(f"El numero {numero1} es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mayor")
elif numero3 > numero2 and numero3 > numero1:
    print(f"El numero {numero3} es el mayor")
else:
    if numero1 == numero2 == numero3:
        print("Todos los números son iguales")
    else:
        print("Hay uno o mas numero iguales")