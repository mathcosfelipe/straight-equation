
def reducedAngular(xa, ya, xb, yb):

    coeficient = ""
   
    ybya = yb - ya
    xbxa = xb - xa
    angular = ybya / xbxa
    
    if angular < 0:
      coeficient = "- ", angular
    elif angular > 0:
      coeficient = "+ ", angular
    else:
      coeficient = ""

    return coeficient
