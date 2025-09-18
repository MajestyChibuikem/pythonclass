"""_summary_

This is a code that runs a simulation of an ATM  operation.The program gives the user a starting balance of $1,000 and then the 
processes comprise of 4 operations :

.Checking  User Balance
.Allwing User to Make Deposits.
.Allowing User to Make Withdrawals.
.Gives the user an option to Exit the program.

    """

balance = 1000  # starting balance

while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose an option (1-4): "))

    if choice == 1:
        print(f"Your current balance is: ${balance}")

    elif choice == 2:
        deposit = int(input("Enter deposit amount: $"))
        if deposit > 0:
            balance += deposit 
            print(f"Deposit successful! New balance: ${balance}")
        else:
            print(" Invalid deposit amount.")

    elif choice == 3:
        withdraw = int(input("Enter withdrawal amount: $"))
        if withdraw > 0:
            if withdraw <= balance:
                balance -= withdraw
                print(f"Transaction successful! New balance: ${balance}")
            else:
                print(" Insufficient funds!")
        else:
            print(" Invalid withdrawal amount.")

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye! 👋")
        break  # exit the loop

    else:
        print(" Invalid option. Please choose between 1 and 4.")
