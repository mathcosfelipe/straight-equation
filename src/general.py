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