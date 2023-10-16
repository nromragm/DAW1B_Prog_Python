n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

opcion = int(input("Introduce una opcion (1 = Suma / 2 = Resta / 3 = Multiplicacion / 4 = Division): "))

while opcion < 1 or opcion > 4:
    opcion = int(input("Introduce una opcion (1 = Suma / 2 = Resta / 3 = Multiplicacion / 4 = Division): "))
    if opcion < 1 or opcion > 4:
        print("Error - No es una opcion correcta (1-4).")

if opcion == 1:
    resultado = n1 + n2
    print("La suma de los dos numeros es:", resultado)
elif opcion == 2:
    resultado = n1 - n2
    print("La resta de los dos numeros es:", resultado)
elif opcion == 3:
    resultado = n1 * n2
    print("La multiplicacion de los dos numeros es:", resultado)
elif opcion == 4:
    if n2 == 0:
        print("La division por cero no es posible")
    else:
        resultado = n1 / n2
        print("La division de los dos numeros es:", resultado)




