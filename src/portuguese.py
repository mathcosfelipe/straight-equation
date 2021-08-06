from reduced import reducedAngular, reducedLinear
from general import generalAngular, generalLinear, generalConstant


def portuguese():
    
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

    reduced = 'y = '+ reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f'\n A equação reduzida é: {reduced} \n A equação geral é: {general}'

    print(answer)

    while True:
        try:
            decision = input("Deseja calcular outra equação (s/n)? ")
        except:
            print("Erro inexperado. Tente novamente.")
        else:
            if decision != "s" and decision != "n":
                print("Erro! Opção inválida. Tente novamente.")
            else:
                break

    if decision == "s":
        portuguese()
    else:
        quit()