def generalLinear():

    coeficient = ""
    
    # d = |x  y  1|x   y|
    #     |xa ya 1|xa ya|
    #     |xb yb 1|xb yb|
    
    secondaryY = xa * -1
    mainY = xb
    linear = secondaryY + mainY
    
    if linear < 0:
      coeficient = " - ", linear * -1, "y"
    elif linear > 0:
      coeficient = " + ", linear, "y"
    else:
      coeficient = ""
      
    return coeficient
