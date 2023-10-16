while True:
    inicial = int(input("Introduce el número de inicio: "))

    incremento = int(input("Introduce el incremento: "))

    total = int(input("Introduce el total de la serie: "))

    if incremento > 0 and total > 0:
        break
    else:
        print("El incremento y el total deben ser mayores que cero.")

serie = str(inicial)

for i in range(1, total - 1):
    inicial += incremento
    serie += f"..{inicial}"
serie += f"-{inicial + incremento}"   

print(f"SERIE => {serie}")