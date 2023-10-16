x = int(input("Escribe un numero: "))
y = int(input("Escribe otro numero: "))

if x <= y:
    numIni = x
    numFin = y
else:
    numIni = y
    numFin = x

while numIni <= numFin:
    print(numIni, end="")
    if numIni != numFin:
        print("-", end="")
    numIni = numIni + 1