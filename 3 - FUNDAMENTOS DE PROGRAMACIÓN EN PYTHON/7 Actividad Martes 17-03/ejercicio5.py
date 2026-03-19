llueve = False

temperatura = int(input("ingresar temperatura: "))
if temperatura < 18:
    if llueve == True:
        print("Llevare paraguas y abrigo")
    else:
        print("Solo llevare abrigo")
else:
    print("No necesito llevar paraguas ni abrigo")