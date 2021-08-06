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