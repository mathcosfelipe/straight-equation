
def reducedLinear(xa, ya, xb, yb):

    coeficient = ""
    
    # y - y0 = m(x - x0)
   
    ybya = yb - ya
    xbxa = xb - xa
    angular = ybya / xbxa
    linear = angular * xa + ya
    
    if linear < 0:
      coeficient = " - ", linear
    elif linear > 0:
      coeficient = " + ", linear
    else:
      coeficient = ""

    return coeficient
