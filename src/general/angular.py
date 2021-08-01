def generalAngular(xa, ya, xb, yb):

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryX = yb * -1
    mainX = ya
    angular = secondaryX + mainX
    
    if angular < 0:
      coeficient = "- ", angular * -1, "x"
    elif angular > 0:
      coeficient = " + ", angular, "x"
    else:
      coeficient = ""
      
    return coeficient
