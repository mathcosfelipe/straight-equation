from angularGeneral import angular
from linearGeneral import linear
from constantGeneral import constant
from angularReduced import angular
from linearReduced import linear

def main():

    while True:
        try:
            xa = float(input("Informe o valor de xa: "))
        except:
            print("Erro! Valor inválido. Digite novamente.")
        else:
            break

    while True:
        try:
            ya = float(input("Informe o valor de ya: "))
        except:
            print("Erro! Valor inválido. Digite novamente.")
        else:
            break

    while True:
        try:
            xb = float(input("Informe o valor de xb: "))
        except:
            print("Erro! Valor inválido. Digite novamente.")
        else:
            break

    while True:
        try:
            yb = float(input("Informe o valor de yb: "))
        except:
            print("Erro! Valor inválido. Digite novamente.")
        else:
            break
            
    reduced = f'y = {angularReduced(xa, ya, xb, yb)}{linearReduced(xa, ya, xb, yb)}'
    general = f'{angularGeneral(xa, ya, xb, yb)}{linearGeneral(xa, ya, xb, yb)}{constantGeneral(xa, ya, xb, yb)}'

main()
