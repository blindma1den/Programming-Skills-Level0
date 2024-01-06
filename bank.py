import sys
import uuid


class Account:
    wrong_login_details_counter = 0
    balance = 2000
    account_id = str(uuid.uuid4())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            return "Not enough funds"

    def view_balance(self):
        return self.balance

    def transfer_money(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            return "Not enough funds"


account1 = Account("online", "bank")
account2 = Account("bank", "online")
account3 = Account("banking", "system")

print("Welcome to the Online Banking System")
print("Please login to your account")
print("---------------------------------")

while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username != account1.username or entered_password != account1.password:
        account1.wrong_login_details_counter += 1
        if account1.wrong_login_details_counter == 3:
            print("You have entered wrong login details 3 times, exiting system")
            sys.exit(0)
        print("Try again")

    print("You have logged in")
    break

while True:
    print("To view your balance, select 1")
    print("To deposit money to your account, select 2")
    print("To withdraw money from your account, select 3")
    print("To transfer money to another account, select 4")
    print("To quit, select 5")

    option = int(input("Enter your choice: "))

    if option == 1:
        print(f"Your account balance is ${account1.balance}")
    if option == 2:
        amount_to_deposit = int(input("Enter the amount that you want to deposit to your account: "))
        account1.deposit(amount_to_deposit)
        print(f"You have deposited ${amount_to_deposit}. Your current balance is ${account1.balance}")
    if option == 3:
        amount_to_withdraw = int(input("Enter the amount that you want to withdraw from your account: "))
        new_balance = account1.withdraw(amount_to_withdraw)
        if type(new_balance) is int:
            print(f"You have withdrawn ${amount_to_withdraw}. Your account balance is ${new_balance}")
        elif type(new_balance) is str:
            print(new_balance)
    if option == 4:
        print("Please select the account to transfer money from your account.")
        print(f"1._ Account: {account2.username}, ID: {account2.account_id}")
        print(f"2._ Account: {account3.username}, ID: {account3.account_id}")
        account_selected_to_transfer = int(input("Enter your choice:"))
        amount_to_transfer = int(input("Enter the amount that you want to transfer from your account:"))
        new_balance = account1.transfer_money(amount_to_transfer)
        if account_selected_to_transfer == 1:
            if type(new_balance) is int:
                print(f"You have transfer the amount of ${amount_to_transfer} to {account2.account_id}."
                      f"Your account balance is ${new_balance}")
            elif type(new_balance) is str:
                print(new_balance)
        elif account_selected_to_transfer == 2:
            if type(new_balance) is int:
                print(f"You have transfer the amount of ${amount_to_transfer} to {account3.account_id}."
                      f"Your account balance is ${new_balance}")
            elif type(new_balance) is str:
                print(new_balance)
    if option == 5:
        sys.exit(0)
