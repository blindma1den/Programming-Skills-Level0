import time

# Dictionary with username and password for each user.
bank_users = {
    'user1': {
        'username': 'Maria',
        'password': '1234',
        'number_account': '123450',
        'balance': 2000
    },
    'user2': {
        'username': 'Jose',
        'password': '4321',
        'number_account': '405060',
        'balance': 2000
    },
    'user3': {
        'username': 'Carlos',
        'password': '2000',
        'number_account': '102030',
        'balance': 2000
    },
}


def login(bank_users):
    # The valid credentials variable changes to true when the credentials match those of a user
    valid_credentials = False

    # Login attempt counter
    login_counter = 0
    logged_user = None

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
                valid_credentials = True
                logged_user = entered_username  # Save name in variable logged_user
                print(f"Welcome to bank {logged_user}")
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
    return logged_user


# This function it useful for displaying a menu.
def show_menu():
    while True:
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Transfer")
        print("0. Logout")
        option_menu = int(input("Enter the number of your choice: "))  # Convert string to int for use in if statement

        if option_menu == 1:
            print("Deposit")
            deposit()
        elif option_menu == 2:
            print("Withdraw")
            withdraw()
        elif option_menu == 3:
            print("View Balance")
            view_balance(logged_user)
        elif option_menu == 4:
            print("Transfer")
            transfer(logged_user)
        elif option_menu == 0:
            print("Log out")
            return
        else:
            print("Error, the option doesn't exist")


# Feature to view the balance of all transactions.
def view_balance(logged_user):
    for user_data in bank_users.values():
        if user_data['username'] == logged_user:
            balance = user_data['balance']
            print(f"-----Welcome {logged_user}")
            print("BALANCE:")
            print(f"Current balance $ {balance}")
        return  # Exit to the function and return to menu


# Function for deposit money in account
def deposit():
    for user_data in bank_users.values():
        amount_deposit = float(input("Enter amount to deposit: "))
        if amount_deposit > 0:
            user_data['balance'] += amount_deposit  # Update balance
            print(f"Deposit of $ {amount_deposit} successful.")
            print(f"Current balance is $ {user_data['balance']}")
            return  # Exit to the function and return to menu
        else:
            print("Invalid amount. Please enter a valid amount to deposit.")


# Withdraw money from account
def withdraw():
    for user_data in bank_users.values():
        amount_withdraw = float(input("Enter amount to withdraw "))
        # Validate is account have money
        if amount_withdraw <= user_data['balance']:
            user_data['balance'] -= amount_withdraw  # Update balance
            print(f"Withdraw of $ {amount_withdraw} successful.")
            print(f"Current balance is $ {user_data['balance']}")
            return  # Exit to the function and return to menu
        else:
            print(
                f"Invalid amount. Please enter a valid amount to withdraw. Your current balance is {user_data['balance']}")


def transfer(logged_user):
    # Request information, the sender bank account and the amount to be transferred
    account_number_to_transfer = input("Enter number account to transfer ")
    amount_to_transfer = float(input("Enter amount to transfer "))

    # Validate if account exists
    account_exists = False  # Variable for validate if account exist
    for user_data in bank_users.values():
        receiver = user_data['number_account']
        if receiver == account_number_to_transfer:
            account_exists = True
            break

    # Validate if account have enough money for transfer
    if account_exists:
        for user_data in bank_users.values():
            name_receiver = user_data['username']
            receiver_balance = user_data['balance']
            # Search for the registered user's account and validate if it has funds
            if user_data['username'] == logged_user and float(user_data['balance']) >= amount_to_transfer:
                # Subtract the amount to be transferred from the initial balance
                user_data['balance'] -= amount_to_transfer
                receiver_balance += amount_to_transfer
                print(f"Your balance is {user_data['balance']}")
                print(
                    f"Successful transfer to {name_receiver} and number account {receiver} amount ${amount_to_transfer}"
                )
                break
        else:
            print(f"Insufficient amount")
    else:
        print("Wrong Account!")


logged_user = login(bank_users)
show_menu()
