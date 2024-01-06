"""1. Create an online banking system with the following features:

* Users must be able to log in with a username and password. X
* If the user enters the wrong credentials three times, the system must lock them out. X
* The initial balance in the bank account is $2000. X
* The system must allow users to deposit, withdraw, view, and transfer money. X
* The system must display a menu for users to perform transactions. X """

print("Online Banking System")
print("Welcome to Bank of China!!!")
print()

auth = False
username = input("Entry you username: ")
password = input("Entry you password: ")

if username == "Lucas" and password == "tortadericota":
    auth = True
else:
    print("Try again you have 2 trie left")
    print()
    print("Insert you username")
    username = input()
    print("Insert you password")
    password = input()
    if  username == "Lucas" and password == "tortadericota":
        auth = True
    else:
        print("Try again you have 1 trie left")
        print()
        print("Insert you username")
        username = input()
        print("Insert you password")
        password = input()
        if username == "Lucas" and password == "tortadericota":
            auth = True
        else:
            print("You are block broooo")


if auth: 
    print("Welcome banking navigator!!")
    userbalance = 2000

    print("1 -> view")
    print("2 -> deposit")
    print("3 -> withdraw")
    print("4 -> transfer money")
    print("5 -> exit")

    option = input()

    if option == "1":
        print(f"you balance is {userbalance}")
    elif option == "2":
        print("Insert you deposit")
        deposit = int(input())
        userbalance += deposit
        print(f"you balance is {userbalance}")
    elif option == "3":
        print("how much you take?")
        withdraw = int(input())
        userbalance -= withdraw
        print(f"you balance is {userbalance}")
    elif option == "4":
        print("transfer ok how much?")
        transferencia = int(input())
        userbalance -= transferencia
        print(f"you was trasnfer {transferencia} and your balance is {userbalance} ")
    elif option == "5":
        print("Goodbye china banker")
    else:
        print("Invalid choise")
    
    

