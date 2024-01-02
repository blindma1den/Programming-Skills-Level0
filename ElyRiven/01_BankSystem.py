# 1. Create an online banking system with the following features:

# * Users must be able to log in with a username and password.
# * If the user enters the wrong credentials three times, the system must lock them out.
# * The initial balance in the bank account is $2000.
# * The system must allow users to deposit, withdraw, view, and transfer money.
# * The system must display a menu for users to perform transactions.

# Users & Credentials
# User1{username:'elyriven', password: 'devtraining123'}
# User2{username:'shadowrun', password: 'devtraining321'}

USERSDATA = {
        'user1': {'username': 'elyriven',
                  'password': 'devtraining123'
                 },
        'user2': {'username': 'shadowrun',
                  'password': 'devtraining321',
                 },
}


def main():    
    attempts = 3
    print('\tWelcome to BankSecurity\n\nPlease Identify with your credentials\n')
    # Login function
    while attempts != 0:
        username,password = login()
        loggedUser = User(username,password)
        if loggedUser.checkUser(username,password):
            print('\nLogin Succesful')
            # CONTINUE THE PROGRAM HERE
            break
        else:
            attempts -= 1
            print(f"\nYou have {attempts} attempts left\n")
            if attempts == 0:
                print('User Locked Out')
                exit()

def login():
    user = str(input('Username: '))
    password = str(input('Password: '))
    return user, password

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def checkUser(self,user,passw):
        x = 0
        y = 0
        userFlag = False
        while x < len(USERSDATA):
            if user == USERSDATA[f'user{x+1}']['username']:
                userFlag = True
                break
            else:
                x += 1
        else:
            print('Wrong Username')
            return False
        if userFlag == True:
            if passw == USERSDATA[f'user{x+1}']['password']:
                return True
            else:
                print('Wrong Password')
                return False

if __name__ == '__main__':
    main()