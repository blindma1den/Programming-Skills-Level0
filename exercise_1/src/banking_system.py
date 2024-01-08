from bank_account import BankAccount

my_account = BankAccount(
    username="pepe", password="123", account_id="AC2323", balance=2000
)

other_accounts = ["AC3211", "AC9812", "AC2382"]


def login():
    """Ask up to three times the user for credentials. If success then log in
    else the program terminates."""
    login_tries_left = 3
    logged_in = False

    while login_tries_left > 0 and not logged_in:
        print(f"\nYou have {login_tries_left} tries left. Be careful.")
        username_input = input("\nUsername:\n")
        password_input = input("\nPassword:\n")
        if (
            my_account.username == username_input
            and my_account.password == password_input
        ):
            print(f"\nWelcome {my_account.username}!\n")
            logged_in = True
        else:
            login_tries_left -= 1

    if not logged_in:
        print(
            "You have entered your credentials wrong three times. For security reasons"
            + " your access is blocked. gl hf contacting to support bud."
        )
        exit()


def display_menu():
    """Displays the main menu."""
    menu_message = "Main menu:\n1. Deposit.\n"
    menu_message += "2. Withdraw.\n"
    menu_message += "3. View balance.\n"
    menu_message += "4. Transference.\n"
    menu_message += "5. Exit."
    print(menu_message)


def select_task(my_account):
    """Select a task from the main menu and performs the task."""
    selected_task = int(input("Enter a number for the task you want: "))

    match selected_task:
        case 1:
            my_account.deposit()

        case 2:
            my_account.withdraw()

        case 3:
            my_account.show_balance()

        case 4:
            my_account.transference(other_accounts)

        case 5:
            print("Thank you for using our services. See you soon!")
            exit()
        case _:
            print("Please select a valid task.")


# Bienvenida
print("Welcome to your favorite home-banking system")
print("To continue please log in:")
login()

# Main Menu
while True:
    display_menu()
    select_task(my_account)
