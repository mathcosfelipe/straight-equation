from ..reduced.angular import reducedAngular as ra
from ..reduced.linear import reducedLinear as rl
from ..general.angular import generalAngular as ga
from ..general.linear import generalLinear as gl
from ..general.constant import generalConstant as gc

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

    reduced = f'{ra(xa, ya, xb, yb)}{rl(xa, ya, xb, yb)}'
    general = f'{ga(xa, ya, xb, yb)}{gl(xa, ya, xb, yb)}{gc(xa, ya, xb, yb)}'
    answer = f'\n The reduced equation is: {reduced} \n The general equation is: {general}'

    print(answer)

    decision = input("Do you wanna calculate another equation (y/n)? ")

    while decision != "y" and decision != "n":
        print("Error! Invalid option. Try again.")

    if decision == "y":
        english()
    else:
        quit()
