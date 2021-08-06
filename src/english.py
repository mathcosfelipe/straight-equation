from reduced import reducedAngular, reducedLinear
from general import generalAngular, generalLinear, generalConstant


def english():
    
    while True:
        try:
            xa = float(input("Inform the xa value: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            break

    while True:
        try:
            ya = float(input("Inform the ya value: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            break

    while True:
        try:
            xb = float(input("Inform the xb value: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            break

    while True:
        try:
            yb = float(input("Informe o valor de yb: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            break

    reduced = 'y = ' + reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f'\n The reduced equation is: {reduced} \n The general equation is: {general}'

    print(answer)

    while True:
        try:
            decision = input("Do you wanna calculate another equation (y/n)? ")
        except:
            print("Unexpected error. Try again.")
        else:
            if decision != "y" and decision != "n":
                print("Error! Invalid option. Try again.")
            else:
                break

    if decision == "y":
        english()
    else:
        quit()