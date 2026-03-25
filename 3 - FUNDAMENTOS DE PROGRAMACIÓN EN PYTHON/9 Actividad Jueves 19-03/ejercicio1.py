for i in range(1, 10): #Ciclo externo ->Tabla
    print(f"\nTabla del {i}")
    for j in range(1, 11): #ciclo interno -> Multiplicador
        resultado =  i * j
        print(f"{i} * {j} * {resultado}")