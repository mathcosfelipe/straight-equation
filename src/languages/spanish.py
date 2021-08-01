from ..reduced.angular import reducedAngular as ra
from ..reduced.linear import reducedLinear as rl
from ..general.angular import generalAngular as ga
from ..general.linear import generalLinear as gl
from ..general.constant import generalConstant as gc

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

    reduced = f'{ra(xa, ya, xb, yb)}{rl(xa, ya, xb, yb)}'
    general = f'{ga(xa, ya, xb, yb)}{gl(xa, ya, xb, yb)}{gc(xa, ya, xb, yb)}'
    answer = f'\n La ecuación reducida es: {reduced} \n La ecuación general es: {general}'

    print(answer)

    decision = input("¿Quieres calcular otra ecuación (s/n)?")

    while decision != "s" and decision != "n":
        print("¡Error! Opción inválida. Escriba otra vez.")

    if decision == "s":
        spanish()
    else:
        quit()
