def generalConstant(xa, ya, xb, yb):

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryC = xb * ya * -1
    mainC = xa * yb
    constant = secondaryC + mainC
    
    if constant < 0:
      coeficient = f' - {constant * -1}'
    elif constant > 0:
      coeficient =  f' + {constant}'
    else:
      coeficient = f''
      
    return coeficient

def generalLinear(xa, ya, xb, yb):

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryY = xa * -1
    mainY = xb
    linear = secondaryY + mainY
    
    if linear < 0:
      coeficient = f' - {linear * -1}y'
    elif linear > 0:
      coeficient = f' + {linear}y'
    else:
      coeficient = f''
      
    return coeficient

def generalAngular(xa, ya, xb, yb):

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryX = yb * -1
    mainX = ya
    angular = secondaryX + mainX
    
    if angular < 0:
      coeficient = f'- {angular * -1}x'
    elif angular > 0:
      coeficient = f'{angular}x'
    else:
      coeficient = ""
      
    return coeficient

def reducedLinear(xa, ya, xb, yb):

    coeficient = ""
    
    # y - y0 = m(x - x0)
   
    ybya = yb - ya
    xbxa = xb - xa
    angular = ybya / xbxa
    linear = angular * xa + ya
    
    if linear < 0:
      coeficient = f' - {linear * -1}'
    elif linear > 0:
      coeficient = f' + {linear}'
    else:
      coeficient = ""

    return coeficient

def reducedAngular(xa, ya, xb, yb):

    coeficient = ""
   
    ybya = yb - ya
    xbxa = xb - xa
    angular = ybya / xbxa
    
    if angular < 0:
      coeficient = f'- {angular * -1}x'
    elif angular > 0:
      coeficient =  f'+ {angular}x'
    else:
      coeficient = ""

    return coeficient

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

    reduced = 'y = ' + reducedAngular(xa, ya, xb, yb) + reducedLinear(xa, ya, xb, yb)
    general = generalAngular(xa, ya, xb, yb) + generalLinear(xa, ya, xb, yb) + generalConstant(xa, ya, xb, yb)
    answer = f'\n La ecuación reducida es: {reduced} \n La ecuación general es: {general}'

    print(answer)

    while True:
        try:
            decision = input("¿Quieres calcular otra ecuación (s/n)?")
        except:
            print("Error inesperado. Inténtalo de nuevo.")
        else:
            if decision != "s" and decision != "n":
                print("¡Error! Opción inválida. Inténtalo de nuevo.")
            else:
                break

    while decision != "s" and decision != "n":
        print("¡Error! Opción inválida. Escriba otra vez.")
        decision = input("¿Quieres calcular otra ecuación (s/n)?")


    if decision == "s":
        spanish()
    else:
        quit()

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

def main():
    while True:
        try:
            language = int(input("Choice the language \n 1. English \n 2. Spanish \n 3. German \n 4. Portuguese \n 5. Italian \n Just insert the correspondent number: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            if language !=1 and language != 2 and language != 3 and language != 4 and language != 5:
                print("Error! Invalid value. Try again.")
            else:
                break

    if language == 1:
        english()
    elif language == 2:
        spanish()
    elif language == 3:
        german()
    elif language == 4:
        portuguese()
    else:
        italian()

main() 