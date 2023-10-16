num = 3

total = int(input("Dime cuántos números debe tener la serie: "))
cont = 1

while cont <= total:
    print(num, end="")
    if cont < total:
        print(" ", end="")
    num = num + 3
    cont = cont + 1