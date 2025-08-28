"""

simple yes or no program
Keep asking the user if he wants to continue
They should choose between y or n
If y. Then keep running he program 
If n then break and end the program
"""

#user choice -input

choice = input("do you want to continue: enter any key to continue or no to stop?")

#loop
while(choice == "y"):
    print("alright continuing the program")
    choice = input("do you want to continue: y or n?")
    if(choice == "y"):
        continue
    elif(choice == "n"):
        break
    else:
        print("invalid input")


