from ..reduced.angular import main as ra
from ..reduced.linear import main as rl
from ..general.angular import main as ga
from ..general.linear import main as gl
from ..general.constant import main as gc

def german():
    
    while True:
        try:
            xa = float(input("Geben Sie den Wert von ein xa: "))
        except:
            print("Fehler! Ungültiger Wert. Tippe nochmal.")
        else:
            break

    while True:
        try:
            ya = float(input("Geben Sie den Wert von ein ya: "))
        except:
            print("Fehler! Ungültiger Wert. Tippe nochmal.")
        else:
            break

    while True:
        try:
            xb = float(input("Geben Sie den Wert von ein xb: "))
        except:
            print("Fehler! Ungültiger Wert. Tippe nochmal.")
        else:
            break

    while True:
        try:
            yb = float(input("Geben Sie den Wert von ein yb: "))
        except:
            print("Fehler! Ungültiger Wert. Tippe nochmal.")
        else:
            break

    reduced = f'{ra(xa, ya, xb, yb)}{rl(xa, ya, xb, yb)}'
    general = f'{ga(xa, ya, xb, yb)}{gl(xa, ya, xb, yb)}{gc(xa, ya, xb, yb)}'
    answer = f'\n Die reduzierte Gleichung lautet: {reduced} \n Die allgemeine Gleichung lautet: {general}'

    print(answer)

    decision = input("Möchten Sie eine andere Gleichung (j/n) berechnen?")

    while decision != "j" and decision != "n":
        print("Fehler! Ungültige Option. Tippe nochmal.")

    if decision == "j":
        german()
    else:
        quit()