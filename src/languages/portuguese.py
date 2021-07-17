from ..reduced.angular import main as ra
from ..reduced.linear import main as rl
from ..general.angular import main as ga
from ..general.linear import main as gl
from ..general.constant import main as gc

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

    reduced = f'{ra(xa, ya, xb, yb)}{rl(xa, ya, xb, yb)}'
    general = f'{ga(xa, ya, xb, yb)}{gl(xa, ya, xb, yb)}{gc(xa, ya, xb, yb)}'
    answer = f'\n A equação reduzida é: {reduced} \n A equação geral é: {general}'

    print(answer)

    decision = input("Deseja calcular outra equação (s/n)? ")

    while decision != "s" and decision != "n":
        print("Erro! Opção inválida. Digite novamente.")

    if decision == "s":
        portuguese()
    else:
        quit()