import os
import sys

option = 0
balance = 2000
login_attempts = 0
username = "mitnick"
password = "god"
login_success = False

os.system('clear')
print("WELCOME TO ONLINE BANKING")
print("=========================")
while login_attempts !=3:
    user_login = input("Username: ")
    pass_login = input("Password: ")
    if username == user_login and password == pass_login:
        login_success = True
        break
    else:
        login_attempts += 1
        if login_attempts == 3:
            print("Better luck next time! Bye.")
            sys.exit()
        print("Sorry, try again.")



while option != 5 and login_success == True:
    os.system('clear')
    print("WELCOME TO ONLINE BANKING")
    print("=========================")
    
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer money")
    print("4. View Account Balance")
    print("5. Exit")
    option = int(input("Choose an option: "))
    if option == 1:
        print("\n")
        deposit = int(input("Amount to deposit: "))
        print("\n")
        balance = balance + deposit
        print("You deposited ", str(deposit), " in your account.")
        input("Press ENTER to continue")
    elif option == 2:
        print("\n")
        withdraw = int(input("Amount to withdraw: "))
        print("\n")
        if balance >= withdraw:
            balance = balance - withdraw
            print("You withdraw ", str(withdraw), ". Your new balance is:", str(balance))
            input("Press ENTER to continue")
        else:
            print("You cannot withdraw {}. You only have {} in your account.".format(withdraw, balance))
            input("Press ENTER to continue")
    elif option == 3:
        print("\n")
        transfer = int(input("Amount to transfer: "))
        print("\n")
        if balance >= transfer:
            transfer_account = input("Account to transfer (numbers only): ")
            balance = balance - transfer
            print("You Transfer ", str(transfer), ". to the account ", transfer_account , ". Your new balance is:", str(balance))
            input("Press ENTER to continue")
        else:
            print("You cannot transfer {}. You only have {} in your account.".format(transfer, balance))
            input("Press ENTER to continue")
    elif option == 4:
        print("\n")
        print("Account Balance: ", str(balance))
        print("\n")
        input("Press ENTER to continue")