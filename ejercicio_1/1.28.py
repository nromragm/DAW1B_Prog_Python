"""
Inicio
Escribe "Ingrese el primer numero entero: "
Lee numero1
Escribe "Ingrese el segundo numero entero: "
Lee numero2

Si numero1 es igual a numero2 hacer
    Escribir "Los números no pueden ser iguales"
Sino
    Si numero1 es menor que numero2 hacer
        menor = numero1
        mayor = numero2
    Sino
        menor = numero2
        mayor = numero1

    diferencia = mayor - menor        


    Escribir "El numero menor es el ", menor, " y entre ellos existen ", diferencia, " numeros enteros"
Fin
"""

numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

if numero1 == numero2:
    print("Los numeros no pueden ser iguales")
else:
    menor = min(numero1, numero2)
    mayor = max(numero1, numero2)

    diferencia = mayor - menor

    print(f"El numero menor es el {menor} y entre ellos existen {diferencia} numeros enteros")