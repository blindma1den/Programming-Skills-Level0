from models.Bank import Bank
from models.User import User


def load_initial_user():
    user: User = User(username="cval0", password="tryHackMe")
    return user


def main():
    bank: Bank = Bank()
    bank.register_user(load_initial_user())
    loop: bool = True
    active_user = None
    while loop:
        option = bank.menu()
        if option == 1:
            username = input("Define username: ")
            password = input("Password: ")
            bank.register_user(User(username, password))
        elif option == 2:
            active_user = bank.login()
        elif option == 3:
            if active_user is not None:
                amount = float(input("Withdraw amount: "))
                active_user.withdraw(amount)
            else:
                print("Not logged in yet")
        elif option == 4:
            if active_user is not None:
                amount = float(input("Deposit amount: "))
                active_user.deposit(amount)
            else:
                print("Not logged in yet")
        elif option == 5:
            if active_user is not None:
                destiny_user = input("Destiny user: ")
                amount = float(input("Transfer amount: "))
                bank.transfer(origin_account=active_user, destination_account=destiny_user, amount=amount)
            else:
                print("Not logged in yet")
        elif option == 6:
            if active_user is not None:
                active_user.view()
            else:
                print("Not logged in yet")
        else:
            loop = False


if __name__ == "__main__":
    main()
