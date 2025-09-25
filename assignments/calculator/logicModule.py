import functionModule as fm
def logicFunction(op, num1, num2):
    if (op.lower() == "sum"): 
        fm.addition(num1, num2)
    elif (op.lower() == "difference"):
        fm.diff(num1, num2)
    elif (op.lower() == "quotient"):
        if (num2 == 0):
            print("undefined")
        else:
            fm.divide(num1, num2)
    elif (op.lower() == "product"):
        fm.multiply(num1, num2)
    else:
        print("invalid operator")