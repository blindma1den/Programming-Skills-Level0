# 4. Create an online shipping system with the following features:
# * 	The system has a login that locks after the third failed attempt.
# * 	Display a menu that allows: Sending a package, exiting the system.
# * 	To send a package, sender and recipient details are required.
# * 	The system assigns a random package number to each sent package.
# * 	The system calculates the shipping price. $2 per kg.
# * 	The user must input the total weight of their package, and the system should display the amount to pay.
# * 	The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
import random

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
    print('\tWelcome to Web Packages\n\nPlease Identify with your credentials\n')
    # Login
    while attempts != 0:
        username,password = login()
        loggedUser = {
            'username': username,
            'password': password}
        if checkUser(loggedUser['username'],loggedUser['password']):
            print('\nLogin Succesful')
            break
        else:
            attempts -= 1
            print(f"\nYou have {attempts} attempts left\n")
    else:
        print('User Locked Out')
        exit()
    # Menu
    while menuOption != 0:
        print('\nPlease select an option\nSend Package [1] - Logout [0]')
        try:
            menuOption = int(input('>> '))
            if menuOption == 1:
                print('\nPlease enter the sender details')
                sender = Sender(getInfo())
                print('\nPlease enter the recipient details')
                recipient = Recipient(getInfo())
                print('\nPlease enter the package weight')
                package = Package(getPackageInfo())
                showShippingInfo(sender, recipient, package)
                print('Package sent succesfully')
                print('\n\nDo you want to send another package? [Y/N]')
                try:
                    checkInput = str(input('>> ')).lower()
                    if checkInput == 'y':
                        continue
                    elif checkInput == 'n':
                        menuOption = 0
                    else:
                        print('Invalid Option')
                except:
                    print('Invalid Option')
        except:
            print('Invalid Option')

def login():
    user = str(input('Username: '))
    password = str(input('Password: '))
    return user, password

def checkUser(user,passw):
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

def showShippingInfo(sender, recipient, package):
    print(f'\nSender----\nName: {sender.name}\nAddress: {sender.address}\n')
    print(f'Recipient----\nName: {recipient.name}\nAddress: {recipient.address}\n')
    print(f'Package Weight: {package.weight} Kg\n')
    print(f'Package Price: ${package.price}\n')
    print(f'Package Number: {package.packageNumber}\n')

def getInfo():
    name = str(input('>>Name: ')).lower()
    adress = str(input('>>Address: ')).lower()
    return name, adress

def getPackageInfo():
    weight = float(input('>>Weight: '))
    return weight

class Sender:
    def __init__(self, info):
        self.name = info[0]
        self.address = info[1]

class Recipient:
    def __init__(self, info):
        self.name = info[0]
        self.address = info[1]

class Package:
    def __init__(self, weight):
        self.weight = round(weight, 2)
        self.price = round(weight * 2, 2)
        self.packageNumber = random.randint(1,1000)

if __name__ == '__main__':
    main()