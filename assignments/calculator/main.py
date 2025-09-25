import inputModule as im
import logicModule as lm
choice = "y"
while(choice =="y"):
    #num1
    num1 = im.getnum()

    #num2
    num2 = im.getnum()

    op = im.getOperation()

    lm.logicFunction(op, num1, num2)

    choice = input("do you want to continue: y to continue or any other key to quit?")


