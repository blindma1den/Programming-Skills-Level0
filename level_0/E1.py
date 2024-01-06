# Create an online banking system with the following features:

# Users must be able to log in with a username and password.
# If the user enters the wrong credentials three times, the system must lock them out.
# The initial balance in the bank account is $2000.
# The system must allow users to deposit, withdraw, view, and transfer money.
# The system must display a menu for users to perform transactions.

from replit import db
import json
import os


class User:

    def __init__(self,
                 username="",
                 password="",
                 status=True,
                 balance=2000,
                 _count=0):
        self.username = username
        self.password = password
        self.status = status
        self.balance = balance
        self._count = 0

    def view(self, debug=True):
        if debug:
            print(
                f'Username: {self.username}\tPassword: {self.password}\tStatus: {self.status}\t Balance: ${self.balance}'
            )
        else:
            print(f'Username: {self.username}\tBalance: ${self.balance}')
        return self.toJson()

    def toJson(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=1)

    def deposit(self, amount):
        self.balance += amount
        self.save()
        return

    def checkFounds(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        if self.checkFounds(amount):
            self.balance -= amount
            self.save()
        else:
            print("Insufficient funds")
        return

    def transfer(self, there, amount):
        if self.checkFounds(amount):
            self.withdraw(amount)
            there.deposit(amount)
            self.save()
        else:
            print("Insufficient funds")
        return

    def checkPassword(self, password):
        if self.password == password:
            return True
        else:
            self._count += 1
            print(f'Wrong password. Attempts: {self._count} of 3')
            if self._count == 3:
                self.lockUser()
            return False

    def lockUser(self):
        self.status = False
        self.save()
        return

    def save(self):
        db[self.username] = self.toJson()
        return

def drawMenu(user,clear = True):
    if clear:
        os.system('clear')

    print(" Please Select an option ".center(50, "="))
    print(" 1) - Check balance")
    print(" 2) - Deposit")
    print(" 3) - Witdraw")
    print(" 4) - Transfer")
    print(" 5) - Exit \n", end="")
    option = int(input())
    if option == 1:
        user.view(False)
        drawMenu(user, False)
    elif option == 2:
        amount = int(input("Enter amount to deposit: "))
        user.deposit(amount)
        drawMenu(user)
    elif option == 3:
        amount = int(input("Enter amount to withdraw: "))
        user.withdraw(amount)
        drawMenu(user)
    elif option == 4:
        username = input("Enter username to transfer to: ")
        userList = db.get(username)
        if (userList != None):
            j = json.loads(userList)
            u = User(**j)
            amount = int(input("Enter amount to transfer: "))
            user.transfer(u, amount)
        else:
            print("User not found")
        drawMenu(user, False)
    elif option == 5:
        drawLogIn()
    else:
        print(f'{option} is an Invalid option {option == 1}')

        #drawMenu(user)
    return


def drawLogIn():
    os.system('clear')
    print(" Please Enter Credentials ".center(50, "="))
    print(" Username: ", end="")
    username = input()
    userList = db.get(username)
    if (userList != None):
        j = json.loads(userList)
        u = User(**j)
        u.view()
        if (u.status):
            logedIn = False
            while (u.status and not logedIn):
                print(" Password: ", end="")
                password = input()
                logedIn = u.checkPassword(password)
            if (not u.status):
                print(f'{username} is locked out')
            else:
                drawMenu(u)
                print("loggedIn")
        else:
            print(f'{username} is locked out')
    else:
        print("user dont exist, do you want to create an account? (y/n)",
              end="")
        create = input()
        if (create == "y" or create == "Y"):
            print(f'Set a Password for Username {username}: ', end="")
            password = input()
            user = User(username, password)
            db[username] = user.view()
            drawMenu(user)

    print(" Thank You ".center(50, "="))
    return

def main():
    print(db.keys())
    drawLogIn()
