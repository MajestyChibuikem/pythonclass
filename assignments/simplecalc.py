"""
simple calculator, that gets two user int inputs and op
returns sum, diff, quotient, product
"""

#user inputs, num1 and num2
num1 = int(input("input your first number: "))
num2 = int(input("enter your second number: "))

#operation input
op = input("enter your operation: sum \nproduct \nquotient \ndifference ").lower()

#sum, difference, quotient, product
def addition():
    sum = num1 + num2
    print(f"this is the sum: {sum}")

def diff():
    difference = num1 - num2
    print(f"this is the difference of the two numbers: {difference}")

def divide():
    quotient  = num1 / num2
    print(f"this is the quotient of two numbers: {quotient}")

def multiply():
    product = num1 * num2
    print(f"this is the product of two numbers: {product}")


if (op.lower() == "sum"): 
    addition()
elif (op.lower() == "difference"):
    diff()
elif (op.lower() == "quotient"):
    if (num2 == 0):
        print("undefined")
    else:
        divide()
elif (op.lower() == "product"):
    multiply()
else:
    print("invalid operator")



print("end of program")