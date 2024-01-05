import csv

def register_form():
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        print("Create an account:")
        print("Enter your username: ")
        username = input()
        print("Enter your password: ")
        password1 = input()
        print("Re-enter your password: ")
        password2 = input()

        if password1 != password2:
            print("Passwords don't match. Try again.")
            return
        else:
            writer.writerow([username, password1])
            print("Account created. You can now login.")


def login_form():
    cont = 0
    while cont < 3:
        print("Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open("users.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login successful")
                    return True
                else:
                    print("Invalid username or password")
                    cont += 1
    print("Too many failed login attempts. Please try again later.")
    return False


balance = 2000

def deposit():
    print("How much would you like to deposit?")
    amount = int(input())
    global balance
    balance += amount
    print("Deposit successful")
    return balance


def withdraw():
    print("How much would you like to withdraw?")
    amount = int(input())
    global balance
    balance -= amount
    print("Withdrawal successful")
    return balance


def view():
    print("Your balance is: ", balance)
    return balance


def transfer():
    print("How much would you like to transfer?")
    amount = int(input())
    global balance
    balance -= amount
    print("Transfer successful")
    return balance


def user_menu():
    print("What would you like to do?")
    print("Deposit (Type 1), Withdraw (Type 2), View (Type 3), Transfer (Type 4), Exit (Type 5)")
    choice = int(input())
    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        view()
    elif choice == 4:
        transfer()
    elif choice == 5:
        exit()

active = True

logged_in = False

while active:
    if logged_in:
        print("Hello! What would you like to do?")
        print("Create a movement (Type 1), Logout (Type 2)")
    else:
        print("View Info Users (Type 0), Register (Type 1), Login (Type 2) or Exit (Type 3)")

    choice = int(input())

    if choice == 0:
        with open('users.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
                print()

    elif choice == 1 and not logged_in:
        register_form()
    elif choice == 1 and logged_in:
        user_menu()
    elif choice == 2 and not logged_in:
        logged_in = login_form()
    elif choice == 2 and logged_in:
        logged_in = False
        print("You have been logged out")
    elif choice == 3 and not logged_in:
        active = False