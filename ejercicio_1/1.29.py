"""
Inicio
Escribe "Ingrese su nombre: "
Lee nombre

Si nombre es vacio hacer
    nombre = "Desconocido"
Fin

Mientras
    Escribe "Ingrese su edad: "
    Lee edad
Hasta que edad este en el rango de 0 a 125

años = 125 - edad

Escribe "Te llamas ", nombre, " y tienes ", edad, " años, te quedan aún ", años, " años por cumplir."
Fin
"""
nombre = input("Ingrese su nombre: ")

if nombre == "":
    nombre = "Desconocido"

while True:
    edad = int(input("Ingrese su edad: "))
    if 0 <= edad <= 125:
        break

años = 125 - edad

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aun {años} años por cumplir.")