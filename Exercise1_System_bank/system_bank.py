import time

# Dictionary with username and password for each user.
bank_users = {
    'user1': {
        'username': 'Maria',
        'password': '1234',
        'number_account': '123450'
    },
    'user2': {
        'username': 'Jose',
        'password': '4321',
        'number_account': '405060'
    },
    'user3': {
        'username': 'Carlos',
        'password': '2000',
        'number_account': '102030'
    },
}


def login(bank_users):
    # The valid credentials variable changes to true when the credentials match those of a user
    valid_credentials = False

    # Login attempt counter
    login_counter = 0

    # user_data search the credentials in bank_users
    while login_counter < 3:
        # Input credentials
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")

        for user_data in bank_users.values():
            username = user_data['username']
            password = user_data['password']

            # Validate credentials
            if entered_username == username and entered_password == password:
                print("Welcome to bank")
                valid_credentials = True
                break
        if valid_credentials:
            break

        login_counter += 1
        if not valid_credentials:
            print('Error! Username or password are incorrect')
    if login_counter == 3:
        print("You've exceeded login attempts. You're block, you need to wait for 10 seconds")
        time.sleep(10)
        login_counter = 0  # Reset login attempts after the wait time
        while login_counter < 3:
            entered_username = input("Enter your username: ")
            entered_password = input("Enter your password: ")

            for user_data in bank_users.values():
                username = user_data['username']
                password = user_data['password']

                if entered_username == username and entered_password == password:
                    print("Welcome to bank")
                    valid_credentials = True
                    break

            if valid_credentials:
                break

            login_counter += 1
            if not valid_credentials:
                print('Error! Username or password are incorrect')

        if login_counter == 3:
            print("You've exceeded login attempts. You're block, you need to wait for 10 seconds")


# This function it useful for displaying a menu.
def show_menu():
    print("Choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Transfer")
    option_menu = int(input("Enter the number of your choice: "))  # Convert string to int for use in if statement

    if option_menu == 1:
        print("Deposit")
        deposit()
    elif option_menu == 2:
        print("Withdraw")
        withdraw()
    elif option_menu == 3:
        print("View Balance")
        view_balance()
    elif option_menu == 4:
        print("Transfer")
    elif option_menu == 0:
        print("Log out")
    else:
        print("Error, the option doesn't exist")


# global variable for balance
balance = 2000


# Feature to view the balance of all transactions.
def view_balance():
    print("BALANCE:")
    print(f"Current balance $ {balance}")
    show_menu()


# Function for deposit money in account
def deposit():
    global balance
    amount_deposit = float(input("Enter amount to deposit: "))
    if amount_deposit > 0:
        balance += amount_deposit  # Update balance
        print(f"Deposit of $ {amount_deposit} successful.")
        print(f"Current balance is $ {balance}")
    else:
        print("Invalid amount. Please enter a valid amount to deposit.")
    show_menu()

# Withdraw money from account
def withdraw():
    global balance
    amount_withdraw = float(input("Enter amount to withdraw "))
    # Validate is account have money
    if amount_withdraw <= balance:
        balance -= amount_withdraw # Update balance
        print(f"Withdraw of $ {amount_withdraw} successful.")
        print(f"Current balance is $ {balance}")
    else:
        print(f"Invalid amount. Please enter a valid amount to withdraw. Your current balance is {balance}")
    show_menu()


def transfer():
    # Request information, the sender bank account and the amount to be transferred
    number_account_to_transfer = int(input("Enter number account to transfer "))
    # To be continue....


login(bank_users)
show_menu()