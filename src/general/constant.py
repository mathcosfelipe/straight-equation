def generalConstant():

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryC = xb * ya * -1
    mainC = xa * yb
    constant = secondaryC + mainC
    
    if constant < 0:
      coeficient = "- ", constant * -1
    elif constant > 0:
      coeficient = " + ", constant
    else:
      coeficient = ""
      
    return coeficient
