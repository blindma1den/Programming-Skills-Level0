# 1. Create an online banking system with the following features:

# * Users must be able to log in with a username and password.
# * If the user enters the wrong credentials three times, the system must lock them out.
# * The initial balance in the bank account is $2000.
# * The system must allow users to deposit, withdraw, view, and transfer money.
# * The system must display a menu for users to perform transactions.

# Users & Credentials
# User1{username:'elyriven', password: 'devtraining123'}
# User2{username:'shadowrun', password: 'devtraining321'}

USERS_DATA = {
        'user1': {'username': 'elyriven',
                  'password': 'devtraining123'
                 },
        'user2': {'username': 'shadowrun',
                  'password': 'devtraining321',
                 },
}

def main():    
    attempts = 3
    menuOption = 1
    print('\tWelcome to BankSecurity\n\nPlease Identify with your credentials\n')

    # Login function
    while attempts != 0:
        username,password = login()
        loggedUser = User(username.lower(),password.lower())
        if loggedUser.checkUser(loggedUser.username,loggedUser.password):
            print('\nLogin Succesful')
            break
        else:
            attempts -= 1
            print(f"\nYou have {attempts} attempts left\n")
    else:
        print('User Locked Out')
        exit()

    # Create Account with User
    userAccount = Account(loggedUser)

    # Create Account to transfer
    transAcc = Account(User('defaultUser','123'))

    # Menu Display
    print(f'\n\t\t\tWelcome {userAccount.user.username}')
    while menuOption != 0:
        menuOption = displayMenu(loggedUser)
        if (menuOption > 4 or menuOption < 0):
            print('Invalid Option')
        if menuOption == 1:
            userAccount.showBalance()
            continue
        if menuOption == 2:
            deposit = input('Enter the ammount to deposit: ')
            userAccount.deposit(deposit)
            continue
        if menuOption == 3:
            withdraw = input('Enter the ammount to withdraw: ')
            userAccount.withdraw(withdraw)
            continue
        if menuOption == 4:
            transfer = input('Enter the ammount to transfer: ')
            userAccount.transfer(transfer, transAcc)
            continue

def login():
    user = str(input('Username: '))
    password = str(input('Password: '))
    return user, password

def displayMenu(user):
    print(f'\n\t\t\tAccount Menu\nShow Balance [1] - Deposit [2] - Withdraw [3] - Transfer [4] - Logout [0]')
    try:
        option = int(input("\n\nSelect an option to continue: "))
    except:
        print('Invalid Input. Please select a valid option')
        return displayMenu(user)
    return option

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def checkUser(self,user,passw):
        x = 0
        userFlag = False
        while x < len(USERS_DATA):
            if user == USERS_DATA[f'user{x+1}']['username']:
                userFlag = True
                break
            else:
                x += 1
        else:
            print('Wrong Username')
            return False
        if userFlag == True:
            if passw == USERS_DATA[f'user{x+1}']['password']:
                return True
            else:
                print('Wrong Password')
                return False

class Account:
    balance = 2000.00

    def __init__(self, user):
        self.user = user
    
    def showBalance(self,):
        balanceStr = '{:.2f}'.format(Account.balance)
        print(f'Your current account balance is ${balanceStr}')
    
    def deposit(self, ammount):
        try:
            if(type(float(ammount)) == float):
                Account.balance += float(ammount)
                self.showBalance()
        except:
            print('\nInvalid ammount. Please enter a valid ammount of money to deposit')

    def withdraw(self, ammount):
        try:
            if(type(float(ammount)) == float):
                checkFunds = Account.balance - float(ammount)
                if checkFunds > 0:
                    Account.balance -= float(ammount)
                    self.showBalance()
                else:
                    print('\nNot enough funds. Transaction canceled')
        except:
            print('\nInvalid ammount. Please enter a valid ammount of money to withdraw')

    def transfer(self, ammount, targetAcc):
        try:
            if(type(float(ammount)) == float):
                print(f'\nTransference ammount: ${ammount}')
                print(f'From {self.user.username} account to {targetAcc.user.username} account')
                try:
                    confirmation = input('Are you sure you want to proceed with the transference? [Y/N]: ')
                    if confirmation.lower() == 'y':
                        checkFunds = Account.balance - float(ammount)
                        if checkFunds > 0:
                            Account.balance -= float(ammount)
                            targetAcc.balance += float(ammount)
                            print('\nTransaction succesful')
                            self.showBalance()
                        else:
                            print('\nNot enough funds. Transaction canceled')
                    elif confirmation.lower() == 'n':
                        print('\nTransaction canceled by user request')
                    else:
                        print('\nInvalid Input. Transaction canceled')
                except:
                    print('\nInvalid input. Try again')
        except:
            print('\nInvalid ammount. Please enter a valid ammount of money to transfer')

if __name__ == '__main__':
    main()