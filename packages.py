'''
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.  
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.


'''


import random
users = {'user1': 'password', 'user2': 'password'}
packages= []
details = {}


def register():
    username = input('Enter a new username: ')
    password = input('Enter a new password: ')
    
    if username in users:
        print('Username already exists. Choose a different username.')
    else:
        users[username] = password
        print('Registration successful. You can now login.')
        
def login():
    attempts = 0
    while attempts < 3:
        username = input('Enter username: ' )
        password = input('Enter password: ')

        if username in users and users[username] == password:
            print('Welcome', username, '!')
            return True
        else:
            print('Username incorrect')
            attempts += 1
    print('Too many incorrect attempts')
    return False

def menu1():
    print('Choose an option:')
    print('1. Register')
    print('2. Login' )

    option = input('Enter your choice (1 or 2): ')

    if option == '1':
        register()
    elif option == '2':
        return login()
    else:
        print('Invalid choice')

def package():
    name1 = input('Enter your name: ')
    address1 = input('Enter your address: ') 
    name2 = input('Enter the person`s name: ')
    address2= input('Enter the person`s address: ')
    weight= int(input('Enter the packages`s weight(in kg): '))
    
    price = round(weight*2)
    pack_num= random.randint(1,600)

    details = {'pack_num' : pack_num, 'weight': weight,  'origin' : address1, 'Sender': name1, 'destination': address2, 'Recipient' : name2}
    packages.append(details)

    print('This is yous package number', pack_num, 'and this is the total amount to pay to send the package', price, '$')
    
def menu2():

    choice_ = True
    while choice_ :
        print('Menu:')
        print('1. Send a package')
        print('2. Exit')

        option = input('Enter your choice (1 or 2): ')

        if option == '1':
            package()
        elif option == '2':
            break
        else:
            print('Invalid choice')

        question = input('Do you want to send another package (y/n) ?' )

        if question == 'y':
            package()

        choice_ = (question == 'y')
        if question == 'n':
            print('Have a nice day!')

        
            
        
if __name__ == "__main__":

    while True:
        if menu1():
            break
        else:
            print('Try again')
    
    menu2()
            
