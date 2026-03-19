grupo1= [5, 13, 16, 7]
grupo2= [5, 14, 15, 20]

for i in grupo1:
    for j in grupo2:
        if i == j:
            continue
        elif i > j:
            break
        else:
            print(f"Conclusion: el numero {i} es menor que el numero {j}")