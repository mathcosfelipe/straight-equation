from reduced import reducedAngular, reducedLinear
from general import generalAngular, generalLinear, generalConstant

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

    reduced = 'y = ' + reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f"\n L'equazione ridotta è: {reduced} \n L'equazione generale è: {general}"

    print(answer)

    while True:
        try:
            decision = input("Vuoi calcolare un'altra equazione (s/n)?")
        except:
            print("Errore inaspettato. Tippe nochmal.")
        else:
            if decision != "s" and decision != "n":
                print("Errore! Opzione non valida. Digita di nuovo.")
            else:
                break

    if decision == "s":
        italian()
    else:
        quit()