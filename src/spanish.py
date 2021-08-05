from reduced import reducedAngular, reducedLinear
from general import generalAngular, generalLinear, generalConstant

def spanish():
    
    while True:
        try:
            xa = float(input("Ingrese el valor de xa: "))
        except:
            print("¡Error! Valor no válido. Escriba otra vez.")
        else:
            break

    while True:
        try:
            ya = float(input("Ingrese el valor de ya: "))
        except:
            print("¡Error! Valor no válido. Escriba otra vez.")
        else:
            break

    while True:
        try:
            xb = float(input("Ingrese el valor de xb: "))
        except:
            print("¡Error! Valor no válido. Escriba otra vez.")
        else:
            break

    while True:
        try:
            yb = float(input("Ingrese el valor de yb: "))
        except:
            print("¡Error! Valor no válido. Escriba otra vez.")
        else:
            break

    reduced = 'y = ' + reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f'\n La ecuación reducida es: {reduced} \n La ecuación general es: {general}'

    print(answer)

    while True:
        try:
            decision = input("¿Quieres calcular otra ecuación (s/n)?")
        except:
            print("Error inesperado. Inténtalo de nuevo.")
        else:
            if decision != "s" and decision != "n":
                print("¡Error! Opción inválida. Inténtalo de nuevo.")
            else:
                break

    while decision != "s" and decision != "n":
        print("¡Error! Opción inválida. Escriba otra vez.")
        decision = input("¿Quieres calcular otra ecuación (s/n)?")


    if decision == "s":
        spanish()
    else:
        quit()