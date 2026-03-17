meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre","Noviembre", "Diciembre")

while True:
    numero = int(input("Ingrese un numero entre 1 y 12: "))
    if numero < 1 or numero > 12:
        print("ERROR: solo se aceptan numeros entre 1 y 12")
    else:
        print(f"El mes correspondiente es: {meses[numero -1]}")
        break