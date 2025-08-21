"""
get two int input and return the greater 
"""

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))


if(num1 == num2):
    print("the numbers are the same")
elif(num1 < num2):
    print(f"num2: {num2} is the greater number" )
else:
    print(f"num1: {num1} is the greater")