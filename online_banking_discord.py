# Users must be able to log in with a username and password.
#If the user enters the wrong credentials three times, the system must lock them out.
def login():
    count_pwd = 0
    auth = False
    while True:
        user=input("Enter username: ")
        password=input("Enter password: ")

        if user == "user1" and password == "password1":
            print("Valid login")
            auth = True
            break
        else:
            count_pwd = count_pwd + 1
            if count_pwd < 3:
                print("Try again")
            else:
                print("User locekd")
                break
# The initial balance in the bank account is $2000.
    if auth == True:
        balance = 2000
        print ("Welcome to your home banking, your balance is :", balance)
        
# The system must allow users to deposit, withdraw, view, and transfer money.
# The system must display a menu for users to perform transactions.
        print("Enter the operation you want to do: ")
        print("a. Deposit") 
        print("b. Withdraw")     
        print("c. View")     
        print("d. Transfer money")
        
        option = input()
        
        if option == "a":
            print("Introduce the amount to deposit: ")
            deposit = int(input())
            balance = balance + deposit
            print ("Your actual balance is: ", balance)
            
        if option == "b":
            print("Introduce the amount to withdraw: ")
            withdraw = int(input())
            balance = balance - withdraw
            print ("Your actual balance is: ", balance)
 
        if option == "c":
            print ("Your actual balance is: ", balance)
        
        if option == "d":
            print("Introduce the amount to transfer: ")
            transfer = int(input())
            balance = balance - transfer
            print ("Your actual balance is: ", balance)        
            
login()
        
