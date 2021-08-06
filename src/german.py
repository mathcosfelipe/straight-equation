from reduced import reducedAngular, reducedLinear
from general import generalAngular, generalLinear, generalConstant

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

    reduced = 'y = ' + reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f'\n Die reduzierte Gleichung lautet: {reduced} \n Die allgemeine Gleichung lautet: {general}'

    print(answer)

    while True:
        try:
            decision = input("Möchten Sie eine andere Gleichung (j/n) berechnen?")
        except:
            print("Unerwarteter fehler. Tippe nochmal.")
        else:
            if decision != "j" and decision != "n":
                print("Error! Invalid option. Try again.")
            else:
                break

    if decision == "j":
        german()
    else:
        quit()