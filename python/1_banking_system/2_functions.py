"""
Author: CodinEric.

This implementations uses functions to make the code more readable and reusable.

Requirements:
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
"""


def authenticate(username: str, password: str) -> bool:
    """This function authenticates the user.

    Args:
        username (str): username of the user
        password (str): password of the user

    Returns:
        bool: True if the user is authenticated, False otherwise
    """
    if username == "codineric" or password == "1234":
        return True
    return False


def print_menu() -> None:
    """This function prints the main menu."""
    print(
        """
        What do you want to do?
            1. Deposit
            2. Withdraw
            3. View
            4. Transfer
            5. Exit
        """
    )


def deposit(balance: int) -> int:
    """This function deposits money into the account.

    Args:
        balance (int): current balance of the account

    Returns:
        int: new balance of the account
    """
    print("How much do you want to deposit?")
    deposit = int(input())
    balance += deposit
    print(f"Your balance is {balance}")
    return balance


def withdraw(balance: int) -> int:
    """This function withdraws money from the account.

    Args:
        balance (int): current balance of the account

    Returns:
        int: new balance of the account
    """
    print("How much do you want to withdraw?")
    withdraw = int(input())
    balance -= withdraw
    print(f"Your balance is {balance}")
    return balance


def show_balance(balance: int) -> int:
    """This function shows the current balance of the account.

    Args:
        balance (int): current balance of the account

    Returns:
        int: current balance of the account
    """
    print(f"Your balance is {balance}")
    return balance


def transfer(balance: int) -> int:
    """This function transfers money from the account.

    Args:
        balance (int): current balance of the account

    Returns:
        int: new balance of the account
    """
    print("How much do you want to transfer?")
    transfer = int(input())
    balance -= transfer
    print(f"Your balance is {balance}")
    return balance


def main():
    """This function is the main function of the program."""
    auth_tries = 3
    auth = False

    while auth_tries > 0 and auth is False:
        print("insert your username")
        username = input()

        print("insert your password")
        password = input()

        auth = authenticate(username, password)
        if auth is False:
            auth_tries -= 1
            print(f"Wrong credentials you have {auth_tries} tries left")

    if auth_tries == 0:
        print("You have been locked out")
    else:
        print("Welcome to the banking system")

        balance = 2000
        menu = True
        while menu:
            print_menu()

            option = input()

            ops_menu = {
                "1": deposit(balance),
                "2": withdraw(balance),
                "3": show_balance(balance),
                "4": transfer(balance),
            }

            if option in ops_menu:
                if option == "5":
                    print("Goodbye")
                    menu = False
                else:
                    balance = ops_menu[option]
            else:
                print(f"{option} is an invalid option")


if __name__ == "__main__":
    main()
