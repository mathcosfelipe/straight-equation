from ..reduced.angular import reducedAngular as ra
from ..reduced.linear import reducedLinear as rl
from ..general.angular import generalAngular as ga
from ..general.linear import generalLinear as gl
from ..general.constant import generalConstant as gc
def italian():
    
    while True:
        try:
            xa = float(input("Inserisci il valore di xa: "))
        except:
            print("Errore! Valore non valido. Digita di nuovo.")
        else:
            break

    while True:
        try:
            ya = float(input("Inserisci il valore di ya: "))
        except:
            print("Errore! Valore non valido. Digita di nuovo.")
        else:
            break

    while True:
        try:
            xb = float(input("Inserisci il valore di xb: "))
        except:
            print("Errore! Valore non valido. Digita di nuovo.")
        else:
            break

    while True:
        try:
            yb = float(input("Inserisci il valore di yb: "))
        except:
            print("Errore! Valore non valido. Digita di nuovo.")
        else:
            break

    reduced = f'{ra(xa, ya, xb, yb)}{rl(xa, ya, xb, yb)}'
    general = f'{ga(xa, ya, xb, yb)}{gl(xa, ya, xb, yb)}{gc(xa, ya, xb, yb)}'
    answer = f"\n L'equazione ridotta è: {reduced} \n L'equazione generale è: {general}"

    print(answer)

    decision = input("Vuoi calcolare un'altra equazione (s/n)?")

    while decision != "s" and decision != "n":
        print("Errore! Opzione non valida. Digita di nuovo.")

    if decision == "s":
        italian()
    else:
        quit()
